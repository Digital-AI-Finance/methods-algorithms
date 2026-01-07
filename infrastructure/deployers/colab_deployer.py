"""Google Colab deployer - syncs notebooks to Google Drive/Colab."""
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

PROJECT_ROOT = Path(__file__).parent.parent.parent
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"


def deploy_to_colab(
    topic: Optional[str] = None,
    output_dir: Optional[Path] = None,
    verbose: bool = False
) -> bool:
    """
    Prepare notebooks for Google Colab deployment.

    Args:
        topic: Topic ID to deploy (None for all)
        output_dir: Output directory for prepared notebooks
        verbose: Show detailed output

    Returns:
        True if deployment preparation succeeded
    """
    print("Preparing notebooks for Colab...")

    if output_dir is None:
        output_dir = PROJECT_ROOT / "deploy" / "colab"

    output_dir.mkdir(parents=True, exist_ok=True)

    notebooks = list(NOTEBOOKS_DIR.glob("*.ipynb"))
    if topic:
        notebooks = [nb for nb in notebooks if topic.upper() in nb.stem.upper()]

    if not notebooks:
        print("  [SKIP] No notebooks found")
        return True

    success_count = 0
    for nb_path in notebooks:
        if _prepare_notebook_for_colab(nb_path, output_dir, verbose):
            success_count += 1

    print(f"  [PASS] {success_count}/{len(notebooks)} notebooks prepared")
    return success_count == len(notebooks)


def sync_notebooks(
    manifest: dict,
    verbose: bool = False
) -> bool:
    """
    Sync notebooks based on manifest.

    Args:
        manifest: Course manifest
        verbose: Show detailed output

    Returns:
        True if all notebooks synced
    """
    print("Syncing notebooks...")

    all_passed = True
    for topic in manifest.get("topics", []):
        notebook = topic.get("assets", {}).get("notebook", {})
        if not notebook:
            continue

        nb_file = notebook.get("file", "")
        nb_path = NOTEBOOKS_DIR / nb_file

        if not nb_path.exists():
            print(f"  [SKIP] {nb_file} - not found")
            continue

        # Validate notebook
        if not _validate_notebook(nb_path, verbose):
            all_passed = False
            continue

        print(f"  [X] {nb_file}")

    return all_passed


def _prepare_notebook_for_colab(
    nb_path: Path,
    output_dir: Path,
    verbose: bool
) -> bool:
    """Prepare a single notebook for Colab."""
    print(f"  Processing {nb_path.name}...")

    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Ensure Colab metadata
        notebook = _add_colab_metadata(notebook)

        # Add setup cell if needed
        notebook = _ensure_setup_cell(notebook)

        # Add badge if not present
        notebook = _ensure_colab_badge(notebook)

        # Save prepared notebook
        output_path = output_dir / nb_path.name
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)

        if verbose:
            print(f"    Saved to {output_path}")

        return True

    except Exception as e:
        print(f"    [FAIL] {e}")
        return False


def _validate_notebook(nb_path: Path, verbose: bool) -> bool:
    """Validate notebook structure."""
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Check basic structure
        if "cells" not in notebook:
            print(f"    [FAIL] No cells in notebook")
            return False

        cells = notebook["cells"]
        if len(cells) < 3:
            print(f"    [WARN] Very few cells ({len(cells)})")

        # Check for code cells
        code_cells = [c for c in cells if c.get("cell_type") == "code"]
        if not code_cells:
            print(f"    [WARN] No code cells found")

        return True

    except json.JSONDecodeError as e:
        print(f"    [FAIL] Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"    [FAIL] {e}")
        return False


def _add_colab_metadata(notebook: dict) -> dict:
    """Add or update Colab-specific metadata."""
    if "metadata" not in notebook:
        notebook["metadata"] = {}

    notebook["metadata"]["colab"] = {
        "provenance": [],
        "toc_visible": True
    }

    notebook["metadata"]["kernelspec"] = {
        "name": "python3",
        "display_name": "Python 3"
    }

    notebook["metadata"]["language_info"] = {
        "name": "python"
    }

    return notebook


def _ensure_setup_cell(notebook: dict) -> dict:
    """Ensure notebook has a setup cell."""
    cells = notebook.get("cells", [])

    # Check if setup cell exists
    for cell in cells[:3]:  # Check first 3 cells
        if cell.get("cell_type") == "code":
            source = cell.get("source", [])
            if isinstance(source, list):
                source = "".join(source)
            if "import" in source.lower():
                return notebook  # Setup exists

    # Add setup cell
    setup_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Setup - Run this cell first\n",
            "import numpy as np\n",
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Set random seed for reproducibility\n",
            "np.random.seed(42)\n",
            "\n",
            "print('Setup complete!')"
        ]
    }

    # Insert after first markdown cell (title)
    insert_pos = 1 if cells and cells[0].get("cell_type") == "markdown" else 0
    cells.insert(insert_pos, setup_cell)
    notebook["cells"] = cells

    return notebook


def _ensure_colab_badge(notebook: dict) -> dict:
    """Ensure notebook has Colab badge in first cell."""
    cells = notebook.get("cells", [])
    if not cells:
        return notebook

    first_cell = cells[0]
    if first_cell.get("cell_type") != "markdown":
        return notebook

    source = first_cell.get("source", [])
    if isinstance(source, list):
        source_text = "".join(source)
    else:
        source_text = source

    if "colab.research.google.com" not in source_text:
        badge = "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)\n\n"
        if isinstance(source, list):
            cells[0]["source"] = [badge] + source
        else:
            cells[0]["source"] = badge + source

    notebook["cells"] = cells
    return notebook


def get_colab_links(manifest: dict) -> List[Dict]:
    """Get Colab links for all notebooks."""
    links = []

    for topic in manifest.get("topics", []):
        notebook = topic.get("assets", {}).get("notebook", {})
        if not notebook:
            continue

        nb_file = notebook.get("file", "")
        nb_path = NOTEBOOKS_DIR / nb_file

        links.append({
            "topic_id": topic["id"],
            "topic_title": topic["title"],
            "file": nb_file,
            "exists": nb_path.exists(),
            "colab_url": f"https://colab.research.google.com/github/REPO_OWNER/REPO_NAME/blob/main/notebooks/{nb_file}"
        })

    return links
