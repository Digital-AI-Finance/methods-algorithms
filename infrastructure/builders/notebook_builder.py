"""Jupyter notebook builder - prepares notebooks for Google Colab."""
import json
import shutil
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATE_PATH = PROJECT_ROOT / "templates" / "notebook_template.ipynb"


def build_notebooks(
    manifest: dict,
    topic: Optional[str] = None,
    verbose: bool = False
) -> bool:
    """
    Build/prepare Jupyter notebooks for deployment.

    Args:
        manifest: Course manifest
        topic: Topic ID to build (None for all)
        verbose: Show detailed output

    Returns:
        True if all builds succeed
    """
    all_passed = True
    topics = manifest["topics"]
    notebooks_dir = PROJECT_ROOT / "notebooks"

    if topic:
        topics = [t for t in topics if t["id"] == topic]

    for t in topics:
        notebook_info = t.get("assets", {}).get("notebook", {})
        notebook_file = notebook_info.get("file", "")

        if not notebook_file:
            print(f"  [SKIP] {t['id']} - no notebook specified")
            continue

        notebook_path = notebooks_dir / notebook_file
        passed = _prepare_notebook(t, notebook_path, verbose)
        if not passed:
            all_passed = False

    return all_passed


def _prepare_notebook(topic: dict, notebook_path: Path, verbose: bool) -> bool:
    """Prepare a notebook for deployment."""
    topic_id = topic["id"]
    print(f"  Preparing {notebook_path.name}...")

    if not notebook_path.exists():
        # Create from template if doesn't exist
        if TEMPLATE_PATH.exists():
            try:
                notebook = _load_template()
                notebook = _customize_notebook(notebook, topic)
                _save_notebook(notebook, notebook_path)
                print(f"    [PASS] Created from template")
                return True
            except Exception as e:
                print(f"    [FAIL] {e}")
                return False
        else:
            print(f"    [SKIP] No template and notebook doesn't exist")
            return True

    # Validate existing notebook
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Check structure
        if "cells" not in notebook:
            print(f"    [FAIL] Invalid notebook structure")
            return False

        # Add Colab badge if missing
        notebook = _ensure_colab_badge(notebook, topic)
        _save_notebook(notebook, notebook_path)

        cell_count = len(notebook.get("cells", []))
        print(f"    [PASS] {cell_count} cells validated")
        return True

    except json.JSONDecodeError as e:
        print(f"    [FAIL] Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"    [FAIL] {e}")
        return False


def _load_template() -> dict:
    """Load the notebook template."""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def _customize_notebook(notebook: dict, topic: dict) -> dict:
    """Customize notebook template for specific topic."""
    # Update title in first markdown cell
    if notebook.get("cells"):
        first_cell = notebook["cells"][0]
        if first_cell.get("cell_type") == "markdown":
            source = first_cell.get("source", [])
            if isinstance(source, list):
                source = [line.replace("{{TOPIC_TITLE}}", topic["title"])
                         .replace("{{TOPIC_ID}}", topic["id"])
                         for line in source]
            else:
                source = source.replace("{{TOPIC_TITLE}}", topic["title"])
                source = source.replace("{{TOPIC_ID}}", topic["id"])
            first_cell["source"] = source
    return notebook


def _ensure_colab_badge(notebook: dict, topic: dict) -> dict:
    """Ensure notebook has Colab badge."""
    if not notebook.get("cells"):
        return notebook

    first_cell = notebook["cells"][0]
    if first_cell.get("cell_type") != "markdown":
        return notebook

    source = first_cell.get("source", [])
    if isinstance(source, list):
        source_text = "".join(source)
    else:
        source_text = source

    if "colab.research.google.com" not in source_text:
        badge = "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]" \
                "(https://colab.research.google.com/)\n\n"
        if isinstance(source, list):
            notebook["cells"][0]["source"] = [badge] + source
        else:
            notebook["cells"][0]["source"] = badge + source

    return notebook


def _save_notebook(notebook: dict, path: Path) -> None:
    """Save notebook to file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
