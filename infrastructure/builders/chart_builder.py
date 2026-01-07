"""Chart builder - runs chart.py scripts."""
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def build_charts(manifest: dict, topic: str = None, verbose: bool = False) -> bool:
    """
    Build charts by running chart.py scripts.

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
        charts = t.get("assets", {}).get("charts", [])
        print(f"\n  Building charts for {t['id']}...")

        for chart in charts:
            chart_file = chart.get("file", "")
            chart_path = PROJECT_ROOT / chart_file

            if not chart_path.exists():
                print(f"    [SKIP] {chart['id']} - chart.py not found")
                continue

            passed = _run_chart_script(chart_path, verbose)
            if not passed:
                all_passed = False

    return all_passed


def _run_chart_script(script_path: Path, verbose: bool) -> bool:
    """Run a chart.py script."""
    print(f"    Running {script_path.parent.name}/chart.py...")

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=script_path.parent,
            capture_output=not verbose,
            text=True,
            timeout=120
        )

        if result.returncode != 0:
            print(f"      [FAIL] {result.stderr[:200] if result.stderr else 'Unknown error'}")
            return False

        # Check if PDF was created
        pdf_path = script_path.parent / "chart.pdf"
        if pdf_path.exists() and pdf_path.stat().st_size > 0:
            print(f"      [PASS] chart.pdf ({pdf_path.stat().st_size} bytes)")
            return True
        else:
            print(f"      [FAIL] PDF not generated")
            return False

    except subprocess.TimeoutExpired:
        print(f"      [FAIL] Timed out")
        return False
    except Exception as e:
        print(f"      [FAIL] {e}")
        return False
