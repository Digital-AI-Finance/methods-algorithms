# Reporters Module - Progress and Quality Reporting

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 -->

## Purpose

Reporting subsystem for generating progress dashboards, quality metrics, and status reports. Outputs include console text, HTML dashboards, and structured data.

**All reporters return `str`:** Formatted output (text, HTML, JSON).

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `__init__.py` | Module exports | 15 | Exports all report generators |
| `progress_report.py` | Text-based progress dashboard | 109 | `generate_progress_report()` |
| `html_dashboard.py` | Interactive HTML dashboard | 355 | `generate_html_dashboard()`, `_collect_all_stats()` |
| `build_report.py` | Build status report | TBD | `generate_build_report()` (stub) |
| `coverage_report.py` | Content coverage metrics | TBD | `generate_coverage_report()` (stub) |
| `quality_report.py` | Quality metrics and scores | TBD | `generate_quality_report()` (stub) |

## For AI Agents

### Module Architecture

All reporters follow a **consistent pattern**:

```python
def generate_<type>_report(manifest: dict, **options) -> str:
    """
    Generate <type> report.

    Args:
        manifest: Course manifest
        **options: Reporter-specific options (detailed, format, etc.)

    Returns:
        Formatted report string (text, HTML, JSON, etc.)
    """
    # Collect statistics
    # Format output
    # Return formatted string
```

### Progress Report (`progress_report.py`)

**Purpose:** Generate console-friendly progress dashboard showing completion status.

**Key Features:**
- Shows overall course progress (topics complete)
- Lists all topics with status icons
- **Detailed mode:** Shows asset-level breakdown
- Includes quizzes, presentations, and capstone status

**Usage:**
```bash
# Basic progress report
python infrastructure/course_cli.py status

# Detailed report with asset breakdown
python infrastructure/course_cli.py status --detailed
```

**Output Format:**

```
============================================================
  Methods and Algorithms - Progress Report
  Version: 1.0.0 | 2026-01-25 14:30
============================================================

OVERALL PROGRESS
----------------------------------------
  Topics: 4/6 complete (66%)
    - Complete: 4
    - In Review: 1
    - Pending: 1

TOPICS
----------------------------------------
  [X] L01: Introduction & Linear Regression
  [X] L02: Logistic Regression
  [X] L03: KNN & K-Means
  [X] L04: Random Forests
  [~] L05: PCA & t-SNE
  [ ] L06: Embeddings & RL

QUIZZES
----------------------------------------
  [X] Q01: Quiz 1 (L01-L02)
  [ ] Q02: Quiz 2 (L03-L04)
  [ ] Q03: Quiz 3 (L05-L06)

PRESENTATIONS
----------------------------------------
  [X] 6 topics (presentations/topics.md)

CAPSTONE
----------------------------------------
  [X] Specification: capstone/specification.md

============================================================
```

**Status Icons:**
- `[X]` - Complete
- `[~]` - In Review
- `[.]` - Draft
- `[ ]` - Pending

**Detailed Mode:**
Shows per-topic asset breakdown:
```
  [X] L01: Introduction & Linear Regression
       overview_slides: [X] slides/L01.../L01_overview.tex
       deepdive_slides: [X] slides/L01.../L01_deepdive.tex
       notebook: [X] notebooks/L01_linear_regression.ipynb
       Assets: 8/8
```

**Statistics Collected:**
- Total topics vs. completed topics
- Topics by status (complete, review, pending)
- Asset existence checks (file on disk)
- Quiz/presentation/capstone status

**Testing:**
```python
from reporters import generate_progress_report
manifest = json.load(open("manifest.json"))

# Basic report
report = generate_progress_report(manifest, detailed=False)
print(report)

# Detailed report
detailed = generate_progress_report(manifest, detailed=True)
print(detailed)
```

### HTML Dashboard (`html_dashboard.py`)

**Purpose:** Generate interactive HTML dashboard with progress bars and statistics.

**Key Features:**
- Real-time progress visualization
- Stat cards for topics, modules, charts, tests
- Color-coded progress bars (green/yellow/red)
- Topic table with slide/chart/notebook status
- Infrastructure component status table

**Usage:**
```bash
# Generate and save to file
python infrastructure/course_cli.py report dashboard --output progress.html
```

**Dashboard Sections:**

1. **Header:**
   - Course title
   - Version and generation timestamp

2. **Stat Cards:**
   - Topics (complete/total)
   - Python Modules (exist/total)
   - Charts (built/total)
   - Functional Tests (pass/total)

3. **Topic Progress Table:**
   - Topic ID and title
   - Status badge (complete/review/pending)
   - Slides status (Yes/No)
   - Charts count (built/total)
   - Notebook status (Yes/No)

4. **Infrastructure Status Table:**
   - Component name (Validators, Builders, etc.)
   - Files count (exist/total)
   - Status badge

**Color Coding:**
- **Green (success):** ≥80% complete
- **Yellow (warning):** 40-79% complete
- **Red (danger):** <40% complete

**Statistics Collection:**
```python
stats = {
    "topics_total": len(manifest["topics"]),
    "topics_complete": count_complete_topics(),
    "modules_total": 33,
    "modules_exist": count_existing_modules(),
    "charts_total": sum(len(t["assets"]["charts"]) for t in topics),
    "charts_built": count_built_charts(),
    "tests_total": 6,
    "tests_pass": 0  # Updated from audit
}
```

**File Checks:**
- **Slides:** Check if `L01_overview.pdf` and `L01_deepdive.pdf` exist
- **Charts:** Check if `chart.pdf` exists in each chart folder
- **Notebooks:** Check if notebook file exists in notebooks/
- **Modules:** Count .py files in infrastructure/

**Testing:**
```python
from reporters import generate_html_dashboard
from pathlib import Path

manifest = json.load(open("manifest.json"))

# Generate HTML
html = generate_html_dashboard(manifest)

# Save to file
output_path = Path("progress_dashboard.html")
html = generate_html_dashboard(manifest, output_path=output_path)
```

### Build Report (`build_report.py`)

**Purpose:** Report on build status and errors (STUB - not yet implemented).

**Planned Features:**
- List all build targets (slides, charts, notebooks, quizzes)
- Show last build time for each target
- Report build errors and warnings
- Show build duration statistics

**Future Usage:**
```bash
python infrastructure/course_cli.py report build
```

**Planned Output:**
```
BUILD REPORT - Last 24 hours
============================================================
SLIDES
  [PASS] L01_overview.pdf (built 2h ago, 12s)
  [PASS] L01_deepdive.pdf (built 2h ago, 15s)
  [FAIL] L06_overview.pdf (LaTeX error: undefined control sequence)

CHARTS
  [PASS] 42/45 charts built successfully
  [FAIL] L06/01_embedding_viz/chart.py (ImportError: torch)

NOTEBOOKS
  [SKIP] Not yet implemented

QUIZZES
  [SKIP] Not yet implemented
```

### Coverage Report (`coverage_report.py`)

**Purpose:** Report on content coverage metrics (STUB - not yet implemented).

**Planned Features:**
- Count slides per topic (target: 17 overview, 30 deepdive)
- Count charts per topic (target: 7-8)
- Check if all PMSP sections present
- Check if instructor guide exists

**Future Usage:**
```bash
python infrastructure/course_cli.py report coverage
```

**Planned Metrics:**
- **Slide count:** Actual vs. target per topic
- **Chart count:** Actual vs. target per topic
- **PMSP coverage:** Problem/Method/Solution/Practice sections
- **Documentation:** Instructor guides, rubrics, solutions
- **External resources:** Datasets, notebook links

### Quality Report (`quality_report.py`)

**Purpose:** Generate quality metrics and scores (STUB - not yet implemented).

**Planned Features:**
- LaTeX warnings and overflow counts
- Chart generation errors
- Notebook execution failures
- Link checker results
- Overall quality score (0-100)

**Future Usage:**
```bash
python infrastructure/course_cli.py report quality
```

**Planned Metrics:**
- **LaTeX Quality:**
  - Overflow warnings per slide file
  - Compilation errors
  - Average slides per topic
- **Chart Quality:**
  - Generation success rate
  - PDF file sizes (detect missing content)
  - Script execution time
- **Notebook Quality:**
  - Execution success rate
  - Cell output completeness
  - Code style violations
- **Overall Score:**
  - 100 = all green, no warnings
  - 80-99 = minor warnings
  - 60-79 = some errors
  - <60 = major issues

### Common Reporter Patterns

**1. Statistics Collection:**
```python
def _collect_stats(manifest: dict) -> dict:
    stats = {}
    for topic in manifest["topics"]:
        # Count assets
        # Check files exist
        # Aggregate totals
    return stats
```

**2. Progress Bar Generation:**
```python
def _calc_percent(current: int, total: int) -> int:
    if total == 0:
        return 0
    return int(100 * current / total)

def _get_progress_class(current: int, total: int) -> str:
    pct = 100 * current / total
    if pct >= 80:
        return "success"
    elif pct >= 40:
        return "warning"
    return "danger"
```

**3. Status Icon Mapping:**
```python
status_icon = {
    "complete": "[X]",
    "review": "[~]",
    "pending": "[ ]",
    "draft": "[.]"
}.get(status, "[ ]")
```

**4. File Existence Checks:**
```python
def _check_file_exists(relative_path: str) -> bool:
    full_path = PROJECT_ROOT / relative_path
    return full_path.exists() and full_path.stat().st_size > 0
```

### HTML Generation Patterns

**Inline CSS Styling:**
All HTML reporters use inline CSS for portability (no external dependencies):

```python
html = f'''<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: sans-serif; }}
        .stat-card {{ background: white; border-radius: 12px; }}
        .progress-bar {{ height: 8px; background: #e0e0e0; }}
        .fill {{ background: {color}; width: {percent}%; }}
    </style>
</head>
<body>
    {content}
</body>
</html>'''
```

**Color Palette:**
- Primary: `#3b82f6` (blue)
- Success: `#22c55e` (green)
- Warning: `#f59e0b` (orange)
- Danger: `#ef4444` (red)
- Background: `#f8fafc` (light gray)
- Card: `#ffffff` (white)
- Text: `#1e293b` (dark gray)
- Border: `#e2e8f0` (light border)

**Responsive Grid Layout:**
```css
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
}
```

### Testing Reporters

**Visual Testing:**
1. Generate HTML report
2. Open in browser
3. Verify:
   - All sections render correctly
   - Progress bars display accurate percentages
   - Colors match completion status
   - Tables are readable and sortable

**Output Testing:**
```python
from reporters import generate_progress_report, generate_html_dashboard

manifest = json.load(open("manifest.json"))

# Test progress report
report = generate_progress_report(manifest, detailed=True)
assert "OVERALL PROGRESS" in report
assert "TOPICS" in report
assert len(report.split("\n")) > 20  # Reasonable line count

# Test HTML dashboard
html = generate_html_dashboard(manifest)
assert "<!DOCTYPE html>" in html
assert "Methods and Algorithms" in html
assert ".stat-card" in html  # CSS present
```

**Integration Testing:**
```bash
# Generate all reports
python infrastructure/course_cli.py report progress > progress.txt
python infrastructure/course_cli.py report build > build.txt
python infrastructure/course_cli.py report coverage > coverage.txt
python infrastructure/course_cli.py report quality > quality.txt

# Check outputs exist and are non-empty
test -s progress.txt && echo "Progress report OK"
```

### Performance Considerations

**File System Overhead:**
- Reporters check file existence for every asset
- Can be slow if checking 100+ files
- Consider caching results in session

**HTML Generation:**
- String concatenation is fast for small reports
- Use template engine (Jinja2) for complex layouts
- Consider pre-rendering static sections

**Statistics Computation:**
- Most stats require full manifest traversal
- Cache statistics in memory for repeated calls
- Update cache only when manifest changes

### Dependencies

**Required:**
- Python standard library (json, pathlib, datetime)

**Optional:**
- None (all reporters use inline CSS, no external dependencies)

**External Files:**
- `manifest.json` (required)
- Course content files (for existence checks)

---

**MANUAL:** This file documents the reporter subsystem for progress dashboards and quality metrics. Reporters generate text and HTML output showing course completion status. They are orchestrated via `course_cli.py status` and `course_cli.py report` commands.
