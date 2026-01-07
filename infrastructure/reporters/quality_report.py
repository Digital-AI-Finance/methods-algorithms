"""Quality report generator - tracks quality metrics."""
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import subprocess
import re

PROJECT_ROOT = Path(__file__).parent.parent.parent


def generate_quality_report(manifest: dict, run_checks: bool = False) -> str:
    """
    Generate a quality metrics report.

    Args:
        manifest: Course manifest
        run_checks: Actually run validation checks (slower)

    Returns:
        Formatted quality report string
    """
    lines = []

    # Header
    course = manifest.get("course", {})
    lines.append("=" * 60)
    lines.append(f"  QUALITY METRICS REPORT")
    lines.append(f"  {course.get('title', 'Course')} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")

    # LaTeX quality
    lines.append("LATEX QUALITY")
    lines.append("-" * 40)
    latex_stats = _check_latex_quality(manifest, run_checks)
    lines.append(f"  Files checked:    {latex_stats['files_checked']}")
    lines.append(f"  Overflow warnings: {latex_stats['overflow_warnings']}")
    lines.append(f"  Compilation errors: {latex_stats['compilation_errors']}")
    lines.append(f"  Missing figures:   {latex_stats['missing_figures']}")
    lines.append("")

    # Chart quality
    lines.append("CHART QUALITY")
    lines.append("-" * 40)
    chart_stats = _check_chart_quality(manifest)
    lines.append(f"  Total charts:     {chart_stats['total']}")
    lines.append(f"  PDFs generated:   {chart_stats['pdfs_exist']}")
    lines.append(f"  With metadata:    {chart_stats['with_metadata']}")
    lines.append(f"  Avg file size:    {chart_stats['avg_size_kb']:.1f} KB")
    lines.append("")

    # Notebook quality
    lines.append("NOTEBOOK QUALITY")
    lines.append("-" * 40)
    nb_stats = _check_notebook_quality(manifest)
    lines.append(f"  Total notebooks:  {nb_stats['total']}")
    lines.append(f"  With badges:      {nb_stats['with_badges']}")
    lines.append(f"  Avg cells:        {nb_stats['avg_cells']:.0f}")
    lines.append(f"  Code cells:       {nb_stats['code_cells']}")
    lines.append(f"  Markdown cells:   {nb_stats['markdown_cells']}")
    lines.append("")

    # Content quality
    lines.append("CONTENT QUALITY")
    lines.append("-" * 40)
    content_stats = _check_content_quality(manifest)
    lines.append(f"  Topics with objectives: {content_stats['with_objectives']}/{content_stats['total_topics']}")
    lines.append(f"  Topics with decision framework: {content_stats['with_decision']}/{content_stats['total_topics']}")
    lines.append(f"  Topics with finance case: {content_stats['with_finance']}/{content_stats['total_topics']}")
    lines.append("")

    # Quality score
    lines.append("OVERALL QUALITY SCORE")
    lines.append("-" * 40)
    score = _calculate_quality_score(latex_stats, chart_stats, nb_stats, content_stats)
    bar = "#" * int(score / 5)
    lines.append(f"  Score: {score}/100 {bar}")
    lines.append("")

    if score < 70:
        lines.append("  [!] Quality below threshold. Review recommendations.")
    elif score < 90:
        lines.append("  [~] Quality acceptable. Minor improvements possible.")
    else:
        lines.append("  [X] Quality excellent!")
    lines.append("")

    # Issues
    issues = _collect_issues(latex_stats, chart_stats, nb_stats, content_stats)
    if issues:
        lines.append("ISSUES TO ADDRESS")
        lines.append("-" * 40)
        for issue in issues[:10]:
            lines.append(f"  - {issue}")
        if len(issues) > 10:
            lines.append(f"  ... and {len(issues) - 10} more")
    lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


def _check_latex_quality(manifest: dict, run_checks: bool) -> Dict:
    """Check LaTeX quality metrics."""
    stats = {
        "files_checked": 0,
        "overflow_warnings": 0,
        "compilation_errors": 0,
        "missing_figures": 0
    }

    for topic in manifest.get("topics", []):
        topic_dir = _get_topic_dir(topic)
        topic_id = topic["id"]

        for suffix in ["overview", "deepdive"]:
            tex_file = topic_dir / f"{topic_id}_{suffix}.tex"
            if tex_file.exists():
                stats["files_checked"] += 1

                if run_checks:
                    # Check for overflow in log
                    log_file = topic_dir / "temp" / f"{topic_id}_{suffix}.log"
                    if log_file.exists():
                        content = log_file.read_text(errors='ignore')
                        stats["overflow_warnings"] += content.count("Overfull")

                # Check for missing figures in tex
                content = tex_file.read_text(errors='ignore')
                includes = re.findall(r'\\includegraphics.*?\{([^}]+)\}', content)
                for inc in includes:
                    fig_path = topic_dir / inc
                    if not fig_path.exists() and not (topic_dir / f"{inc}.pdf").exists():
                        stats["missing_figures"] += 1

    return stats


def _check_chart_quality(manifest: dict) -> Dict:
    """Check chart quality metrics."""
    stats = {
        "total": 0,
        "pdfs_exist": 0,
        "with_metadata": 0,
        "avg_size_kb": 0.0
    }

    total_size = 0

    for topic in manifest.get("topics", []):
        charts = topic.get("assets", {}).get("charts", [])
        stats["total"] += len(charts)

        for chart in charts:
            chart_file = chart.get("file", "")
            if chart_file:
                chart_dir = PROJECT_ROOT / Path(chart_file).parent
                pdf_path = chart_dir / "chart.pdf"
                py_path = chart_dir / "chart.py"

                if pdf_path.exists():
                    stats["pdfs_exist"] += 1
                    total_size += pdf_path.stat().st_size

                if py_path.exists():
                    content = py_path.read_text(errors='ignore')
                    if "CHART_METADATA" in content:
                        stats["with_metadata"] += 1

    if stats["pdfs_exist"] > 0:
        stats["avg_size_kb"] = (total_size / stats["pdfs_exist"]) / 1024

    return stats


def _check_notebook_quality(manifest: dict) -> Dict:
    """Check notebook quality metrics."""
    import json

    stats = {
        "total": 0,
        "with_badges": 0,
        "avg_cells": 0.0,
        "code_cells": 0,
        "markdown_cells": 0
    }

    total_cells = 0
    notebooks_checked = 0

    notebooks_dir = PROJECT_ROOT / "notebooks"
    for nb_file in notebooks_dir.glob("*.ipynb"):
        stats["total"] += 1
        try:
            with open(nb_file, 'r', encoding='utf-8') as f:
                nb = json.load(f)

            cells = nb.get("cells", [])
            total_cells += len(cells)
            notebooks_checked += 1

            for cell in cells:
                cell_type = cell.get("cell_type", "")
                if cell_type == "code":
                    stats["code_cells"] += 1
                elif cell_type == "markdown":
                    stats["markdown_cells"] += 1
                    source = cell.get("source", [])
                    if isinstance(source, list):
                        source = "".join(source)
                    if "colab" in source.lower():
                        stats["with_badges"] += 1
                        break

        except (json.JSONDecodeError, Exception):
            continue

    if notebooks_checked > 0:
        stats["avg_cells"] = total_cells / notebooks_checked

    return stats


def _check_content_quality(manifest: dict) -> Dict:
    """Check content quality metrics."""
    stats = {
        "total_topics": len(manifest.get("topics", [])),
        "with_objectives": 0,
        "with_decision": 0,
        "with_finance": 0
    }

    for topic in manifest.get("topics", []):
        if topic.get("learning_objectives"):
            stats["with_objectives"] += 1
        if topic.get("decision_framework"):
            stats["with_decision"] += 1
        if topic.get("finance_case"):
            stats["with_finance"] += 1

    return stats


def _calculate_quality_score(latex: Dict, chart: Dict, nb: Dict, content: Dict) -> int:
    """Calculate overall quality score (0-100)."""
    score = 0

    # LaTeX (25 points)
    if latex["files_checked"] > 0:
        if latex["overflow_warnings"] == 0:
            score += 15
        if latex["compilation_errors"] == 0:
            score += 5
        if latex["missing_figures"] == 0:
            score += 5

    # Charts (25 points)
    if chart["total"] > 0:
        score += int(25 * chart["pdfs_exist"] / chart["total"])

    # Notebooks (25 points)
    if nb["total"] > 0:
        score += int(15 * nb["with_badges"] / max(1, nb["total"]))
        if nb["avg_cells"] >= 10:
            score += 10

    # Content (25 points)
    if content["total_topics"] > 0:
        score += int(10 * content["with_objectives"] / content["total_topics"])
        score += int(10 * content["with_decision"] / content["total_topics"])
        score += int(5 * content["with_finance"] / content["total_topics"])

    return min(100, score)


def _collect_issues(latex: Dict, chart: Dict, nb: Dict, content: Dict) -> List[str]:
    """Collect quality issues."""
    issues = []

    if latex["overflow_warnings"] > 0:
        issues.append(f"LaTeX: {latex['overflow_warnings']} overflow warnings")
    if latex["missing_figures"] > 0:
        issues.append(f"LaTeX: {latex['missing_figures']} missing figures")
    if chart["total"] > chart["pdfs_exist"]:
        issues.append(f"Charts: {chart['total'] - chart['pdfs_exist']} PDFs not generated")
    if content["with_objectives"] < content["total_topics"]:
        issues.append(f"Content: {content['total_topics'] - content['with_objectives']} topics missing objectives")
    if content["with_decision"] < content["total_topics"]:
        issues.append(f"Content: {content['total_topics'] - content['with_decision']} topics missing decision framework")

    return issues


def _get_topic_dir(topic: dict) -> Path:
    """Get topic directory path."""
    topic_id = topic["id"]
    topic_title = topic["title"].replace(" ", "_").replace("&", "").replace("/", "_")
    return PROJECT_ROOT / "slides" / f"{topic_id}_{topic_title}"
