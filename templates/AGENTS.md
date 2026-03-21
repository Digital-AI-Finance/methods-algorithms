# templates/

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-03-21 -->

**Generated**: 2026-01-25 | **Updated**: 2026-03-21
**Purpose**: Source-of-truth templates for all course content - charts, slides, notebooks, quizzes, and instructor guides

---

## Overview

This directory contains the master templates that define the styling, structure, and conventions for all course materials. **These templates are the authoritative source** for formatting standards - all content in `slides/`, `notebooks/`, and `quizzes/` must adhere to these specifications.

---

## Key Files

| File | Purpose | Used By |
|------|---------|---------|
| `chart_style.py` | **Shared chart styling module** (Mar 2026): defines `apply_style()`, `COLORS`, and ML color constants (`MLPURPLE`, `MLBLUE`, `MLORANGE`, `MLGREEN`, `MLRED`, `MLLAVENDER`). Imported by all 162+ `chart.py` files. | All `XX_chart_name/chart.py` files |
| `chart_template.py` | Python chart template boilerplate with correct import block and `apply_style()` call | New chart.py files |
| `beamer_template.tex` | Master LaTeX/Beamer slide template with PMSP structure | All `L0X_overview.tex` and `L0X_deepdive.tex` files |
| `beamer_template_v2.tex` | Extended v2 Beamer template with additional layout patterns | Reference template |
| `notebook_template.ipynb` | Jupyter notebook template with standard structure | All `notebooks/L0X_*.ipynb` files |
| `quiz_template.xml` | Moodle XML quiz template | All `quizzes/quiz*.xml` files |
| `instructor_guide_template.md` | Instructor guide template | All `slides/L0X_Topic/L0X_instructor_guide.md` files |

---

## For AI Agents

### Using These Templates

When creating or modifying course content, **ALWAYS reference these templates first**:

1. **Chart creation**: Copy `chart_template.py` to new chart folder; it already contains the `chart_style` import block — do not add inline `plt.rcParams.update` or color constants
2. **Slide creation**: Use `beamer_template.tex` structure with PMSP sections (Problem, Method, Solution, Practice)
3. **Notebook creation**: Use `notebook_template.ipynb` structure (Setup → Theory → Scratch Implementation → scikit-learn → Exercises)
4. **Quiz creation**: Follow `quiz_template.xml` XML structure for Moodle compatibility
5. **Instructor guide**: Use `instructor_guide_template.md` for consistent guide structure

### Critical Standards

#### Beamer/LaTeX (beamer_template.tex)

```latex
% REQUIRED settings
\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}

% REQUIRED color palette (defined in template)
MLPurple: #3333B2
MLBlue: #0066CC
MLOrange: #FF7F0E
MLGreen: #2CA02C
MLRed: #D62728

% Chart inclusion widths
0.55\textwidth  % With text alongside
0.65\textwidth  % Chart-only slides

% Custom commands
\bottomnote{...}  % Slide footnotes
\highlight{...}   % Orange bold text
```

**PMSP Structure** (must follow this order):
1. Problem (finance use case, business challenge)
2. Method (algorithm overview, mathematical foundation)
3. Solution (implementation, results visualization)
4. Practice (hands-on exercises, Colab notebook link)
5. Decision Framework (when to use, pros/cons)
6. Summary (key takeaways, references)

**Overflow Prevention**:
- Max 3-4 bullet points per slide
- Use `\vspace{1em}` for spacing instead of extra items
- Run `python infrastructure/course_cli.py validate latex --strict` to catch "Overfull" warnings

#### Chart Python (chart_style.py + chart_template.py)

`chart_style.py` is the **shared style module** (introduced Mar 2026). All chart.py files MUST import it:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()
```

`apply_style()` sets all rcParams. Font sizes after `apply_style()`:
- font.size: 15, axes.labelsize: 16, axes.titlesize: 18
- xtick/ytick: 14, legend: 13, figsize: (10, 6), dpi: 150

**Do NOT define inline `plt.rcParams.update()` or color constants** — use the shared module. Use `tools/patch_charts.py` to migrate old chart.py files.

```python
# REQUIRED outputs
# 1. Single figure only (no subplots)
# 2. File: chart.pdf in same directory
# 3. savefig with facecolor='white', bbox_inches='tight'
```

**Chart folder structure**:
```
XX_descriptive_name/
├── chart.py          # Python script
└── chart.pdf         # Generated output
```

#### Notebook (notebook_template.ipynb)

**Standard cell structure**:
1. Title + Colab badge
2. Learning Objectives
3. Setup (imports, random seed, plotting config)
4. Theory Recap
5. Generate/Load Data
6. NumPy Implementation (from scratch)
7. scikit-learn Implementation
8. Visualization
9. Exercises (with solutions)
10. Summary

**Key conventions**:
- `np.random.seed(42)` for reproducibility
- Try local dataset first, fallback to GitHub URL for Colab compatibility
- Include both working solutions and exercise placeholders

#### Quiz XML (quiz_template.xml)

**Moodle XML structure**:
```xml
<question type="multichoice">
  <name><text>Question Name</text></name>
  <questiontext format="html">
    <text><![CDATA[<p>Question text</p>]]></text>
  </questiontext>
  <defaultgrade>1</defaultgrade>
  <penalty>0.3333333</penalty>
  <single>true</single>
  <shuffleanswers>true</shuffleanswers>
  <answernumbering>abc</answernumbering>

  <!-- Correct answer: fraction="100" -->
  <answer fraction="100" format="html">
    <text><![CDATA[Correct answer]]></text>
    <feedback format="html">
      <text><![CDATA[Explanation why correct]]></text>
    </feedback>
  </answer>

  <!-- Incorrect answers: fraction="0" -->
  <answer fraction="0" format="html">
    <text><![CDATA[Incorrect answer]]></text>
    <feedback format="html">
      <text><![CDATA[Explanation why incorrect]]></text>
    </feedback>
  </answer>
</question>
```

### Validation Requirements

Before committing template changes:

1. **LaTeX**: Test compile with `pdflatex -interaction=nonstopmode beamer_template.tex`
2. **Charts**: Run `python chart_template.py` → verify chart.pdf generated
3. **Notebooks**: Open in Jupyter, run all cells without errors
4. **Quiz XML**: Validate XML syntax with `xmllint quiz_template.xml`

### Dependencies

**LaTeX/Beamer**:
- TeX Live or MiKTeX distribution
- Packages: inputenc, fontenc, amsmath, amssymb, graphicx, booktabs, tikz, hyperref

**Python**:
- matplotlib (chart generation)
- numpy (data generation)
- jupyter/nbformat (notebook validation)

**XML**:
- lxml or xmllint (quiz validation)

---

## Template Modification Protocol

**CRITICAL**: Changing templates affects ALL course content downstream.

**Before modifying templates**:
1. Document reason for change
2. Check impact on existing content (run full validation)
3. Update this AGENTS.md file with new conventions
4. Regenerate sample content to verify compatibility

**After template changes**:
```bash
# Rebuild all affected content
python infrastructure/course_cli.py build charts --topic all
python infrastructure/course_cli.py build slides --topic all
python infrastructure/course_cli.py validate --all
```

---

## Common Template Use Cases

### Creating New Chart
```bash
# 1. Create folder
mkdir slides/L01_Introduction_Linear_Regression/08_new_chart

# 2. Copy template (already has chart_style import block)
cp templates/chart_template.py slides/L01_Introduction_Linear_Regression/08_new_chart/chart.py

# 3. Edit chart.py: update data generation and plotting code
#    DO NOT add inline rcParams or color constants — use apply_style() + COLORS

# 4. Run script from project root
python slides/L01_Introduction_Linear_Regression/08_new_chart/chart.py

# 5. Verify chart.pdf generated
```

### Creating New Slide Deck
```bash
# 1. Copy template
cp templates/beamer_template.tex slides/L07_New_Topic/L07_overview.tex

# 2. Replace placeholders: TOPIC_SHORT, TOPIC_TITLE, SUBTITLE, FINANCE_CASE

# 3. Add chart references and content

# 4. Compile
cd slides/L07_New_Topic
pdflatex -interaction=nonstopmode L07_overview.tex

# 5. Validate no overflow warnings
python ../../infrastructure/course_cli.py validate latex --strict
```

### Creating New Notebook
```bash
# 1. Copy template
cp templates/notebook_template.ipynb notebooks/L07_new_topic.ipynb

# 2. Edit cells: update title, learning objectives, code examples

# 3. Test execution
jupyter nbconvert --execute --to notebook notebooks/L07_new_topic.ipynb
```

---

## Color Palette Reference

All charts and slides use this consistent palette:

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| MLPurple (primary) | #3333B2 | (51, 51, 178) | Titles, structure elements, primary data |
| MLBlue (secondary) | #0066CC | (0, 102, 204) | Secondary data, scatter points |
| MLOrange (accent) | #FF7F0E | (255, 127, 14) | Highlights, emphasis, warnings |
| MLGreen (success) | #2CA02C | (44, 160, 44) | Positive indicators, "when to use" |
| MLRed (danger) | #D62728 | (214, 39, 40) | Errors, "when NOT to use" |
| MLLavender | #ADADE0 | (173, 173, 224) | Light fills, backgrounds |

**Usage guidelines**:
- Primary data: MLPurple or MLBlue
- Comparison: Use MLBlue vs MLOrange
- Good/Bad: MLGreen vs MLRed
- Avoid using >3 colors per chart for clarity

---

## Related Files

- **Parent hierarchy**: `../AGENTS.md` (project root)
- **Generated content**: `slides/L0X_Topic/`, `notebooks/`, `quizzes/`
- **Validators**: `infrastructure/validators/latex_validator.py`, `infrastructure/validators/chart_validator.py`
- **CLI**: `infrastructure/course_cli.py` (build and validate commands)
