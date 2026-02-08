# Group Assignment Grading Rubric

**Course:** Methods and Algorithms (MSc Data Science)
**Assignment:** ML Pipeline Challenge - Group Project
**Total Points:** 100
**Weight:** 60% of final course grade
**Date:** Academic Year 2025/26

---

## Overview

This rubric evaluates your group's machine learning pipeline project across four dimensions: technical analysis, communication, problem framing, and peer review quality. The technical section includes a difficulty multiplier based on topic coverage.

---

## Section 1: Technical Analysis (50 points)

### 1.1 Method Application (25 points)

Apply methods from 5 course topics (L01-L06). Each topic is worth 5 points.

**Covered Topics:** L01 (Linear Regression), L02 (Logistic Regression), L03 (KNN/K-Means), L04 (Random Forests), L05 (PCA/t-SNE), L06 (Embeddings/RL)

**Per-Topic Scoring Rubric (0-5 points):**

| Score | Description |
|-------|-------------|
| **5** | Method correctly applied with hyperparameter tuning (grid search, random search, or justified defaults), proper validation strategy (cross-validation or holdout with justification), results interpreted with domain context and statistical rigor |
| **4** | Method correctly applied with some tuning effort, adequate validation approach, basic interpretation of results with some domain relevance |
| **3** | Method correctly applied with default parameters, train/test split implemented, minimal interpretation provided |
| **2** | Method runs but has significant issues (data leakage, missing validation, inappropriate metrics, incorrect implementation details) |
| **1** | Method attempted but fundamentally incorrect or produces uninterpretable results |
| **0** | Not attempted or completely wrong |

**Minimum Depth Requirements for Score ≥3:**
- (a) Data preprocessing appropriate for the method
- (b) Hyperparameter tuning or justified use of defaults
- (c) Appropriate evaluation metric for the problem type
- (d) Interpretation of results in problem context

**Note:** Simply calling `model.fit()` and `model.predict()` with default parameters = maximum 2/5 points.

**Statistical Rigor:** For comparison claims ("Model A outperforms Model B"), you must provide statistical evidence such as paired t-test on cross-validation folds, McNemar's test, or confidence intervals. Statements without statistical testing are insufficient for scores ≥4.

---

### 1.2 Model Comparison & Evaluation (10 points)

| Score | Description |
|-------|-------------|
| **10** | All models compared using appropriate statistical tests (e.g., paired t-test, McNemar's test), metrics suitable for the problem (accuracy, precision, recall, F1, AUC, RMSE, etc.), cross-validation properly implemented |
| **7** | Models compared with some statistical rigor, mostly appropriate metrics selected, adequate validation approach |
| **4** | Basic comparison (reporting metrics only), no statistical hypothesis testing, limited justification for metric choices |
| **0** | No comparison provided or inappropriate comparison methods used |

**Expected Elements:**
- Multiple models compared systematically
- Statistical significance testing between models
- Appropriate metrics for problem type (classification vs regression, balanced vs imbalanced)
- Cross-validation or proper holdout validation
- Clear presentation of results (tables, plots)

---

### 1.3 Feature Engineering & Preprocessing (10 points)

| Score | Description |
|-------|-------------|
| **10** | Thorough preprocessing pipeline, proper train/test split maintained throughout, class imbalance addressed if relevant, feature encoding/scaling justified and appropriate, no data leakage |
| **7** | Adequate preprocessing implemented, correct data splitting, some feature engineering performed, minor issues present |
| **4** | Basic preprocessing only, potential data leakage concerns, missing key steps (e.g., scaling for distance-based methods) |
| **0** | No preprocessing or severe issues (e.g., fitting scalers on test data, using future information) |

**Expected Elements:**
- Proper train/test/validation splitting before any transformations
- Handling of missing values with justification
- Appropriate encoding of categorical variables
- Feature scaling where required by algorithms
- Class imbalance handling if applicable (SMOTE, class weights, etc.)
- Feature selection or dimensionality reduction with justification

---

### 1.4 Reproducibility (5 points)

| Score | Description |
|-------|-------------|
| **5** | Clone, install dependencies, run works perfectly on first try; random seeds set consistently; requirements.txt complete and accurate; clear README with setup instructions |
| **3** | Code runs with minor fixes needed (e.g., path adjustments); random seeds mostly set; requirements.txt mostly complete |
| **1** | Code requires significant effort to run; missing dependencies; unclear instructions |
| **0** | Code does not run or is fundamentally broken |

**Expected Elements:**
- `requirements.txt` or `environment.yml` with all dependencies
- Random seeds set for reproducibility (`np.random.seed()`, `random_state` parameters)
- Clear README with installation and execution instructions
- Data loading instructions or sample data provided
- No hardcoded absolute paths

---

### DIFFICULTY MULTIPLIER

After calculating the Technical Analysis subtotal (sum of sections 1.1-1.4, maximum 50 points), apply the difficulty multiplier based on topic coverage:

| Omitted Topic | Remaining Topics | Multiplier | Maximum Technical Score |
|---------------|-----------------|------------|------------------------|
| **L01 or L02** (1 point each) | 12 total points | 1.00 | 50.0 |
| **L03 or L04** (2 points each) | 11 total points | 0.96 | 48.0 |
| **L05** (3 points) | 10 total points | 0.92 | 46.0 |
| **L06** (4 points) | 9 total points | 0.88 | 44.0 |

**Example:** Group covers L01, L02, L03, L04, L05 (omits L06). Raw technical score = 48/50. Adjusted score = 48 × 0.88 = 42.24 points.

**Rationale:** This multiplier rewards groups tackling more advanced/complex methods (L05, L06) while still allowing strong performance with simpler method selections.

---

## Section 2: Communication (30 points)

### 2.1 Presentation (15 points)

| Score | Quality Level | Description |
|-------|--------------|-------------|
| **13-15** | Excellent | Clear structure, well-timed (15 min ±2), all members demonstrate strong understanding, compelling visualizations, engaging delivery, effective Q&A responses |
| **10-12** | Good | Good structure, minor timing issues, most members contribute well, clear visuals, adequate delivery |
| **7-9** | Adequate | Adequate structure but uneven, some members weak or disengaged, basic visuals, some clarity issues |
| **0-6** | Poor | Unclear structure, poorly timed (significantly over/under), uneven participation, weak or missing visuals, difficult to follow |

**Expected Elements:**
- All team members speak for roughly equal time
- Clear problem statement and motivation
- Logical flow from problem → methods → results → insights
- Effective use of visual aids
- Professional delivery and body language
- Confident handling of questions

---

### 2.2 Written Report (10 points)

| Score | Quality Level | Description |
|-------|--------------|-------------|
| **9-10** | Excellent | Professional quality, well-structured with clear sections, proper citations (APA/IEEE), technical accuracy, engaging narrative, appropriate length (10-15 pages) |
| **7-8** | Good | Good structure, minor writing issues (grammar, clarity), mostly proper citations, adequate technical content |
| **5-6** | Adequate | Complete but dry or unclear sections, some structural issues, limited citations, meets minimum requirements |
| **0-4** | Poor | Poor structure, hard to follow, significant writing issues, missing citations, too short or rambling |

**Expected Elements:**
- Executive summary (1 page)
- Introduction with problem statement
- Literature review or background
- Methodology section with technical details
- Results with tables and figures
- Discussion and interpretation
- Conclusions and recommendations
- Proper citations and references

---

### 2.3 Visualizations (5 points)

| Score | Quality Level | Description |
|-------|--------------|-------------|
| **5** | Excellent | Publication-quality figures, insightful chart choices (confusion matrices, ROC curves, feature importance, etc.), proper labeling (axes, legends, titles), appropriate color schemes |
| **4** | Good | Good plots with proper labels, mostly insightful choices, minor aesthetic issues |
| **3** | Adequate | Basic plots with adequate labeling, some labeling issues or suboptimal chart types |
| **0-2** | Poor | Missing visualizations, misleading plots, unlabeled axes, inappropriate chart types |

**Expected Elements:**
- Model performance visualizations (confusion matrix, ROC/AUC, learning curves)
- Feature importance or dimensionality reduction plots
- Comparative visualizations across models
- Exploratory data analysis plots
- Professional aesthetics (consistent fonts, readable sizes, color-blind friendly)

---

## Section 3: Problem Framing & Insight (10 points)

### 3.1 Problem Definition (5 points)

| Score | Quality Level | Description |
|-------|--------------|-------------|
| **5** | Excellent | Clear business problem articulation, well-motivated with real-world context, appropriate scope for ML solution, success criteria defined |
| **4** | Good | Clear problem statement, adequate motivation, reasonable scope |
| **3** | Adequate | Problem stated but vague or overly broad, limited motivation |
| **0-2** | Poor | Unclear or missing problem statement, no motivation |

**Expected Elements:**
- Clear articulation of the business or research question
- Motivation for why ML is appropriate
- Defined success criteria (business metrics, not just accuracy)
- Appropriate scope given time and data constraints

---

### 3.2 Business Insights (5 points)

| Score | Quality Level | Description |
|-------|--------------|-------------|
| **5** | Excellent | Actionable, data-driven recommendations; insights go beyond metrics to business implications; demonstrates understanding of stakeholder needs |
| **4** | Good | Some business context provided beyond just reporting metrics; mentions stakeholder relevance |
| **3** | Adequate | Mentions business relevance but mostly focuses on technical metrics |
| **0-2** | Poor | Only reports accuracy/performance metrics with no business interpretation |

**Expected Elements:**
- Recommendations for stakeholders based on model results
- Discussion of model limitations and deployment considerations
- Cost-benefit analysis or ROI discussion if applicable
- Interpretation of feature importance in business terms
- Discussion of ethical implications if relevant

---

## Section 4: Peer Review Quality (10 points)

**Note:** This section is NOT subject to the difficulty multiplier.

### 4.1 Thoroughness (5 points)

| Score | Quality Level | Description |
|-------|--------------|-------------|
| **5** | Excellent | Substantive feedback on both reviewed projects, specific references to code/results/report sections, demonstrates deep engagement with peers' work |
| **4** | Good | Good feedback with some specific references, covers major elements |
| **3** | Adequate | Generic feedback covering basics, limited specificity |
| **0-2** | Poor | Minimal effort, missing reviews, or unhelpful comments |

---

### 4.2 Constructiveness (5 points)

| Score | Quality Level | Description |
|-------|--------------|-------------|
| **5** | Excellent | Identifies both strengths AND areas for improvement, actionable suggestions provided, respectful and professional tone |
| **4** | Good | Balanced feedback, mostly actionable suggestions |
| **3** | Adequate | Mostly critical or mostly praise without balance |
| **0-2** | Poor | Unhelpful, hostile, or purely superficial comments |

---

## Grade Conversion Table

| Score | Letter Grade |
|-------|-------------|
| 93-100 | A |
| 85-92 | A- |
| 78-84 | B+ |
| 70-77 | B |
| 62-69 | C+ |
| 55-61 | C |
| <55 | F |

---

## Deductions

| Issue | Penalty |
|-------|---------|
| Late submission (within 24h grace period) | -5 points |
| Late submission (beyond 24h) | -10 points per day (max -30) |
| Over page limit (>18 pages) | -5 points |
| Under page limit (<8 pages) | -10 points |
| Plagiarism or academic dishonesty | Automatic failure (0 points) |

---

## Bonus

**Two-person groups only:** +3 points added to final score (recognizing smaller team size).

---

## Scoring Sheet

**Group Number:** ___________
**Group Members:** _____________________________________
**Reviewer:** ___________
**Date:** ___________

### Technical Analysis (before multiplier)

| Criterion | Points Possible | Points Awarded | Notes |
|-----------|-----------------|----------------|-------|
| Method Application: L01 | 5 | | |
| Method Application: L02 | 5 | | |
| Method Application: L03 | 5 | | |
| Method Application: L04 | 5 | | |
| Method Application: L05 | 5 | | |
| Method Application: L06 | 5 | | |
| Model Comparison | 10 | | |
| Feature Engineering | 10 | | |
| Reproducibility | 5 | | |
| **Subtotal** | **50** | | |

**Topics Omitted:** ___________
**Difficulty Multiplier:** ___________
**Adjusted Technical Score:** ___________ / 50

### Communication

| Criterion | Points Possible | Points Awarded | Notes |
|-----------|-----------------|----------------|-------|
| Presentation | 15 | | |
| Written Report | 10 | | |
| Visualizations | 5 | | |
| **Subtotal** | **30** | | |

### Problem Framing & Insight

| Criterion | Points Possible | Points Awarded | Notes |
|-----------|-----------------|----------------|-------|
| Problem Definition | 5 | | |
| Business Insights | 5 | | |
| **Subtotal** | **10** | | |

### Peer Review Quality

| Criterion | Points Possible | Points Awarded | Notes |
|-----------|-----------------|----------------|-------|
| Thoroughness | 5 | | |
| Constructiveness | 5 | | |
| **Subtotal** | **10** | | |

### Final Calculation

| Item | Points |
|------|--------|
| Technical Analysis (adjusted) | ___ / 50 |
| Communication | ___ / 30 |
| Problem Framing & Insight | ___ / 10 |
| Peer Review Quality | ___ / 10 |
| **Subtotal** | ___ / 100 |
| Bonus (2-person groups) | ___ |
| Deductions | ___ |
| **FINAL SCORE** | ___ / 100 |

**Letter Grade:** ___________

---

## Feedback

**Strengths:**

**Areas for Improvement:**

**Additional Comments:**

---

**Instructor Signature:** _____________________ **Date:** ___________
