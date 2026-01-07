"""LaTeX/Beamer slide validation."""
import subprocess
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def validate_latex(manifest: dict, strict: bool = False) -> bool:
    """
    Validate LaTeX files.

    Args:
        manifest: Course manifest
        strict: If True, fail on warnings (overflow)

    Returns:
        True if all validations pass
    """
    all_passed = True

    for topic in manifest["topics"]:
        topic_dir = PROJECT_ROOT / f"slides/{topic['id']}_{topic['title'].replace(' ', '_').replace('&', '').replace('/', '_')}"

        # Check overview slides
        overview_tex = topic_dir / f"{topic['id']}_overview.tex"
        if overview_tex.exists():
            passed = _validate_tex_file(overview_tex, strict)
            if not passed:
                all_passed = False
        else:
            print(f"  [SKIP] {overview_tex.name} - not found")

        # Check deepdive slides
        deepdive_tex = topic_dir / f"{topic['id']}_deepdive.tex"
        if deepdive_tex.exists():
            passed = _validate_tex_file(deepdive_tex, strict)
            if not passed:
                all_passed = False
        else:
            print(f"  [SKIP] {deepdive_tex.name} - not found")

    return all_passed


def _validate_tex_file(tex_path: Path, strict: bool) -> bool:
    """Validate a single TeX file."""
    print(f"  Checking {tex_path.name}...")

    # Check for common issues in source
    issues = []
    with open(tex_path, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.split("\n")

        for i, line in enumerate(lines, 1):
            # Check for incorrect itemize/enumerate closing
            if "</end{" in line:
                issues.append(f"Line {i}: Invalid closing tag (</end{{...}})")

            # Check for straight quotes instead of LaTeX quotes
            if re.search(r'[^`]"[^"]', line):
                issues.append(f"Line {i}: Possible straight quotes (use `` and '')")

            # Check for missing \textwidth in includegraphics
            if "\\includegraphics" in line and "width=" not in line:
                issues.append(f"Line {i}: includegraphics without width specification")

    if issues:
        for issue in issues:
            print(f"    [WARN] {issue}")
        if strict:
            return False

    # Try to compile (if pdflatex available)
    try:
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", str(tex_path)],
            cwd=tex_path.parent,
            capture_output=True,
            text=True,
            timeout=60
        )

        # Check for errors
        if result.returncode != 0:
            print(f"    [FAIL] Compilation failed")
            # Extract error message
            error_match = re.search(r"^!.*$", result.stdout, re.MULTILINE)
            if error_match:
                print(f"    Error: {error_match.group()}")
            return False

        # Check for overflow warnings
        if strict:
            overflow_warnings = re.findall(r"Overfull \\[hv]box", result.stdout)
            if overflow_warnings:
                print(f"    [FAIL] {len(overflow_warnings)} overflow warnings")
                return False

        print(f"    [PASS]")
        return True

    except FileNotFoundError:
        print(f"    [SKIP] pdflatex not found")
        return True  # Can't validate, assume OK
    except subprocess.TimeoutExpired:
        print(f"    [FAIL] Compilation timed out")
        return False
