# Auditors Module - Full Course Audit System

<!-- Parent: ../AGENTS.md -->
<!-- Updated: 2026-02-07 -->

## Purpose

Comprehensive audit system that verifies course development completeness by comparing actual files against expected structure, manifest inventory, and plan specifications. Generates multi-format reports (console, JSON, Markdown, HTML).

**Entry Point:** `run_audit.py` in project root (imports from this module).

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `__init__.py` | Module exports | minimal | Package initialization |
| `audit_system.py` | Main audit orchestration | 555 | `run_full_audit()`, `check_directories()`, `check_python_modules()`, `run_functional_tests()` |
| `report_generator.py` | Multi-format report generation | 431 | `print_console_report()`, `generate_json_report()`, `generate_markdown_report()`, `generate_html_report()`, `generate_all_reports()` |

## For AI Agents

### Audit System Architecture

The audit system uses a **comparison-based verification model**:

```
Expected Structure          Actual Files on Disk          Audit Result
    (hardcoded)        →    (filesystem scan)      →   (missing items + recommendations)
        ↓
    manifest.json
    (inventory)
```

**Audit Flow:**
1. **Define expectations:** Directories, modules, templates, config files, content items
2. **Scan filesystem:** Check if expected files/directories exist
3. **Run functional tests:** Test CLI, manifest validity, module imports
4. **Generate recommendations:** Prioritize missing items by importance
5. **Output reports:** Console, JSON, Markdown, HTML formats

### Audit System (`audit_system.py`)

**Purpose:** Orchestrate full course audit and collect findings.

**Key Data Structures:**

```python
@dataclass
class AuditItem:
    """Single item being audited."""
    path: str                # Relative path from project root
    category: str            # "directory", "python_module", "template", "config", "content"
    expected: bool = True    # Should this exist?
    found: bool = False      # Was it found on disk?
    priority: int = 3        # 1=critical, 2=high, 3=medium, 4=low
    details: str = ""        # Additional notes

@dataclass
class FunctionalTest:
    """Result of a functional test."""
    name: str                # Test identifier
    status: str              # "pass", "fail", "skip"
    duration_ms: int = 0     # Execution time
    error: str = ""          # Error message if failed

@dataclass
class AuditResult:
    """Complete audit results."""
    metadata: Dict                        # Generation time, project info
    summary: Dict                         # Aggregate statistics
    directories: List[AuditItem]          # Directory checks
    python_modules: List[AuditItem]       # Python file checks
    templates: List[AuditItem]            # Template file checks
    config_files: List[AuditItem]         # Config file checks
    content_items: List[AuditItem]        # Content file checks
    functional_tests: List[FunctionalTest] # Test results
    missing_items: List[AuditItem]        # All missing items
    recommendations: List[Dict]           # Prioritized actions
```

**Expected Items (Hardcoded):**

The audit system defines expected structure in module-level constants:

```python
EXPECTED_DIRECTORIES = [
    "docs", "slides", "quizzes", "notebooks", "datasets",
    "infrastructure", "infrastructure/validators", "infrastructure/builders",
    "slides/L01_Introduction_Linear_Regression", "slides/L02_Logistic_Regression",
    # ... all L01-L06 slide directories
]

EXPECTED_PYTHON_MODULES = [
    "infrastructure/course_cli.py",
    "infrastructure/validators/latex_validator.py",
    "infrastructure/builders/slide_builder.py",
    # ... all infrastructure modules
]

EXPECTED_TEMPLATES = [
    "templates/beamer_template.tex",
    "templates/chart_template.py",
    # ... all templates
]

EXPECTED_CONFIG_FILES = [
    "manifest.json",
    "config.yaml",
    "README.md",
    ".gitignore"
]

CONTENT_ITEMS_PER_TOPIC = [
    "{topic}_overview.tex",
    "{topic}_deepdive.tex",
    "{topic}_instructor_guide.md"
]
```

**Audit Functions:**

**1. Directory Checks:**
```python
def check_directories(result: AuditResult) -> None:
    """Check all expected directories exist."""
    for dir_path in EXPECTED_DIRECTORIES:
        full_path = PROJECT_ROOT / dir_path
        item = AuditItem(
            path=dir_path,
            category="directory",
            found=full_path.is_dir(),
            priority=2 if "infrastructure" in dir_path else 3
        )
        result.directories.append(item)
        if not item.found:
            result.missing_items.append(item)
```

**2. Python Module Checks:**
```python
def check_python_modules(result: AuditResult) -> None:
    """Check all expected Python modules exist."""
    for mod_path in EXPECTED_PYTHON_MODULES:
        full_path = PROJECT_ROOT / mod_path
        priority = 1 if "auditors" in mod_path else 2 if "validators" in mod_path else 3
        item = AuditItem(
            path=mod_path,
            category="python_module",
            found=full_path.is_file(),
            priority=priority
        )
        # Add to results...
```

**3. Functional Tests:**
```python
def run_functional_tests(result: AuditResult) -> None:
    """Run functional tests on existing modules."""

    # Test 1: CLI --help
    try:
        proc = subprocess.run([sys.executable, "infrastructure/course_cli.py", "--help"],
                              capture_output=True, timeout=10)
        status = "pass" if proc.returncode == 0 else "fail"
    except Exception as e:
        status = "fail"
        error = str(e)
    result.functional_tests.append(FunctionalTest("cli_help", status, duration, error))

    # Test 2: Manifest valid JSON
    try:
        with open("manifest.json") as f:
            json.load(f)
        status = "pass"
    except json.JSONDecodeError:
        status = "fail"
    result.functional_tests.append(FunctionalTest("manifest_valid_json", status, ...))

    # Test 3-6: Config YAML, imports, etc.
```

**Functional Tests Included:**
1. **cli_help:** `python course_cli.py --help` returns 0
2. **manifest_valid_json:** manifest.json parses without errors
3. **config_valid_yaml:** config.yaml parses without errors (if exists)
4. **progress_report_import:** Can import progress_report module
5. **validators_importable:** Can import all validator functions
6. **builders_importable:** Can import all builder functions

**Priority Levels:**
- **Priority 1 (Critical):** Auditors, utils, config files
- **Priority 2 (High):** Validators, builders, infrastructure directories
- **Priority 3 (Medium):** Reporters, generators, content items
- **Priority 4 (Low):** Optional documentation, examples

**Recommendation Generation:**
```python
def generate_recommendations(result: AuditResult) -> None:
    """Generate prioritized recommendations based on missing items."""
    sorted_missing = sorted(result.missing_items, key=lambda x: x.priority)

    for item in sorted_missing:
        result.recommendations.append({
            "priority": item.priority,
            "action": f"Create {item.path}",
            "reason": _get_reason(item),
            "category": item.category,
            "estimated_effort": estimate_effort(item)
        })
```

**Effort Estimation:**
```python
effort_map = {
    "python_module": {1: "~50-100 lines, 30 min", 2: "~80-150 lines, 1 hour"},
    "directory": {1: "mkdir, 1 min"},
    "template": {2: "~50-200 lines, 30-60 min"},
    "content": {3: "~30-40 slides, 2-4 hours"}
}
```

**Running Full Audit:**
```python
def run_full_audit(include_functional: bool = True) -> AuditResult:
    """Run complete audit of the course development project."""
    result = AuditResult()

    # Set metadata
    result.metadata = {
        "generated": datetime.now().isoformat(),
        "project": "Methods and Algorithms",
        "version": "1.0.0"
    }

    # Run all checks
    check_directories(result)
    check_python_modules(result)
    check_templates(result)
    check_config_files(result)
    check_content_items(result)

    if include_functional:
        run_functional_tests(result)

    # Generate recommendations
    generate_recommendations(result)

    # Calculate summary statistics
    calculate_summary(result)

    return result
```

**Usage:**
```python
from auditors.audit_system import run_full_audit
from auditors.report_generator import generate_all_reports

# Run audit
result = run_full_audit(include_functional=True)

# Generate all report formats
reports = generate_all_reports(result)
```

### Report Generator (`report_generator.py`)

**Purpose:** Generate audit reports in multiple formats from AuditResult.

**Report Formats:**

**1. Console Report:**
```python
def print_console_report(result: AuditResult) -> str:
    """Generate and print console-friendly report."""
    # Format:
    # - Header with timestamp
    # - Summary statistics table
    # - Functional test results
    # - Gap analysis by priority
    # - Top 10 recommendations
```

**Output Example:**
```
============================================================
  COURSE AUDIT REPORT - Methods and Algorithms
  Generated: 2026-01-25 14:30:00
============================================================

SUMMARY
----------------------------------------
  Directories:     42/45 (93%)
  Python Modules:  28/33 (85%)
  Templates:       4/5 (80%)
  Config Files:    4/4 (100%)
  Content Items:   14/18 (78%)

FUNCTIONAL TESTS
----------------------------------------
  [PASS] cli_help
  [PASS] manifest_valid_json
  [PASS] config_valid_yaml
  [PASS] progress_report_import
  [FAIL] validators_importable - ModuleNotFoundError: chart_validator
  [PASS] builders_importable

GAP ANALYSIS
----------------------------------------
  Priority 1 (Critical):
    - infrastructure/auditors/report_generator.py
    - infrastructure/utils/retry_strategy.py

  Priority 2 (High):
    - infrastructure/validators/chart_validator.py
    - infrastructure/builders/quiz_builder.py
    ... and 3 more

RECOMMENDATIONS
----------------------------------------
  1. [1] Create infrastructure/auditors/report_generator.py
     Reason: Required for other modules to work
  2. [2] Create infrastructure/validators/chart_validator.py
     Reason: Core functionality for course management
  ... and 8 more

============================================================
```

**2. JSON Report:**
```python
def generate_json_report(result: AuditResult, output_path: Path = None) -> str:
    """Generate JSON report for machine processing."""
    report_data = {
        "metadata": result.metadata,
        "summary": result.summary,
        "functional_tests": [...],
        "missing_items": [...],
        "recommendations": [...],
        "details": {
            "directories": {"found": [...], "missing": [...]},
            "python_modules": {"found": [...], "missing": [...]},
            # ... other categories
        }
    }
    return json.dumps(report_data, indent=2)
```

**3. Markdown Report:**
```python
def generate_markdown_report(result: AuditResult, output_path: Path = None) -> str:
    """Generate Markdown report for documentation."""
    # Format:
    # - H1: Course Audit Report
    # - Table: Summary statistics
    # - Table: Functional tests
    # - H2-H4: Gap analysis by priority
    # - Numbered list: Recommendations
```

**4. HTML Dashboard:**
```python
def generate_html_report(result: AuditResult, output_path: Path = None) -> str:
    """Generate HTML dashboard report."""
    # Features:
    # - Dark theme (#0f172a background)
    # - Stat cards with color-coded progress bars
    # - Functional test results table
    # - Missing items table (top 20)
    # - Recommendations table (top 10)
    # - Priority badges (critical/high/medium)
```

**HTML Dashboard Features:**
- **Stat Cards:** Show percentages with color coding (green ≥80%, yellow 40-79%, red <40%)
- **Priority Badges:** Visual priority indicators (red=critical, orange=high, yellow=medium)
- **Tables:** Sortable tables for test results, missing items, recommendations
- **Responsive:** Grid layout adapts to screen size

**Generate All Reports:**
```python
def generate_all_reports(result: AuditResult, output_dir: Path = None) -> dict:
    """Generate all report formats at once."""
    console = print_console_report(result)
    json_report = generate_json_report(result, output_dir / "audit_report.json")
    md_report = generate_markdown_report(result, output_dir / "audit_report.md")
    html_report = generate_html_report(result, output_dir / "audit_dashboard.html")

    return {
        "console": console,
        "json": json_report,
        "markdown": md_report,
        "html": html_report
    }
```

### Running the Audit

**From Project Root:**
```bash
# Run full audit (generates JSON, MD, HTML)
python run_audit.py

# Output files created:
# - audit_report.json     (machine-readable)
# - audit_report.md       (documentation)
# - audit_dashboard.html  (visual dashboard)
```

**From Python:**
```python
from infrastructure.auditors.audit_system import run_full_audit
from infrastructure.auditors.report_generator import generate_all_reports

# Run audit
result = run_full_audit(include_functional=True)

# Generate reports
reports = generate_all_reports(result, output_dir=Path("."))

# Access individual reports
print(reports["console"])
with open("audit.json", "w") as f:
    f.write(reports["json"])
```

### Testing the Audit System

**Verify Audit Completeness:**
```python
from auditors.audit_system import run_full_audit

result = run_full_audit()

# Check all expected categories populated
assert len(result.directories) > 40
assert len(result.python_modules) > 30
assert len(result.templates) > 3
assert len(result.config_files) >= 4
assert len(result.content_items) > 12

# Check functional tests ran
assert len(result.functional_tests) == 6

# Check summary calculated
assert "directories" in result.summary
assert "python_modules" in result.summary
```

**Verify Report Generation:**
```python
from auditors.report_generator import generate_all_reports

result = run_full_audit()
reports = generate_all_reports(result)

# Check all formats generated
assert "console" in reports
assert "json" in reports
assert "markdown" in reports
assert "html" in reports

# Verify JSON is valid
import json
json_data = json.loads(reports["json"])
assert "metadata" in json_data
assert "summary" in json_data

# Verify HTML has required elements
assert "<!DOCTYPE html>" in reports["html"]
assert "Methods and Algorithms" in reports["html"]
```

### Extending the Audit System

**Add New Expected Items:**

Edit `audit_system.py` constants:
```python
EXPECTED_DIRECTORIES = [
    # ... existing directories ...
    "new_directory/subdirectory"
]

EXPECTED_PYTHON_MODULES = [
    # ... existing modules ...
    "infrastructure/new_module/new_validator.py"
]
```

**Add New Functional Tests:**

Add to `run_functional_tests()`:
```python
def run_functional_tests(result: AuditResult) -> None:
    # ... existing tests ...

    # Test 7: New functionality
    start = time.time()
    try:
        # Test code here
        status = "pass"
        error = ""
    except Exception as e:
        status = "fail"
        error = str(e)
    duration = int((time.time() - start) * 1000)
    result.functional_tests.append(FunctionalTest("new_test", status, duration, error))
```

**Add New Report Format:**

Add to `report_generator.py`:
```python
def generate_xml_report(result: AuditResult, output_path: Path = None) -> str:
    """Generate XML report."""
    xml = '<?xml version="1.0"?>\n<audit>\n'
    # ... generate XML content ...
    xml += '</audit>'

    if output_path:
        output_path.write_text(xml)

    return xml
```

### Performance Considerations

**Audit Execution Time:**
- Directory checks: ~100ms (filesystem operations)
- File existence checks: ~500ms (300+ files)
- Functional tests: ~2-5s (subprocess overhead)
- Report generation: ~100ms per format
- **Total:** ~5-10 seconds for full audit

**Optimization Opportunities:**
- **Parallel checking:** Use multiprocessing for file existence checks
- **Caching:** Cache audit results, regenerate only on manifest change
- **Incremental audits:** Only check changed files since last audit

### Dependencies

**Required:**
- Python standard library (subprocess, json, pathlib, dataclasses, datetime)

**Optional:**
- `yaml` (for config.yaml validation test)

**External Files:**
- `manifest.json` (required for content checks)
- All course files (for existence checks)
- `config.yaml` (optional, for YAML validation test)

### Common Issues

**"Module not found" in functional tests:**
- Ensure `sys.path` includes infrastructure directory
- Check `__init__.py` files exist in all packages
- Verify imports in `__init__.py` match module names

**False positives (item marked missing but exists):**
- Check path spelling and case sensitivity (Windows vs Linux)
- Verify PROJECT_ROOT is calculated correctly
- Check for symlinks or unusual filesystem setups

**Functional tests timeout:**
- Increase timeout in `subprocess.run(timeout=10)`
- Check for infinite loops in CLI code
- Verify subprocess calls don't hang

---

**MANUAL:** This file documents the audit subsystem for comprehensive course verification. The audit system compares expected structure against actual files, runs functional tests, and generates multi-format reports. Run via `python run_audit.py` from project root.
