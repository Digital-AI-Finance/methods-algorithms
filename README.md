# Methods and Algorithms - MSc Data Science

> Master core ML algorithms and develop a systematic approach to choosing the right method for data-driven decision making in finance and business contexts.

## Course Overview

| Attribute | Value |
|-----------|-------|
| Program | MSc Data Science |
| Sessions | 6 x 3 hours |
| Prerequisites | Python, Statistics, Linear Algebra |
| Domain Focus | Finance and Banking |

## Topics

1. **Introduction & Linear Regression** - Factor models, house price prediction
2. **Logistic Regression** - Credit scoring, default prediction
3. **K-Nearest Neighbours & K-Means** - Customer segmentation, anomaly detection
4. **Random Forests** - Fraud detection, feature importance
5. **PCA & t-SNE** - Portfolio risk decomposition, visualization
6. **Embeddings & Reinforcement Learning** - Sentiment analysis, trading strategies

## Course Structure

Each lecture follows the **PMSP** framework:
- **Problem** (15 min) - Real finance use case
- **Method** (45 min) - Algorithm theory and mathematics
- **Solution** (45 min) - Implementation and results
- **Practice** (75 min) - Hands-on notebook exercises

## Materials

- **Slides**: LaTeX Beamer (overview + deep dive per topic)
- **Notebooks**: Google Colab with synthetic data
- **Quizzes**: Moodle format (30 min, timed)
- **Capstone**: Open-ended project (report only)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run course CLI
python infrastructure/course_cli.py status

# Build all slides
python infrastructure/course_cli.py build slides --all

# Validate all content
python infrastructure/course_cli.py validate --all
```

## Directory Structure

```
Methods_and_Algorithms/
├── infrastructure/     # Python course management CLI
├── slides/            # LaTeX slides per topic
├── notebooks/         # Colab notebooks
├── quizzes/           # Moodle XML files
├── datasets/          # Synthetic data
├── docs/              # GitHub Pages site
├── templates/         # Beamer, chart, notebook templates
├── rubrics/           # Grading rubrics
├── capstone/          # Project specification
└── syllabus/          # Multi-format syllabus
```

## Learning Outcomes

By course completion, students will:
1. **Select** appropriate ML methods for business problems
2. **Implement** solutions from scratch and with libraries
3. **Interpret** results for non-technical stakeholders

## License

Course materials for educational use only.
