# Builders Module - Content Generation

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 -->

## Purpose

Build subsystem for generating course content from source files. Compiles LaTeX slides, runs chart scripts, builds notebooks, and generates quizzes.

**All builders return `bool`:** `True` = build succeeded, `False` = build failed.

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `__init__.py` | Module exports | 8 | Exports all build functions |
| `slide_builder.py` | Compile LaTeX to PDF slides | 99 | `build_slides()`, `_compile_latex()` |
| `chart_builder.py` | Execute chart.py scripts | 78 | `build_charts()`, `_run_chart_script()` |
| `notebook_builder.py` | Build/process Jupyter notebooks | TBD | `build_notebooks()` (stub) |
| `quiz_builder.py` | Generate quiz XML from templates | TBD | `build_quizzes()` (stub) |

## For AI Agents

### Module Architecture

All builders follow a **consistent pattern**:

```python
def build_<type>(manifest: dict, topic: str = None, verbose: bool = False) -> bool:
    """
    Build <type> content.

    Args:
        manifest: Course manifest
        topic: Topic ID to build (None = all topics)
        verbose: Show detailed output

    Returns:
        True if all builds succeed
    """
    all_passed = True
    topics = manifest["topics"]

    if topic:
        topics = [t for t in topics if t["id"] == topic]

    for t in topics:
        # Build content for this topic
        # Update all_passed flag

    return all_passed
```

### Slide Builder (`slide_builder.py`)

**Purpose:** Compile LaTeX Beamer slides to PDF using pdflatex.

**Key Features:**
- Compiles both `*_overview.tex` and `*_deepdive.tex` per topic
- Runs pdflatex **twice** (for references/cross-refs)
- Moves auxiliary files to `temp/` subdirectory
- Supports single-topic builds via `--topic` flag

**Usage:**
```bash
# Build all slides
python infrastructure/course_cli.py build slides

# Build single topic
python infrastructure/course_cli.py build slides --topic L01

# Verbose output
python infrastructure/course_cli.py build slides --topic L01 --verbose
```

**Build Process:**

1. **Locate .tex files:**
   ```
   slides/L01_Introduction_Linear_Regression/L01_overview.tex
   slides/L01_Introduction_Linear_Regression/L01_deepdive.tex
   ```

2. **Compile LaTeX:**
   ```bash
   pdflatex -interaction=nonstopmode L01_overview.tex
   pdflatex -interaction=nonstopmode L01_overview.tex  # Second pass for refs
   ```

3. **Clean up auxiliary files:**
   Move to `temp/` subdirectory:
   - `.aux` - Auxiliary data
   - `.log` - Compilation log
   - `.nav` - Navigation (Beamer)
   - `.out` - PDF bookmarks
   - `.snm` - Snippet names (Beamer)
   - `.toc` - Table of contents
   - `.vrb` - Verbatim content

4. **Verify PDF created:**
   Check that `.pdf` file exists in same directory as `.tex` source.

**Status Codes:**
- `[PASS]` - PDF generated successfully
- `[FAIL]` - Compilation failed or PDF not created
- `[SKIP]` - .tex file not found or pdflatex not installed

**Error Handling:**
- `FileNotFoundError` → pdflatex not installed (skip, don't fail)
- `subprocess.TimeoutExpired` → compilation timeout (120s limit)
- `returncode != 0` → LaTeX error (fail with error message)

**Testing:**
```python
from builders import build_slides
manifest = json.load(open("manifest.json"))

# Build one topic
success = build_slides(manifest, topic="L01", verbose=True)

# Build all topics
success = build_slides(manifest)
```

### Chart Builder (`chart_builder.py`)

**Purpose:** Execute chart.py scripts to generate chart.pdf files.

**Key Features:**
- Runs each chart's `chart.py` script via subprocess
- Sets working directory to chart folder
- Verifies `chart.pdf` output
- Supports single-topic builds

**Usage:**
```bash
# Build all charts
python infrastructure/course_cli.py build charts

# Build charts for one topic
python infrastructure/course_cli.py build charts --topic L01

# Verbose output
python infrastructure/course_cli.py build charts --topic L01 --verbose
```

**Build Process:**

1. **Iterate through chart assets:**
   ```python
   for chart in topic["assets"]["charts"]:
       chart_file = chart["file"]  # e.g., "slides/L01.../01_simple_regression/chart.py"
   ```

2. **Execute chart script:**
   ```bash
   python slides/L01_Introduction_Linear_Regression/01_simple_regression/chart.py
   ```
   - Working directory: chart folder (where chart.py lives)
   - Timeout: 120 seconds
   - Capture stdout/stderr

3. **Verify output:**
   - Check `chart.pdf` exists in same folder
   - Check file size > 0 bytes
   - Print file size on success

**Status Codes:**
- `[PASS]` - chart.pdf generated (shows size in bytes)
- `[FAIL]` - Script error, timeout, or PDF not created
- `[SKIP]` - chart.py not found

**Chart Requirements:**
Each `chart.py` must:
- Be executable as standalone script
- Generate exactly one `chart.pdf` in same directory
- Use `plt.savefig("chart.pdf", format="pdf", bbox_inches="tight")`
- Not require command-line arguments

**Testing:**
```python
from builders import build_charts
manifest = json.load(open("manifest.json"))

# Build all charts
success = build_charts(manifest, verbose=False)

# Build one topic
success = build_charts(manifest, topic="L01", verbose=True)
```

### Notebook Builder (`notebook_builder.py`)

**Purpose:** Build and process Jupyter notebooks (STUB - not yet implemented).

**Planned Features:**
- Generate notebooks from templates
- Execute notebooks and save outputs
- Convert notebooks to HTML/PDF
- Inject dataset paths and imports

**Future Usage:**
```bash
# Build all notebooks
python infrastructure/course_cli.py build notebooks

# Build for one topic
python infrastructure/course_cli.py build notebooks --topic L01
```

**Implementation Notes:**
- Will use `nbformat` for notebook manipulation
- Will use `nbconvert` for execution/conversion
- Should support template variables (dataset paths, imports)
- Should validate notebook executes without errors

### Quiz Builder (`quiz_builder.py`)

**Purpose:** Generate quiz XML from templates (STUB - not yet implemented).

**Planned Features:**
- Generate Moodle XML from quiz definitions
- Support multiple question types (MC, short answer, etc.)
- Validate quiz structure
- Export to multiple formats (Moodle, Canvas, etc.)

**Future Usage:**
```bash
# Build all quizzes
python infrastructure/course_cli.py build quizzes

# Build specific quiz
python infrastructure/course_cli.py build quizzes --id Q01
```

**Implementation Notes:**
- Will read quiz definitions from YAML or JSON
- Will use template files for each question type
- Should validate XML against Moodle schema
- Should support randomization of answer order

### Common Build Patterns

**1. Two-Pass Compilation:**
LaTeX requires two passes for cross-references:
```python
for i in range(2):
    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", str(tex_path)],
        cwd=tex_path.parent,
        capture_output=not verbose,
        timeout=120
    )
    if result.returncode != 0 and i == 1:
        # Only fail on second pass
        return False
```

**2. Working Directory Management:**
Always set `cwd=` to the directory containing the source file:
```python
subprocess.run(
    [command, source_file.name],  # Use filename only
    cwd=source_file.parent,       # Set working directory
    ...
)
```

**3. Auxiliary File Cleanup:**
Move build artifacts to temp/ folder:
```python
temp_dir = source_path.parent / "temp"
temp_dir.mkdir(exist_ok=True)

for ext in [".aux", ".log", ".nav", ".out", ".snm", ".toc", ".vrb"]:
    aux_file = source_path.with_suffix(ext)
    if aux_file.exists():
        shutil.move(str(aux_file), str(temp_dir / aux_file.name))
```

**4. Progress Messages:**
```python
print(f"  Compiling {tex_path.name}...")
# ... run build ...
print(f"    [PASS] {pdf_path.name}")
```

### Build Dependencies

**Slide Builder Dependencies:**
- `pdflatex` (TeX Live or MiKTeX)
- LaTeX packages: beamer, graphicx, hyperref, amsmath
- Chart PDFs must exist before slides are compiled

**Chart Builder Dependencies:**
- Python 3.7+
- matplotlib, numpy, pandas (in chart scripts)
- Dataset files (if charts load data)

**Build Order:**
1. **Charts first** - Generate all chart PDFs
2. **Slides second** - Compile LaTeX (references chart PDFs)
3. **Notebooks** - Can be built anytime (independent)
4. **Quizzes** - Can be built anytime (independent)

### Testing Builders

**Integration test:**
```bash
# Full build sequence
python infrastructure/course_cli.py build charts
python infrastructure/course_cli.py build slides
python infrastructure/course_cli.py build notebooks
python infrastructure/course_cli.py build quizzes

# Or use "all" command
python infrastructure/course_cli.py build all
```

**Unit test pattern:**
```python
import json
from pathlib import Path
from builders import build_slides, build_charts

manifest_path = Path(__file__).parent.parent.parent / "manifest.json"
manifest = json.load(open(manifest_path))

# Test single topic
charts_ok = build_charts(manifest, topic="L01", verbose=False)
assert charts_ok, "Chart build failed"

slides_ok = build_slides(manifest, topic="L01", verbose=False)
assert slides_ok, "Slide build failed"
```

**Verify outputs:**
```python
from pathlib import Path

topic_dir = Path("slides/L01_Introduction_Linear_Regression")

# Check overview PDF
assert (topic_dir / "L01_overview.pdf").exists()

# Check deepdive PDF
assert (topic_dir / "L01_deepdive.pdf").exists()

# Check chart PDFs
assert (topic_dir / "01_simple_regression/chart.pdf").exists()
```

### Performance Considerations

**Build Times:**
- Chart building: ~5s per chart (matplotlib overhead)
- Slide compilation: ~10-15s per .tex file (pdflatex is slow)
- Total for one topic: ~30-45s (7-8 charts + 2 slide files)

**Parallelization:**
- **Charts:** Can build in parallel (independent scripts)
- **Slides:** Must build sequentially (pdflatex not thread-safe)
- **Future:** Use multiprocessing.Pool for chart building

**Incremental Builds:**
- Check if source file is newer than output
- Skip build if output is up-to-date
- Use file modification times or content hashes

### Error Recovery

**Partial Build Failures:**
- Continue building other topics even if one fails
- Collect all errors and report at end
- Return overall success/failure status

**Cleanup on Failure:**
- Don't delete partial outputs (useful for debugging)
- Leave auxiliary files in place for inspection
- Log full error messages to build.log

**Retry Strategy:**
- LaTeX errors are usually permanent (don't retry)
- Chart errors might be transient (network issues, random seed)
- Consider implementing retry with exponential backoff

### Dependencies

**Required:**
- Python standard library (subprocess, shutil, pathlib, sys)

**Optional (graceful degradation):**
- `pdflatex` (slide builder)
- Chart script dependencies (matplotlib, numpy, pandas)

**External Files:**
- `manifest.json` (required)
- `slides/L0X_Topic/*.tex` (LaTeX sources)
- `slides/L0X_Topic/*/chart.py` (chart scripts)
- `templates/` (for notebook/quiz builders)

---

**MANUAL:** This file documents the builder subsystem for content generation. Builders compile LaTeX, execute chart scripts, and generate notebooks/quizzes. They are orchestrated via `course_cli.py build` command.
