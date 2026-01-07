"""Progress report generator."""
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent.parent


def generate_progress_report(manifest: dict, detailed: bool = False) -> str:
    """
    Generate a progress report for the course.

    Args:
        manifest: Course manifest
        detailed: Show detailed breakdown

    Returns:
        Formatted report string
    """
    lines = []

    # Header
    course = manifest.get("course", {})
    lines.append("=" * 60)
    lines.append(f"  {course.get('title', 'Course')} - Progress Report")
    lines.append(f"  Version: {course.get('version', 'N/A')} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")

    # Overall progress
    topics = manifest.get("topics", [])
    total_topics = len(topics)
    completed_topics = sum(1 for t in topics if t.get("status") == "complete")
    review_topics = sum(1 for t in topics if t.get("status") == "review")
    pending_topics = total_topics - completed_topics - review_topics

    lines.append("OVERALL PROGRESS")
    lines.append("-" * 40)
    lines.append(f"  Topics: {completed_topics}/{total_topics} complete ({100*completed_topics//total_topics}%)")
    lines.append(f"    - Complete: {completed_topics}")
    lines.append(f"    - In Review: {review_topics}")
    lines.append(f"    - Pending: {pending_topics}")
    lines.append("")

    # Topic breakdown
    lines.append("TOPICS")
    lines.append("-" * 40)
    for topic in topics:
        status_icon = {"complete": "[X]", "review": "[~]", "pending": "[ ]", "draft": "[.]"}.get(topic.get("status", "pending"), "[ ]")
        lines.append(f"  {status_icon} {topic['id']}: {topic['title']}")

        if detailed:
            assets = topic.get("assets", {})

            # Count asset status
            total_assets = 0
            complete_assets = 0

            for asset_key, asset_value in assets.items():
                if isinstance(asset_value, dict):
                    total_assets += 1
                    if asset_value.get("status") == "complete":
                        complete_assets += 1
                    # Check if file exists
                    file_path = PROJECT_ROOT / asset_value.get("file", "")
                    exists = file_path.exists()
                    lines.append(f"       {asset_key}: {'[X]' if exists else '[ ]'} {asset_value.get('file', 'N/A')}")
                elif isinstance(asset_value, list):
                    for item in asset_value:
                        total_assets += 1
                        if item.get("status") == "complete":
                            complete_assets += 1

            if total_assets > 0:
                lines.append(f"       Assets: {complete_assets}/{total_assets}")
            lines.append("")

    # Quizzes
    quizzes = manifest.get("quizzes", [])
    if quizzes:
        lines.append("")
        lines.append("QUIZZES")
        lines.append("-" * 40)
        for quiz in quizzes:
            status_icon = "[X]" if quiz.get("status") == "complete" else "[ ]"
            lines.append(f"  {status_icon} {quiz['id']}: {quiz['title']}")

    # Presentations
    presentations = manifest.get("presentations", {})
    if presentations:
        lines.append("")
        lines.append("PRESENTATIONS")
        lines.append("-" * 40)
        status_icon = "[X]" if presentations.get("status") == "complete" else "[ ]"
        lines.append(f"  {status_icon} {presentations.get('count', 0)} topics ({presentations.get('file', 'N/A')})")

    # Capstone
    capstone = manifest.get("capstone", {})
    if capstone:
        lines.append("")
        lines.append("CAPSTONE")
        lines.append("-" * 40)
        status_icon = "[X]" if capstone.get("status") == "complete" else "[ ]"
        lines.append(f"  {status_icon} Specification: {capstone.get('specification_file', 'N/A')}")

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)
