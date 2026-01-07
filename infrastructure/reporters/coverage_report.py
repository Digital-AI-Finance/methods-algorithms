"""Coverage report generator - tracks learning objectives coverage."""
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

PROJECT_ROOT = Path(__file__).parent.parent.parent


def generate_coverage_report(manifest: dict) -> str:
    """
    Generate a learning objectives coverage report.

    Args:
        manifest: Course manifest

    Returns:
        Formatted coverage report string
    """
    lines = []

    # Header
    course = manifest.get("course", {})
    lines.append("=" * 60)
    lines.append(f"  LEARNING OBJECTIVES COVERAGE REPORT")
    lines.append(f"  {course.get('title', 'Course')} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")

    # Collect all objectives
    all_objectives = []
    bloom_levels = {"remember": 0, "understand": 0, "apply": 0, "analyze": 0, "evaluate": 0, "create": 0}

    for topic in manifest.get("topics", []):
        objectives = topic.get("learning_objectives", [])
        for obj in objectives:
            all_objectives.append({
                "id": obj.get("id", ""),
                "text": obj.get("text", ""),
                "bloom_level": obj.get("bloom_level", "understand"),
                "topic_id": topic["id"],
                "topic_title": topic["title"]
            })
            level = obj.get("bloom_level", "understand").lower()
            if level in bloom_levels:
                bloom_levels[level] += 1

    # Summary
    lines.append("SUMMARY")
    lines.append("-" * 40)
    lines.append(f"  Total Objectives: {len(all_objectives)}")
    lines.append("")
    lines.append("  Bloom's Taxonomy Distribution:")
    for level, count in bloom_levels.items():
        if count > 0:
            bar = "#" * min(count * 3, 30)
            lines.append(f"    {level.capitalize():12} {count:3} {bar}")
    lines.append("")

    # Per-topic objectives
    lines.append("OBJECTIVES BY TOPIC")
    lines.append("-" * 40)

    for topic in manifest.get("topics", []):
        topic_id = topic["id"]
        lines.append(f"\n  {topic_id}: {topic['title']}")

        objectives = topic.get("learning_objectives", [])
        if not objectives:
            lines.append("    (no objectives defined)")
            continue

        for obj in objectives:
            bloom = obj.get("bloom_level", "understand")
            lines.append(f"    [{bloom[:3].upper()}] {obj.get('text', '')}")

    # Coverage matrix
    lines.append("")
    lines.append("ASSESSMENT COVERAGE MATRIX")
    lines.append("-" * 40)
    lines.append("  (Mapping objectives to assessments)")
    lines.append("")
    lines.append("  Objective ID    | Slides | Quiz | Notebook | Presentation")
    lines.append("  " + "-" * 56)

    for obj in all_objectives:
        obj_id = obj["id"]
        topic_id = obj["topic_id"]

        # Check coverage (simplified - would need actual mapping in manifest)
        slides = "X" if True else " "  # Assume slides always cover
        quiz = "X" if _quiz_covers_topic(manifest, topic_id) else " "
        notebook = "X" if _notebook_exists(manifest, topic_id) else " "
        presentation = "?" # Would need presentation mapping

        lines.append(f"  {obj_id:16} |   {slides}    |   {quiz}  |    {notebook}     |      {presentation}")

    # Recommendations
    lines.append("")
    lines.append("RECOMMENDATIONS")
    lines.append("-" * 40)

    # Check for gaps
    gaps = []
    for level, count in bloom_levels.items():
        if level in ["create", "evaluate"] and count < len(manifest.get("topics", [])) // 2:
            gaps.append(f"  - Add more {level}-level objectives for higher-order thinking")

    if not gaps:
        lines.append("  - Coverage appears adequate")
    else:
        lines.extend(gaps)

    lines.append("")
    lines.append("=" * 60)
    return "\n".join(lines)


def _quiz_covers_topic(manifest: dict, topic_id: str) -> bool:
    """Check if any quiz covers this topic."""
    for quiz in manifest.get("quizzes", []):
        if topic_id in quiz.get("topics", []):
            return True
    return False


def _notebook_exists(manifest: dict, topic_id: str) -> bool:
    """Check if notebook exists for topic."""
    for topic in manifest.get("topics", []):
        if topic["id"] == topic_id:
            notebook = topic.get("assets", {}).get("notebook", {})
            if notebook:
                nb_path = PROJECT_ROOT / "notebooks" / notebook.get("file", "")
                return nb_path.exists()
    return False


def get_bloom_statistics(manifest: dict) -> Dict:
    """Get Bloom's taxonomy statistics."""
    stats = {"remember": 0, "understand": 0, "apply": 0, "analyze": 0, "evaluate": 0, "create": 0}

    for topic in manifest.get("topics", []):
        for obj in topic.get("learning_objectives", []):
            level = obj.get("bloom_level", "understand").lower()
            if level in stats:
                stats[level] += 1

    return stats


def get_uncovered_objectives(manifest: dict) -> List[Dict]:
    """Find objectives not covered by assessments."""
    uncovered = []

    for topic in manifest.get("topics", []):
        topic_id = topic["id"]
        has_quiz = _quiz_covers_topic(manifest, topic_id)
        has_notebook = _notebook_exists(manifest, topic_id)

        if not has_quiz and not has_notebook:
            for obj in topic.get("learning_objectives", []):
                uncovered.append({
                    "objective": obj,
                    "topic_id": topic_id,
                    "missing": ["quiz", "notebook"]
                })

    return uncovered
