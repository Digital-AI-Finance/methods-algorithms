# Semester Group Assignment: Methods & Algorithms MSc Course

**Version**: 3 (revised after Critic review, Iteration 2)

## Plan Overview

Design a semester-long group assignment (60% of final grade) where groups of 2-3 MSc Data Science students apply 5 of the 6 course topics to a self-sourced dataset, present their analysis (15 min + 5 min Q&A), and submit via GitHub with cross-group peer review.

---

## 1. Assignment Structure

### 1.1 Core Concept: "ML Pipeline Challenge"

Each group selects a **real-world finance/business problem**, sources their own dataset, and builds a complete ML pipeline applying **5 of the 6 course topics**. The key innovation: **topic difficulty points determine the technical score multiplier**.

### 1.2 Topic Difficulty Scoring (Revised)

Rather than a cap system (which creates perverse incentives to skip hard topics), we use a **difficulty point system** where harder topic combinations earn a multiplier.

**Topic difficulty points:**

| Topic | Difficulty Points | Rationale |
|-------|-------------------|-----------|
| L01: Linear Regression | 1 | Foundation, well-understood |
| L02: Logistic Regression | 1 | Foundation, well-understood |
| L03: KNN & K-Means | 2 | Two algorithms, unsupervised + supervised |
| L04: Random Forests & Boosting | 2 | Ensemble methods, hyperparameter-heavy |
| L05: PCA & t-SNE | 3 | Mathematical depth, interpretation challenges |
| L06: Embeddings & RL | 4 | Two distinct paradigms (NLP + RL), most implementation complexity |

**Note**: L05 and L06 are NOT equally difficult. L06 covers two fundamentally different domains (NLP and RL) while L05 covers related techniques within one domain (dimensionality reduction).

**How it works**: Sum the difficulty points of the 5 chosen topics (total possible = 13). Apply a multiplier to the Technical Analysis score (50 points):

| Omitted Topic | Remaining Points | Multiplier | Effect on 50-pt Technical Score |
|---------------|-----------------|------------|----------------------------------|
| L01 (1 pt) or L02 (1 pt) | 12 | 1.00 | No reduction |
| L03 (2 pts) or L04 (2 pts) | 11 | 0.96 | Max technical = 48.0/50 |
| L05 (3 pts) | 10 | 0.92 | Max technical = 46.0/50 |
| L06 (4 pts) | 9 | 0.88 | Max technical = 44.0/50 |

**Effect**: A group scoring 45/50 on technical analysis that omitted L06 (remaining 9 points) gets 45 x 0.88 = 39.6/50. A group scoring 45/50 that included L06 and omitted L01 (remaining 12 points) keeps 45/50. This creates a ~5-point incentive to tackle harder combinations without making it impossible to earn a good grade with easier ones.

**Maximum achievable grade by omitted topic:**

| Omitted Topic | Remaining Points | Max Technical (after multiplier) | Max Total | Effective Max Grade |
|---------------|-----------------|----------------------------------|-----------|---------------------|
| L01 or L02 | 12 | 50.0 | 100 | A (100) |
| L03 or L04 | 11 | 48.0 | 98.0 | A (98) |
| L05 | 10 | 46.0 | 96.0 | A (96) |
| L06 | 9 | 44.0 | 94.0 | A- (94) |

Every combination can still earn an A-range grade, but harder combinations have more headroom.

### 1.3 Group Formation

- **Size**: 2-3 students
- **Formation**: Self-selected with instructor approval by Session 2
- **Diversity**: Encouraged to mix backgrounds (finance, CS, statistics)
- **Individual accountability**: Each group member must be able to explain any part during Q&A
- **2-person group adjustment**: 3 bonus points (not 5) added to final score to partially compensate for fewer hands

---

## 2. Course Grade Breakdown

This assignment replaces the individual capstone project. The full course grade structure:

| Component | Weight | Description |
|-----------|--------|-------------|
| **Group Assignment** | **60%** | This assignment (ML Pipeline Challenge) |
| Session Quizzes | 20% | 3 quizzes covering L01-L02, L03-L04, L05-L06 |
| Class Participation | 10% | Attendance, in-class exercises, discussion |
| Lightning Talks | 10% | Session 3 & 5 progress presentations (formative) |

The existing `capstone/specification.md` (40% individual capstone) is superseded. Files to archive: `capstone/specification.md` -> `archiv/capstone_specification_v1.md`.

---

## 3. Deliverables

### 3.1 GitHub Repository (Primary Submission)

Each group creates a **public or private GitHub repository** containing:

```
group-project/
+-- README.md                 # Project overview, how to run, team members
+-- requirements.txt          # Python dependencies
+-- data/                     # Dataset (or link if too large)
+--   +-- README.md           # Data dictionary, source, license
+-- notebooks/
+--   +-- 01_eda.ipynb        # Exploratory data analysis
+--   +-- 02_preprocessing.ipynb
+--   +-- 03_modeling.ipynb   # All 5 methods applied
+--   +-- 04_evaluation.ipynb # Comparison and evaluation
+-- presentation/
+--   +-- slides.pptx         # PowerPoint presentation
+-- report/
+--   +-- report.pdf          # Written report (10-15 pages)
```

**Repository requirements:**
- Clean commit history (not one giant commit) -- minimum 10 meaningful commits
- README with setup instructions (clone, install, run)
- All code must be reproducible (random seeds, requirements.txt)
- No API keys or credentials committed
- All team members must have commits (visible contribution)
- Add instructor as collaborator for private repos

**GitHub tutorial**: A 30-minute GitHub tutorial will be provided in Session 1 covering: account creation, repository setup, clone/commit/push workflow, and the required folder structure. Students without GitHub accounts will create them during this session.

### 3.2 Written Report (10-15 pages)

| Section | Pages | Content |
|---------|-------|---------|
| Executive Summary | 0.5 | Problem, approach, key findings |
| Problem Definition & Data | 1.5 | Business context, dataset description, EDA summary |
| Methodology | 4-5 | Each of 5 methods: why selected, how applied, hyperparameters, validation |
| Results & Comparison | 3-4 | Performance metrics, model comparison, visualizations |
| Business Insights | 1 | Actionable recommendations from findings |
| Limitations & Reflection | 1 | What worked, what didn't, what would improve |

### 3.3 PowerPoint Presentation (15 min + 5 min Q&A)

- **15 slides maximum** (1 min per slide guideline)
- All group members must present (roughly equal time)
- Must include: problem statement, data overview, method pipeline diagram, key results, walkthrough of one key result
- Q&A: Instructor and peers may ask **any group member** about **any part** -- this enforces individual accountability
- **Scheduling**: All groups present in a single 3-hour session. With 4-7 groups at 20 min each, this fits within 80-140 minutes.

### 3.4 Cross-Group Peer Review

After presentations, each group reviews **2 other groups'** GitHub repositories. Groups are assigned by the instructor (round-robin, ensuring no reciprocal reviews).

**Peer review form** (each criterion has anchoring descriptors):

| Criterion | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|-----------|----------|---------------|---------------|
| Code quality & reproducibility | Code doesn't run or has no comments | Code runs with minor issues, some documentation | Clone, install, run works perfectly, well-documented |
| Method application correctness | Methods applied incorrectly or superficially | Methods correct but limited tuning/validation | Methods correct with tuning, CV, proper evaluation |
| Visualization quality | No visualizations or misleading charts | Basic plots, adequate labeling | Publication-quality figures, insightful chart choices |
| Report clarity | Hard to follow, missing sections | Complete but dry, adequate structure | Engaging, well-structured, clear narrative |
| Presentation effectiveness | Unclear, poorly timed, unbalanced | Adequate clarity and timing | Compelling, well-paced, all members strong |

**Moderation**: Instructor reviews all peer evaluations. Outlier scores (>2 points from instructor assessment) are replaced by instructor scores. This prevents one hostile reviewer from tanking another group.

---

## 4. Grading Rubric (100 points, worth 60% of final course grade)

### 4.1 Technical Analysis (50 points)

| Criterion | Points | Scoring Guide |
|-----------|--------|---------------|
| Method Application (5 topics) | 25 | 5 pts each: see per-topic rubric below |
| Model Comparison & Evaluation | 10 | Cross-validation, appropriate metrics, paired comparison |
| Feature Engineering & Preprocessing | 10 | Cleaning, encoding, scaling, train/test split, handling imbalance |
| Reproducibility | 5 | Code runs from clone, seeds set, requirements.txt works |

**Per-topic scoring (5 points each):**

| Score | Description |
|-------|-------------|
| 5 | Method correctly applied with hyperparameter tuning (grid/random search or justified defaults), proper validation (CV or holdout), results interpreted with domain context |
| 4 | Method correctly applied with some tuning, adequate validation, basic interpretation |
| 3 | Method correctly applied with default parameters, train/test split used, minimal interpretation |
| 2 | Method runs but with issues (e.g., data leakage, no validation, wrong metric) |
| 1 | Method attempted but produces incorrect or uninterpretable results |
| 0 | Method not attempted or completely wrong |

**Minimum method depth**: Each topic must demonstrate at least: (a) appropriate preprocessing for that method, (b) hyperparameter tuning or justified default choice, (c) proper evaluation metric, and (d) interpretation of results. Simply calling `model.fit(); model.predict()` with defaults earns at most 2/5.

**Statistical comparison**: For model comparison, students should use at least one of: paired t-test on CV folds, McNemar's test for classification, or confidence intervals on performance metrics. The specific test is the student's choice, but "Model A has AUC 0.82 and Model B has AUC 0.80 therefore A is better" without significance testing is insufficient.

**After scoring, apply difficulty multiplier** (Section 1.2) to the 50-point Technical Analysis subtotal.

### 4.2 Communication (30 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Presentation | 15 | Clarity, structure, timing, visual aids, all members contribute equally |
| Written Report | 10 | Professional writing, clear structure, proper citations |
| Visualizations | 5 | Publication-quality figures, appropriate chart types, properly labeled |

### 4.3 Problem Framing & Insight (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Problem Definition | 5 | Clear business problem, well-motivated, appropriate scope |
| Business Insights | 5 | Actionable conclusions beyond "model X had best accuracy" |

### 4.4 Peer Review Quality (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Review Thoroughness | 5 | Substantive feedback on both reviewed projects |
| Constructiveness | 5 | Actionable suggestions, identifies both strengths and weaknesses |

**Note**: Peer review quality is scored by the instructor based on the reviews each group writes. It is NOT subject to the difficulty multiplier (only the Technical Analysis subtotal is).

**How received peer review scores are used**: The average peer review score a group *receives* (across both reviewing groups, moderated by instructor) serves as a **calibration input** for the instructor's own grading. If peer reviewers consistently rate a project lower than the instructor's initial assessment, the instructor re-examines those specific criteria. Peer-received scores do NOT directly determine any portion of the grade — they are advisory. This avoids giving students direct grading power over each other while still leveraging their observations.

### 4.5 Grade Conversion

| Score | Grade | Description |
|-------|-------|-------------|
| 93-100 | A | Outstanding -- exceeds expectations in all areas |
| 85-92 | A- | Excellent -- strong in all areas, minor gaps |
| 78-84 | B+ | Very good -- solid work with some room for improvement |
| 70-77 | B | Good -- meets expectations, notable gaps in 1-2 areas |
| 62-69 | C+ | Satisfactory -- meets minimum requirements |
| 55-61 | C | Adequate -- significant gaps but demonstrates learning |
| <55 | F | Fail -- does not demonstrate sufficient competence |

### 4.6 Within-Group Contribution Assessment

Each group member completes a **confidential contribution survey** rating each team member (including themselves) on:
- Technical contribution (coding, analysis)
- Communication contribution (writing, presentation prep)
- Project management (coordination, deadlines)

Scale: 1 (minimal) to 5 (exceptional). If a member's average rating is >1.5 standard deviations below the group mean, the instructor conducts a 5-minute individual oral defense. Individual grades may be adjusted +/- 10% based on contribution evidence (survey + commit history + oral defense).

---

## 5. Three Worked Examples

### Example 1: Credit Risk Modeling (Moderate Difficulty -- Omits L06, remaining 9 pts)

**Dataset**: Kaggle "Home Credit Default Risk" (300K+ loans, 120+ features, binary target: default/no-default)

**Topic Application Pipeline:**

| # | Topic | Application | Key Quantitative Analysis |
|---|-------|-------------|---------------------------|
| 1 | L01: Linear Regression | Predict log(annuity amount) from applicant features as a precursor model | Adjusted $R^2 = 0.48$, VIF analysis for multicollinearity ($\text{VIF} > 10$ for 3 features removed), Breusch-Pagan test ($p = 0.003$, heteroscedasticity detected -- use robust SEs), F-test for joint significance ($F = 245, p < 0.001$) |
| 2 | L02: Logistic Regression | Classify default/no-default ($y \in \{0,1\}$) | AUC = 0.76, LRT comparing nested models ($\chi^2 = 45.3, p < 0.001$), calibration plot with Hosmer-Lemeshow ($\hat{C} = 12.1, p = 0.15$ -- adequate fit), odds ratios for top features |
| 3 | L03: K-Means | Segment borrowers into risk clusters | Silhouette analysis ($k=4$ optimal, $\bar{s} = 0.38$), Gap statistic confirms $k=4$, cluster profiles: "low-risk salaried" vs. "high-risk self-employed" |
| 4 | L04: Random Forest + XGBoost | Main prediction model with boosting comparison | RF AUC = 0.80, XGBoost AUC = 0.82, paired t-test on 5-fold CV AUCs ($p = 0.04$, XGBoost significantly better). SHAP analysis: top 3 features are EXT_SOURCE_2, EXT_SOURCE_3, DAYS_BIRTH. Permutation importance with 95% CI. |
| 5 | L05: PCA + t-SNE | Reduce 120 features, visualize risk structure | First 15 PCs explain 78% variance, scree plot elbow at $k=8$, parallel analysis retains 10 components. t-SNE visualization ($\text{perplexity}=30$) reveals default clusters heavily overlap non-defaults (confirms difficulty of the prediction task) |

**Omitted**: L06 (Tier 3, 4 pts) -- difficulty multiplier 0.88 applied to technical score.

**Business Insight**: "The XGBoost model identifies 72% of defaults in the top 20% riskiest applicants. Deploying this as a pre-screening tool would reduce default losses by an estimated 30% while rejecting only 15% of ultimately good borrowers. SHAP analysis reveals EXT_SOURCE features (credit bureau scores) dominate -- the bank should invest in enriching credit bureau data."

---

### Example 2: Customer Churn Prediction (High Difficulty -- Omits L01, remaining 12 pts)

**Dataset**: Kaggle "Telco Customer Churn" (7K customers, 21 features) + Twitter/Reddit financial complaints corpus for sentiment (publicly available from SemEval or Financial PhraseBank)

**Topic Application Pipeline:**

| # | Topic | Application | Key Quantitative Analysis |
|---|-------|-------------|---------------------------|
| 1 | L02: Logistic Regression | Baseline churn prediction | AUC = 0.83, odds ratios: month-to-month contract OR = 4.2 ($p < 0.001$), fiber optic OR = 1.8. AIC model selection: reduced model (12 features) vs. full (21): $\Delta\text{AIC} = -8.3$ favors reduced model |
| 2 | L03: KNN + K-Means | KNN churn classifier + customer segmentation | KNN ($k=7$, Euclidean with standardized features): AUC = 0.79. K-Means ($k=3$): "high-value loyal" (tenure > 40mo, low churn), "at-risk new" (tenure < 12mo, churn rate = 47%), "price-sensitive" (high monthly charges). Silhouette $\bar{s} = 0.35$. |
| 3 | L04: Random Forest + XGBoost | Best-performing churn model | XGBoost AUC = 0.86, F1 = 0.68. Feature importance: contract type > tenure > monthly charges. SHAP: interaction effect between tenure and contract type. 5-fold CV: XGBoost vs. Logistic AUC difference = 0.03, paired t-test $p = 0.02$. |
| 4 | L05: PCA + t-SNE | Dimensionality reduction and customer visualization | PCA: 5 components explain 72% variance, PC1 = "engagement" factor (tenure, streaming services), PC2 = "spending" factor (monthly charges, total charges). t-SNE ($\text{perplexity}=30$): visual separation between churners and stayers, especially in the "at-risk" segment. |
| 5 | L06: Word Embeddings | Sentiment from public complaint text | Pre-trained Word2Vec (Google News 300d) applied to Financial PhraseBank sentences. Cosine similarity clustering reveals 4 topic themes (billing, service quality, pricing, support). Embed complaint categories as features -- adding sentiment feature to XGBoost improves AUC by 0.01 (modest but demonstrates the NLP pipeline). |

**Omitted**: L01 (1 pt) -- remaining 12 pts, difficulty multiplier 1.00 (maximum).

**Business Insight**: "Combining the XGBoost churn model with K-Means segmentation, we recommend a targeted retention program: offer 12-month contract discounts to the 'at-risk new' segment (estimated 23% churn reduction). The embedding-based sentiment analysis shows billing complaints are the most common theme, suggesting process improvements in billing communication."

---

### Example 3: Equity Factor Investing with RL (Maximum Difficulty -- Omits L03, remaining 11 pts)

**Dataset**: Yahoo Finance daily prices for 50 liquid S&P 500 stocks (2015-2025), augmented with financial ratios from SimFin.

**Topic Application Pipeline:**

| # | Topic | Application | Key Quantitative Analysis |
|---|-------|-------------|---------------------------|
| 1 | L01: Linear Regression | Fama-French factor model estimation | $R_i - R_f = \alpha_i + \beta_1 \text{MKT} + \beta_2 \text{SMB} + \beta_3 \text{HML} + \varepsilon$. Adjusted $R^2 = 0.31$ (typical for individual stocks), F-test ($F = 87, p < 0.001$). Durbin-Watson = 1.92 (no autocorrelation). Alpha significantly positive for 5 of 50 stocks ($\alpha > 0, p < 0.05$). Breusch-Pagan detects heteroscedasticity ($p = 0.01$) -- use HAC standard errors. |
| 2 | L02: Logistic Regression | Predict next-month outperformance ($y = 1$ if $R_i > R_m$) | AUC = 0.56 (hard problem -- barely above random). Features: 12-month momentum, book-to-market, market cap, volatility. LRT: momentum + value model significantly better than value-only ($\chi^2 = 18.3, p < 0.001$). Calibration: Brier score = 0.25. Honest conclusion: logistic regression has limited predictive power for stock returns. |
| 3 | L04: Random Forest + XGBoost | Feature-rich return prediction | 30 financial ratios as features. RF accuracy = 53%, XGBoost = 55% (above 50% random baseline, binomial test $p = 0.04$). SHAP: 12-month momentum and P/E ratio are top predictors. Rolling 5-year walk-forward validation shows unstable performance (feature importance shifts across windows). |
| 4 | L05: PCA | Factor structure of equity returns | PCA on 50-stock return correlation matrix: PC1 = market factor (explains 42%), PC2 = sector rotation (9%), PC3 = size (5%). Parallel analysis retains 6 factors. Interpretation: PCs correspond to interpretable risk factors. Scree plot shows clear elbow at 3 components. |
| 5 | L06: RL (Q-Learning) | Simple trading agent on a single stock | State: (momentum quintile, volatility regime [low/high], current position [flat/long]). Actions: buy/hold/sell. Reward: daily return minus 10bps transaction cost. Q-learning: $\epsilon$-greedy ($\epsilon: 0.3 \to 0.01$ over 500 episodes), $\alpha = 0.1$, $\gamma = 0.95$. Backtested Sharpe = 0.45 vs. buy-and-hold 0.55. **Honest result**: agent underperforms buy-and-hold after costs. Discussion of why: small state space loses information, transaction costs dominate, non-stationarity of financial markets violates MDP assumptions. This negative result is graded positively because the analysis and reflection are rigorous. |

**Omitted**: L03 (2 pts) -- remaining 11 pts, difficulty multiplier 0.96 applied to technical score.

**Business Insight**: "The PCA factor structure reveals 6 principal components explain 73% of cross-sectional return variation. The Q-learning agent fails to beat buy-and-hold after costs -- an honest and important finding. The most actionable result is the XGBoost model: a top-quintile portfolio rebalanced monthly achieves 55% directional accuracy and 1.2% estimated annual alpha before costs, which disappears after realistic transaction costs of 20bps round-trip. This underscores the efficiency of equity markets."

---

## 6. Policies (Resolved)

### 6.1 Dataset Requirements
- Must be real-world data (not course-provided synthetic datasets)
- Minimum 1,000 observations and 10 features
- Must include appropriate target variable(s) for supervised methods
- Data source and license must be documented in `data/README.md`
- Suggested sources: Kaggle, UCI ML Repository, Yahoo Finance, FRED, ECB, World Bank, SimFin, Financial PhraseBank
- **Dataset approval**: Instructor approves datasets at Session 2 checkpoint. Groups submit a 1-paragraph dataset description + link. Approval within 48 hours. This prevents groups from investing weeks in an unsuitable dataset.

### 6.2 Academic Integrity
- All code must be original (no copying from other groups or online solutions)
- AI tools (ChatGPT, GitHub Copilot) permitted for coding assistance but must be disclosed in report appendix ("AI tools used: ...")
- Written analysis and interpretation must be in students' own words
- Cross-referencing with other groups is encouraged during peer review phase only
- Plagiarism detection applied to reports (Turnitin or equivalent)

### 6.3 Deadline & Late Submission
- **Hard deadline** for GitHub repo, report, and slides: Session 6 + 7 days, 23:59 local time
- **24-hour grace period**: Submissions within 24 hours of deadline receive -5 points (out of 100)
- **Beyond 24 hours**: -10 points per additional day, maximum -30 points
- **No extensions** without documented medical/personal emergency

### 6.4 Presentation Scheduling
- All groups present in a single 3-hour session (Session 6 + 2 weeks)
- Order drawn randomly at start of session
- 15 min presentation + 5 min Q&A + 2 min changeover = 22 min per group
- For 6 groups: 132 min total, fits in one session with breaks

### 6.5 Lightning Talks (10% of Course Grade)

Two progress check-ins during the semester where each group gives a brief presentation:

**Lightning Talk 1 (Session 3):** 5 minutes per group
- Present: chosen dataset, problem statement, 5 selected topics, initial EDA findings
- Purpose: Ensure groups are on track, receive early feedback
- Grading: 50% of Lightning Talks grade (5% of course)

**Lightning Talk 2 (Session 5):** 5 minutes per group
- Present: preliminary results from at least 3 of 5 methods, challenges encountered
- Purpose: Progress checkpoint, identify struggling groups for instructor support
- Grading: 50% of Lightning Talks grade (5% of course)

**Scoring (each talk, out of 5):**

| Score | Description |
|-------|-------------|
| 5 | Clear progress, well-prepared, demonstrates understanding |
| 3 | Adequate progress, some preparation gaps |
| 1 | Minimal progress, unprepared, or no-show |

Lightning Talks are **formative** — instructor provides written feedback within 48 hours. A low score on LT1 is a warning signal, not a grade sentence; groups can recover fully by LT2 and the final submission.

### 6.6 Group Dissolution
- If a group dissolves before Session 4: members may join other groups or form new ones (instructor facilitates)
- If a group dissolves after Session 4: remaining members complete the project with adjusted expectations (instructor may reduce scope to 4 topics, no difficulty multiplier penalty)
- In all cases: instructor must be notified within 48 hours of dissolution

### 6.7 Combined Topic Coverage Requirements

Topics L03, L04, and L05 each cover two related techniques. The minimum requirements for earning full credit on each:

| Topic | Contains | Minimum for Full Credit (5/5) | Acceptable Partial (3-4/5) |
|-------|----------|-------------------------------|----------------------------|
| L03 | KNN + K-Means | Both applied (one supervised, one unsupervised) | One applied with strong analysis |
| L04 | RF + Boosting | At least one tree ensemble + one boosting method compared | Only RF or only boosting |
| L05 | PCA + t-SNE | PCA for dimensionality reduction + t-SNE for visualization | Only PCA (t-SNE optional if dataset unsuitable for visualization) |

**Rationale**: These topics are paired because the techniques complement each other. L03 pairs supervised (KNN) with unsupervised (K-Means); L04 pairs bagging (RF) with boosting (XGBoost); L05 pairs linear (PCA) with nonlinear (t-SNE) dimensionality reduction. Applying both demonstrates deeper understanding.

**Exception**: If a dataset genuinely doesn't support one technique (e.g., no meaningful clusters for K-Means, or too few features for PCA), students may substitute a well-justified explanation of why the technique is inapplicable. This itself demonstrates analytical thinking.

### 6.8 L06 (RL) Feasibility
- Groups choosing L06 may apply EITHER the embeddings component OR the RL component (not required to do both)
- For RL: A simplified trading environment with discrete states (3-5 state variables) and 2-3 actions is sufficient. Students are NOT expected to build complex gym environments.
- For Embeddings: Pre-trained word vectors (Word2Vec, GloVe, or FinBERT) are acceptable. Students are NOT expected to train embeddings from scratch.
- **A negative RL result is graded positively** if the analysis, reflection, and explanation of why it failed are rigorous. The course slides explicitly note that beating buy-and-hold after costs is extremely difficult.

---

## 7. Files to Create

| File | Purpose | Location |
|------|---------|----------|
| `group_assignment_specification.md` | Full assignment brief for students | `capstone/` |
| `group_assignment_rubric.md` | Detailed rubric with per-score descriptors | `rubrics/` |
| `peer_review_form.md` | Structured peer review with anchoring descriptors | `rubrics/` |
| `contribution_survey.md` | Within-group contribution assessment form | `rubrics/` |
| `example_projects.md` | The 3 worked examples (student-facing, simplified) | `capstone/` |

Existing files to archive:
- `capstone/specification.md` -> `archiv/capstone_specification_v1.md`
- `rubrics/capstone_rubric.md` -> `archiv/capstone_rubric_v1.md`

---

## 8. Summary

This group assignment replaces the individual capstone (now 60% of grade) with a collaborative ML pipeline project that:
- Requires applying **5 of 6 topics** (comprehensive coverage)
- Rewards difficulty through a **point-based multiplier** (not a cap) -- all combinations can earn an A
- Develops real-world skills: **GitHub**, **team collaboration**, **presentation**
- Includes **cross-group peer review** with instructor moderation and anchoring descriptors
- Provides **3 detailed examples** with realistic, verified quantitative analysis
- Maintains academic rigor through **individual accountability** (Q&A, commit history, contribution survey, optional oral defense)
- Resolves all policy questions upfront (deadlines, GitHub tutorial, late policy, group dissolution, L06 feasibility)

---

## Appendix: Critic Review Changes (Iteration 1)

| Critic Issue | Resolution |
|--------------|------------|
| F1: L05 and L06 equally tiered | Fixed: L05 = 3 pts, L06 = 4 pts (different tiers) |
| F2: Perverse incentive (skip hard, no penalty) | Fixed: Replaced cap system with difficulty multiplier. All topics carry some incentive weight. |
| F3: 5-point 2-person bonus too large | Fixed: Reduced to 3 points |
| F4: Cap applied to peer review score | Fixed: Multiplier applies only to Technical Analysis subtotal (50 pts), not peer review (10 pts) |
| C1: Grade weight contradiction | Fixed: Added Section 2 with full course grade breakdown, explicit archival of old capstone |
| C2: No peer review form | Fixed: Added anchoring descriptors (1/3/5 scale) in Section 3.4 |
| C3: Old capstone not addressed | Fixed: Explicit archival plan in Section 7 |
| C4: Peer review assignment mechanism | Fixed: Instructor-assigned round-robin, no reciprocal reviews |
| FE2: FinBERT on non-existent tickets | Fixed: Changed to Financial PhraseBank + Word2Vec (publicly available NLP corpus) |
| FE3: Unrealistic RL expectations | Fixed: Section 6.6 allows either embeddings OR RL, negative results graded positively |
| R1: Cap applied after full 100 | Fixed: Multiplier on 50-pt technical subtotal only |
| R2: No per-score descriptors | Fixed: 0-5 scale with descriptors in Section 4.1 |
| R3: Grade conversion missing | Fixed: Added Section 4.5 with explicit grade table |
| Example 1: Home Credit target is binary | Fixed: L01 now predicts log(annuity amount), a continuous variable in the dataset |
| Example 3: Fama-French R^2 = 0.65 | Fixed: Lowered to 0.31 (realistic for individual stocks) |
| Example 3: Sharpe = 0.8 for RL | Fixed: Lowered to 0.45, and agent now honestly underperforms buy-and-hold |
| 8 unresolved questions | Fixed: All resolved in Section 6 (Policies) |
| P1: Statistical significance undefined | Fixed: Added guidance in Section 4.1 (paired t-test, McNemar's, CIs) |
| P2: Minimum method depth | Fixed: Explicit minimum depth + scoring descriptors in Section 4.1 |
| PR3: Peer review reliability | Fixed: Instructor moderation, outlier replacement |
| PR4: Within-group assessment | Fixed: Contribution survey instrument defined in Section 4.6 |

## Appendix: Critic Review Changes (Iteration 2)

| Critic Issue | Resolution |
|--------------|------------|
| N1/N2/N3 (CRITICAL): Multiplier table arithmetic wrong | Fixed: Corrected all point totals (omit L01/L02→12, L03/L04→11, L05→10, L06→9). Total possible = 13. |
| Example 1 reference "8 difficulty pts" | Fixed: Changed to "remaining 9 pts" |
| Example 2 reference inconsistent phrasing | Fixed: Changed to "remaining 12 pts" with consistent language |
| Example 3 reference "10 difficulty pts" | Fixed: Changed to "remaining 11 pts, multiplier 0.96" |
| N5: Lightning Talks at 10% with zero specification | Fixed: Added Section 6.5 with full specification (2 talks at Sessions 3 & 5, 5 min each, scoring rubric, formative purpose) |
| N6: Received peer review scores unused | Fixed: Added clarification in Section 4.4 — received scores serve as calibration input for instructor grading (advisory, not determinative) |
| N4/N7: Partial topic coverage for combined topics | Fixed: Added Section 6.7 with explicit minimum requirements for L03 (KNN+K-Means), L04 (RF+Boosting), L05 (PCA+t-SNE) |
