"""
Report generator for audit results.

Supports three output formats:
- Console (terminal output)
- JSON (machine-readable)
- HTML (visual dashboard)
"""
import json
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .audit_system import AuditResult

PROJECT_ROOT = Path(__file__).parent.parent.parent


def print_console_report(result: "AuditResult") -> str:
    """Generate and print console-friendly report."""
    lines = []

    # Header
    lines.append("=" * 60)
    lines.append("  COURSE AUDIT REPORT - Methods and Algorithms")
    lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 60)
    lines.append("")

    # Summary
    lines.append("SUMMARY")
    lines.append("-" * 40)
    s = result.summary
    lines.append(f"  Directories:     {s['directories']['found']}/{s['directories']['expected']} ({s['directories']['percent']}%)")
    lines.append(f"  Python Modules:  {s['python_modules']['found']}/{s['python_modules']['expected']} ({s['python_modules']['percent']}%)")
    lines.append(f"  Templates:       {s['templates']['found']}/{s['templates']['expected']} ({s['templates']['percent']}%)")
    lines.append(f"  Config Files:    {s['config_files']['found']}/{s['config_files']['expected']} ({s['config_files']['percent']}%)")
    lines.append(f"  Content Items:   {s['content']['found']}/{s['content']['expected']} ({s['content']['percent']}%)")
    lines.append("")

    # Functional Tests
    if result.functional_tests:
        lines.append("FUNCTIONAL TESTS")
        lines.append("-" * 40)
        for test in result.functional_tests:
            icon = "[PASS]" if test.status == "pass" else "[FAIL]" if test.status == "fail" else "[SKIP]"
            error_msg = f" - {test.error}" if test.error else ""
            lines.append(f"  {icon} {test.name}{error_msg}")
        lines.append("")

    # Gap Analysis
    lines.append("GAP ANALYSIS")
    lines.append("-" * 40)

    # Group by priority
    priority_groups = {1: [], 2: [], 3: [], 4: []}
    for item in result.missing_items:
        priority_groups.get(item.priority, []).append(item)

    priority_labels = {
        1: "Priority 1 (Critical):",
        2: "Priority 2 (High):",
        3: "Priority 3 (Medium):",
        4: "Priority 4 (Low):"
    }

    for priority in [1, 2, 3, 4]:
        items = priority_groups.get(priority, [])
        if items:
            lines.append(f"  {priority_labels[priority]}")
            for item in items[:10]:  # Limit to 10 per category
                lines.append(f"    - {item.path}")
            if len(items) > 10:
                lines.append(f"    ... and {len(items) - 10} more")
            lines.append("")

    # Recommendations
    if result.recommendations:
        lines.append("RECOMMENDATIONS")
        lines.append("-" * 40)
        for i, rec in enumerate(result.recommendations[:10], 1):
            lines.append(f"  {i}. [{rec['priority']}] {rec['action']}")
            lines.append(f"     Reason: {rec['reason']}")
        if len(result.recommendations) > 10:
            lines.append(f"  ... and {len(result.recommendations) - 10} more")
        lines.append("")

    lines.append("=" * 60)

    report = "\n".join(lines)
    print(report)
    return report


def generate_json_report(result: "AuditResult", output_path: Path = None) -> str:
    """Generate JSON report."""
    report_data = {
        "metadata": result.metadata,
        "summary": result.summary,
        "functional_tests": [
            {
                "name": t.name,
                "status": t.status,
                "duration_ms": t.duration_ms,
                "error": t.error
            }
            for t in result.functional_tests
        ],
        "missing_items": [
            {
                "path": item.path,
                "category": item.category,
                "priority": item.priority
            }
            for item in result.missing_items
        ],
        "recommendations": result.recommendations,
        "details": {
            "directories": {
                "found": [d.path for d in result.directories if d.found],
                "missing": [d.path for d in result.directories if not d.found]
            },
            "python_modules": {
                "found": [m.path for m in result.python_modules if m.found],
                "missing": [m.path for m in result.python_modules if not m.found]
            },
            "templates": {
                "found": [t.path for t in result.templates if t.found],
                "missing": [t.path for t in result.templates if not t.found]
            },
            "config_files": {
                "found": [c.path for c in result.config_files if c.found],
                "missing": [c.path for c in result.config_files if not c.found]
            },
            "content_items": {
                "found": [c.path for c in result.content_items if c.found],
                "missing": [c.path for c in result.content_items if not c.found]
            }
        }
    }

    json_str = json.dumps(report_data, indent=2)

    if output_path:
        output_path.write_text(json_str)
        print(f"JSON report saved to: {output_path}")

    return json_str


def generate_markdown_report(result: "AuditResult", output_path: Path = None) -> str:
    """Generate Markdown report."""
    lines = []

    lines.append("# Course Audit Report - Methods and Algorithms")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Summary Table
    lines.append("## Summary")
    lines.append("")
    lines.append("| Category | Found | Expected | Completion |")
    lines.append("|----------|-------|----------|------------|")
    s = result.summary
    lines.append(f"| Directories | {s['directories']['found']} | {s['directories']['expected']} | {s['directories']['percent']}% |")
    lines.append(f"| Python Modules | {s['python_modules']['found']} | {s['python_modules']['expected']} | {s['python_modules']['percent']}% |")
    lines.append(f"| Templates | {s['templates']['found']} | {s['templates']['expected']} | {s['templates']['percent']}% |")
    lines.append(f"| Config Files | {s['config_files']['found']} | {s['config_files']['expected']} | {s['config_files']['percent']}% |")
    lines.append(f"| Content Items | {s['content']['found']} | {s['content']['expected']} | {s['content']['percent']}% |")
    lines.append("")

    # Functional Tests
    if result.functional_tests:
        lines.append("## Functional Tests")
        lines.append("")
        lines.append("| Test | Status | Duration | Error |")
        lines.append("|------|--------|----------|-------|")
        for test in result.functional_tests:
            status_icon = "PASS" if test.status == "pass" else "FAIL" if test.status == "fail" else "SKIP"
            error = test.error[:50] + "..." if len(test.error) > 50 else test.error
            lines.append(f"| {test.name} | {status_icon} | {test.duration_ms}ms | {error} |")
        lines.append("")

    # Missing Items by Priority
    lines.append("## Gap Analysis")
    lines.append("")

    priority_labels = {
        1: "### Priority 1 (Critical)",
        2: "### Priority 2 (High)",
        3: "### Priority 3 (Medium)",
        4: "### Priority 4 (Low)"
    }

    priority_groups = {1: [], 2: [], 3: [], 4: []}
    for item in result.missing_items:
        priority_groups.get(item.priority, []).append(item)

    for priority in [1, 2, 3, 4]:
        items = priority_groups.get(priority, [])
        if items:
            lines.append(priority_labels[priority])
            lines.append("")
            for item in items:
                lines.append(f"- `{item.path}` ({item.category})")
            lines.append("")

    # Recommendations
    if result.recommendations:
        lines.append("## Recommendations")
        lines.append("")
        for i, rec in enumerate(result.recommendations[:15], 1):
            lines.append(f"{i}. **[P{rec['priority']}]** {rec['action']}")
            lines.append(f"   - Reason: {rec['reason']}")
        lines.append("")

    md_str = "\n".join(lines)

    if output_path:
        output_path.write_text(md_str)
        print(f"Markdown report saved to: {output_path}")

    return md_str


def generate_html_report(result: "AuditResult", output_path: Path = None) -> str:
    """Generate HTML dashboard report."""
    s = result.summary

    # Calculate overall progress
    total_found = (s['directories']['found'] + s['python_modules']['found'] +
                   s['templates']['found'] + s['config_files']['found'])
    total_expected = (s['directories']['expected'] + s['python_modules']['expected'] +
                      s['templates']['expected'] + s['config_files']['expected'])
    overall_percent = round(100 * total_found / total_expected) if total_expected > 0 else 0

    # Color based on percentage
    def get_color(pct):
        if pct >= 80:
            return "#22c55e"  # green
        elif pct >= 50:
            return "#eab308"  # yellow
        else:
            return "#ef4444"  # red

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Audit Dashboard - Methods and Algorithms</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #e2e8f0; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ font-size: 24px; margin-bottom: 8px; color: #f8fafc; }}
        .subtitle {{ color: #94a3b8; margin-bottom: 24px; }}
        .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }}
        .card {{ background: #1e293b; border-radius: 12px; padding: 20px; }}
        .card-title {{ font-size: 12px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }}
        .card-value {{ font-size: 32px; font-weight: 700; }}
        .card-detail {{ font-size: 14px; color: #64748b; margin-top: 4px; }}
        .progress-bar {{ height: 8px; background: #334155; border-radius: 4px; margin-top: 12px; overflow: hidden; }}
        .progress-fill {{ height: 100%; border-radius: 4px; transition: width 0.3s; }}
        .section {{ background: #1e293b; border-radius: 12px; padding: 20px; margin-bottom: 16px; }}
        .section-title {{ font-size: 16px; font-weight: 600; margin-bottom: 16px; color: #f8fafc; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ text-align: left; padding: 12px; border-bottom: 1px solid #334155; }}
        th {{ color: #94a3b8; font-size: 12px; text-transform: uppercase; }}
        .status-pass {{ color: #22c55e; }}
        .status-fail {{ color: #ef4444; }}
        .status-skip {{ color: #94a3b8; }}
        .priority-1 {{ color: #ef4444; }}
        .priority-2 {{ color: #f97316; }}
        .priority-3 {{ color: #eab308; }}
        .badge {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 12px; }}
        .badge-critical {{ background: #7f1d1d; color: #fecaca; }}
        .badge-high {{ background: #7c2d12; color: #fed7aa; }}
        .badge-medium {{ background: #713f12; color: #fef08a; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Course Audit Dashboard</h1>
        <p class="subtitle">Methods and Algorithms - Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>

        <div class="cards">
            <div class="card">
                <div class="card-title">Overall Progress</div>
                <div class="card-value" style="color: {get_color(overall_percent)}">{overall_percent}%</div>
                <div class="card-detail">{total_found} of {total_expected} items</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {overall_percent}%; background: {get_color(overall_percent)}"></div>
                </div>
            </div>
            <div class="card">
                <div class="card-title">Directories</div>
                <div class="card-value" style="color: {get_color(s['directories']['percent'])}">{s['directories']['percent']}%</div>
                <div class="card-detail">{s['directories']['found']} of {s['directories']['expected']}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {s['directories']['percent']}%; background: {get_color(s['directories']['percent'])}"></div>
                </div>
            </div>
            <div class="card">
                <div class="card-title">Python Modules</div>
                <div class="card-value" style="color: {get_color(s['python_modules']['percent'])}">{s['python_modules']['percent']}%</div>
                <div class="card-detail">{s['python_modules']['found']} of {s['python_modules']['expected']}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {s['python_modules']['percent']}%; background: {get_color(s['python_modules']['percent'])}"></div>
                </div>
            </div>
            <div class="card">
                <div class="card-title">Templates</div>
                <div class="card-value" style="color: {get_color(s['templates']['percent'])}">{s['templates']['percent']}%</div>
                <div class="card-detail">{s['templates']['found']} of {s['templates']['expected']}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {s['templates']['percent']}%; background: {get_color(s['templates']['percent'])}"></div>
                </div>
            </div>
            <div class="card">
                <div class="card-title">Functional Tests</div>
                <div class="card-value" style="color: {get_color(s['functional_tests']['percent'])}">{s['functional_tests']['passed']}/{s['functional_tests']['total']}</div>
                <div class="card-detail">Tests passing</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {s['functional_tests']['percent']}%; background: {get_color(s['functional_tests']['percent'])}"></div>
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Functional Tests</div>
            <table>
                <thead>
                    <tr><th>Test</th><th>Status</th><th>Duration</th><th>Error</th></tr>
                </thead>
                <tbody>
'''

    for test in result.functional_tests:
        status_class = f"status-{test.status}"
        error = test.error[:60] + "..." if len(test.error) > 60 else test.error
        html += f'''                    <tr>
                        <td>{test.name}</td>
                        <td class="{status_class}">{test.status.upper()}</td>
                        <td>{test.duration_ms}ms</td>
                        <td>{error}</td>
                    </tr>
'''

    html += '''                </tbody>
            </table>
        </div>

        <div class="section">
            <div class="section-title">Missing Items (Top 20)</div>
            <table>
                <thead>
                    <tr><th>Path</th><th>Category</th><th>Priority</th></tr>
                </thead>
                <tbody>
'''

    for item in result.missing_items[:20]:
        priority_class = f"priority-{item.priority}"
        badge_class = {1: "badge-critical", 2: "badge-high", 3: "badge-medium"}.get(item.priority, "")
        priority_label = {1: "Critical", 2: "High", 3: "Medium", 4: "Low"}.get(item.priority, "")
        html += f'''                    <tr>
                        <td><code>{item.path}</code></td>
                        <td>{item.category}</td>
                        <td><span class="badge {badge_class}">{priority_label}</span></td>
                    </tr>
'''

    html += '''                </tbody>
            </table>
        </div>

        <div class="section">
            <div class="section-title">Recommendations</div>
            <table>
                <thead>
                    <tr><th>#</th><th>Action</th><th>Reason</th><th>Priority</th></tr>
                </thead>
                <tbody>
'''

    for i, rec in enumerate(result.recommendations[:10], 1):
        badge_class = {1: "badge-critical", 2: "badge-high", 3: "badge-medium"}.get(rec['priority'], "")
        priority_label = {1: "Critical", 2: "High", 3: "Medium", 4: "Low"}.get(rec['priority'], "")
        html += f'''                    <tr>
                        <td>{i}</td>
                        <td>{rec['action']}</td>
                        <td>{rec['reason']}</td>
                        <td><span class="badge {badge_class}">{priority_label}</span></td>
                    </tr>
'''

    html += '''                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
'''

    if output_path:
        output_path.write_text(html)
        print(f"HTML dashboard saved to: {output_path}")

    return html


def generate_all_reports(result: "AuditResult", output_dir: Path = None) -> dict:
    """Generate all report formats."""
    if output_dir is None:
        output_dir = PROJECT_ROOT

    console = print_console_report(result)
    json_report = generate_json_report(result, output_dir / "audit_report.json")
    md_report = generate_markdown_report(result, output_dir / "audit_report.md")
    html_report = generate_html_report(result, output_dir / "audit_dashboard.html")

    return {
        "console": console,
        "json": json_report,
        "markdown": md_report,
        "html": html_report
    }
