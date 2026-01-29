# MSc Data Science: Methods and Algorithms - Course Development Plan

## Project Summary
- **Course**: Methods and Algorithms (MSc Data Science)
- **Students**: 10-15, individual presentations (15 min, each student presents once)
- **Sessions**: 6 x 3 hours
- **Repository**: GitHub (Digital-AI-Finance, private)
- **Working Directory**: `D:\Joerg\Research\slides\Methods_and_Algorithms`
- **Prerequisites**: Python + Statistics + Linear Algebra

## Course Purpose & Differentiators

### One-Sentence Purpose
> Master core ML algorithms and develop a systematic approach to choosing the right method for data-driven decision making in finance and business contexts.

### What Makes This Course Unique
| Differentiator | Description |
|----------------|-------------|
| **Finance Focus** | All examples from banking, risk, trading, fraud detection |
| **Decision Framework** | Emphasis on WHEN to use WHAT algorithm |
| **Practical Depth** | Balance of mathematical theory and hands-on implementation |

### Course-Level Problem-Solution
| Element | Description |
|---------|-------------|
| **PROBLEM** | Data scientists struggle to choose appropriate ML methods for business problems |
| **SOLUTION** | Systematic framework for algorithm selection with finance applications |
| **OUTCOME** | Students can select, implement, and interpret ML models for business decisions |

## Learning Outcomes (Bloom's Full Range Per Topic)

By course completion, students will demonstrate:

1. **Algorithm Selection** (Analyze/Evaluate)
   - Given a business problem, choose the appropriate ML method with justification

2. **Implementation** (Apply/Create)
   - Code ML solutions from scratch (NumPy) and with libraries (scikit-learn)

3. **Interpretation** (Understand/Evaluate)
   - Explain model results to non-technical stakeholders in business terms

## Pedagogical Framework

### Primary Approach: Problem-Based Learning
Each topic starts with a real finance problem that motivates the algorithm.

### Lecture Structure: Problem-Method-Solution-Practice (PMSP)

| Phase | Duration | Content |
|-------|----------|---------|
| **PROBLEM** | 15 min | Real finance use case, why existing methods fail |
| **METHOD** | 45 min | Algorithm theory, mathematics, intuition |
| **SOLUTION** | 45 min | Implementation, code walkthrough, results |
| **PRACTICE** | 75 min | Hands-on notebook, exercises, Q&A |

### Decision Framework (Three Formats Per Topic)
1. **When to Use / When NOT to Use** - Clear criteria checklist
2. **Pros/Cons/Tradeoffs Table** - Structured comparison matrix
3. **Decision Flowchart** - Visual algorithm selection guide

## Topics (6 Sessions) with Finance Use Cases

| # | Topic | Finance Use Case | Problem Statement |
|---|-------|------------------|-------------------|
| 1 | Introduction & Linear Regression | House price prediction, factor models | How do we model continuous outcomes from multiple features? |
| 2 | Logistic Regression | Credit scoring, default prediction | How do we predict binary outcomes with probability estimates? |
| 3 | KNN & K-Means | Customer segmentation, anomaly detection | How do we group similar entities or find nearest matches? |
| 4 | Random Forests | Fraud detection, feature importance | How do we build robust models and understand feature contributions? |
| 5 | PCA & t-SNE | Portfolio risk decomposition, visualization | How do we reduce dimensions while preserving structure? |
| 6 | Embeddings & RL | Sentiment analysis, trading strategies | How do we represent text and learn optimal sequential decisions? |

## Deliverables Overview

| Deliverable | Quantity | Format |
|-------------|----------|--------|
| Beamer Slides | 12 PDFs (overview + deep dive per topic) | LaTeX/PDF |
| Charts | ~8-12 per topic (48-72 total) | Python + PDF |
| Moodle Quizzes | 3 quizzes (MC format, 30 min timed) | Moodle XML |
| Presentation Topics | 15 total | Markdown list |
| Colab Notebooks | 6 (one per topic) | .ipynb on Colab |
| GitHub Pages | 1 site | HTML/CSS/JS |
| Synthetic Datasets | 6+ | CSV/JSON |
| **Capstone Project** | 1 (open-ended, report only) | PDF template |
| **Rubrics** | 2 (presentation + capstone) | Easy-to-grade format |
| **Syllabus** | 1 (multi-format export) | PDF + HTML + Moodle |
| **Instructor Guides** | 6 (one per lecture) | Markdown |
| **Decision Flowcharts** | 6 (one per topic) | Python/Graphviz |

---

## Python Course Management Infrastructure

### CLI Tool: `course_cli.py`

```
python course_cli.py <command> [options]

COMMANDS:
  build       Build course components
  validate    Run validation checks
  deploy      Deploy to GitHub/Colab
  status      Show progress dashboard
  inventory   Manage content inventory
  report      Generate reports
  syllabus    Export syllabus
```

### Command Details

| Command | Subcommands | Description |
|---------|-------------|-------------|
| `build slides` | `--topic L01` | Compile LaTeX slides |
| `build charts` | `--topic L01` | Generate all charts for topic |
| `build notebooks` | `--all` | Prepare notebooks for Colab |
| `build quizzes` | `--quiz 1` | Export quiz to Moodle XML |
| `validate latex` | `--strict` | Zero overflow, zero errors |
| `validate links` | `--external` | Check all URLs accessible |
| `validate notebooks` | `--execute` | Run all cells, check errors |
| `validate charts` | `--regenerate` | Verify chart generation |
| `deploy site` | `--prod` | Push to GitHub Pages |
| `deploy colab` | `--topic L01` | Sync notebook to Colab |
| `status` | `--detailed` | Show completion by component |
| `inventory list` | `--topic L01` | List all assets for topic |
| `inventory add` | `--type chart` | Add new asset to manifest |
| `report build` | | Build status report |
| `report coverage` | | Learning objectives coverage |
| `report progress` | | Overall completion dashboard |
| `report quality` | | Quality metrics summary |
| `syllabus export` | `--format pdf` | Generate syllabus |

### Infrastructure Files

```
infrastructure/
├── course_cli.py              # Main CLI entry point
├── config.yaml                # Course configuration
├── manifest.json              # Content inventory (JSON)
├── validators/
│   ├── latex_validator.py     # LaTeX compilation checks
│   ├── link_validator.py      # URL accessibility checks
│   ├── notebook_validator.py  # Jupyter execution checks
│   └── chart_validator.py     # Chart generation checks
├── builders/
│   ├── slide_builder.py       # LaTeX compilation
│   ├── chart_builder.py       # Run all chart.py scripts
│   ├── notebook_builder.py    # Prepare Colab notebooks
│   └── quiz_builder.py        # Moodle XML export
├── reporters/
│   ├── build_report.py        # What compiled/failed
│   ├── coverage_report.py     # Learning objectives mapping
│   ├── progress_report.py     # Completion percentages
│   └── quality_report.py      # Quality metrics
├── deployers/
│   ├── github_deployer.py     # Push to GitHub
│   └── colab_deployer.py      # Sync to Google Colab
├── generators/
│   ├── syllabus_generator.py  # Multi-format syllabus
│   ├── rubric_generator.py    # Easy-to-grade rubrics
│   └── guide_generator.py     # Instructor guides
└── templates/
    ├── beamer_template.tex
    ├── chart_template.py
    ├── notebook_template.ipynb
    ├── quiz_template.xml
    ├── syllabus_template.md
    └── rubric_template.md
```

---

## Content Manifest Schema (manifest.json)

```json
{
  "course": {
    "id": "methods-algorithms-2026",
    "title": "Methods and Algorithms",
    "version": "1.0.0",
    "semester": "Spring 2026"
  },
  "topics": [
    {
      "id": "L01",
      "title": "Introduction & Linear Regression",
      "status": "draft|review|complete",
      "finance_case": "House price prediction, factor models",
      "problem_statement": "How do we model continuous outcomes?",
      "learning_objectives": [
        {"id": "L01-O1", "text": "Derive OLS estimator", "bloom_level": "understand"},
        {"id": "L01-O2", "text": "Implement gradient descent", "bloom_level": "apply"},
        {"id": "L01-O3", "text": "Interpret coefficients", "bloom_level": "analyze"}
      ],
      "prerequisites": ["linear_algebra", "calculus", "python_basics"],
      "keywords": ["regression", "OLS", "gradient descent", "MSE", "R-squared"],
      "estimated_time_minutes": 180,
      "difficulty": "intermediate",
      "pmsp_sections": {
        "problem": {"start_slide": 1, "end_slide": 3},
        "method": {"start_slide": 4, "end_slide": 18},
        "solution": {"start_slide": 19, "end_slide": 32},
        "practice": {"start_slide": 33, "end_slide": 40}
      },
      "assets": {
        "overview_slides": {"file": "L01_overview.tex", "status": "pending"},
        "deepdive_slides": {"file": "L01_deepdive.tex", "status": "pending"},
        "charts": [
          {"id": "01_simple_regression", "file": "01_simple_regression/chart.py", "status": "pending"},
          {"id": "02_gradient_descent", "file": "02_gradient_descent/chart.py", "status": "pending"}
        ],
        "notebook": {"file": "L01_linear_regression.ipynb", "status": "pending"},
        "dataset": {"file": "housing_synthetic.csv", "status": "pending"},
        "decision_flowchart": {"file": "L01_decision_flowchart/chart.py", "status": "pending"},
        "instructor_guide": {"file": "L01_instructor_guide.md", "status": "pending"}
      },
      "decision_framework": {
        "when_to_use": [
          "Continuous target variable",
          "Linear relationship suspected",
          "Interpretability required"
        ],
        "when_not_to_use": [
          "Non-linear relationships",
          "Classification problems",
          "High multicollinearity"
        ],
        "pros": ["Interpretable", "Fast", "Well-understood"],
        "cons": ["Assumes linearity", "Sensitive to outliers"]
      },
      "related_topics": ["L02", "L04"],
      "created": "2026-01-07",
      "updated": "2026-01-07"
    }
  ],
  "quizzes": [...],
  "presentations": [...],
  "capstone": {...}
}
```

---

## Topic Dependency Graph

```
L01 (Linear Regression)
 │
 ├──> L02 (Logistic Regression) [extends classification]
 │     │
 │     └──> L03 (KNN/K-Means) [alternative classifiers]
 │
 └──> L04 (Random Forests) [ensemble methods]
       │
       └──> L05 (PCA/t-SNE) [dimensionality for trees]
             │
             └──> L06 (Embeddings/RL) [representations]
```

### Concept Map (Tracked Across Topics)

| Concept | L01 | L02 | L03 | L04 | L05 | L06 |
|---------|-----|-----|-----|-----|-----|-----|
| Loss functions | MSE | Cross-entropy | - | Gini/Entropy | Reconstruction | Reward |
| Optimization | Gradient descent | Gradient descent | - | Greedy | Eigen | Q-learning |
| Overfitting | Regularization | Regularization | K choice | Pruning/OOB | Components | - |
| Evaluation | R2, RMSE | AUC, F1 | Silhouette | OOB, Feature imp | Variance explained | Reward curve |

---

## Quality Assurance System

### Three-Stage Review Process

| Stage | Reviewer | Focus | Checklist |
|-------|----------|-------|-----------|
| **1. Self-Review** | Instructor | Content accuracy, pedagogy | See below |
| **2. Colleague Review** | Faculty peer | Academic rigor, clarity | External checklist |
| **3. Student Pilot** | 2-3 students | Comprehension, pacing | Feedback form |

### Automated Validation Suite

```python
# Run full validation
python course_cli.py validate --all

# Validation checks:
# 1. LaTeX: Zero overflow, zero errors, consistent formatting
# 2. Links: All URLs return 200, all file refs exist
# 3. Notebooks: All cells execute, outputs match expected
# 4. Charts: All chart.py scripts run, PDFs generated
# 5. Quizzes: Valid Moodle XML, answers marked correctly
# 6. Manifest: All assets exist, no orphaned files
```

### Self-Review Checklist (Per Topic)

**Content Quality**
- [ ] Learning objectives clearly stated
- [ ] PMSP structure followed (Problem-Method-Solution-Practice)
- [ ] Finance use case is realistic and engaging
- [ ] Mathematics is correct and well-explained
- [ ] Code examples are tested and work
- [ ] Decision framework complete (when to use, pros/cons, flowchart)

**Pedagogical Quality**
- [ ] Bloom's taxonomy levels appropriate
- [ ] Prerequisites clearly stated
- [ ] Difficulty progression logical
- [ ] Practice exercises match objectives
- [ ] Estimated time is realistic

**Technical Quality**
- [ ] Zero LaTeX overflow warnings
- [ ] All charts render correctly
- [ ] Notebook executes without errors
- [ ] All links accessible
- [ ] Consistent formatting

---

## Easy-to-Grade Rubrics

### Presentation Rubric (15 min, 100 points)

| Criterion | Excellent (25) | Good (20) | Adequate (15) | Needs Work (10) |
|-----------|----------------|-----------|---------------|-----------------|
| **Content Accuracy** | All facts correct, sources cited | Minor errors, mostly cited | Some errors, few citations | Major errors, no citations |
| **Clarity** | Crystal clear, logical flow | Clear, minor jumps | Somewhat clear | Confusing |
| **Visuals** | Professional, aids understanding | Good, mostly helpful | Basic, some help | Poor or distracting |
| **Timing** | 14-16 min, well-paced | 12-18 min, mostly paced | 10-20 min, uneven | <10 or >20 min |

**Quick Grading**: Check boxes, sum points. Takes <5 min per student.

### Capstone Rubric (Report Only, 100 points)

| Criterion | Excellent (20) | Good (15) | Adequate (10) | Needs Work (5) |
|-----------|----------------|-----------|---------------|-----------------|
| **Problem Definition** | Clear, well-motivated business problem | Clear problem | Somewhat clear | Unclear |
| **Method Selection** | Justified choice with alternatives considered | Justified choice | Choice stated | No justification |
| **Implementation** | Correct, efficient, well-documented | Correct, documented | Works, basic docs | Errors or no docs |
| **Results Interpretation** | Business insights, limitations discussed | Good interpretation | Basic interpretation | No interpretation |
| **Report Quality** | Professional, well-structured | Good structure | Adequate | Poor |

**Quick Grading**: Read report, check boxes. Takes <15 min per student.

---

## Capstone Project Specification

### Overview
- **Format**: Open-ended, individual project
- **Deliverable**: Written report (PDF, 10-15 pages)
- **Timeline**: Introduced Session 4, Due 2 weeks after Session 6

### Requirements

1. **Problem Selection** (student chooses)
   - Must be from finance/business domain
   - Must require ML solution
   - Must have available or synthetic data

2. **Method Application**
   - Use at least 2 methods from the course
   - Compare and justify final selection
   - Include decision framework reasoning

3. **Report Structure**
   ```
   1. Executive Summary (1 page)
   2. Problem Definition (2 pages)
   3. Data Description (1 page)
   4. Methodology (3 pages)
   5. Results & Interpretation (3 pages)
   6. Limitations & Future Work (1 page)
   7. References
   8. Appendix: Code snippets
   ```

### Example Capstone Topics (Finance)
- Credit default prediction using logistic regression vs random forest
- Customer churn prediction for a retail bank
- Portfolio risk factor analysis using PCA
- Fraud detection system comparison
- Algorithmic trading signal generation

---

## Content Library Structure (Reusable)

```
content_library/
├── methods/
│   ├── linear_regression/
│   │   ├── theory/
│   │   ├── charts/
│   │   ├── notebooks/
│   │   └── quizzes/
│   ├── logistic_regression/
│   ├── knn/
│   ├── kmeans/
│   ├── random_forests/
│   ├── pca/
│   ├── tsne/
│   ├── embeddings/
│   └── reinforcement_learning/
├── domains/
│   ├── finance/
│   │   ├── credit_risk/
│   │   ├── fraud_detection/
│   │   ├── trading/
│   │   └── customer_analytics/
│   └── general/
├── datasets/
│   ├── synthetic/
│   └── generators/
└── templates/
    ├── beamer/
    ├── notebooks/
    └── rubrics/
```

### Reuse Workflow
```bash
# Import component to new course
python course_cli.py import --source library/methods/pca --target new_course/L05

# Export component to library
python course_cli.py export --topic L01 --to library/methods/linear_regression
```

---

## Versioning System

### Git Tags
```
v1.0.0-2026-spring    # Initial release
v1.0.1-2026-spring    # Minor fixes during semester
v1.1.0-2026-fall      # Updates for next semester
```

### Changelog (CHANGELOG.md)
```markdown
## [1.0.0] - 2026-02-01
### Added
- Initial 6 lectures
- 3 quizzes
- 15 presentation topics
- Capstone specification

### Changed
- N/A (initial release)

### Fixed
- N/A (initial release)
```

### Backward Compatibility
- Old notebook links redirect to new versions
- Deprecated content archived in `archive/` folder
- Breaking changes documented in CHANGELOG

---

## Phase 1: Project Structure Setup

### 1.1 Complete Directory Structure
```
Methods_and_Algorithms/
├── README.md
├── CHANGELOG.md
├── .gitignore
├── manifest.json                   # Content inventory
├── config.yaml                     # Course configuration
│
├── infrastructure/                 # Python course management
│   ├── course_cli.py              # Main CLI entry point
│   ├── validators/
│   │   ├── latex_validator.py
│   │   ├── link_validator.py
│   │   ├── notebook_validator.py
│   │   └── chart_validator.py
│   ├── builders/
│   │   ├── slide_builder.py
│   │   ├── chart_builder.py
│   │   ├── notebook_builder.py
│   │   └── quiz_builder.py
│   ├── reporters/
│   │   ├── build_report.py
│   │   ├── coverage_report.py
│   │   ├── progress_report.py
│   │   └── quality_report.py
│   ├── deployers/
│   │   ├── github_deployer.py
│   │   └── colab_deployer.py
│   └── generators/
│       ├── syllabus_generator.py
│       ├── rubric_generator.py
│       └── guide_generator.py
│
├── docs/                          # GitHub Pages source
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
│
├── slides/
│   ├── L01_Introduction_Linear_Regression/
│   │   ├── L01_overview.tex
│   │   ├── L01_deepdive.tex
│   │   ├── L01_instructor_guide.md
│   │   ├── 01_simple_regression/
│   │   │   ├── chart.py
│   │   │   └── chart.pdf
│   │   ├── 02_gradient_descent/
│   │   ├── ...
│   │   ├── L01_decision_flowchart/
│   │   └── temp/
│   ├── L02_Logistic_Regression/
│   ├── L03_KNN_KMeans/
│   ├── L04_Random_Forests/
│   ├── L05_PCA_tSNE/
│   └── L06_Embeddings_RL/
│
├── quizzes/
│   ├── quiz1_topics_1_2.xml       # Moodle XML
│   ├── quiz2_topics_3_4.xml
│   └── quiz3_topics_5_6.xml
│
├── notebooks/                      # Local copies, deploy to Colab
│   ├── L01_linear_regression.ipynb
│   ├── L02_logistic_regression.ipynb
│   ├── L03_knn_kmeans.ipynb
│   ├── L04_random_forests.ipynb
│   ├── L05_pca_tsne.ipynb
│   └── L06_embeddings_rl.ipynb
│
├── datasets/                       # Synthetic data
│   ├── housing_synthetic.csv
│   ├── credit_synthetic.csv
│   ├── customers_synthetic.csv
│   ├── transactions_synthetic.csv
│   ├── portfolio_synthetic.csv
│   └── text_corpus_synthetic.json
│
├── presentations/
│   └── topics.md                   # 15 student presentation topics
│
├── capstone/
│   ├── specification.md
│   ├── report_template.tex
│   └── examples/
│
├── rubrics/
│   ├── presentation_rubric.md
│   └── capstone_rubric.md
│
├── syllabus/
│   ├── syllabus.md                # Source
│   ├── syllabus.pdf               # Generated
│   └── syllabus.html              # Generated
│
└── templates/
    ├── beamer_template.tex
    ├── chart_template.py
    ├── notebook_template.ipynb
    ├── quiz_template.xml
    └── instructor_guide_template.md
```

### 1.2 Git Setup
- Initialize repo
- Create .gitignore (exclude temp/, __pycache__, .aux, .log, etc.)
- Push to GitHub Digital-AI-Finance (private)

---

## Phase 2: Templates & Branding

### 2.1 Beamer Template
- Madrid theme, 8pt font
- Course header: "Methods and Algorithms - MSc Data Science"
- Footer with slide numbers
- Custom colors (ML purple/blue palette)

### 2.2 Chart Template
- figsize=(10, 6)
- Font scaling for Beamer (14pt base)
- Full GitHub URL in bottom-right corner of each chart
- Consistent color palette across all charts

### 2.3 Notebook Template
- Google Colab header with badges
- Synthetic data generation section
- Theory + Code + Visualization structure

---

## Phase 3: Slides Development (Per Topic)

### Slide Structure (40 slides per topic)
**Overview (10 slides)**:
1. Title slide
2. Learning objectives
3. Motivation/real-world applications
4. Key concepts (3-4 slides)
5. Algorithm overview
6. Intuition visualization
7. Key takeaways
8. Preview of deep dive

**Deep Dive (30 slides)**:
1. Mathematical foundations (5-7 slides)
2. Algorithm step-by-step (5-7 slides)
3. Implementation details (3-4 slides)
4. Visualizations & examples (8-10 slides)
5. Hyperparameters & tuning (3-4 slides)
6. Practical considerations (2-3 slides)
7. Summary & references (2 slides)

### Topic-Specific Content

#### L01: Introduction & Linear Regression
**Charts**:
- Simple linear regression fit
- Multiple regression 3D surface
- Residual plots
- Gradient descent visualization
- Learning curves
- Regularization comparison (Ridge/Lasso)
- Bias-variance tradeoff

**Key Concepts**: OLS, gradient descent, MSE, R-squared, regularization

#### L02: Logistic Regression
**Charts**:
- Sigmoid function
- Decision boundary (2D)
- Log-loss visualization
- ROC curve
- Precision-recall curve
- Confusion matrix heatmap
- Multiclass extension (softmax)

**Key Concepts**: Maximum likelihood, cross-entropy, classification metrics

#### L03: K-Nearest Neighbours & K-Means
**Charts**:
- KNN decision boundaries (varying K)
- Distance metrics comparison
- K-Means iteration animation
- Elbow method
- Silhouette analysis
- Voronoi diagrams
- Curse of dimensionality

**Key Concepts**: Distance metrics, choosing K, convergence

#### L04: Random Forests
**Charts**:
- Decision tree structure
- Feature importance
- Bootstrap sampling
- Out-of-bag error
- Ensemble voting
- Bias-variance decomposition
- Hyperparameter effects

**Key Concepts**: Bagging, feature randomization, OOB, interpretability

#### L05: PCA & t-SNE
**Charts**:
- Variance explained (scree plot)
- Principal components visualization
- Reconstruction error
- t-SNE perplexity comparison
- High-dim to 2D projection
- Cluster preservation
- PCA vs t-SNE comparison

**Key Concepts**: Eigendecomposition, variance, perplexity, non-linear embedding

#### L06: Embeddings & Reinforcement Learning
**Charts**:
- Word embedding space (Word2Vec)
- Embedding similarity heatmap
- RL agent-environment loop
- Q-learning grid world
- Reward curves
- Policy visualization
- Exploration vs exploitation

**Key Concepts**: Word2Vec, similarity, MDP, Q-learning, policy

---

## Phase 4: Quizzes (Moodle XML Format)

### Quiz Structure
Each quiz: 10-15 MC questions covering 2 topics

**Quiz 1** (Topics 1-2): Linear & Logistic Regression
- 5-7 questions on linear regression
- 5-7 questions on logistic regression
- Mix of conceptual and calculation-based

**Quiz 2** (Topics 3-4): KNN/K-Means & Random Forests
- 5-7 questions on KNN/K-Means
- 5-7 questions on Random Forests

**Quiz 3** (Topics 5-6): PCA/t-SNE & Embeddings/RL
- 5-7 questions on dimensionality reduction
- 5-7 questions on embeddings/RL

### Question Types
- Conceptual understanding
- Formula application
- Algorithm behavior prediction
- Hyperparameter effects
- Output interpretation

---

## Phase 5: Presentation Topics (15 Total)

Students present ONCE during the course. Topics distributed across all 6 sessions.

### Proposed Topics

**Session 1-2 (Regression)**:
1. Ridge vs Lasso: When to use which?
2. Logistic Regression in Healthcare: Disease Prediction
3. Feature Engineering for Linear Models

**Session 3 (KNN/K-Means)**:
4. Distance Metrics Beyond Euclidean
5. K-Means++ and Initialization Strategies
6. DBSCAN vs K-Means: Density-Based Clustering

**Session 4 (Random Forests)**:
7. XGBoost vs Random Forest: A Comparison
8. SHAP Values for Model Interpretability
9. Imbalanced Classification with Tree Ensembles

**Session 5 (PCA/t-SNE)**:
10. UMAP: The Modern Alternative to t-SNE
11. PCA in Finance: Portfolio Optimization
12. Autoencoders vs PCA for Dimensionality Reduction

**Session 6 (Embeddings/RL)**:
13. BERT and Transformer Embeddings
14. Deep Q-Networks: From Atari to Real World
15. Multi-Armed Bandits in A/B Testing

---

## Phase 6: Google Colab Notebooks

### Notebook Structure (Each ~45-60 min hands-on)
1. **Introduction** (5 min): Learning objectives, prerequisites
2. **Theory Recap** (10 min): Key formulas, intuition
3. **Data Generation** (5 min): Synthetic dataset creation
4. **Implementation from Scratch** (15 min): NumPy implementation
5. **Scikit-learn Implementation** (10 min): Using libraries
6. **Visualization** (10 min): Results interpretation
7. **Exercises** (5 min): Practice problems

### Synthetic Datasets
- **L01**: Housing prices (continuous target)
- **L02**: Binary classification (spam/not spam)
- **L03**: Clustering dataset (blobs/moons)
- **L04**: Multi-class with feature importance
- **L05**: High-dimensional for reduction
- **L06**: Text corpus + grid world

---

## Phase 7: GitHub Pages Site

### Site Structure
```
index.html
├── Hero: Course title, description
├── Schedule: 6 sessions (no dates, just topics)
├── Materials:
│   ├── Slides (PDF download links)
│   ├── Notebooks (Colab links)
│   └── Datasets (download links)
├── Presentations:
│   └── 15 topics with descriptions
├── Quizzes:
│   └── Links to Moodle quizzes
└── Resources:
    └── Textbooks, papers, tutorials (20 verified links)
```
**Note**: No instructor section per user preference.

### Features
- Responsive design (mobile-friendly)
- Dark/light mode toggle
- Collapsible sections per session
- Direct Colab "Open in Colab" badges
- Progress tracking (session completed indicators)

---

## Phase 8: Execution Order

### Step 1: Infrastructure (Day 1)
- [ ] Create directory structure
- [ ] Initialize Git repo
- [ ] Create Beamer template
- [ ] Create chart template
- [ ] Create notebook template

### Step 2: Content Development (Per Topic)
For each of 6 topics:
- [ ] Write 10 overview slides
- [ ] Write 30 deep dive slides
- [ ] Create all charts (8-12 per topic)
- [ ] Compile and verify zero overflow
- [ ] Create Colab notebook
- [ ] Generate synthetic dataset

### Step 3: Quizzes
- [ ] Write Quiz 1 (Topics 1-2)
- [ ] Write Quiz 2 (Topics 3-4)
- [ ] Write Quiz 3 (Topics 5-6)
- [ ] Export to Moodle XML

### Step 4: Presentation Topics
- [ ] Finalize 15 topics with descriptions
- [ ] Create topic selection document

### Step 5: GitHub Pages
- [ ] Build site HTML/CSS/JS
- [ ] Add all download links
- [ ] Test Colab integration
- [ ] Deploy via GitHub Pages

### Step 6: Final Integration
- [ ] Push all to GitHub
- [ ] Verify all links work
- [ ] Create course announcement

---

## Quality Checklist

### Slides
- [ ] Zero LaTeX overflow warnings
- [ ] Consistent formatting across all topics
- [ ] Charts readable at 0.55-0.65 textwidth
- [ ] GitHub URL on every chart
- [ ] All citations verified

### Notebooks
- [ ] All cells execute without error
- [ ] Synthetic data reproducible (seed=42)
- [ ] Clear explanations
- [ ] Exercises included

### Quizzes
- [ ] Valid Moodle XML format
- [ ] Balanced difficulty
- [ ] Clear, unambiguous questions
- [ ] Correct answers verified

### Website
- [ ] All links functional
- [ ] Mobile responsive
- [ ] Fast loading
- [ ] Accessible

---

## Estimated Outputs

| Component | Count |
|-----------|-------|
| LaTeX files | 12 (2 per topic: overview + deep dive) |
| Chart folders | ~60 |
| Chart PDFs | ~60 |
| Notebook files | 6 |
| Quiz XML files | 3 |
| Synthetic datasets | 6+ |
| HTML pages | 1 (single-page app) |
| Total slides | ~240 |

---

## Clarified Requirements

- **Slides**: Separate PDFs (L01_overview.pdf + L01_deepdive.pdf)
- **Quizzes**: 30 min timed, 1 attempt
- **Topic Selection**: Before Session 1 (first-come-first-served online)

---

## Phase 9: Verified References (20 Resources)

### Textbooks (Free PDFs - Links Verified)

| # | Title | Authors | URL |
|---|-------|---------|-----|
| 1 | Introduction to Statistical Learning (R), 2nd Ed | James, Witten, Hastie, Tibshirani | https://www.statlearning.com/ |
| 2 | Introduction to Statistical Learning (Python) | James, Witten, Hastie, Tibshirani | https://www.statlearning.com/ |
| 3 | Elements of Statistical Learning, 2nd Ed | Hastie, Tibshirani, Friedman | https://hastie.su.domains/ElemStatLearn/ |
| 4 | Deep Learning | Goodfellow, Bengio, Courville | https://www.deeplearningbook.org/ |
| 5 | Reinforcement Learning: An Introduction, 2nd Ed | Sutton, Barto | http://incompleteideas.net/book/the-book-2nd.html |
| 6 | Pattern Recognition and Machine Learning | Bishop | https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/ |
| 7 | Mathematics for Machine Learning | Deisenroth, Faisal, Ong | https://mml-book.github.io/ |
| 8 | Dive into Deep Learning | Zhang, Lipton, Li, Smola | https://d2l.ai/ |
| 9 | Patterns, Predictions, and Actions | Hardt, Recht | https://mlstory.org/ |
| 10 | Information Retrieval | Manning, Raghavan, Schutze | https://nlp.stanford.edu/IR-book/ |

### Online Courses & Tutorials

| # | Title | Platform | URL |
|---|-------|----------|-----|
| 11 | CS229: Machine Learning | Stanford | https://cs229.stanford.edu/ |
| 12 | Scikit-learn User Guide | scikit-learn | https://scikit-learn.org/stable/user_guide.html |
| 13 | Kaggle Learn (ML courses) | Kaggle | https://www.kaggle.com/learn |
| 14 | Fast.ai Practical Deep Learning | fast.ai | https://course.fast.ai/ |
| 15 | 3Blue1Brown Neural Networks | YouTube | https://www.3blue1brown.com/topics/neural-networks |

### Documentation & References

| # | Title | Type | URL |
|---|-------|------|-----|
| 16 | NumPy Documentation | Docs | https://numpy.org/doc/stable/ |
| 17 | Pandas Documentation | Docs | https://pandas.pydata.org/docs/ |
| 18 | Matplotlib Tutorials | Docs | https://matplotlib.org/stable/tutorials/ |
| 19 | PyTorch Tutorials | Docs | https://pytorch.org/tutorials/ |
| 20 | TensorFlow Tutorials | Docs | https://www.tensorflow.org/tutorials |

**Note**: All links will be verified via Python script during implementation to ensure accessibility.

---

## Execution Summary

### Total Deliverables
| Category | Item | Count |
|----------|------|-------|
| **Slides** | LaTeX files (overview + deep dive) | 12 |
| | Slide PDFs | 12 |
| | Instructor guides | 6 |
| **Charts** | Chart folders | ~60 |
| | Decision flowcharts | 6 |
| **Assessment** | Moodle quiz XMLs | 3 |
| | Rubrics | 2 |
| **Notebooks** | Colab notebooks | 6 |
| **Data** | Synthetic datasets | 6 |
| **Infrastructure** | Python CLI modules | ~20 |
| | Templates | 5 |
| **Documentation** | GitHub Pages site | 1 |
| | Syllabus (3 formats) | 3 |
| | Presentation topics | 15 |
| | Capstone specification | 1 |
| | Reference links | 20 |

### Execution Order (13 Phases)

**Phase A: Infrastructure Setup**
1. Create directory structure
2. Initialize Git repo, push to GitHub (private)
3. Build Python CLI framework (`course_cli.py`)
4. Create all templates (Beamer, chart, notebook, quiz)
5. Initialize `manifest.json` with empty structure

**Phase B: Content Development (Per Topic)**
6. **L01**: Overview + Deep dive + 8 charts + notebook + dataset + guide + flowchart
7. **L02**: Overview + Deep dive + 7 charts + notebook + dataset + guide + flowchart
8. **Quiz 1**: 10-15 MC questions on Topics 1-2
9. **L03**: Overview + Deep dive + 7 charts + notebook + dataset + guide + flowchart
10. **L04**: Overview + Deep dive + 7 charts + notebook + dataset + guide + flowchart
11. **Quiz 2**: 10-15 MC questions on Topics 3-4
12. **L05**: Overview + Deep dive + 7 charts + notebook + dataset + guide + flowchart
13. **L06**: Overview + Deep dive + 7 charts + notebook + dataset + guide + flowchart
14. **Quiz 3**: 10-15 MC questions on Topics 5-6

**Phase C: Supporting Materials**
15. Create 15 presentation topics with descriptions
16. Write capstone specification + report template
17. Generate rubrics (presentation + capstone)
18. Generate syllabus (MD -> PDF + HTML + Moodle)

**Phase D: Deployment & QA**
19. Build GitHub Pages site
20. Deploy notebooks to Google Colab
21. Run full validation suite (`course_cli.py validate --all`)
22. Three-stage review (self -> colleague -> student pilot)
23. Tag release `v1.0.0-2026-spring`

### Python Files to Create

```
infrastructure/
├── course_cli.py                  # ~200 lines
├── validators/
│   ├── __init__.py
│   ├── latex_validator.py         # ~100 lines
│   ├── link_validator.py          # ~80 lines
│   ├── notebook_validator.py      # ~120 lines
│   └── chart_validator.py         # ~60 lines
├── builders/
│   ├── __init__.py
│   ├── slide_builder.py           # ~80 lines
│   ├── chart_builder.py           # ~100 lines
│   ├── notebook_builder.py        # ~80 lines
│   └── quiz_builder.py            # ~150 lines
├── reporters/
│   ├── __init__.py
│   ├── build_report.py            # ~60 lines
│   ├── coverage_report.py         # ~80 lines
│   ├── progress_report.py         # ~100 lines
│   └── quality_report.py          # ~80 lines
├── deployers/
│   ├── __init__.py
│   ├── github_deployer.py         # ~100 lines
│   └── colab_deployer.py          # ~80 lines
└── generators/
    ├── __init__.py
    ├── syllabus_generator.py      # ~150 lines
    ├── rubric_generator.py        # ~80 lines
    └── guide_generator.py         # ~100 lines

Total: ~1800 lines of Python infrastructure
```

### Key Content Files

```
D:\Joerg\Research\slides\Methods_and_Algorithms\
│
├── manifest.json                              # Master inventory
├── config.yaml                                # Course config
│
├── slides\L01_Introduction_Linear_Regression\
│   ├── L01_overview.tex                       # 10 slides
│   ├── L01_deepdive.tex                       # 30 slides
│   ├── L01_instructor_guide.md                # Teaching notes
│   ├── 01_simple_regression\chart.py          # Chart 1
│   ├── 02_multiple_regression\chart.py        # Chart 2
│   ├── 03_residual_plots\chart.py             # Chart 3
│   ├── 04_gradient_descent\chart.py           # Chart 4
│   ├── 05_learning_curves\chart.py            # Chart 5
│   ├── 06_regularization\chart.py             # Chart 6
│   ├── 07_bias_variance\chart.py              # Chart 7
│   ├── 08_decision_flowchart\chart.py         # Decision guide
│   └── temp\                                  # LaTeX aux files
│
├── [Similar structure for L02-L06]
│
├── quizzes\
│   ├── quiz1_topics_1_2.xml                   # ~15 questions
│   ├── quiz2_topics_3_4.xml                   # ~15 questions
│   └── quiz3_topics_5_6.xml                   # ~15 questions
│
├── notebooks\
│   ├── L01_linear_regression.ipynb            # ~45 min hands-on
│   └── [L02-L06 notebooks]
│
├── datasets\
│   ├── housing_synthetic.csv                  # L01
│   ├── credit_synthetic.csv                   # L02
│   ├── customers_synthetic.csv                # L03
│   ├── transactions_synthetic.csv             # L04
│   ├── portfolio_synthetic.csv                # L05
│   └── text_corpus_synthetic.json             # L06
│
├── presentations\topics.md                    # 15 topics
├── capstone\specification.md                  # Project spec
├── rubrics\presentation_rubric.md             # Easy grading
├── rubrics\capstone_rubric.md                 # Easy grading
├── syllabus\syllabus.md                       # Source
└── docs\index.html                            # GitHub Pages
```

---

## Enhanced Infrastructure (New Modules)

### PDF Downloader System

Downloads and manages course reference materials (textbooks, papers, slides).

```
infrastructure/downloaders/
├── __init__.py
├── pdf_downloader.py          # ~200 lines
├── resource_registry.json     # Track all downloadable resources
└── download_cache/            # Local cache directory
```

**Features:**
- Download from multiple sources (direct URLs, arXiv, SSRN, etc.)
- Retry logic (3 attempts with exponential backoff)
- Skip with manual fallback list when all retries fail
- Progress tracking and resume support
- SHA256 verification for integrity
- Automatic filename sanitization

**CLI Commands:**
```bash
python course_cli.py download --all              # Download all resources
python course_cli.py download --topic L01        # Download for specific topic
python course_cli.py download --check            # Verify existing downloads
python course_cli.py download --status           # Show download status
python course_cli.py download --retry-failed     # Retry failed downloads
```

**Resource Registry Schema (resource_registry.json):**
```json
{
  "resources": [
    {
      "id": "islr-book",
      "title": "Introduction to Statistical Learning",
      "type": "textbook",
      "url": "https://www.statlearning.com/s/ISLRv2.pdf",
      "topics": ["L01", "L02", "L03", "L04"],
      "sha256": "abc123...",
      "status": "downloaded|pending|failed|manual",
      "local_path": "resources/textbooks/ISLRv2.pdf",
      "last_attempt": "2026-01-07T10:30:00Z",
      "attempts": 0,
      "error_message": null
    }
  ]
}
```

---

### Activity Logger (Full Audit Trail)

Tracks every action taken during course development.

```
infrastructure/trackers/
├── __init__.py
├── activity_log.py            # ~150 lines
├── activity_log.json          # JSON log file
└── activity_log.db            # SQLite for queries (optional)
```

**Tracked Events:**
| Event Type | Data Captured |
|------------|---------------|
| file_created | path, timestamp, size, content_hash |
| file_modified | path, timestamp, old_hash, new_hash, diff_summary |
| file_deleted | path, timestamp, last_hash |
| cli_command | command, args, exit_code, duration, output_summary |
| validation_run | validator, target, result, warnings, errors |
| build_run | builder, target, success, output_path |
| download_attempt | resource_id, url, success, error |
| git_operation | operation, branch, commit_hash, files_changed |

**Log Entry Schema:**
```json
{
  "id": "uuid",
  "timestamp": "2026-01-07T10:30:00Z",
  "event_type": "file_modified",
  "actor": "claude-code|user|system",
  "target": "slides/L01_overview.tex",
  "details": {
    "old_hash": "abc123",
    "new_hash": "def456",
    "lines_added": 15,
    "lines_removed": 3
  },
  "session_id": "session-uuid"
}
```

**CLI Commands:**
```bash
python course_cli.py log --show                  # Show recent activity
python course_cli.py log --show --topic L01      # Filter by topic
python course_cli.py log --show --type build     # Filter by event type
python course_cli.py log --export markdown       # Export to markdown
python course_cli.py log --export html           # Export to HTML
python course_cli.py log --stats                 # Show activity statistics
```

---

### HTML Dashboard Reporter

Generates interactive HTML dashboards for progress visualization.

```
infrastructure/reporters/
├── html_dashboard.py          # ~250 lines
├── dashboard_template.html    # Jinja2 template
└── dashboard_assets/
    ├── style.css
    └── chart.js               # Progress charts
```

**Dashboard Sections:**
1. **Overview Cards**: Total progress, items complete, items pending
2. **Topic Progress**: Bar chart per topic (slides, charts, notebooks)
3. **Timeline**: Activity log visualization
4. **Asset Status Table**: Sortable table of all assets
5. **Validation Results**: Latest validation run summary
6. **Build History**: Recent builds with success/failure

**Report Formats:**
| Format | Use Case | Output |
|--------|----------|--------|
| Console | Quick status check | Terminal output |
| Markdown | Git-friendly reports | progress_report.md |
| HTML | Visual dashboard | dashboard.html |

**CLI Commands:**
```bash
python course_cli.py report progress --format console
python course_cli.py report progress --format markdown --output status.md
python course_cli.py report progress --format html --output dashboard.html
python course_cli.py report progress --all-formats  # Generate all three
```

---

### Error Handling Strategy

All infrastructure modules implement consistent error handling:

```python
class RetryStrategy:
    """Retry failed operations with exponential backoff."""

    def __init__(self, max_retries=3, base_delay=1.0):
        self.max_retries = max_retries
        self.base_delay = base_delay

    def execute(self, operation, *args, **kwargs):
        for attempt in range(self.max_retries):
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    self.log_failure(operation, e)
                    return self.manual_fallback(operation, e)
                delay = self.base_delay * (2 ** attempt)
                time.sleep(delay)

    def manual_fallback(self, operation, error):
        """Add to manual review list when all retries fail."""
        # Log to manual_review.json for human intervention
        pass
```

**Error Recovery Workflow:**
1. Attempt operation
2. On failure: retry up to 3 times with exponential backoff (1s, 2s, 4s)
3. If all retries fail: add to `manual_review.json`
4. Continue with next item (don't block entire process)
5. Generate manual review report at end

**Manual Review File (manual_review.json):**
```json
{
  "items": [
    {
      "type": "download_failed",
      "resource_id": "esl-book",
      "url": "https://...",
      "error": "Connection timeout",
      "attempts": 3,
      "last_attempt": "2026-01-07T10:30:00Z",
      "suggested_action": "Verify URL or download manually"
    }
  ]
}
```

---

### Updated Infrastructure File Tree

```
infrastructure/
├── course_cli.py                  # Main CLI (~250 lines, updated)
├── config.yaml                    # Course configuration
├── manifest.json                  # Content inventory
│
├── validators/
│   ├── __init__.py
│   ├── latex_validator.py         # ~100 lines
│   ├── link_validator.py          # ~80 lines
│   ├── notebook_validator.py      # ~120 lines
│   └── chart_validator.py         # ~60 lines
│
├── builders/
│   ├── __init__.py
│   ├── slide_builder.py           # ~80 lines
│   ├── chart_builder.py           # ~100 lines
│   ├── notebook_builder.py        # ~80 lines
│   └── quiz_builder.py            # ~150 lines
│
├── reporters/
│   ├── __init__.py
│   ├── build_report.py            # ~60 lines
│   ├── coverage_report.py         # ~80 lines
│   ├── progress_report.py         # ~100 lines
│   ├── quality_report.py          # ~80 lines
│   ├── html_dashboard.py          # ~250 lines (NEW)
│   ├── dashboard_template.html    # (NEW)
│   └── dashboard_assets/          # (NEW)
│
├── deployers/
│   ├── __init__.py
│   ├── github_deployer.py         # ~100 lines
│   └── colab_deployer.py          # ~80 lines
│
├── generators/
│   ├── __init__.py
│   ├── syllabus_generator.py      # ~150 lines
│   ├── rubric_generator.py        # ~80 lines
│   └── guide_generator.py         # ~100 lines
│
├── downloaders/                   # (NEW)
│   ├── __init__.py
│   ├── pdf_downloader.py          # ~200 lines
│   ├── resource_registry.json
│   └── download_cache/
│
├── trackers/                      # (NEW)
│   ├── __init__.py
│   ├── activity_log.py            # ~150 lines
│   ├── activity_log.json
│   └── manual_review.json
│
└── utils/                         # (NEW)
    ├── __init__.py
    ├── retry_strategy.py          # ~50 lines
    └── hash_utils.py              # ~30 lines

Total: ~2400 lines of Python infrastructure (+600 new)
```

---

## Implementation Priority (Next Steps)

1. **Create audit system** - FIRST PRIORITY (see below)
2. **Create downloaders module** - pdf_downloader.py with retry logic
3. **Create trackers module** - activity_log.py for audit trail
4. **Create HTML dashboard** - html_dashboard.py with template
5. **Update course_cli.py** - Add download, log, and report --format commands
6. **Create utility modules** - retry_strategy.py, hash_utils.py
7. **Test full workflow** - End-to-end validation of new infrastructure

---

## Audit System (FIRST PRIORITY)

### Purpose
Verify what has been completed in the course development project by comparing:
- Actual files on disk
- Plan file specifications
- manifest.json inventory

### Directory Structure
```
infrastructure/auditors/
├── __init__.py
├── audit_system.py           # Main audit orchestration (~300 lines)
├── plan_parser.py            # Parse plan.md for expected items (~100 lines)
├── manifest_auditor.py       # Verify manifest.json entries (~80 lines)
├── file_auditor.py           # Check actual files on disk (~100 lines)
├── functional_auditor.py     # Test that modules work (~150 lines)
└── report_generator.py       # Multi-format output (~200 lines)
```

### Audit Scope (User Selected: Full + Functional)

**Infrastructure Audit:**
| Category | What to Check |
|----------|---------------|
| Directories | All 74 planned directories exist |
| Python modules | All infrastructure/*.py files exist and are importable |
| Templates | All templates/ files exist with correct structure |
| Config files | manifest.json, config.yaml valid and complete |
| Slide folders | L01-L06 folder structure exists |

**Functional Audit:**
| Test | Method |
|------|--------|
| CLI works | `python course_cli.py --help` returns 0 |
| Validators importable | `from validators import *` succeeds |
| Builders importable | `from builders import *` succeeds |
| Progress report runs | `generate_progress_report()` executes |
| Manifest valid JSON | `json.load(manifest.json)` succeeds |
| Config valid YAML | `yaml.safe_load(config.yaml)` succeeds |

### Output Formats (User Selected: All Three)

**1. Console Output:**
```
============================================================
  COURSE AUDIT REPORT - Methods and Algorithms
  Generated: 2026-01-07 10:30:00
============================================================

SUMMARY
-------
Infrastructure:  45/74 directories (61%)
Python Modules:  18/25 files (72%)
Templates:       5/5 complete (100%)
Content:         0/6 topics started (0%)

FUNCTIONAL TESTS
----------------
[PASS] CLI --help
[PASS] Manifest valid JSON
[PASS] Config valid YAML
[FAIL] latex_validator importable - ModuleNotFoundError

GAP ANALYSIS
------------
Priority 1 (Critical):
  - infrastructure/auditors/ (this audit system!)
  - infrastructure/utils/ (dependencies)

Priority 2 (High):
  - infrastructure/downloaders/
  - infrastructure/trackers/

Priority 3 (Medium):
  - slides/L01_*/charts (no charts created yet)
  - notebooks/ (no notebooks created yet)
```

**2. JSON Output (audit_report.json):**
```json
{
  "metadata": {
    "generated": "2026-01-07T10:30:00Z",
    "project": "Methods and Algorithms",
    "version": "1.0.0"
  },
  "summary": {
    "directories": {"found": 45, "expected": 74, "percent": 61},
    "python_modules": {"found": 18, "expected": 25, "percent": 72},
    "templates": {"found": 5, "expected": 5, "percent": 100},
    "content": {"found": 0, "expected": 6, "percent": 0}
  },
  "functional_tests": [
    {"name": "cli_help", "status": "pass", "duration_ms": 120},
    {"name": "manifest_valid", "status": "pass", "duration_ms": 5},
    {"name": "latex_validator_import", "status": "fail", "error": "ModuleNotFoundError"}
  ],
  "missing_items": [
    {"path": "infrastructure/auditors/", "priority": 1, "category": "infrastructure"},
    {"path": "infrastructure/utils/", "priority": 1, "category": "infrastructure"}
  ],
  "recommendations": [
    {"priority": 1, "action": "Create audit system", "reason": "Required for tracking progress"},
    {"priority": 2, "action": "Create utils module", "reason": "Dependency for other modules"}
  ]
}
```

**3. HTML Dashboard (audit_dashboard.html):**
- Progress bars for each category
- Traffic light indicators (green/yellow/red)
- Expandable sections for details
- Sortable table of all items
- Charts showing completion over time (if historical data available)

### CLI Integration
```bash
python course_cli.py audit                    # Full audit, console output
python course_cli.py audit --format json      # JSON output
python course_cli.py audit --format html      # HTML dashboard
python course_cli.py audit --format all       # All formats
python course_cli.py audit --functional       # Include functional tests
python course_cli.py audit --quick            # Skip functional tests
```

### Gap Analysis Algorithm
```python
def calculate_priority(item):
    """
    Priority 1 (Critical): Required for other items to work
    Priority 2 (High): Core functionality
    Priority 3 (Medium): Content items
    Priority 4 (Low): Nice-to-have
    """
    if is_dependency_for_others(item):
        return 1
    if is_infrastructure(item):
        return 2
    if is_content(item):
        return 3
    return 4

def generate_recommendations(missing_items):
    """Generate actionable recommendations with reasoning."""
    sorted_items = sorted(missing_items, key=calculate_priority)
    return [
        {
            "priority": item.priority,
            "action": f"Create {item.path}",
            "reason": get_reason(item),
            "estimated_effort": estimate_effort(item)
        }
        for item in sorted_items
    ]
```

### Files to Create
1. `infrastructure/auditors/__init__.py`
2. `infrastructure/auditors/audit_system.py` - Main orchestration
3. `infrastructure/auditors/plan_parser.py` - Parse plan.md
4. `infrastructure/auditors/manifest_auditor.py` - Check manifest
5. `infrastructure/auditors/file_auditor.py` - Check files
6. `infrastructure/auditors/functional_auditor.py` - Run tests
7. `infrastructure/auditors/report_generator.py` - Generate outputs
