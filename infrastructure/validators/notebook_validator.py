"""Jupyter notebook validation."""
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def validate_notebooks(manifest: dict, execute: bool = False) -> bool:
    """
    Validate Jupyter notebooks.

    Args:
        manifest: Course manifest
        execute: If True, execute all cells

    Returns:
        True if all validations pass
    """
    all_passed = True
    notebooks_dir = PROJECT_ROOT / "notebooks"

    for topic in manifest["topics"]:
        notebook_info = topic.get("assets", {}).get("notebook", {})
        if not notebook_info:
            continue

        notebook_file = notebook_info.get("file", "")
        notebook_path = PROJECT_ROOT / notebook_file

        if not notebook_path.exists():
            if notebook_info.get("status") == "complete":
                print(f"  [FAIL] Missing: {notebook_file}")
                all_passed = False
            else:
                print(f"  [SKIP] {notebook_file} - not yet created")
            continue

        # Validate notebook structure
        passed = _validate_notebook_structure(notebook_path)
        if not passed:
            all_passed = False

        # Execute if requested
        if execute:
            passed = _execute_notebook(notebook_path)
            if not passed:
                all_passed = False

    return all_passed


def _validate_notebook_structure(notebook_path: Path) -> bool:
    """Validate notebook JSON structure."""
    print(f"  Checking {notebook_path.name}...")

    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        # Check required keys
        required_keys = ["cells", "metadata", "nbformat"]
        for key in required_keys:
            if key not in nb:
                print(f"    [FAIL] Missing key: {key}")
                return False

        # Check cells
        if not nb["cells"]:
            print(f"    [WARN] No cells in notebook")

        # Check for markdown and code cells
        cell_types = [cell.get("cell_type") for cell in nb["cells"]]
        if "markdown" not in cell_types:
            print(f"    [WARN] No markdown cells")
        if "code" not in cell_types:
            print(f"    [WARN] No code cells")

        print(f"    [PASS] Structure valid ({len(nb['cells'])} cells)")
        return True

    except json.JSONDecodeError as e:
        print(f"    [FAIL] Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"    [FAIL] Error: {e}")
        return False


def _execute_notebook(notebook_path: Path) -> bool:
    """Execute notebook and check for errors."""
    print(f"  Executing {notebook_path.name}...")

    try:
        import nbformat
        from nbconvert.preprocessors import ExecutePreprocessor

        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": str(notebook_path.parent)}})

        print(f"    [PASS] Execution successful")
        return True

    except ImportError:
        print(f"    [SKIP] nbformat/nbconvert not installed")
        return True
    except Exception as e:
        print(f"    [FAIL] Execution error: {e}")
        return False
