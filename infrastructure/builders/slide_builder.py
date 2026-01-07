"""LaTeX slide builder."""
import subprocess
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def build_slides(manifest: dict, topic: str = None, verbose: bool = False) -> bool:
    """
    Build LaTeX slides.

    Args:
        manifest: Course manifest
        topic: Topic ID to build (None for all)
        verbose: Show detailed output

    Returns:
        True if all builds succeed
    """
    all_passed = True
    topics = manifest["topics"]

    if topic:
        topics = [t for t in topics if t["id"] == topic]

    for t in topics:
        topic_id = t["id"]
        topic_title = t["title"].replace(" ", "_").replace("&", "").replace("/", "_")
        topic_dir = PROJECT_ROOT / f"slides/{topic_id}_{topic_title}"

        if not topic_dir.exists():
            print(f"  [SKIP] {topic_id} - directory not found")
            continue

        # Build overview
        overview_tex = topic_dir / f"{topic_id}_overview.tex"
        if overview_tex.exists():
            passed = _compile_latex(overview_tex, verbose)
            if not passed:
                all_passed = False
        else:
            print(f"  [SKIP] {topic_id}_overview.tex - not found")

        # Build deepdive
        deepdive_tex = topic_dir / f"{topic_id}_deepdive.tex"
        if deepdive_tex.exists():
            passed = _compile_latex(deepdive_tex, verbose)
            if not passed:
                all_passed = False
        else:
            print(f"  [SKIP] {topic_id}_deepdive.tex - not found")

    return all_passed


def _compile_latex(tex_path: Path, verbose: bool) -> bool:
    """Compile a LaTeX file to PDF."""
    print(f"  Compiling {tex_path.name}...")

    try:
        # Run pdflatex twice for references
        for i in range(2):
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", str(tex_path)],
                cwd=tex_path.parent,
                capture_output=not verbose,
                text=True,
                timeout=120
            )

            if result.returncode != 0 and i == 1:
                print(f"    [FAIL] Compilation failed")
                return False

        # Move auxiliary files to temp
        temp_dir = tex_path.parent / "temp"
        temp_dir.mkdir(exist_ok=True)

        for ext in [".aux", ".log", ".nav", ".out", ".snm", ".toc", ".vrb"]:
            aux_file = tex_path.with_suffix(ext)
            if aux_file.exists():
                shutil.move(str(aux_file), str(temp_dir / aux_file.name))

        pdf_path = tex_path.with_suffix(".pdf")
        if pdf_path.exists():
            print(f"    [PASS] {pdf_path.name}")
            return True
        else:
            print(f"    [FAIL] PDF not created")
            return False

    except FileNotFoundError:
        print(f"    [FAIL] pdflatex not found")
        return False
    except subprocess.TimeoutExpired:
        print(f"    [FAIL] Compilation timed out")
        return False
