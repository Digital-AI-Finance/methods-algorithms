"""Chart validation and regeneration."""
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def validate_charts(manifest: dict, regenerate: bool = False) -> bool:
    """
    Validate chart scripts and PDFs.

    Args:
        manifest: Course manifest
        regenerate: If True, regenerate all charts

    Returns:
        True if all validations pass
    """
    all_passed = True

    for topic in manifest["topics"]:
        charts = topic.get("assets", {}).get("charts", [])

        for chart in charts:
            chart_file = chart.get("file", "")
            chart_path = PROJECT_ROOT / chart_file

            if not chart_path.exists():
                if chart.get("status") == "complete":
                    print(f"  [FAIL] Missing: {chart_file}")
                    all_passed = False
                else:
                    print(f"  [SKIP] {chart_file} - not yet created")
                continue

            # Check if PDF exists
            pdf_path = chart_path.parent / "chart.pdf"

            if regenerate or not pdf_path.exists():
                # Try to run the chart script
                passed = _run_chart_script(chart_path)
                if not passed:
                    all_passed = False
            else:
                # Just verify PDF exists and is not empty
                if pdf_path.stat().st_size > 0:
                    print(f"  [PASS] {chart['id']}")
                else:
                    print(f"  [FAIL] {chart['id']} - PDF is empty")
                    all_passed = False

    return all_passed


def _run_chart_script(script_path: Path) -> bool:
    """Run a chart.py script and verify PDF output."""
    print(f"  Running {script_path.parent.name}/chart.py...")

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=script_path.parent,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            print(f"    [FAIL] Script error: {result.stderr[:200]}")
            return False

        # Check if PDF was created
        pdf_path = script_path.parent / "chart.pdf"
        if pdf_path.exists() and pdf_path.stat().st_size > 0:
            print(f"    [PASS] PDF generated")
            return True
        else:
            print(f"    [FAIL] PDF not generated")
            return False

    except subprocess.TimeoutExpired:
        print(f"    [FAIL] Script timed out")
        return False
    except Exception as e:
        print(f"    [FAIL] Error: {e}")
        return False
