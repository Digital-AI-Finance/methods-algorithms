"""Syllabus generator - creates syllabus in multiple formats."""
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List

PROJECT_ROOT = Path(__file__).parent.parent.parent
SYLLABUS_DIR = PROJECT_ROOT / "syllabus"


def generate_syllabus(manifest: dict, verbose: bool = False) -> str:
    """
    Generate syllabus markdown from manifest.

    Args:
        manifest: Course manifest
        verbose: Show detailed output

    Returns:
        Syllabus markdown string
    """
    course = manifest.get("course", {})
    topics = manifest.get("topics", [])

    lines = []

    # Header
    lines.append(f"# {course.get('title', 'Course Syllabus')}")
    lines.append("")
    lines.append(f"**Program**: MSc Data Science")
    lines.append(f"**Semester**: {course.get('semester', 'TBD')}")
    lines.append(f"**Version**: {course.get('version', '1.0.0')}")
    lines.append("")

    # Course Description
    lines.append("## Course Description")
    lines.append("")
    lines.append("This course covers fundamental methods and algorithms in machine learning,")
    lines.append("with a focus on practical applications in finance and business contexts.")
    lines.append("Students will learn when and how to apply different algorithms,")
    lines.append("implement them from scratch, and interpret results for business decisions.")
    lines.append("")

    # Learning Outcomes
    lines.append("## Learning Outcomes")
    lines.append("")
    lines.append("Upon completion, students will be able to:")
    lines.append("")
    lines.append("1. **Analyze** business problems and select appropriate ML methods")
    lines.append("2. **Implement** algorithms using Python (NumPy and scikit-learn)")
    lines.append("3. **Evaluate** model performance and interpret results")
    lines.append("4. **Communicate** findings to technical and non-technical audiences")
    lines.append("")

    # Prerequisites
    lines.append("## Prerequisites")
    lines.append("")
    lines.append("- Python programming (intermediate level)")
    lines.append("- Statistics (descriptive and inferential)")
    lines.append("- Linear algebra (vectors, matrices, operations)")
    lines.append("")

    # Schedule
    lines.append("## Course Schedule")
    lines.append("")
    lines.append("| Session | Topic | Description |")
    lines.append("|---------|-------|-------------|")

    for i, topic in enumerate(topics, 1):
        topic_id = topic.get("id", f"L{i:02d}")
        title = topic.get("title", "TBD")
        finance_case = topic.get("finance_case", "")
        lines.append(f"| {i} | {title} | {finance_case} |")

    lines.append("")

    # Assessment
    lines.append("## Assessment")
    lines.append("")
    lines.append("| Component | Weight | Description |")
    lines.append("|-----------|--------|-------------|")
    lines.append("| Quizzes | 30% | 3 quizzes, 30 min each, timed |")
    lines.append("| Presentation | 30% | 15 min individual presentation |")
    lines.append("| Capstone | 40% | Final project report |")
    lines.append("")

    # Quizzes
    lines.append("### Quizzes")
    lines.append("")
    for quiz in manifest.get("quizzes", []):
        quiz_topics = ", ".join(quiz.get("topics", []))
        lines.append(f"- **{quiz.get('title', quiz.get('id'))}**: Covers {quiz_topics}")
    lines.append("")

    # Presentations
    lines.append("### Presentations")
    lines.append("")
    lines.append("Each student presents once during the semester (15 minutes).")
    lines.append("Topics are assigned on a first-come, first-served basis.")
    lines.append("See the presentation topics document for available topics.")
    lines.append("")

    # Capstone
    lines.append("### Capstone Project")
    lines.append("")
    lines.append("An individual project applying course methods to a finance/business problem.")
    lines.append("Deliverable: Written report (10-15 pages PDF).")
    lines.append("See capstone specification for details.")
    lines.append("")

    # Materials
    lines.append("## Course Materials")
    lines.append("")
    lines.append("### Required")
    lines.append("")
    lines.append("- Course slides (provided)")
    lines.append("- Jupyter notebooks (Google Colab)")
    lines.append("")
    lines.append("### Recommended Textbooks")
    lines.append("")
    lines.append("- James et al., *Introduction to Statistical Learning* (free PDF)")
    lines.append("- Hastie et al., *Elements of Statistical Learning* (free PDF)")
    lines.append("")

    # Policies
    lines.append("## Policies")
    lines.append("")
    lines.append("### Attendance")
    lines.append("Attendance is expected. Contact instructor in advance for absences.")
    lines.append("")
    lines.append("### Academic Integrity")
    lines.append("All work must be original. Cite all sources. Collaboration on")
    lines.append("individual assignments is not permitted.")
    lines.append("")

    # Footer
    lines.append("---")
    lines.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d')}*")

    return "\n".join(lines)


def export_syllabus(
    manifest: dict,
    format: str = "all",
    verbose: bool = False
) -> Dict[str, Path]:
    """
    Export syllabus to various formats.

    Args:
        manifest: Course manifest
        format: Output format (md, pdf, html, all)
        verbose: Show detailed output

    Returns:
        Dictionary of format -> output path
    """
    print("Generating syllabus...")
    SYLLABUS_DIR.mkdir(parents=True, exist_ok=True)

    outputs = {}

    # Generate markdown
    md_content = generate_syllabus(manifest, verbose)
    md_path = SYLLABUS_DIR / "syllabus.md"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    outputs["md"] = md_path
    print(f"  [X] Markdown: {md_path.name}")

    if format in ["html", "all"]:
        html_path = _export_html(md_content, verbose)
        if html_path:
            outputs["html"] = html_path
            print(f"  [X] HTML: {html_path.name}")

    if format in ["pdf", "all"]:
        pdf_path = _export_pdf(md_path, verbose)
        if pdf_path:
            outputs["pdf"] = pdf_path
            print(f"  [X] PDF: {pdf_path.name}")

    return outputs


def _export_html(md_content: str, verbose: bool) -> Optional[Path]:
    """Export to HTML."""
    html_path = SYLLABUS_DIR / "syllabus.html"

    # Simple markdown to HTML conversion
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Syllabus</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
        }}
        h1 {{ color: #1a365d; border-bottom: 2px solid #3182ce; padding-bottom: 10px; }}
        h2 {{ color: #2c5282; margin-top: 30px; }}
        h3 {{ color: #2b6cb0; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #e2e8f0; padding: 10px; text-align: left; }}
        th {{ background: #edf2f7; }}
        code {{ background: #edf2f7; padding: 2px 6px; border-radius: 3px; }}
        ul {{ margin: 10px 0; }}
    </style>
</head>
<body>
{_md_to_html(md_content)}
</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return html_path


def _export_pdf(md_path: Path, verbose: bool) -> Optional[Path]:
    """Export to PDF using pandoc if available."""
    pdf_path = SYLLABUS_DIR / "syllabus.pdf"

    try:
        result = subprocess.run(
            ["pandoc", str(md_path), "-o", str(pdf_path),
             "--pdf-engine=pdflatex", "-V", "geometry:margin=1in"],
            capture_output=not verbose,
            text=True
        )
        if result.returncode == 0:
            return pdf_path
    except FileNotFoundError:
        if verbose:
            print("    [SKIP] pandoc not found")
    except Exception as e:
        if verbose:
            print(f"    [FAIL] {e}")

    return None


def _md_to_html(md: str) -> str:
    """Simple markdown to HTML converter."""
    import re

    html = md

    # Headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Lists
    lines = html.split('\n')
    result = []
    in_list = False
    for line in lines:
        if line.startswith('- '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(f'<li>{line[2:]}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
    if in_list:
        result.append('</ul>')
    html = '\n'.join(result)

    # Tables (simple)
    html = re.sub(r'\|(.+)\|', lambda m: _table_row(m.group(1)), html)

    # Paragraphs
    html = re.sub(r'\n\n', r'\n<p></p>\n', html)

    return html


def _table_row(content: str) -> str:
    """Convert table row."""
    cells = [c.strip() for c in content.split('|')]
    if all(c.startswith('-') for c in cells if c):
        return ''
    return '<tr>' + ''.join(f'<td>{c}</td>' for c in cells if c) + '</tr>'
