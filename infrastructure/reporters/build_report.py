"""Build report generator - tracks compilation status."""
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).parent.parent.parent


def generate_build_report(
    manifest: dict,
    include_timestamps: bool = True
) -> str:
    """
    Generate a build status report.

    Args:
        manifest: Course manifest
        include_timestamps: Include file modification times

    Returns:
        Formatted build report string
    """
    lines = []

    # Header
    course = manifest.get("course", {})
    lines.append("=" * 60)
    lines.append(f"  BUILD STATUS REPORT")
    lines.append(f"  {course.get('title', 'Course')} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")

    # Summary stats
    stats = _collect_build_stats(manifest)

    lines.append("SUMMARY")
    lines.append("-" * 40)
    lines.append(f"  Slides:     {stats['slides_built']}/{stats['slides_total']} built")
    lines.append(f"  Charts:     {stats['charts_built']}/{stats['charts_total']} generated")
    lines.append(f"  Notebooks:  {stats['notebooks_ready']}/{stats['notebooks_total']} ready")
    lines.append(f"  Quizzes:    {stats['quizzes_built']}/{stats['quizzes_total']} exported")
    lines.append("")

    # Per-topic details
    lines.append("TOPIC DETAILS")
    lines.append("-" * 40)

    for topic in manifest.get("topics", []):
        topic_id = topic["id"]
        topic_title = topic["title"]
        lines.append(f"\n  {topic_id}: {topic_title}")

        assets = topic.get("assets", {})
        topic_dir = _get_topic_dir(topic)

        # Overview slides
        overview = assets.get("overview_slides", {})
        if overview:
            overview_pdf = topic_dir / f"{topic_id}_overview.pdf"
            status = "[X]" if overview_pdf.exists() else "[ ]"
            lines.append(f"    {status} Overview slides")

        # Deep dive slides
        deepdive = assets.get("deepdive_slides", {})
        if deepdive:
            deepdive_pdf = topic_dir / f"{topic_id}_deepdive.pdf"
            status = "[X]" if deepdive_pdf.exists() else "[ ]"
            lines.append(f"    {status} Deep dive slides")

        # Charts
        charts = assets.get("charts", [])
        if charts:
            charts_built = sum(1 for c in charts if _chart_exists(c))
            lines.append(f"    Charts: {charts_built}/{len(charts)} built")

        # Notebook
        notebook = assets.get("notebook", {})
        if notebook:
            nb_path = PROJECT_ROOT / "notebooks" / notebook.get("file", "")
            status = "[X]" if nb_path.exists() else "[ ]"
            lines.append(f"    {status} Notebook")

    # Recent builds
    if include_timestamps:
        lines.append("")
        lines.append("RECENT BUILDS")
        lines.append("-" * 40)
        recent = _get_recent_builds()
        for item in recent[:10]:
            lines.append(f"  {item['time']} | {item['file']}")

    lines.append("")
    lines.append("=" * 60)
    return "\n".join(lines)


def _collect_build_stats(manifest: dict) -> Dict:
    """Collect build statistics from manifest."""
    stats = {
        "slides_built": 0,
        "slides_total": 0,
        "charts_built": 0,
        "charts_total": 0,
        "notebooks_ready": 0,
        "notebooks_total": 0,
        "quizzes_built": 0,
        "quizzes_total": 0,
    }

    for topic in manifest.get("topics", []):
        assets = topic.get("assets", {})
        topic_dir = _get_topic_dir(topic)
        topic_id = topic["id"]

        # Slides
        if assets.get("overview_slides"):
            stats["slides_total"] += 1
            if (topic_dir / f"{topic_id}_overview.pdf").exists():
                stats["slides_built"] += 1

        if assets.get("deepdive_slides"):
            stats["slides_total"] += 1
            if (topic_dir / f"{topic_id}_deepdive.pdf").exists():
                stats["slides_built"] += 1

        # Charts
        charts = assets.get("charts", [])
        stats["charts_total"] += len(charts)
        stats["charts_built"] += sum(1 for c in charts if _chart_exists(c))

        # Notebooks
        if assets.get("notebook"):
            stats["notebooks_total"] += 1
            nb_file = assets["notebook"].get("file", "")
            if (PROJECT_ROOT / "notebooks" / nb_file).exists():
                stats["notebooks_ready"] += 1

    # Quizzes
    quizzes = manifest.get("quizzes", [])
    stats["quizzes_total"] = len(quizzes)
    for quiz in quizzes:
        quiz_file = quiz.get("file", "")
        if (PROJECT_ROOT / "quizzes" / quiz_file).exists():
            stats["quizzes_built"] += 1

    return stats


def _get_topic_dir(topic: dict) -> Path:
    """Get topic directory path."""
    topic_id = topic["id"]
    topic_title = topic["title"].replace(" ", "_").replace("&", "").replace("/", "_")
    return PROJECT_ROOT / "slides" / f"{topic_id}_{topic_title}"


def _chart_exists(chart: dict) -> bool:
    """Check if chart PDF exists."""
    chart_file = chart.get("file", "")
    if not chart_file:
        return False
    chart_dir = PROJECT_ROOT / Path(chart_file).parent
    return (chart_dir / "chart.pdf").exists()


def _get_recent_builds() -> List[Dict]:
    """Get recently modified PDFs."""
    pdfs = []
    for pdf in PROJECT_ROOT.rglob("*.pdf"):
        if "temp" not in str(pdf) and ".git" not in str(pdf):
            pdfs.append({
                "file": str(pdf.relative_to(PROJECT_ROOT)),
                "time": datetime.fromtimestamp(pdf.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
                "mtime": pdf.stat().st_mtime
            })

    pdfs.sort(key=lambda x: x["mtime"], reverse=True)
    return pdfs
