# capstone/

<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-02-07 -->

**Generated**: 2026-01-25 | **Updated**: 2026-02-07
**Purpose**: Capstone project materials - specification, templates, and guidelines for final course project

---

## Overview

This directory contains materials for the **capstone project**, the culminating assessment for the Methods and Algorithms course. The capstone is an **individual, open-ended project** where students apply ML methods to solve a real-world finance or business problem.

**Weight**: 40% of final grade
**Deliverable**: Written report (PDF, 10-15 pages)
**Timeline**: Introduced in Session 4, due 2 weeks after Session 6

---

## Key Files

| File | Purpose | Format |
|------|---------|--------|
| `specification.md` | Project requirements, timeline, evaluation criteria | Markdown |
| `report_template.tex` | LaTeX template for final report | LaTeX |

**Related files**:
- Grading rubric: `../rubrics/capstone_rubric.md`
- Example datasets: `../datasets/*.csv`
- Reference notebooks: `../notebooks/L0X_*.ipynb`

---

## For AI Agents

### specification.md

**Purpose**: Defines capstone project requirements and expectations for students.

**Structure**:
1. **Overview**: Project goals and learning objectives
2. **Timeline**: Key milestones and deadlines
3. **Requirements**: What must be included (problem selection, methods, implementation, report)
4. **Report Structure**: Required sections (Executive Summary, Problem Definition, Data, Methodology, Results, Limitations, References, Appendix)
5. **Evaluation Criteria**: How project is graded (links to rubric)
6. **Example Topics**: Inspiration for project ideas
7. **Submission Guidelines**: Format, naming, submission process
8. **Academic Integrity**: Plagiarism policy, AI tool usage

**Key requirements from specification**:

| Requirement | Details |
|-------------|---------|
| **Methods** | Must apply **at least 2 methods** from course (L01-L06) |
| **Comparison** | Compare methods and justify final selection using decision framework |
| **Data** | Use public dataset or synthetic data (no real PII) |
| **Code** | Functional, documented, reproducible (random seeds set) |
| **Report** | 10-15 pages (excluding appendix), professional academic writing |
| **Sections** | Executive Summary, Problem Definition, Data Description, Methodology, Results, Limitations, References, Appendix |

**Example project topics** (from specification):
- Credit default prediction (Logistic Regression vs Random Forest)
- Customer churn analysis (K-Means segmentation + classification)
- Portfolio risk decomposition (PCA for factor analysis)
- Fraud detection (handling extreme class imbalance)
- Financial sentiment analysis (word embeddings + classification)
- Trading signal generation (Q-learning for simple trading policy)

---

### report_template.tex

**Purpose**: LaTeX template for structuring the final capstone report.

**Expected structure** (10-15 pages):

```latex
\documentclass[12pt,a4paper]{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{hyperref}

\title{Project Title: Problem Statement}
\author{Student Name \\ Student ID}
\date{Due Date}

\begin{document}

\maketitle

% 1. Executive Summary (1 page)
\section*{Executive Summary}
% Problem statement, methods used, key findings, business implications, main recommendation

% 2. Problem Definition (2 pages)
\section{Problem Definition}
% Business context, motivation, research question, success criteria

% 3. Data Description (1 page)
\section{Data Description}
% Data source, observations/features, target variable, quality issues, train/test split

% 4. Methodology (3 pages)
\section{Methodology}
% Why methods chosen, decision framework reasoning, feature engineering,
% hyperparameter tuning, evaluation metrics

% 5. Results and Interpretation (3 pages)
\section{Results and Interpretation}
% Model comparison, feature importance, visualizations, business interpretation, insights

% 6. Limitations and Future Work (1 page)
\section{Limitations and Future Work}
% Assumptions, potential violations, improvements, next steps, generalization

% 7. References
\bibliographystyle{plain}
\bibliography{references}

% 8. Appendix
\appendix
\section{Code Snippets}
% Key code (not full notebooks)

\end{document}
```

**Formatting requirements**:
- Font: 12pt, Times New Roman or similar
- Margins: 1 inch all sides
- Line spacing: 1.5 lines
- Figures/tables: Numbered, captioned, referenced in text
- Citations: IEEE or APA format (consistent)

---

### How to Use Capstone Materials

#### For Instructors

**Session 4 (Introduction)**:
```
1. Distribute specification.md (post to Moodle)
2. Walk through requirements and timeline
3. Show example projects from previous cohorts
4. Discuss topic selection strategies
5. Open Q&A
```

**Session 5 (Topic Proposals)**:
```
1. Students submit 1-page topic proposal
   - Problem statement
   - Proposed methods (at least 2)
   - Data source
   - Expected challenges

2. Instructor reviews proposals (15 min per student)
   - Feasibility check
   - Scope check (not too broad/narrow)
   - Data availability check
   - Provide feedback and approve/request revision
```

**Session 6 - End of Course**:
```
1. Students work on projects (2 weeks)
2. Office hours available for questions
3. Final report due 2 weeks after Session 6
```

**Grading**:
```
1. Use capstone_rubric.md for grading
2. Grade each of 5 criteria (20 points each)
3. Apply bonus/deductions if applicable
4. Write feedback summary
5. Return graded rubric + comments to student
```

**Typical grading time**: 15 minutes per report with rubric

---

#### For Students

**Getting started**:
```
1. Read specification.md thoroughly
2. Review example topics for inspiration
3. Browse public datasets:
   - Kaggle (https://www.kaggle.com/datasets)
   - UCI ML Repository (https://archive.ics.uci.edu/ml/index.php)
   - Data.gov (https://data.gov)
   - Financial data APIs (Yahoo Finance, Alpha Vantage)
4. Brainstorm problem ideas (3-5 options)
5. Check data availability for each
6. Select most feasible + interesting topic
```

**Topic proposal** (1 page, due Session 5):
```markdown
# Capstone Topic Proposal

**Student Name**: [Your Name]
**Student ID**: [Your ID]

## Problem Statement
[2-3 sentences describing the business problem you'll solve]

## Proposed Methods
1. Method 1 (e.g., Logistic Regression) - why suitable for this problem
2. Method 2 (e.g., Random Forest) - comparison point

## Data Source
- Dataset: [Name and URL]
- Observations: [Number of rows]
- Features: [Number of columns, key features]
- Target variable: [What you're predicting]

## Expected Challenges
- Challenge 1 (e.g., class imbalance) - how you'll address
- Challenge 2 (e.g., missing data) - planned approach
```

**Writing the report**:
```
1. Download report_template.tex (or use Word/Markdown alternative)
2. Fill in sections incrementally:
   - Start with Data Description (based on EDA)
   - Write Methodology (as you implement)
   - Write Results (after running experiments)
   - Write Problem Definition and Executive Summary last
3. Run code experiments in Jupyter notebook
4. Export key visualizations as PDF/PNG for report
5. Include code snippets in Appendix (not full notebooks)
6. Proofread and check against rubric before submission
```

**Self-assessment** (before submission):
```
Use capstone_rubric.md to self-assess:

Problem Definition (20 points):
☐ Business context explained clearly
☐ Problem statement is specific
☐ Success criteria defined
☐ Relevance to course topics evident

Method Selection (20 points):
☐ At least 2 methods from course applied
☐ Justification for method selection
☐ Alternatives considered
☐ Decision framework reasoning used

Implementation (20 points):
☐ Code runs correctly
☐ Preprocessing appropriate
☐ Train/test split proper
☐ Hyperparameter tuning attempted
☐ Random seeds set

Results Interpretation (20 points):
☐ Results clearly presented
☐ Model comparison included
☐ Feature importance analyzed (if applicable)
☐ Business implications discussed
☐ Limitations acknowledged

Report Quality (20 points):
☐ Follows template structure
☐ 10-15 pages (excluding appendix)
☐ Figures/tables labeled and referenced
☐ Citations included
☐ Professional writing
```

---

### Common Capstone Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Scope too broad** | "Predict stock market crashes using all ML methods" | Narrow to specific stock, specific method comparison, specific timeframe |
| **Scope too narrow** | "Compare R² values of 2 regression models" | Add feature engineering, hyperparameter tuning, business interpretation |
| **Data unavailable** | Can't find suitable dataset | Use synthetic data (generate with NumPy) or pick different problem |
| **Methods unrelated** | Methods don't fit the problem | Use decision framework from lectures to select appropriate methods |
| **No business context** | Treats as pure ML exercise | Add section on why this matters to finance/business |
| **Code doesn't run** | Missing dependencies, errors | Set up clean environment, test code end-to-end before submission |
| **Report too short** | 6 pages instead of 10-15 | Expand Methodology and Results sections with more detail and visualizations |
| **Report too long** | 25 pages | Cut unnecessary details, move extra content to Appendix |
| **Poor writing** | Unclear, typos, grammatical errors | Use Grammarly, proofread, ask peer to review |

---

### Updating Capstone Materials

**When to update**:
- After first cohort (based on student questions and common issues)
- When course content changes (new methods added)
- When new example topics become relevant
- When rubric is updated

**Update protocol**:

```bash
# 1. Identify what needs updating
# - specification.md: Add new example topic, clarify timeline
# - report_template.tex: Add section for new requirement

# 2. Make changes
# Edit files, add content

# 3. Review with teaching team
# Get feedback from other instructors

# 4. Test with sample student
# Ask TA or advanced student to review updated materials

# 5. Update AGENTS.md
# Document changes made

# 6. Commit
git add capstone/specification.md capstone/AGENTS.md
git commit -m "Update capstone spec: add RL trading project example"
```

---

### Integration with Course Timeline

**Week-by-week**:

| Week | Topic | Capstone Activity |
|------|-------|-------------------|
| 1-2 | L01-L02 | (Not yet introduced) |
| 3 | L03 | (Not yet introduced) |
| 4 | L04 | **Capstone introduced**, review spec, brainstorm topics |
| 5 | L05 | **Topic proposal due**, instructor reviews and provides feedback |
| 6 | L06 | Final session, students begin work on projects |
| 7-8 | (No class) | Students work on projects, office hours available |
| 9 | (Deadline) | **Final report due** (2 weeks after Session 6) |
| 10 | (Optional) | Presentations (if time allows) |

**Office hours** (Weeks 6-8):
- Scheduled times for project questions
- Review methodology choices
- Help with code debugging
- Clarify rubric criteria
- Do NOT write the report for students (guidance only)

---

### Example Student Workflow

**Example: Credit Default Prediction Project**

```
Week 4:
- Read specification.md
- Browse Kaggle for credit datasets
- Select "Credit Card Default Dataset" (UCI)
- Draft topic proposal

Week 5:
- Submit topic proposal
- Receive instructor feedback: "Good choice, consider handling class imbalance"
- Revise approach to include SMOTE

Week 6:
- Download dataset, perform EDA
- Write Data Description section
- Implement Logistic Regression baseline

Week 7:
- Implement Random Forest
- Hyperparameter tuning with GridSearchCV
- Compare models (ROC, AUC, confusion matrix)
- Write Methodology section

Week 8:
- Analyze feature importance
- Interpret results in business context
- Write Results section
- Write Problem Definition and Executive Summary
- Create visualizations
- Extract code snippets for Appendix

Week 9:
- Proofread report
- Self-assess using rubric
- Format with LaTeX template
- Generate PDF
- Submit via Moodle
```

**Example project structure**:
```
credit_default_project/
├── data/
│   └── credit_default.csv
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_logistic_regression.ipynb
│   └── 03_random_forest.ipynb
├── figures/
│   ├── confusion_matrix.pdf
│   ├── feature_importance.pdf
│   └── roc_curve.pdf
├── report/
│   ├── report.tex
│   ├── references.bib
│   └── report.pdf  ← Final submission
└── README.md
```

---

### Validation Checklist

Before submission, verify:

**Content**:
- [ ] Problem clearly defined with business context
- [ ] At least 2 methods from course applied
- [ ] Methods compared and justified
- [ ] Data described (source, features, target)
- [ ] Results interpreted in business context
- [ ] Limitations acknowledged
- [ ] References cited properly

**Format**:
- [ ] 10-15 pages (excluding appendix)
- [ ] Follows template structure
- [ ] Figures/tables numbered and captioned
- [ ] Citations in consistent format
- [ ] Code snippets in appendix (not full notebooks)
- [ ] PDF format

**Technical**:
- [ ] Code runs without errors
- [ ] Random seeds set for reproducibility
- [ ] Train/test split used (no data leakage)
- [ ] Evaluation metrics appropriate for problem
- [ ] Hyperparameter tuning attempted

**Quality**:
- [ ] No typos or grammatical errors
- [ ] Professional academic writing
- [ ] Figures are clear and readable
- [ ] Self-assessed using rubric (score ≥70)

---

### Academic Integrity

**Allowed**:
- Using course materials (slides, notebooks) as reference
- Using scikit-learn documentation
- Using ChatGPT/Copilot for code debugging (cite usage)
- Discussing general approaches with classmates

**NOT allowed**:
- Copying code from another student's project
- Using ChatGPT to write report text (must be your own writing)
- Submitting work done by someone else
- Plagiarizing from online sources without citation

**Detection**:
- Reports screened with Turnitin (plagiarism detection)
- Code screened for similarity (if suspicion)
- Violations reported to academic integrity office

**Consequences**:
- First offense: Zero on project (40% of grade)
- Severe cases: Fail course, academic probation

**How to avoid**:
- Write in your own words
- Cite all external sources
- Include `# Code adapted from [source]` comments
- When in doubt, ask instructor

---

## Related Files

- **Parent hierarchy**: `../AGENTS.md` (project root)
- **Grading rubric**: `../rubrics/capstone_rubric.md` (detailed evaluation criteria)
- **Presentation rubric**: `../rubrics/presentation_rubric.md` (if presentations required)
- **Example datasets**: `../datasets/*.csv` (can be used for capstone)
- **Reference notebooks**: `../notebooks/L0X_*.ipynb` (examples of implementations)
- **Slides**: `../slides/L0X_Topic/` (method references and decision frameworks)
- **Manifest**: `../manifest.json` (tracks capstone materials)
- **CLI**: `python infrastructure/course_cli.py inventory list` (shows capstone files)

---

## Student Resources

**Dataset sources**:
- [Kaggle Datasets](https://www.kaggle.com/datasets) - Large collection, finance category
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php) - Classic datasets
- [Data.gov](https://data.gov) - US government data
- [Yahoo Finance API](https://finance.yahoo.com/) - Stock price data
- [Alpha Vantage](https://www.alphavantage.co/) - Free financial data API
- [Quandl](https://www.quandl.com/) - Financial and economic data

**Writing resources**:
- [Purdue OWL](https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html) - Citation formats
- [Grammarly](https://www.grammarly.com/) - Grammar and writing checker
- [Overleaf](https://www.overleaf.com/) - Online LaTeX editor (for report_template.tex)

**Code resources**:
- [scikit-learn documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)
- Course notebooks (`../notebooks/`) - Reference implementations
