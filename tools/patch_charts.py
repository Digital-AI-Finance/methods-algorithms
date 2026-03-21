#!/usr/bin/env python3
"""
Batch-patch all chart.py files under slides/ to use the shared chart_style module.

Actions per file:
  1. Insert  import sys; sys.path.insert(...); from chart_style import ...; apply_style()
  2. Remove  inline plt.rcParams.update({...}) block
  3. Remove  individual ML color constant lines (MLPURPLE = '#...', etc.)
  4. Ensure  savefig calls include facecolor='white' and bbox_inches='tight'

Usage:
  python tools/patch_charts.py                      # dry-run (default)
  python tools/patch_charts.py --apply              # patch files (creates .bak)
  python tools/patch_charts.py --apply --no-backup  # patch without backups
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SLIDES_DIR = PROJECT_ROOT / 'slides'

IMPORT_BLOCK = [
    'import sys',
    "sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))",
    'from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER',
    'apply_style()',
]

# Patterns that identify a standard ML color constant assignment.
# Matches: MLPURPLE = '#3333B2'  /  ML_PURPLE = "#3333B2"  /  MLGRAY = '#808080'
# Does NOT match list/dict definitions like  COLORS = [...]
_COLOR_CONST_RE = re.compile(
    r"^\s*ML_?(?:PURPLE|BLUE|ORANGE|GREEN|RED|LAVENDER|GRAY)\s*=\s*['\"]#[0-9A-Fa-f]{6}['\"]\s*$"
)

# Detect an import line (for finding insert position)
_IMPORT_LINE_RE = re.compile(
    r"^(?:import |from \S+ import )"
)

# Detect  matplotlib.use(...)  which counts as import-region
_MPL_USE_RE = re.compile(r"^matplotlib\.use\(")

# Detect  from pathlib import Path  (any variation)
_PATH_IMPORT_RE = re.compile(r"^from\s+pathlib\s+import\s+.*\bPath\b")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _find_last_import_line(lines: list[str]) -> int:
    """Return the index of the last top-level import/from line."""
    last = -1
    for i, line in enumerate(lines):
        stripped = line.strip()
        if _IMPORT_LINE_RE.match(stripped) or _MPL_USE_RE.match(stripped):
            last = i
    return last


def _has_path_import(lines: list[str]) -> bool:
    for line in lines:
        if _PATH_IMPORT_RE.match(line.strip()):
            return True
    return False


def _already_patched(lines: list[str]) -> bool:
    for line in lines:
        if 'from chart_style import' in line:
            return True
    return False


# ---------------------------------------------------------------------------
# Step 1 -- Insert import block after last import line
# ---------------------------------------------------------------------------

def _insert_import_block(lines: list[str], log: list[str]) -> list[str]:
    """Insert the shared-style import block after the last import line."""
    insert_idx = _find_last_import_line(lines)
    if insert_idx == -1:
        # Fallback: insert after docstring / first line
        insert_idx = 0

    needs_path = not _has_path_import(lines)

    block: list[str] = []
    if needs_path:
        block.append('from pathlib import Path\n')
    block.extend(line + '\n' for line in IMPORT_BLOCK)

    # Insert after the identified line (insert_idx + 1)
    new_lines = lines[: insert_idx + 1] + block + lines[insert_idx + 1 :]
    log.append(f"  + Inserted import block after line {insert_idx + 1} ({len(block)} lines)")
    return new_lines


# ---------------------------------------------------------------------------
# Step 2 -- Remove plt.rcParams.update({...}) block
# ---------------------------------------------------------------------------

_RCPARAMS_COMMENT_RE = re.compile(
    r'^#\s*(?:Chart settings|Standard rcParams|Configure matplotlib|'
    r'Font sizes|Beamer (?:chart|font)|rcParams|Style)\b',
    re.IGNORECASE,
)


def _remove_rcparams_block(lines: list[str], log: list[str]) -> list[str]:
    """Remove contiguous plt.rcParams.update({...}) blocks (multi-line).

    Also removes the comment line immediately preceding the block if it is
    a recognisable rcParams header comment.
    """
    result: list[str] = []
    i = 0
    removed = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith('plt.rcParams.update('):
            # Check if the previous line in result is an rcParams header comment
            if result and _RCPARAMS_COMMENT_RE.match(result[-1].strip()):
                result.pop()

            # Find closing })  -- may be on same line or later
            if '})' in stripped:
                # Single- or compact-line block
                i += 1
                removed += 1
            else:
                # Multi-line: scan until we find a line containing })
                i += 1
                while i < len(lines):
                    if '})' in lines[i]:
                        i += 1
                        break
                    i += 1
                removed += 1

            # Also skip any blank line immediately after the block
            if i < len(lines) and lines[i].strip() == '':
                i += 1
        else:
            result.append(lines[i])
            i += 1

    if removed:
        log.append(f"  - Removed {removed} rcParams block(s)")
    return result


# ---------------------------------------------------------------------------
# Step 3 -- Remove inline color constants
# ---------------------------------------------------------------------------

def _remove_color_constants(lines: list[str], log: list[str]) -> list[str]:
    """Remove individual ML color constant assignments."""
    result: list[str] = []
    removed = 0
    # Track if we're inside a region of consecutive color lines,
    # so we can also remove the preceding comment line like "# Colors"
    for i, line in enumerate(lines):
        if _COLOR_CONST_RE.match(line):
            removed += 1
            continue
        result.append(line)

    if removed:
        log.append(f"  - Removed {removed} color constant line(s)")

    # Second pass: remove orphan comment headers like "# Colors", "# Color palette",
    # "# ML color palette" that now precede a blank line or end-of-section
    final: list[str] = []
    removed_comments = 0
    for i, line in enumerate(result):
        stripped = line.strip()
        if re.match(r'^#\s*(?:Colors?|Color palette|ML [Cc]olor palette)\s*$', stripped):
            # Check if the next non-blank line is NOT a color constant (they were removed)
            # i.e. the comment is now orphaned
            next_content = ''
            for j in range(i + 1, len(result)):
                if result[j].strip():
                    next_content = result[j].strip()
                    break
            if not _COLOR_CONST_RE.match(next_content):
                removed_comments += 1
                continue
        final.append(line)

    if removed_comments:
        log.append(f"  - Removed {removed_comments} orphan color-header comment(s)")

    return final


# ---------------------------------------------------------------------------
# Step 4 -- Patch savefig calls (add facecolor='white', bbox_inches='tight')
# ---------------------------------------------------------------------------

def _patch_savefig(lines: list[str], log: list[str]) -> list[str]:
    """Ensure savefig calls include facecolor='white' and bbox_inches='tight'."""
    result: list[str] = []
    patched = 0
    for line in lines:
        if 'savefig(' in line and '.png' not in line:
            changed = False
            if "facecolor" not in line and line.rstrip().endswith(')'):
                # Single-line savefig -- inject facecolor before closing paren
                line = line.rstrip()
                line = line[:-1] + ", facecolor='white')"
                changed = True
            if "bbox_inches" not in line and line.rstrip().endswith(')'):
                line = line.rstrip()
                line = line[:-1] + ", bbox_inches='tight')"
                changed = True
            if changed:
                # Ensure it still ends with newline
                if not line.endswith('\n'):
                    line += '\n'
                patched += 1
        result.append(line)

    if patched:
        log.append(f"  ~ Patched {patched} savefig call(s) (facecolor/bbox)")
    return result


# ---------------------------------------------------------------------------
# Step 5 -- Remove redundant blank lines left by removals
# ---------------------------------------------------------------------------

def _collapse_blanks(lines: list[str]) -> list[str]:
    """Collapse runs of 3+ blank lines down to 2."""
    result: list[str] = []
    blank_count = 0
    for line in lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)
    return result


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def patch_file(filepath: Path, apply: bool, backup: bool) -> dict:
    """Patch a single chart.py file. Returns status dict."""
    text = filepath.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)

    if _already_patched(lines):
        return {'status': 'skipped', 'reason': 'already patched', 'changes': []}

    log: list[str] = []

    # Apply transforms in order
    lines = _insert_import_block(lines, log)
    lines = _remove_rcparams_block(lines, log)
    lines = _remove_color_constants(lines, log)
    lines = _patch_savefig(lines, log)
    lines = _collapse_blanks(lines)

    new_text = ''.join(lines)

    if new_text == text:
        return {'status': 'skipped', 'reason': 'no changes needed', 'changes': []}

    if apply:
        if backup:
            bak = filepath.parent / f'.{filepath.name}.bak'
            shutil.copy2(filepath, bak)
        filepath.write_text(new_text, encoding='utf-8')
        return {'status': 'patched', 'changes': log}
    else:
        return {'status': 'would_patch', 'changes': log}


def main():
    parser = argparse.ArgumentParser(description='Patch chart.py files to use chart_style module')
    parser.add_argument('--apply', action='store_true', help='Actually modify files (default: dry-run)')
    parser.add_argument('--no-backup', action='store_true', help='Skip creating .bak files')
    args = parser.parse_args()

    charts = sorted(SLIDES_DIR.rglob('chart.py'))
    if not charts:
        print(f"No chart.py files found under {SLIDES_DIR}")
        sys.exit(1)

    mode = 'APPLY' if args.apply else 'DRY-RUN'
    print(f"\n=== Chart Style Patcher ({mode}) ===")
    print(f"Found {len(charts)} chart.py file(s)\n")

    counts = {'patched': 0, 'would_patch': 0, 'skipped': 0, 'failed': 0}

    for chart in charts:
        rel = chart.relative_to(PROJECT_ROOT)
        try:
            result = patch_file(chart, apply=args.apply, backup=not args.no_backup)
            status = result['status']
            counts[status] = counts.get(status, 0) + 1

            if status == 'skipped':
                print(f"  SKIP  {rel}  ({result['reason']})")
            elif status == 'would_patch':
                print(f"  PATCH {rel}")
                for line in result['changes']:
                    print(f"        {line}")
            elif status == 'patched':
                print(f"  DONE  {rel}")
                for line in result['changes']:
                    print(f"        {line}")
        except Exception as exc:
            counts['failed'] += 1
            print(f"  FAIL  {rel}  ({exc})")

    # Summary
    print(f"\n--- Summary ---")
    if args.apply:
        print(f"  Patched:  {counts.get('patched', 0)}")
    else:
        print(f"  Would patch: {counts.get('would_patch', 0)}")
    print(f"  Skipped:  {counts.get('skipped', 0)}")
    print(f"  Failed:   {counts.get('failed', 0)}")
    print(f"  Total:    {len(charts)}")

    if not args.apply and counts.get('would_patch', 0):
        print(f"\nRe-run with --apply to modify files.")


if __name__ == '__main__':
    main()
