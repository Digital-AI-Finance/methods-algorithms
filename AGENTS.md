<!-- Generated: 2026-01-25 | Updated: 2026-03-22 -->

# Methods and Algorithms

## Purpose

MSc Data Science course covering core ML algorithms with finance/banking applications. The course spans 6 sessions (3 hours each) following the PMSP framework (Problem-Method-Solution-Practice). This repository contains all course materials: LaTeX slides, Python visualization charts, Jupyter notebooks, quizzes, datasets, and supporting infrastructure.

**Recent updates**: Course underwent comprehensive hostile review (Feb 2026) scoring 67.7/100 (C+). All 6 lectures received systematic remediation with 1,886 insertions and 502 deletions. L06 received additional ultra-deep pedagogical flow review (Mar 2026) fixing symbol collisions, term-before-use violations, and topic transitions, plus RL overhaul adding bandits, Actor-Critic, PPO, offline RL, and 5 new charts (20-24). All 12 core PDFs compile clean with zero overflow warnings. L05 and L06 extended with formula-free visual lectures (Mar 2026): L05 has PCA simple + t-SNE simple; L06 has embeddings basics (L06a), RL basics (L06b), embeddings evolution (L06c), modern embeddings (L06d), and modern RL (L06e). 20+ interactive quizzes deployed to GitHub Pages. Discovery handouts published in `docs/handouts/`. Shared chart styling module introduced (`templates/chart_style.py`, used by 162+ chart.py files). Total: 47+ compiled PDFs across all variants.

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
| `templates/` | Beamer, chart, and notebook templates — including shared `chart_style.py` (see `templates/AGENTS.md`) |
| `notebooks/` | Jupyter notebooks for hands-on exercises (see `notebooks/AGENTS.md`) |
| `datasets/` | Synthetic datasets for each topic (see `datasets/AGENTS.md`) |
| `quizzes/` | Moodle XML quiz files (see `quizzes/AGENTS.md`) |
| `rubrics/` | Grading rubrics for assessments (see `rubrics/AGENTS.md`) |
| `capstone/` | Group assignment specification and templates (see `capstone/AGENTS.md`) |
| `presentations/` | Student presentation topics (see `presentations/AGENTS.md`) |
| `syllabus/` | Course syllabus materials (see `syllabus/AGENTS.md`) |
| `skills/` | Reusable AI skill definitions for lecture construction (see `skills/AGENTS.md`) |
| `tools/` | Utility scripts for batch maintenance, e.g. `patch_charts.py` (see `tools/AGENTS.md`) |
| `archiv/` | Archived prior versions of course materials |
| `docs/` | GitHub Pages deployment site with 47+ PDFs, 20 quizzes, and discovery handouts (see `docs/AGENTS.md`) |

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
- **Chart styling**: All chart.py files import `from chart_style import apply_style, COLORS, ...` from `templates/chart_style.py`; call `apply_style()` before plotting

### Course Structure

| Topic | Title | Finance Application | Status |
|-------|-------|---------------------|--------|
| L01 | Linear Regression | House price prediction, factor models, CAPM | Remediated (Feb 2026) |
| L02 | Logistic Regression | Credit scoring, default prediction, Basel scorecards | Remediated (Feb 2026) |
| L03 | KNN & K-Means | Customer segmentation, anomaly detection | Remediated (Feb 2026) |
| L04 | Random Forests | Fraud detection, feature importance, boosting | Remediated (Feb 2026), 32 charts (5 new GB) |
| L05 | PCA & t-SNE | Portfolio risk decomposition, visualization | Remediated (Feb 2026) |
| L06 | Embeddings & RL | Sentiment analysis, trading strategies | Remediated + RL overhaul (Mar 2026), 11 lectures (added L06f) |

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
