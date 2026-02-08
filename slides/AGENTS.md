<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-02-07 -->

# slides/

**Parent**: [../AGENTS.md](../AGENTS.md) (Methods_and_Algorithms root)

## Purpose

This directory contains all LaTeX Beamer slides for the 6-session MSc Data Science course on Methods and Algorithms. Each lesson follows the PMSP framework (Problem-Method-Solution-Practice) and includes finance/banking case studies.

**Recent remediation (Feb 2026)**: All lectures underwent systematic content review. Learning objectives rewritten to Bloom's Level 4-5, formulas added to overview slides, proofs/derivations added to deep dives. All 12 PDFs compile clean (zero overflow warnings).

## Structure

```
slides/
├── L01_Introduction_Linear_Regression/    # House price prediction
├── L02_Logistic_Regression/               # Credit scoring
├── L03_KNN_KMeans/                        # Customer segmentation
├── L04_Random_Forests/                    # Fraud detection
├── L05_PCA_tSNE/                          # Portfolio risk decomposition
└── L06_Embeddings_RL/                     # Sentiment analysis, trading
```

Each lesson directory contains:
- **LXX_overview.tex** - Overview slides (~17 slides with 7-8 charts, includes formulas/equations)
- **LXX_deepdive.tex** - Deep dive slides (~30 slides with 7-8 charts, includes proofs/derivations)
- **LXX_instructor_guide.md** - Teaching guide with PMSP breakdown
- **XX_chart_name/** - Chart directories (each with chart.py → chart.pdf)
- **images/** - XKCD cartoons and supporting visuals

## Lessons Overview

| Lesson | Topic | Finance Case | Difficulty | Charts |
|--------|-------|--------------|------------|--------|
| L01 | Linear Regression | House price prediction, factor models | Intermediate | 8 |
| L02 | Logistic Regression | Credit scoring, default prediction | Intermediate | 7 |
| L03 | KNN & K-Means | Customer segmentation, anomaly detection | Intermediate | 7 |
| L04 | Random Forests | Fraud detection, feature importance | Intermediate | 8 |
| L05 | PCA & t-SNE | Portfolio risk decomposition | Advanced | 12 |
| L06 | Embeddings & RL | Sentiment analysis, trading strategies | Advanced | 7 |

## Beamer Theme & Standards

All slides use:
- **Theme**: Madrid
- **Aspect ratio**: 16:9
- **Font size**: 8pt
- **Custom colors**: MLPurple (#3333B2), MLBlue (#0066CC), MLOrange (#FF7F0E), MLGreen (#2CA02C), MLRed (#D62728)
- **Footer**: "Methods and Algorithms | MSc Data Science | Slide X / Total"

## Chart Standards

Every chart MUST:
1. Live in its own directory: `XX_descriptive_name/chart.py`
2. Generate exactly ONE figure (NO subplots)
3. Use `figsize=(10, 6)` for consistent Beamer display
4. Output to `chart.pdf` in the same directory
5. Use scaled fonts (font.size=14, legend=13, labels=14)

**Naming convention**: Charts are numbered sequentially (01, 02, 03...) with the final chart always being `07_decision_flowchart` (when to use this algorithm).

## LaTeX Inclusion Rules

Charts are included in Beamer slides with:
```latex
\includegraphics[width=0.55\textwidth]{01_chart_name/chart.pdf}  % With text
\includegraphics[width=0.65\textwidth]{01_chart_name/chart.pdf}  % Chart-only slide
```

**Critical**: ZERO overflow warnings allowed. Use `--strict` flag when validating:
```bash
python infrastructure/course_cli.py validate latex --strict
```

## Building Slides

```bash
# Build all charts for one topic
python infrastructure/course_cli.py build charts --topic L01

# Build all charts for all topics
python infrastructure/course_cli.py build charts --topic all

# Compile LaTeX slides manually (from lesson directory)
cd slides/L01_Introduction_Linear_Regression
pdflatex -interaction=nonstopmode L01_overview.tex
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/

# Build slides via CLI (from project root)
python infrastructure/course_cli.py build slides --topic L01
```

## Content Tracking

All lesson assets are tracked in `manifest.json` at the project root. Each chart has:
- `id`: Chart identifier (e.g., "01_simple_regression")
- `file`: Path to chart.py script
- `status`: `pending`, `in_progress`, or `complete`

## PMSP Framework

All lessons follow the PMSP structure:
1. **Problem** (15 min): Present finance case, motivate the algorithm
2. **Method** (45 min): Mathematical foundation, assumptions, algorithm steps
3. **Solution** (45 min): Implementation (NumPy + scikit-learn), live coding
4. **Practice** (75 min): Hands-on Jupyter notebook with exercises

Instructor guides provide detailed timing, discussion prompts, common misconceptions, and exercise solutions.

## Common Commands

```bash
# Check slide status
python infrastructure/course_cli.py status --detailed

# Validate all LaTeX files
python infrastructure/course_cli.py validate latex

# List all charts for a topic
python infrastructure/course_cli.py inventory list --topic L01

# Run full audit
python run_audit.py
```

## Related Directories

- `../templates/` - Beamer and chart templates
- `../notebooks/` - Jupyter notebooks for Practice phase
- `../datasets/` - Synthetic datasets for each lesson
- `../infrastructure/validators/` - LaTeX validation scripts

## Children

- [L01_Introduction_Linear_Regression/AGENTS.md](L01_Introduction_Linear_Regression/AGENTS.md)
- [L02_Logistic_Regression/AGENTS.md](L02_Logistic_Regression/AGENTS.md)
- [L03_KNN_KMeans/AGENTS.md](L03_KNN_KMeans/AGENTS.md)
- [L04_Random_Forests/AGENTS.md](L04_Random_Forests/AGENTS.md)
- [L05_PCA_tSNE/AGENTS.md](L05_PCA_tSNE/AGENTS.md)
- [L06_Embeddings_RL/AGENTS.md](L06_Embeddings_RL/AGENTS.md)
