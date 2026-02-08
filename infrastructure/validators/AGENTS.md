# Validators Module - Content Integrity Checks

<!-- Parent: ../AGENTS.md -->
<!-- Updated: 2026-02-07 -->

## Purpose

Validation subsystem for ensuring course content meets quality standards. Checks LaTeX compilation, link validity, notebook structure, and chart generation across all topics.

**All validators return `bool`:** `True` = validation passed, `False` = validation failed.

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `__init__.py` | Module exports | 8 | Exports all validation functions |
| `latex_validator.py` | Validate Beamer slides compilation | 110 | `validate_latex()`, `_validate_tex_file()` |
| `chart_validator.py` | Validate chart scripts and PDFs | 88 | `validate_charts()`, `_run_chart_script()` |
| `link_validator.py` | Validate file references and URLs | 233 | `validate_links()`, `validate_html_links()`, `_check_url()` |
| `notebook_validator.py` | Validate Jupyter notebook structure | 112 | `validate_notebooks()`, `_validate_notebook_structure()`, `_execute_notebook()` |

## For AI Agents

### Module Architecture

All validators follow a **consistent pattern**:

```python
def validate_<type>(manifest: dict, **options) -> bool:
    """
    Validate <type> content.

    Args:
        manifest: Course manifest (from manifest.json)
        **options: Validator-specific flags (strict, external, execute, regenerate)

    Returns:
        True if all validations pass
    """
    all_passed = True

    for topic in manifest["topics"]:
        # Iterate through topic assets
        # Perform checks
        # Update all_passed flag

    return all_passed
```

### LaTeX Validator (`latex_validator.py`)

**Purpose:** Compile LaTeX slides and check for errors/warnings.

**Key Features:**
- Compiles both `*_overview.tex` and `*_deepdive.tex` for each topic
- **Strict mode** (`--strict`): Fails on overflow warnings (required for production)
- **Lenient mode** (default): Only fails on compilation errors
- Detects common issues: invalid closing tags, straight quotes, missing width specs

**Usage:**
```bash
# Standard validation
python infrastructure/course_cli.py validate latex

# Strict mode (fail on overflow)
python infrastructure/course_cli.py validate latex --strict
```

**Checks Performed:**
1. **Source-level checks** (no compilation required):
   - Invalid closing tags: `</end{...}>`
   - Straight quotes instead of LaTeX quotes
   - `\includegraphics` without `width=` parameter

2. **Compilation checks** (requires pdflatex):
   - Runs `pdflatex -interaction=nonstopmode -halt-on-error`
   - Checks return code for errors
   - Scans output for `Overfull \hbox` or `Overfull \vbox` warnings (strict mode only)

**Return Codes:**
- `[PASS]` - Compilation succeeded, no issues
- `[FAIL]` - Compilation failed or overflow warnings in strict mode
- `[SKIP]` - pdflatex not found or file doesn't exist

**Testing:**
```python
from validators import validate_latex
manifest = json.load(open("manifest.json"))
passed = validate_latex(manifest, strict=True)
```

### Chart Validator (`chart_validator.py`)

**Purpose:** Verify chart.py scripts execute and generate PDF output.

**Key Features:**
- Runs each `chart.py` script via subprocess
- Verifies `chart.pdf` exists and is non-empty
- **Regenerate mode** (`--regenerate`): Force rebuild all charts
- **Validation mode** (default): Only check if PDF exists

**Usage:**
```bash
# Check existing PDFs
python infrastructure/course_cli.py validate charts

# Regenerate all charts
python infrastructure/course_cli.py validate charts --regenerate
```

**Checks Performed:**
1. **File existence:** Verify chart.py script exists
2. **PDF existence:** Check if chart.pdf exists and size > 0
3. **Execution test** (regenerate mode):
   - Run `python chart.py` in chart directory
   - Capture stdout/stderr
   - Verify chart.pdf created
   - Check timeout (60 seconds)

**Status Codes:**
- `[PASS]` - PDF exists and valid
- `[FAIL]` - Script error, PDF not generated, or empty
- `[SKIP]` - Chart marked as pending/in_progress

**Testing:**
```python
from validators import validate_charts
manifest = json.load(open("manifest.json"))
passed = validate_charts(manifest, regenerate=False)
```

### Link Validator (`link_validator.py`)

**Purpose:** Validate file references in manifest and HTML links in docs/.

**Key Features:**
- Checks manifest file paths exist on disk
- **HTML validation:** Scans docs/ for broken links
- **External URL checking** (`--external`): Verify HTTP/HTTPS URLs
- Detects links escaping docs/ directory (won't work on GitHub Pages)

**Usage:**
```bash
# Check manifest references
python infrastructure/course_cli.py validate links

# Check external URLs
python infrastructure/course_cli.py validate links --external

# Validate HTML (standalone)
python infrastructure/validators/link_validator.py --external
```

**Checks Performed:**
1. **Manifest checks:**
   - File paths in manifest exist on disk
   - Only fails if status = "complete" but file missing

2. **HTML checks** (standalone mode):
   - Extract all `<a href>`, `<img src>`, `<script src>`, `<link href>`
   - Resolve relative paths from HTML file location
   - Check local files exist
   - Verify links stay within docs/ (GitHub Pages requirement)
   - Check external URLs respond with HTTP 200 (optional)

**Special Cases:**
- Skips anchor links (`#section`)
- Skips data URIs (`data:image/png;base64,...`)
- Skips preconnect/prefetch hints (not actual resources)
- Skips Colab links (they redirect based on repo)

**Testing:**
```python
from validators import validate_links
manifest = json.load(open("manifest.json"))

# Basic check
passed = validate_links(manifest, external=False)

# HTML validation
results = validate_html_links(check_external=True)
print(results["summary"])
```

### Notebook Validator (`notebook_validator.py`)

**Purpose:** Validate Jupyter notebook JSON structure and optionally execute cells.

**Key Features:**
- Validates JSON structure (cells, metadata, nbformat)
- **Execute mode** (`--execute`): Run all cells and check for errors
- Checks for markdown and code cells
- Requires `nbformat` and `nbconvert` for execution

**Usage:**
```bash
# Structure validation only
python infrastructure/course_cli.py validate notebooks

# Execute all cells
python infrastructure/course_cli.py validate notebooks --execute
```

**Checks Performed:**
1. **Structure checks:**
   - Valid JSON syntax
   - Required keys: `cells`, `metadata`, `nbformat`
   - At least one markdown cell
   - At least one code cell

2. **Execution checks** (optional):
   - Install nbformat/nbconvert first: `pip install nbformat nbconvert`
   - Runs cells in Python 3 kernel
   - Timeout: 600 seconds (10 minutes)
   - Fails if any cell raises exception

**Status Codes:**
- `[PASS]` - Structure valid (and execution succeeded if requested)
- `[FAIL]` - Invalid JSON or execution error
- `[WARN]` - No markdown/code cells (still passes)
- `[SKIP]` - Notebook file doesn't exist or dependencies missing

**Testing:**
```python
from validators import validate_notebooks
manifest = json.load(open("manifest.json"))

# Structure only
passed = validate_notebooks(manifest, execute=False)

# Full execution test
passed = validate_notebooks(manifest, execute=True)
```

### Common Patterns Across Validators

**1. Manifest Iteration:**
```python
for topic in manifest["topics"]:
    topic_dir = _get_topic_dir(topic)
    assets = topic.get("assets", {})
    # Validate assets
```

**2. Status Filtering:**
```python
if asset.get("status") == "complete":
    # Only check complete items
elif asset.get("status") in ["pending", "in_progress"]:
    print(f"  [SKIP] - not yet ready")
```

**3. Subprocess Pattern:**
```python
try:
    result = subprocess.run(
        [command, *args],
        cwd=working_dir,
        capture_output=True,
        text=True,
        timeout=60
    )
    if result.returncode != 0:
        print(f"  [FAIL] {result.stderr}")
        return False
except FileNotFoundError:
    print(f"  [SKIP] {command} not found")
    return True  # Graceful degradation
except subprocess.TimeoutExpired:
    print(f"  [FAIL] Timed out")
    return False
```

**4. Output Messages:**
- `[PASS]` - Validation succeeded
- `[FAIL]` - Validation failed (counts as failure)
- `[SKIP]` - Cannot validate (doesn't count as failure)
- `[WARN]` - Potential issue (doesn't count as failure)

### Testing Validators

**Unit test pattern:**
```python
import json
from pathlib import Path
from validators import validate_latex, validate_charts, validate_links, validate_notebooks

# Load manifest
manifest_path = Path(__file__).parent.parent.parent / "manifest.json"
manifest = json.load(open(manifest_path))

# Run validators
latex_ok = validate_latex(manifest, strict=True)
charts_ok = validate_charts(manifest, regenerate=False)
links_ok = validate_links(manifest, external=False)
notebooks_ok = validate_notebooks(manifest, execute=False)

# All must pass
assert latex_ok and charts_ok and links_ok and notebooks_ok
```

**Integration test via CLI:**
```bash
# Run all validators
python infrastructure/course_cli.py validate --all

# Check exit code
echo $?  # 0 = all passed, 1 = at least one failed
```

### Performance Considerations

**Execution Times:**
- LaTeX validation: ~5-10s per topic (compilation overhead)
- Chart validation: ~30-60s total (if regenerating)
- Link validation: ~1-2s (local files only)
- Notebook validation: ~10-30s per notebook (if executing)

**Parallelization Opportunities:**
- Each topic can be validated independently
- Chart scripts can run in parallel
- Link checks can be parallelized
- Notebook execution can be parallelized

**Current Limitation:** All validators run sequentially. Future enhancement could use `multiprocessing` or `concurrent.futures` for parallel validation.

### Dependencies

**Required:**
- Python standard library (subprocess, json, pathlib, re)

**Optional (graceful degradation):**
- `pdflatex` (LaTeX validator)
- `nbformat`, `nbconvert` (notebook execution)
- `urllib` (external link checking)

**External Files:**
- `manifest.json` (required)
- `slides/L0X_Topic/*.tex` (LaTeX files)
- `slides/L0X_Topic/*/chart.py` (chart scripts)
- `notebooks/*.ipynb` (notebook files)
- `docs/*.html` (HTML files)

---

**MANUAL:** This file documents the validation subsystem. All validators return bool and follow consistent patterns. They are orchestrated via `course_cli.py validate` command.
