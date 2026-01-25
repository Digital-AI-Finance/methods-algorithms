# Generators Module - Document Generation

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 -->

## Purpose

Generation subsystem for creating course documentation from manifest data. Generates syllabi, rubrics, and instructor guides in multiple formats (Markdown, HTML, PDF).

**All generators return `str` or `Path`:** Generated content or output file path.

## Key Files

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `__init__.py` | Module exports | minimal | Package initialization |
| `syllabus_generator.py` | Generate course syllabus | 301 | `generate_syllabus()`, `export_syllabus()`, `_export_html()`, `_export_pdf()` |
| `rubric_generator.py` | Generate assessment rubrics | TBD | `generate_rubric()` (stub) |
| `guide_generator.py` | Generate instructor guides | TBD | `generate_guide()` (stub) |

## For AI Agents

### Module Architecture

All generators follow a **template-based generation pattern**:

```python
def generate_<type>(manifest: dict, **options) -> str:
    """
    Generate <type> content from manifest.

    Args:
        manifest: Course manifest
        **options: Generator-specific options

    Returns:
        Generated content as string (Markdown, HTML, etc.)
    """
    # Extract data from manifest
    # Format content using templates
    # Return formatted string

def export_<type>(manifest: dict, format: str = "all", **options) -> Dict[str, Path]:
    """
    Export <type> to files in multiple formats.

    Args:
        manifest: Course manifest
        format: Output format (md, html, pdf, all)
        **options: Generator-specific options

    Returns:
        Dictionary of format -> output file path
    """
    # Generate content
    # Save to files in requested formats
    # Return paths to generated files
```

### Syllabus Generator (`syllabus_generator.py`)

**Purpose:** Generate course syllabus from manifest data in multiple formats.

**Key Features:**
- Extracts course info from manifest.json
- Generates Markdown syllabus with standard sections
- Exports to HTML (standalone, styled)
- Exports to PDF (via pandoc if available)
- Includes all topics, quizzes, presentations, capstone

**Usage:**
```bash
# Generate syllabus in all formats
python infrastructure/course_cli.py syllabus --format all

# Generate specific format
python infrastructure/course_cli.py syllabus --format pdf
python infrastructure/course_cli.py syllabus --format html
```

**Syllabus Sections:**

**1. Header:**
```markdown
# Methods and Algorithms

**Program**: MSc Data Science
**Semester**: Spring 2026
**Version**: 1.0.0
```

**2. Course Description:**
- Overview of course content
- Focus on finance/business applications
- Implementation from scratch emphasis

**3. Learning Outcomes:**
1. Analyze business problems and select ML methods
2. Implement algorithms using Python
3. Evaluate model performance
4. Communicate findings

**4. Prerequisites:**
- Python programming (intermediate)
- Statistics (descriptive and inferential)
- Linear algebra (vectors, matrices)

**5. Course Schedule:**
```markdown
| Session | Topic | Description |
|---------|-------|-------------|
| 1 | Introduction & Linear Regression | Predict loan default risk |
| 2 | Logistic Regression | Credit card fraud detection |
| 3 | KNN & K-Means | Customer segmentation |
| 4 | Random Forests | Stock price prediction |
| 5 | PCA & t-SNE | Portfolio risk analysis |
| 6 | Embeddings & RL | Trading strategy optimization |
```

**6. Assessment:**
```markdown
| Component | Weight | Description |
|-----------|--------|-------------|
| Quizzes | 30% | 3 quizzes, 30 min each, timed |
| Presentation | 30% | 15 min individual presentation |
| Capstone | 40% | Final project report |
```

**7. Quizzes:**
- Quiz 1: Covers L01-L02
- Quiz 2: Covers L03-L04
- Quiz 3: Covers L05-L06

**8. Presentations:**
- Each student presents once (15 minutes)
- Topics assigned first-come, first-served
- See presentation topics document

**9. Capstone Project:**
- Individual project applying course methods
- Deliverable: Written report (10-15 pages PDF)
- See capstone specification for details

**10. Course Materials:**
- Required: Course slides, Jupyter notebooks
- Recommended: James et al. (ISLR), Hastie et al. (ESL)

**11. Policies:**
- Attendance expectations
- Academic integrity rules

**Generation Functions:**

**Markdown Generation:**
```python
def generate_syllabus(manifest: dict, verbose: bool = False) -> str:
    """Generate syllabus markdown from manifest."""
    course = manifest.get("course", {})
    topics = manifest.get("topics", [])

    lines = []
    lines.append(f"# {course.get('title', 'Course Syllabus')}")
    lines.append(f"**Program**: MSc Data Science")
    lines.append(f"**Semester**: {course.get('semester', 'TBD')}")
    # ... build all sections ...

    return "\n".join(lines)
```

**HTML Export:**
```python
def _export_html(md_content: str, verbose: bool) -> Optional[Path]:
    """Export to HTML with inline CSS."""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Course Syllabus</title>
    <style>
        body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; }}
        h1 {{ color: #1a365d; border-bottom: 2px solid #3182ce; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #e2e8f0; padding: 10px; }}
    </style>
</head>
<body>
    {_md_to_html(md_content)}
</body>
</html>'''

    html_path = SYLLABUS_DIR / "syllabus.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return html_path
```

**PDF Export:**
```python
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
    return None
```

**Markdown to HTML Converter:**
Simple converter for basic markdown elements:
```python
def _md_to_html(md: str) -> str:
    """Simple markdown to HTML converter."""
    html = md

    # Headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Lists (simple implementation)
    # Tables (regex-based)

    return html
```

**Export Function:**
```python
def export_syllabus(manifest: dict, format: str = "all", verbose: bool = False) -> Dict[str, Path]:
    """Export syllabus to various formats."""
    outputs = {}

    # Generate markdown
    md_content = generate_syllabus(manifest, verbose)
    md_path = SYLLABUS_DIR / "syllabus.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    outputs["md"] = md_path

    # Export HTML if requested
    if format in ["html", "all"]:
        html_path = _export_html(md_content, verbose)
        if html_path:
            outputs["html"] = html_path

    # Export PDF if requested and pandoc available
    if format in ["pdf", "all"]:
        pdf_path = _export_pdf(md_path, verbose)
        if pdf_path:
            outputs["pdf"] = pdf_path

    return outputs
```

**Testing:**
```python
from generators import generate_syllabus, export_syllabus
manifest = json.load(open("manifest.json"))

# Generate markdown only
syllabus_md = generate_syllabus(manifest)
assert "Methods and Algorithms" in syllabus_md
assert "Course Schedule" in syllabus_md

# Export to all formats
outputs = export_syllabus(manifest, format="all")
assert "md" in outputs
assert outputs["md"].exists()
```

### Rubric Generator (`rubric_generator.py`)

**Purpose:** Generate assessment rubrics for quizzes, presentations, and capstone (STUB).

**Planned Features:**
- Generate grading rubrics from templates
- Support different assessment types (quiz, presentation, project)
- Include criteria, point values, descriptors
- Export to Markdown, HTML, PDF

**Future Usage:**
```bash
python infrastructure/course_cli.py rubric --type presentation
python infrastructure/course_cli.py rubric --type capstone
```

**Planned Structure:**

**Presentation Rubric:**
```markdown
# Presentation Rubric (30 points)

| Criterion | Excellent (4) | Good (3) | Satisfactory (2) | Needs Improvement (1) |
|-----------|---------------|----------|------------------|-----------------------|
| Content Understanding | Deep understanding, connects concepts | Solid understanding | Basic understanding | Gaps in understanding |
| Visual Aids | Clear, effective slides | Good slides | Adequate slides | Poor slides |
| Communication | Clear, engaging delivery | Clear delivery | Adequate delivery | Unclear delivery |
| Time Management | 14-16 minutes, well-paced | 13-17 minutes | 12-18 minutes | <12 or >18 minutes |

**Total: _____ / 30 points**
```

**Capstone Rubric:**
```markdown
# Capstone Project Rubric (40 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Problem Definition | 5 | Clear business problem, relevant to course |
| Method Selection | 10 | Appropriate algorithm choice, justified |
| Implementation | 10 | Correct implementation, clean code |
| Evaluation | 8 | Proper metrics, validation, interpretation |
| Communication | 7 | Clear writing, visualizations, conclusions |

**Total: _____ / 40 points**
```

### Guide Generator (`guide_generator.py`)

**Purpose:** Generate instructor guides for each topic (STUB).

**Planned Features:**
- Generate teaching notes from topic data
- Include timing recommendations
- List common student questions
- Provide solution keys for exercises
- Export to Markdown, HTML

**Future Usage:**
```bash
python infrastructure/course_cli.py guide --topic L01
python infrastructure/course_cli.py guide --topic all
```

**Planned Structure:**

**Instructor Guide:**
```markdown
# L01: Introduction & Linear Regression - Instructor Guide

## Session Overview
- **Duration**: 90 minutes
- **Format**: 45 min lecture + 30 min practice + 15 min Q&A
- **Prerequisites**: Basic Python, numpy, pandas

## Learning Objectives
By the end of this session, students should be able to:
1. Explain when to use linear regression
2. Implement simple and multiple regression
3. Interpret coefficients and p-values
4. Evaluate model performance using R² and RMSE

## Session Outline
### Part 1: Problem (10 min)
- Present loan default prediction case
- Discuss real-world applications
- Show dataset (slides 1-3)

### Part 2: Method (25 min)
- Linear regression theory (slides 4-8)
- Gradient descent visualization (slide 9)
- Regularization (Ridge, Lasso) (slides 10-12)

### Part 3: Solution (20 min)
- Live coding demo (notebook)
- Fit model, interpret results
- Cross-validation

### Part 4: Practice (30 min)
- Students work on exercises
- Walk around, answer questions

### Wrap-up (5 min)
- Preview next session (Logistic Regression)
- Assign homework

## Common Student Questions
**Q: When should I use Ridge vs Lasso?**
A: Ridge when all features matter (shrink but keep all). Lasso when you want feature selection (some coefficients → 0).

**Q: What's a good R² value?**
A: Depends on domain. Finance: 0.3-0.5 is typical. Lab sciences: 0.8+ expected.

## Teaching Tips
- Emphasize interpretation over math
- Connect to banking examples throughout
- Use Colab notebooks for instant setup
- Have backup plan if Wi-Fi fails (local notebooks)

## Exercise Solutions
See `solutions/L01_exercises_solutions.ipynb`
```

### Common Generator Patterns

**1. Manifest Data Extraction:**
```python
def extract_topic_info(manifest: dict, topic_id: str) -> dict:
    """Extract topic data from manifest."""
    for topic in manifest["topics"]:
        if topic["id"] == topic_id:
            return {
                "id": topic["id"],
                "title": topic["title"],
                "finance_case": topic.get("finance_case", ""),
                "duration": topic.get("duration", "90 min"),
                "assets": topic.get("assets", {})
            }
    return {}
```

**2. Section Building:**
```python
def build_section(title: str, content: List[str], level: int = 2) -> str:
    """Build a markdown section."""
    header = "#" * level + " " + title
    lines = [header, ""]
    lines.extend(content)
    lines.append("")
    return "\n".join(lines)
```

**3. Table Generation:**
```python
def generate_table(headers: List[str], rows: List[List[str]]) -> str:
    """Generate markdown table."""
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["-" * (len(h) + 2) for h in headers]) + "|")
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)
```

**4. File Output:**
```python
def save_output(content: str, output_dir: Path, filename: str, format: str = "md") -> Path:
    """Save generated content to file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{filename}.{format}"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return output_path
```

### Testing Generators

**Syllabus Generation Test:**
```python
from generators import generate_syllabus, export_syllabus
manifest = json.load(open("manifest.json"))

# Test markdown generation
md = generate_syllabus(manifest)
assert "# Methods and Algorithms" in md
assert "Course Schedule" in md
assert "Assessment" in md
assert len(md.split("\n")) > 50  # Reasonable line count

# Test export to all formats
outputs = export_syllabus(manifest, format="all")
assert (outputs["md"]).exists()
if "html" in outputs:
    assert outputs["html"].exists()
    html_content = outputs["html"].read_text()
    assert "<!DOCTYPE html>" in html_content
if "pdf" in outputs:
    assert outputs["pdf"].exists()
    assert outputs["pdf"].stat().st_size > 1000  # PDF not empty
```

**Content Validation:**
```python
def validate_syllabus_content(md: str, manifest: dict) -> bool:
    """Validate syllabus contains all expected content."""
    # Check all topics listed
    for topic in manifest["topics"]:
        assert topic["title"] in md, f"Topic {topic['id']} missing"

    # Check all quizzes listed
    for quiz in manifest.get("quizzes", []):
        assert quiz["id"] in md, f"Quiz {quiz['id']} missing"

    # Check assessment section
    assert "Quizzes" in md and "30%" in md
    assert "Presentation" in md and "30%" in md
    assert "Capstone" in md and "40%" in md

    return True
```

### Performance Considerations

**Generation Speed:**
- Markdown generation: ~50ms (string concatenation)
- HTML conversion: ~100ms (regex-based)
- PDF export: ~2-5s (pandoc subprocess)

**Optimization:**
- Cache generated content
- Only regenerate if manifest changes
- Parallelize PDF generation for multiple documents

### Dependencies

**Required:**
- Python standard library (re, pathlib, subprocess, datetime)

**Optional:**
- `pandoc` (for PDF export via LaTeX)
- `pdflatex` (for pandoc PDF generation)

**External Files:**
- `manifest.json` (required)
- `syllabus/` directory (created automatically)

### Future Enhancements

**Template Engine:**
Use Jinja2 for more flexible templating:
```python
from jinja2 import Template

template = Template('''
# {{ course.title }}

## Topics
{% for topic in topics %}
- {{ topic.id }}: {{ topic.title }}
{% endfor %}
''')

output = template.render(course=course, topics=topics)
```

**Multi-Language Support:**
Generate syllabi in multiple languages:
```python
def generate_syllabus(manifest: dict, language: str = "en") -> str:
    translations = load_translations(language)
    # Use translations dictionary for section headers
```

**Custom Styling:**
Allow custom CSS for HTML export:
```python
def export_html(md_content: str, css_file: Path = None) -> Path:
    if css_file:
        css = css_file.read_text()
    else:
        css = DEFAULT_CSS
    # Insert custom CSS into HTML
```

---

**MANUAL:** This file documents the generator subsystem for creating course documentation. Generators extract data from manifest.json and format it as syllabi, rubrics, and guides. Primary implementation is syllabus_generator.py; rubric and guide generators are planned.
