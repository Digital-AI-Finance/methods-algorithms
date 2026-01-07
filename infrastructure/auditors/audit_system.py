"""
Main audit system orchestration for Methods and Algorithms course.

Verifies what has been completed by comparing:
- Actual files on disk
- Plan file specifications
- manifest.json inventory
"""
import json
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).parent.parent.parent


@dataclass
class AuditItem:
    """Single item being audited."""
    path: str
    category: str
    expected: bool = True
    found: bool = False
    priority: int = 3
    details: str = ""


@dataclass
class FunctionalTest:
    """Result of a functional test."""
    name: str
    status: str  # "pass", "fail", "skip"
    duration_ms: int = 0
    error: str = ""


@dataclass
class AuditResult:
    """Complete audit results."""
    metadata: Dict = field(default_factory=dict)
    summary: Dict = field(default_factory=dict)
    directories: List[AuditItem] = field(default_factory=list)
    python_modules: List[AuditItem] = field(default_factory=list)
    templates: List[AuditItem] = field(default_factory=list)
    config_files: List[AuditItem] = field(default_factory=list)
    content_items: List[AuditItem] = field(default_factory=list)
    functional_tests: List[FunctionalTest] = field(default_factory=list)
    missing_items: List[AuditItem] = field(default_factory=list)
    recommendations: List[Dict] = field(default_factory=list)


# Expected directories (from plan)
EXPECTED_DIRECTORIES = [
    # Root level
    "docs", "docs/css", "docs/js", "docs/assets",
    "slides", "quizzes", "notebooks", "datasets",
    "presentations", "capstone", "capstone/examples",
    "rubrics", "syllabus", "templates",
    # Infrastructure
    "infrastructure", "infrastructure/validators", "infrastructure/builders",
    "infrastructure/reporters", "infrastructure/deployers", "infrastructure/generators",
    "infrastructure/auditors", "infrastructure/downloaders", "infrastructure/trackers",
    "infrastructure/utils", "infrastructure/reporters/dashboard_assets",
    # Slide folders (L01-L06)
    "slides/L01_Introduction_Linear_Regression",
    "slides/L01_Introduction_Linear_Regression/temp",
    "slides/L02_Logistic_Regression",
    "slides/L02_Logistic_Regression/temp",
    "slides/L03_KNN_KMeans",
    "slides/L03_KNN_KMeans/temp",
    "slides/L04_Random_Forests",
    "slides/L04_Random_Forests/temp",
    "slides/L05_PCA_tSNE",
    "slides/L05_PCA_tSNE/temp",
    "slides/L06_Embeddings_RL",
    "slides/L06_Embeddings_RL/temp",
]

# Expected Python modules
EXPECTED_PYTHON_MODULES = [
    # CLI
    "infrastructure/course_cli.py",
    # Validators
    "infrastructure/validators/__init__.py",
    "infrastructure/validators/latex_validator.py",
    "infrastructure/validators/link_validator.py",
    "infrastructure/validators/notebook_validator.py",
    "infrastructure/validators/chart_validator.py",
    # Builders
    "infrastructure/builders/__init__.py",
    "infrastructure/builders/slide_builder.py",
    "infrastructure/builders/chart_builder.py",
    "infrastructure/builders/notebook_builder.py",
    "infrastructure/builders/quiz_builder.py",
    # Reporters
    "infrastructure/reporters/__init__.py",
    "infrastructure/reporters/build_report.py",
    "infrastructure/reporters/coverage_report.py",
    "infrastructure/reporters/progress_report.py",
    "infrastructure/reporters/quality_report.py",
    "infrastructure/reporters/html_dashboard.py",
    # Deployers
    "infrastructure/deployers/__init__.py",
    "infrastructure/deployers/github_deployer.py",
    "infrastructure/deployers/colab_deployer.py",
    # Generators
    "infrastructure/generators/__init__.py",
    "infrastructure/generators/syllabus_generator.py",
    "infrastructure/generators/rubric_generator.py",
    "infrastructure/generators/guide_generator.py",
    # Auditors (this module)
    "infrastructure/auditors/__init__.py",
    "infrastructure/auditors/audit_system.py",
    # Downloaders
    "infrastructure/downloaders/__init__.py",
    "infrastructure/downloaders/pdf_downloader.py",
    # Trackers
    "infrastructure/trackers/__init__.py",
    "infrastructure/trackers/activity_log.py",
    # Utils
    "infrastructure/utils/__init__.py",
    "infrastructure/utils/retry_strategy.py",
    "infrastructure/utils/hash_utils.py",
]

# Expected templates
EXPECTED_TEMPLATES = [
    "templates/beamer_template.tex",
    "templates/chart_template.py",
    "templates/notebook_template.ipynb",
    "templates/quiz_template.xml",
    "templates/instructor_guide_template.md",
]

# Expected config files
EXPECTED_CONFIG_FILES = [
    "manifest.json",
    "config.yaml",
    "README.md",
    ".gitignore",
]

# Content items per topic
CONTENT_ITEMS_PER_TOPIC = [
    "{topic}_overview.tex",
    "{topic}_deepdive.tex",
    "{topic}_instructor_guide.md",
]


def check_directories(result: AuditResult) -> None:
    """Check all expected directories exist."""
    for dir_path in EXPECTED_DIRECTORIES:
        full_path = PROJECT_ROOT / dir_path
        item = AuditItem(
            path=dir_path,
            category="directory",
            expected=True,
            found=full_path.is_dir(),
            priority=2 if "infrastructure" in dir_path else 3
        )
        result.directories.append(item)
        if not item.found:
            result.missing_items.append(item)


def check_python_modules(result: AuditResult) -> None:
    """Check all expected Python modules exist."""
    for mod_path in EXPECTED_PYTHON_MODULES:
        full_path = PROJECT_ROOT / mod_path

        # Determine priority
        if "auditors" in mod_path or "utils" in mod_path:
            priority = 1
        elif "validators" in mod_path or "builders" in mod_path:
            priority = 2
        else:
            priority = 3

        item = AuditItem(
            path=mod_path,
            category="python_module",
            expected=True,
            found=full_path.is_file(),
            priority=priority
        )
        result.python_modules.append(item)
        if not item.found:
            result.missing_items.append(item)


def check_templates(result: AuditResult) -> None:
    """Check all expected templates exist."""
    for tmpl_path in EXPECTED_TEMPLATES:
        full_path = PROJECT_ROOT / tmpl_path
        item = AuditItem(
            path=tmpl_path,
            category="template",
            expected=True,
            found=full_path.is_file(),
            priority=2
        )
        result.templates.append(item)
        if not item.found:
            result.missing_items.append(item)


def check_config_files(result: AuditResult) -> None:
    """Check config files exist and are valid."""
    for cfg_path in EXPECTED_CONFIG_FILES:
        full_path = PROJECT_ROOT / cfg_path
        item = AuditItem(
            path=cfg_path,
            category="config",
            expected=True,
            found=full_path.is_file(),
            priority=1
        )
        result.config_files.append(item)
        if not item.found:
            result.missing_items.append(item)


def check_content_items(result: AuditResult) -> None:
    """Check content items for each topic."""
    topics = ["L01", "L02", "L03", "L04", "L05", "L06"]
    topic_dirs = {
        "L01": "slides/L01_Introduction_Linear_Regression",
        "L02": "slides/L02_Logistic_Regression",
        "L03": "slides/L03_KNN_KMeans",
        "L04": "slides/L04_Random_Forests",
        "L05": "slides/L05_PCA_tSNE",
        "L06": "slides/L06_Embeddings_RL",
    }

    for topic in topics:
        topic_dir = topic_dirs[topic]
        for item_template in CONTENT_ITEMS_PER_TOPIC:
            item_name = item_template.format(topic=topic)
            item_path = f"{topic_dir}/{item_name}"
            full_path = PROJECT_ROOT / item_path

            item = AuditItem(
                path=item_path,
                category="content",
                expected=True,
                found=full_path.is_file(),
                priority=3
            )
            result.content_items.append(item)
            if not item.found:
                result.missing_items.append(item)


def run_functional_tests(result: AuditResult) -> None:
    """Run functional tests on existing modules."""
    import time

    # Test 1: CLI --help
    start = time.time()
    try:
        cli_path = PROJECT_ROOT / "infrastructure" / "course_cli.py"
        if cli_path.exists():
            proc = subprocess.run(
                [sys.executable, str(cli_path), "--help"],
                capture_output=True,
                timeout=10
            )
            status = "pass" if proc.returncode == 0 else "fail"
            error = proc.stderr.decode() if proc.returncode != 0 else ""
        else:
            status = "skip"
            error = "CLI not found"
    except Exception as e:
        status = "fail"
        error = str(e)
    duration = int((time.time() - start) * 1000)
    result.functional_tests.append(FunctionalTest("cli_help", status, duration, error))

    # Test 2: Manifest valid JSON
    start = time.time()
    try:
        manifest_path = PROJECT_ROOT / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path) as f:
                json.load(f)
            status = "pass"
            error = ""
        else:
            status = "skip"
            error = "manifest.json not found"
    except json.JSONDecodeError as e:
        status = "fail"
        error = str(e)
    except Exception as e:
        status = "fail"
        error = str(e)
    duration = int((time.time() - start) * 1000)
    result.functional_tests.append(FunctionalTest("manifest_valid_json", status, duration, error))

    # Test 3: Config valid YAML
    start = time.time()
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if config_path.exists():
            with open(config_path) as f:
                yaml.safe_load(f)
            status = "pass"
            error = ""
        else:
            status = "skip"
            error = "config.yaml not found"
    except Exception as e:
        status = "fail"
        error = str(e)
    duration = int((time.time() - start) * 1000)
    result.functional_tests.append(FunctionalTest("config_valid_yaml", status, duration, error))

    # Test 4: Progress report importable
    start = time.time()
    try:
        sys.path.insert(0, str(PROJECT_ROOT / "infrastructure"))
        from reporters import generate_progress_report
        status = "pass"
        error = ""
    except ImportError as e:
        status = "fail"
        error = str(e)
    except Exception as e:
        status = "fail"
        error = str(e)
    finally:
        if str(PROJECT_ROOT / "infrastructure") in sys.path:
            sys.path.remove(str(PROJECT_ROOT / "infrastructure"))
    duration = int((time.time() - start) * 1000)
    result.functional_tests.append(FunctionalTest("progress_report_import", status, duration, error))

    # Test 5: Validators importable
    start = time.time()
    try:
        sys.path.insert(0, str(PROJECT_ROOT / "infrastructure"))
        validators_init = PROJECT_ROOT / "infrastructure" / "validators" / "__init__.py"
        if validators_init.exists():
            from validators import validate_latex, validate_links, validate_notebooks, validate_charts
            status = "pass"
            error = ""
        else:
            status = "skip"
            error = "validators/__init__.py not found"
    except ImportError as e:
        status = "fail"
        error = str(e)
    except Exception as e:
        status = "fail"
        error = str(e)
    finally:
        if str(PROJECT_ROOT / "infrastructure") in sys.path:
            sys.path.remove(str(PROJECT_ROOT / "infrastructure"))
    duration = int((time.time() - start) * 1000)
    result.functional_tests.append(FunctionalTest("validators_importable", status, duration, error))

    # Test 6: Builders importable
    start = time.time()
    try:
        sys.path.insert(0, str(PROJECT_ROOT / "infrastructure"))
        builders_init = PROJECT_ROOT / "infrastructure" / "builders" / "__init__.py"
        if builders_init.exists():
            from builders import build_slides, build_charts, build_notebooks, build_quizzes
            status = "pass"
            error = ""
        else:
            status = "skip"
            error = "builders/__init__.py not found"
    except ImportError as e:
        status = "fail"
        error = str(e)
    except Exception as e:
        status = "fail"
        error = str(e)
    finally:
        if str(PROJECT_ROOT / "infrastructure") in sys.path:
            sys.path.remove(str(PROJECT_ROOT / "infrastructure"))
    duration = int((time.time() - start) * 1000)
    result.functional_tests.append(FunctionalTest("builders_importable", status, duration, error))


def estimate_effort(item: AuditItem) -> str:
    """Estimate effort required to create missing item."""
    effort_map = {
        "python_module": {
            1: "~50-100 lines, 30 min",
            2: "~80-150 lines, 1 hour",
            3: "~50-100 lines, 30 min",
        },
        "directory": {
            1: "mkdir, 1 min",
            2: "mkdir, 1 min",
            3: "mkdir, 1 min",
        },
        "template": {
            2: "~50-200 lines, 30-60 min",
        },
        "config": {
            1: "~20-100 lines, 15-30 min",
        },
        "content": {
            3: "~30-40 slides, 2-4 hours",
        }
    }
    return effort_map.get(item.category, {}).get(item.priority, "varies")


def generate_recommendations(result: AuditResult) -> None:
    """Generate prioritized recommendations based on missing items."""
    # Sort missing items by priority
    sorted_missing = sorted(result.missing_items, key=lambda x: x.priority)

    # Reasons for each category
    reasons = {
        "python_module": {
            1: "Required for other modules to work",
            2: "Core functionality for course management",
            3: "Supporting functionality",
        },
        "directory": {
            1: "Required directory structure",
            2: "Core project structure",
            3: "Content directory",
        },
        "template": {
            2: "Required for generating content",
        },
        "config": {
            1: "Required for project configuration",
        },
        "content": {
            3: "Course content item",
        }
    }

    seen_paths = set()
    for item in sorted_missing:
        if item.path in seen_paths:
            continue
        seen_paths.add(item.path)

        reason = reasons.get(item.category, {}).get(item.priority, "Required item")

        result.recommendations.append({
            "priority": item.priority,
            "action": f"Create {item.path}",
            "reason": reason,
            "category": item.category,
            "estimated_effort": estimate_effort(item)
        })


def calculate_summary(result: AuditResult) -> None:
    """Calculate summary statistics."""
    dir_found = sum(1 for d in result.directories if d.found)
    dir_total = len(result.directories)

    mod_found = sum(1 for m in result.python_modules if m.found)
    mod_total = len(result.python_modules)

    tmpl_found = sum(1 for t in result.templates if t.found)
    tmpl_total = len(result.templates)

    cfg_found = sum(1 for c in result.config_files if c.found)
    cfg_total = len(result.config_files)

    content_found = sum(1 for c in result.content_items if c.found)
    content_total = len(result.content_items)

    tests_passed = sum(1 for t in result.functional_tests if t.status == "pass")
    tests_total = len(result.functional_tests)

    result.summary = {
        "directories": {
            "found": dir_found, "expected": dir_total,
            "percent": round(100 * dir_found / dir_total) if dir_total > 0 else 0
        },
        "python_modules": {
            "found": mod_found, "expected": mod_total,
            "percent": round(100 * mod_found / mod_total) if mod_total > 0 else 0
        },
        "templates": {
            "found": tmpl_found, "expected": tmpl_total,
            "percent": round(100 * tmpl_found / tmpl_total) if tmpl_total > 0 else 0
        },
        "config_files": {
            "found": cfg_found, "expected": cfg_total,
            "percent": round(100 * cfg_found / cfg_total) if cfg_total > 0 else 0
        },
        "content": {
            "found": content_found, "expected": content_total,
            "percent": round(100 * content_found / content_total) if content_total > 0 else 0
        },
        "functional_tests": {
            "passed": tests_passed, "total": tests_total,
            "percent": round(100 * tests_passed / tests_total) if tests_total > 0 else 0
        }
    }


def run_full_audit(include_functional: bool = True) -> AuditResult:
    """
    Run complete audit of the course development project.

    Args:
        include_functional: Whether to run functional tests

    Returns:
        AuditResult with all findings
    """
    result = AuditResult()

    # Set metadata
    result.metadata = {
        "generated": datetime.now().isoformat(),
        "project": "Methods and Algorithms",
        "version": "1.0.0",
        "project_root": str(PROJECT_ROOT)
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

    # Calculate summary
    calculate_summary(result)

    return result


if __name__ == "__main__":
    # Run audit and print results
    from .report_generator import print_console_report

    result = run_full_audit()
    print_console_report(result)
