<!-- Generated: 2026-01-25 | Updated: 2026-01-25 -->

# Methods and Algorithms

## Purpose

MSc Data Science course covering core ML algorithms with finance/banking applications. The course spans 6 sessions (3 hours each) following the PMSP framework (Problem-Method-Solution-Practice). This repository contains all course materials: LaTeX slides, Python visualization charts, Jupyter notebooks, quizzes, datasets, and supporting infrastructure.

## Key Files

| File | Description |
|------|-------------|
| `manifest.json` | Course content inventory tracking all assets and their completion status |
| `CLAUDE.md` | AI assistant instructions for working with this codebase |
| `README.md` | Course overview and quick start guide |
| `requirements.txt` | Python dependencies for charts and notebooks |
| `config.yaml` | Course configuration settings |
| `run_audit.py` | Full course audit script (generates JSON, MD, HTML reports) |
| `setup_structure.py` | Initial repository scaffolding script |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `infrastructure/` | Python CLI for course management (see `infrastructure/AGENTS.md`) |
| `slides/` | LaTeX Beamer slides organized by topic L01-L06 (see `slides/AGENTS.md`) |
| `templates/` | Beamer, chart, and notebook templates (see `templates/AGENTS.md`) |
| `notebooks/` | Jupyter notebooks for hands-on exercises (see `notebooks/AGENTS.md`) |
| `datasets/` | Synthetic datasets for each topic (see `datasets/AGENTS.md`) |
| `quizzes/` | Moodle XML quiz files (see `quizzes/AGENTS.md`) |
| `rubrics/` | Grading rubrics for assessments (see `rubrics/AGENTS.md`) |
| `capstone/` | Capstone project specification and templates (see `capstone/AGENTS.md`) |
| `docs/` | GitHub Pages deployment site (see `docs/AGENTS.md`) |

## For AI Agents

### Working In This Directory

- **Primary entry point**: Use `python infrastructure/course_cli.py` for all course operations
- **Validation first**: Run `python infrastructure/course_cli.py validate --all` before committing changes
- **Manifest sync**: Update `manifest.json` when adding/removing assets
- **Chart generation**: Run charts from project root: `python slides/L0X_Topic/XX_chart_name/chart.py`

### Testing Requirements

```bash
# Validate all content
python infrastructure/course_cli.py validate --all

# Check for LaTeX overflow (strict mode)
python infrastructure/course_cli.py validate latex --strict

# Full audit with reports
python run_audit.py
```

### Common Patterns

- **Topic IDs**: L01 through L06 identify course topics
- **Status tracking**: Assets use `pending`, `in_progress`, `complete` states in manifest.json
- **PMSP framework**: Each topic follows Problem-Method-Solution-Practice structure
- **Chart conventions**: Each chart lives in `XX_descriptive_name/chart.py`, outputs `chart.pdf`

### Course Structure

| Topic | Title | Finance Application |
|-------|-------|---------------------|
| L01 | Linear Regression | House price prediction, factor models |
| L02 | Logistic Regression | Credit scoring, default prediction |
| L03 | KNN & K-Means | Customer segmentation, anomaly detection |
| L04 | Random Forests | Fraud detection, feature importance |
| L05 | PCA & t-SNE | Portfolio risk decomposition, visualization |
| L06 | Embeddings & RL | Sentiment analysis, trading strategies |

## Dependencies

### Internal

- All subdirectories follow consistent patterns defined in `templates/`
- `manifest.json` is the single source of truth for asset inventory
- `infrastructure/` orchestrates all build/validate/report operations

### External

- Python 3.x with matplotlib, numpy, scikit-learn for charts
- LaTeX with Beamer for slides
- Jupyter for notebooks

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
