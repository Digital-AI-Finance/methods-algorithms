"""HTML dashboard generator - creates interactive progress dashboard."""
from pathlib import Path
from datetime import datetime
from typing import Dict, List
import json

PROJECT_ROOT = Path(__file__).parent.parent.parent


def generate_html_dashboard(manifest: dict, output_path: Path = None) -> str:
    """
    Generate an interactive HTML dashboard.

    Args:
        manifest: Course manifest
        output_path: Path to save HTML file (optional)

    Returns:
        HTML string
    """
    course = manifest.get("course", {})
    stats = _collect_all_stats(manifest)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course.get("title", "Course")} - Dashboard</title>
    <style>
        :root {{
            --primary: #3b82f6;
            --success: #22c55e;
            --warning: #f59e0b;
            --danger: #ef4444;
            --bg: #f8fafc;
            --card: #ffffff;
            --text: #1e293b;
            --border: #e2e8f0;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        header {{
            background: var(--primary);
            color: white;
            padding: 24px;
            border-radius: 12px;
            margin-bottom: 24px;
        }}
        header h1 {{ font-size: 24px; font-weight: 600; }}
        header p {{ opacity: 0.9; font-size: 14px; margin-top: 4px; }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }}
        .stat-card {{
            background: var(--card);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid var(--border);
        }}
        .stat-card h3 {{ font-size: 12px; text-transform: uppercase; color: #64748b; }}
        .stat-card .value {{ font-size: 32px; font-weight: 700; margin: 8px 0; }}
        .stat-card .sub {{ font-size: 13px; color: #64748b; }}
        .progress-bar {{
            height: 8px;
            background: #e2e8f0;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 12px;
        }}
        .progress-bar .fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s;
        }}
        .fill.success {{ background: var(--success); }}
        .fill.warning {{ background: var(--warning); }}
        .fill.danger {{ background: var(--danger); }}
        section {{
            background: var(--card);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            border: 1px solid var(--border);
        }}
        section h2 {{
            font-size: 18px;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--border);
        }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid var(--border); }}
        th {{ font-size: 12px; text-transform: uppercase; color: #64748b; }}
        .status {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
        }}
        .status.complete {{ background: #dcfce7; color: #166534; }}
        .status.review {{ background: #fef3c7; color: #92400e; }}
        .status.pending {{ background: #f1f5f9; color: #475569; }}
        .status.draft {{ background: #e0e7ff; color: #3730a3; }}
        .test-result {{ display: flex; align-items: center; gap: 8px; padding: 8px 0; }}
        .test-result .icon {{ width: 20px; height: 20px; border-radius: 50%; }}
        .test-result .pass {{ background: var(--success); }}
        .test-result .fail {{ background: var(--danger); }}
        footer {{ text-align: center; color: #64748b; font-size: 13px; margin-top: 24px; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{course.get("title", "Course Dashboard")}</h1>
            <p>Version {course.get("version", "1.0.0")} | Generated {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <h3>Topics</h3>
                <div class="value">{stats['topics_complete']}/{stats['topics_total']}</div>
                <div class="sub">Complete</div>
                <div class="progress-bar">
                    <div class="fill {_get_progress_class(stats['topics_complete'], stats['topics_total'])}"
                         style="width: {_calc_percent(stats['topics_complete'], stats['topics_total'])}%"></div>
                </div>
            </div>
            <div class="stat-card">
                <h3>Python Modules</h3>
                <div class="value">{stats['modules_exist']}/{stats['modules_total']}</div>
                <div class="sub">Created</div>
                <div class="progress-bar">
                    <div class="fill {_get_progress_class(stats['modules_exist'], stats['modules_total'])}"
                         style="width: {_calc_percent(stats['modules_exist'], stats['modules_total'])}%"></div>
                </div>
            </div>
            <div class="stat-card">
                <h3>Charts</h3>
                <div class="value">{stats['charts_built']}/{stats['charts_total']}</div>
                <div class="sub">Generated</div>
                <div class="progress-bar">
                    <div class="fill {_get_progress_class(stats['charts_built'], stats['charts_total'])}"
                         style="width: {_calc_percent(stats['charts_built'], stats['charts_total'])}%"></div>
                </div>
            </div>
            <div class="stat-card">
                <h3>Functional Tests</h3>
                <div class="value">{stats['tests_pass']}/{stats['tests_total']}</div>
                <div class="sub">Passing</div>
                <div class="progress-bar">
                    <div class="fill {_get_progress_class(stats['tests_pass'], stats['tests_total'])}"
                         style="width: {_calc_percent(stats['tests_pass'], stats['tests_total'])}%"></div>
                </div>
            </div>
        </div>

        <section>
            <h2>Topic Progress</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title</th>
                        <th>Status</th>
                        <th>Slides</th>
                        <th>Charts</th>
                        <th>Notebook</th>
                    </tr>
                </thead>
                <tbody>
                    {_generate_topic_rows(manifest)}
                </tbody>
            </table>
        </section>

        <section>
            <h2>Infrastructure Status</h2>
            <table>
                <thead>
                    <tr>
                        <th>Component</th>
                        <th>Files</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {_generate_infra_rows()}
                </tbody>
            </table>
        </section>

        <footer>
            <p>Methods and Algorithms - MSc Data Science | Auto-generated dashboard</p>
        </footer>
    </div>
</body>
</html>'''

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

    return html


def _collect_all_stats(manifest: dict) -> Dict:
    """Collect all statistics for dashboard."""
    stats = {
        "topics_total": len(manifest.get("topics", [])),
        "topics_complete": 0,
        "modules_total": 33,  # From audit
        "modules_exist": 0,
        "charts_total": 0,
        "charts_built": 0,
        "tests_total": 6,
        "tests_pass": 0
    }

    # Count complete topics
    for topic in manifest.get("topics", []):
        if topic.get("status") == "complete":
            stats["topics_complete"] += 1

        # Count charts
        charts = topic.get("assets", {}).get("charts", [])
        stats["charts_total"] += len(charts)
        for chart in charts:
            chart_file = chart.get("file", "")
            if chart_file:
                pdf_path = PROJECT_ROOT / Path(chart_file).parent / "chart.pdf"
                if pdf_path.exists():
                    stats["charts_built"] += 1

    # Count modules
    infra_dir = PROJECT_ROOT / "infrastructure"
    for py_file in infra_dir.rglob("*.py"):
        if py_file.name != "__pycache__":
            stats["modules_exist"] += 1

    return stats


def _calc_percent(current: int, total: int) -> int:
    """Calculate percentage."""
    if total == 0:
        return 0
    return int(100 * current / total)


def _get_progress_class(current: int, total: int) -> str:
    """Get CSS class based on progress."""
    if total == 0:
        return "warning"
    pct = 100 * current / total
    if pct >= 80:
        return "success"
    elif pct >= 40:
        return "warning"
    return "danger"


def _generate_topic_rows(manifest: dict) -> str:
    """Generate topic table rows."""
    rows = []
    for topic in manifest.get("topics", []):
        topic_id = topic["id"]
        title = topic["title"]
        status = topic.get("status", "pending")
        assets = topic.get("assets", {})

        # Check slides
        topic_dir = _get_topic_dir(topic)
        overview_exists = (topic_dir / f"{topic_id}_overview.pdf").exists()
        deepdive_exists = (topic_dir / f"{topic_id}_deepdive.pdf").exists()
        slides_status = "complete" if overview_exists and deepdive_exists else ("draft" if overview_exists or deepdive_exists else "pending")

        # Check charts
        charts = assets.get("charts", [])
        charts_built = sum(1 for c in charts if _chart_pdf_exists(c))
        charts_status = f"{charts_built}/{len(charts)}"

        # Check notebook
        notebook = assets.get("notebook", {})
        nb_path = PROJECT_ROOT / "notebooks" / notebook.get("file", "")
        nb_status = "complete" if nb_path.exists() else "pending"

        rows.append(f'''
            <tr>
                <td><strong>{topic_id}</strong></td>
                <td>{title}</td>
                <td><span class="status {status}">{status}</span></td>
                <td><span class="status {slides_status}">{'Yes' if slides_status == 'complete' else 'No'}</span></td>
                <td>{charts_status}</td>
                <td><span class="status {nb_status}">{'Yes' if nb_status == 'complete' else 'No'}</span></td>
            </tr>
        ''')

    return "\n".join(rows)


def _generate_infra_rows() -> str:
    """Generate infrastructure table rows."""
    components = [
        ("Validators", "infrastructure/validators", ["latex_validator.py", "link_validator.py", "notebook_validator.py", "chart_validator.py"]),
        ("Builders", "infrastructure/builders", ["slide_builder.py", "chart_builder.py", "notebook_builder.py", "quiz_builder.py"]),
        ("Reporters", "infrastructure/reporters", ["progress_report.py", "build_report.py", "coverage_report.py", "quality_report.py"]),
        ("Generators", "infrastructure/generators", ["syllabus_generator.py", "rubric_generator.py", "guide_generator.py"]),
        ("Deployers", "infrastructure/deployers", ["github_deployer.py", "colab_deployer.py"]),
    ]

    rows = []
    for name, path, files in components:
        comp_path = PROJECT_ROOT / path
        existing = [f for f in files if (comp_path / f).exists()]
        status = "complete" if len(existing) == len(files) else ("draft" if existing else "pending")

        rows.append(f'''
            <tr>
                <td><strong>{name}</strong></td>
                <td>{len(existing)}/{len(files)}</td>
                <td><span class="status {status}">{status}</span></td>
            </tr>
        ''')

    return "\n".join(rows)


def _get_topic_dir(topic: dict) -> Path:
    """Get topic directory path."""
    topic_id = topic["id"]
    topic_title = topic["title"].replace(" ", "_").replace("&", "").replace("/", "_")
    return PROJECT_ROOT / "slides" / f"{topic_id}_{topic_title}"


def _chart_pdf_exists(chart: dict) -> bool:
    """Check if chart PDF exists."""
    chart_file = chart.get("file", "")
    if not chart_file:
        return False
    chart_dir = PROJECT_ROOT / Path(chart_file).parent
    return (chart_dir / "chart.pdf").exists()
