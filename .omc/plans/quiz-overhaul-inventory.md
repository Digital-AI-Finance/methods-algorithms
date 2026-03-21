# Plan: Quiz Overhaul & JSON Inventory System

**Created:** 2026-03-06
**Type:** Content overhaul + infrastructure
**Complexity:** HIGH (6 quizzes rewritten, inventory schema, dashboard update)

---

## 1. Context

### 1.1 Original Request
Create one canonical 20-question quiz per lecture (L01-L06) at MSc quality, with JSON-based inventory tracking for ongoing management.

### 1.2 Current State
**15 HTML quiz files** exist in `docs/quiz/`, but they are fragmented and inconsistent:

| Lecture | Files | Problem |
|---------|-------|---------|
| L01 | 1 file | 45% L1 recall, ZERO calculation questions, 1/20 finance |
| L02 | 1 file | Decent L3+ but only 1/20 finance |
| L03 | 4 files (knn, kmeans, combined, accessible) | Fragmented; combined is LOW quality; accessible is BEST |
| L04 | 3 files (random_forests, decision_trees, ensemble_methods) | RF was already upgraded (40% L3+, 5/20 finance) |
| L05 | 1 file | 45% L1, ZERO Evaluate, 1/20 finance |
| L06 | 1 file | 40% L1, ZERO Analyze, RL section pure recall, 1/20 finance |

Additionally 3 Moodle XML quizzes exist in `quizzes/` (15 questions each, cross-topic).
Plus 3 overview HTML quizzes in `docs/quiz/` (quiz1_regression, quiz2_classification_ensemble, quiz3_advanced).

### 1.3 Bloom Audit Findings (from `.omc/reports/quiz-bloom-audit.md`)
- Overall L1 (Remember) = 27% -- target for MSc is 10-15%
- Overall L5 (Evaluate) = 5% -- target is 10%+
- Finance application = 10% -- target is 20%+
- L01 has zero Apply questions despite being the most computation-friendly topic
- L06 RL section (Q11-16) is pure recall
- L03 combined quiz is low quality vs standalone/accessible versions

### 1.4 Research: What "Good" Looks Like
The post-upgrade L04 quiz is the quality benchmark:
- Bloom distribution: L1=4, L2=8, L3=2, L4=4, L5=2 (40% at L3+)
- Finance: 5/20 questions with real scenarios (SHAP loan denial, ECOA compliance, fraud detection)
- Calculations: Gini impurity, entropy, information gain with worked solutions
- Each question references specific slide content in its explanation
- "Diagnose the failure" pattern (Q5: low train error + high test error)

---

## 2. Work Objectives

### 2.1 Core Objective
Produce 6 canonical quizzes (one per lecture, 20 questions each) at uniform MSc quality, tracked by a JSON inventory system.

### 2.2 Deliverables

| # | Deliverable | File(s) |
|---|------------|---------|
| D1 | L01 canonical quiz (rewrite) | `docs/quiz/L01_linear_regression.html` |
| D2 | L02 canonical quiz (rewrite) | `docs/quiz/L02_logistic_regression.html` |
| D3 | L03 canonical quiz (rewrite) | `docs/quiz/L03_knn_kmeans.html` |
| D4 | L04 canonical quiz (keep) | `docs/quiz/L04_random_forests.html` (already upgraded) |
| D5 | L05 canonical quiz (rewrite) | `docs/quiz/L05_pca_tsne.html` |
| D6 | L06 canonical quiz (rewrite) | `docs/quiz/L06_embeddings_rl.html` |
| D7 | Quiz inventory JSON | `quizzes/quiz_inventory.json` |
| D8 | Updated manifest.json | `manifest.json` (quiz entries reflect new canonical set) |
| D9 | Updated docs/index.html | `docs/index.html` (link to 6 canonical + 3 overview + deep variants) |

### 2.3 Definition of Done
- [ ] Each of 6 canonical quizzes has exactly 20 questions
- [ ] Each quiz meets Bloom targets: L1 <= 15%, L2 25-30%, L3 25-30%, L4 20-25%, L5 >= 10%
- [ ] Each quiz has >= 4 finance/banking scenario questions (20%+)
- [ ] Each quiz has >= 2 calculation/computation questions
- [ ] Each quiz has >= 1 "diagnose the failure" question
- [ ] Every question explanation references specific slide content
- [ ] KaTeX math renders correctly in all quizzes
- [ ] Quiz inventory JSON is valid and complete
- [ ] manifest.json updated with canonical quiz entries
- [ ] docs/index.html updated with clean quiz navigation
- [ ] All existing non-canonical quizzes preserved (not deleted) but clearly labeled as deep/supplementary

---

## 3. Guardrails

### 3.1 MUST Have
- Exactly 20 questions per quiz (matching current format)
- 4-option MCQ format (A/B/C/D) matching existing template
- Explanation field for every question with slide reference
- Finance scenarios grounded in the course's stated finance cases per topic
- Bloom level metadata per question in the inventory JSON
- Backward compatibility: existing quiz URLs must not break

### 3.2 MUST NOT Have
- No deletion of existing non-canonical quiz files (keep L03_knn.html, L03_kmeans.html, L04_decision_trees.html, L04_ensemble_methods.html as "deep" variants)
- No changes to the quiz HTML template structure (CSS, JS, layout)
- No changes to the Moodle XML quizzes (quizzes/*.xml) -- out of scope
- No changes to the 3 overview quizzes (quiz1_regression.html, quiz2_classification_ensemble.html, quiz3_advanced.html) -- out of scope
- No new question types (keep MCQ only)
- No changes to chart files or slide .tex files

---

## 4. Quiz Disposition Matrix

Decision on what happens to each existing file:

| File | Action | Rationale |
|------|--------|-----------|
| `L01_linear_regression.html` | **REWRITE** | 45% L1, zero calculations, 1 finance question |
| `L02_logistic_regression.html` | **REWRITE** | Good L3+ but only 1 finance, needs rebalancing |
| `L03_knn_kmeans.html` | **REWRITE** | Replaces low-quality combined quiz with new content modeled on accessible version quality |
| `L03_knn_kmeans_accessible.html` | **KEEP as deep variant** | Rename concept: becomes supplementary. No file changes. |
| `L03_knn.html` | **KEEP as deep variant** | Excellent quality standalone (60% L3+). Supplementary. |
| `L03_kmeans.html` | **KEEP as deep variant** | Excellent quality standalone (70% L3+). Supplementary. |
| `L04_random_forests.html` | **KEEP as canonical** | Already upgraded to 40% L3+, 5/20 finance. Minor tune-up only. |
| `L04_decision_trees.html` | **KEEP as deep variant** | Supplementary. |
| `L04_ensemble_methods.html` | **KEEP as deep variant** | Supplementary. |
| `L05_pca_tsne.html` | **REWRITE** | 45% L1, zero Evaluate, 1 finance |
| `L06_embeddings_rl.html` | **REWRITE** | 40% L1, zero Analyze, RL pure recall, 1 finance |
| `quiz1_regression.html` | **KEEP** | Out of scope (overview quiz) |
| `quiz2_classification_ensemble.html` | **KEEP** | Out of scope (overview quiz) |
| `quiz3_advanced.html` | **KEEP** | Out of scope (overview quiz) |
| `quiz_template.html` | **KEEP** | Template for future quizzes |

---

## 5. Per-Lecture Quiz Specifications

### 5.1 Universal Quality Targets

| Metric | Target | Rationale |
|--------|--------|-----------|
| Total questions | 20 | Matches current format, 25-minute quiz |
| L1 Remember | 2-3 (10-15%) | MSc students need minimal rote recall |
| L2 Understand | 5-6 (25-30%) | Conceptual understanding foundation |
| L3 Apply | 5-6 (25-30%) | Calculations, worked examples |
| L4 Analyze | 4-5 (20-25%) | Compare, diagnose, interpret |
| L5 Evaluate | 2-3 (10-15%) | Judge, recommend, critique |
| Finance questions | 4-5 (20-25%) | Course has finance/banking focus |
| Calculation questions | 3-4 (15-20%) | MSc must test quantitative skill |
| "Diagnose failure" | 1-2 | Pattern from L04 benchmark |
| Slide references | 20/20 | Every explanation cites slide content |

### 5.2 L01: Linear Regression (REWRITE)

**Finance case:** House price prediction, factor models (from manifest)
**Slide topics to cover:** OLS derivation, gradient descent, MSE/RMSE/R-squared, residual analysis, regularization (Ridge/Lasso/ElasticNet), bias-variance tradeoff, cross-validation
**Learning objectives:** L01-O1 (derive OLS), L01-O2 (implement GD), L01-O3 (interpret coefficients), L01-O4 (choose regularization)

**Target Bloom distribution:**
| Level | Count | Questions (indicative) |
|-------|-------|----------------------|
| L1 Remember | 2 | OLS formula recall, Ridge vs Lasso penalty form |
| L2 Understand | 6 | Why GD diverges with high LR, R-squared meaning, adjusted R-squared vs R-squared, bias-variance concept, regularization purpose, residual pattern meaning |
| L3 Apply | 6 | Compute MSE from residuals, compute R-squared from SSR/SST, GD update step calculation, predict house price from coefficients, Ridge coefficient shrinkage calculation, cross-validation fold assignment |
| L4 Analyze | 4 | Residual plot diagnosis (heteroscedasticity), learning curve interpretation (overfit vs underfit), compare Ridge vs Lasso coefficient paths, factor model coefficient interpretation for portfolio |
| L5 Evaluate | 2 | Choose between normal equation vs GD for given n/p, recommend regularization method for correlated features in credit risk |

**Finance scenarios (min 4):**
1. House price prediction: interpret coefficients (location, sqft, age) in $ terms
2. Factor model: which market factor contributes most to portfolio variance
3. Credit risk: choose Ridge vs Lasso when features are correlated (income, debt, DTI)
4. Trading strategy: diagnose overfitting from learning curve (in-sample vs out-of-sample returns)

**Key gaps to fix vs current:**
- Add 6 calculation questions (currently ZERO)
- Add 4 finance scenarios (currently 1)
- Drop 7 of 9 L1-recall questions
- Add 2 Evaluate questions

---

### 5.3 L02: Logistic Regression (REWRITE)

**Finance case:** Credit scoring, default prediction (from manifest)
**Slide topics to cover:** Sigmoid function, log-odds/logit, MLE/cross-entropy, decision boundary, confusion matrix, precision/recall/F1, ROC/AUC, PR curve, regularization, class imbalance
**Learning objectives:** L02-O1 (derive from MLE), L02-O2 (implement with GD), L02-O3 (interpret odds ratios), L02-O4 (evaluate with ROC/PR)

**Target Bloom distribution:**
| Level | Count | Questions (indicative) |
|-------|-------|----------------------|
| L1 Remember | 2 | Sigmoid range [0,1], confusion matrix cell definitions |
| L2 Understand | 6 | Why cross-entropy not MSE, logit meaning, precision vs recall tradeoff, AUC=0.5 meaning, softmax for multi-class, regularization effect |
| L3 Apply | 6 | Sigmoid at z=2 calculation, odds ratio from coefficient, cross-entropy loss for given prediction, precision from TP/FP, F1 score computation, threshold selection for given cost |
| L4 Analyze | 4 | Threshold effect on precision/recall for credit scoring, ROC vs PR curve for imbalanced fraud data, coefficient sign interpretation for default prediction, compare two models via ROC |
| L5 Evaluate | 2 | Choose threshold for bank (cost of FP vs FN), recommend PR vs ROC for 1% default rate dataset |

**Finance scenarios (min 4):**
1. Credit scoring: interpret odds ratio for income coefficient (each $10k increase -> X times less likely to default)
2. Fraud detection: choose precision vs recall emphasis (cost of blocking legitimate vs missing fraud)
3. Default prediction: analyze confusion matrix (bank loses $50k per FN, $200 per FP -- choose threshold)
4. Loan approval: two models compared on ROC -- which to deploy and why

**Key gaps to fix vs current:**
- Add 3 more finance scenarios (currently 1)
- Keep strong L3 Apply base (current strength)
- Add 1 more Evaluate question
- Reduce L1 from 7 to 2

---

### 5.4 L03: KNN & K-Means (REWRITE)

**Finance case:** Customer segmentation, anomaly detection (from manifest)
**Slide topics to cover:** Distance metrics (Euclidean, Manhattan, Cosine, Mahalanobis), KNN classification, K selection, curse of dimensionality, K-Means algorithm, elbow method, silhouette score, K-Means++ initialization, Voronoi cells, DBSCAN comparison
**Learning objectives:** L03-O1 (distance metrics), L03-O2 (implement KNN/K-Means), L03-O3 (analyze cluster quality), L03-O4 (select optimal K)

**Source material:** Draw BEST questions from accessible version; draw depth from standalone KNN/K-Means quizzes. Write new finance scenarios.

**Target Bloom distribution:**
| Level | Count | Questions (indicative) |
|-------|-------|----------------------|
| L1 Remember | 2 | KNN lazy learner definition, K-Means two-step description |
| L2 Understand | 5 | Curse of dimensionality effect, why feature scaling matters, K-Means convergence guarantee, silhouette score range, K-Means++ vs random init |
| L3 Apply | 6 | Euclidean distance calculation (2 features), KNN majority vote worked example, K-Means centroid update step, silhouette score interpretation for given cluster, Manhattan distance calculation, elbow plot K selection |
| L4 Analyze | 5 | K=1 vs K=15 boundary tradeoff, empty cluster diagnosis, non-convex shape failure of K-Means, imbalanced fraud detection 99% accuracy trap, compare distance metrics for text vs numeric |
| L5 Evaluate | 2 | Choose K-Means vs DBSCAN for given data shape, recommend supervised vs unsupervised approach for customer segmentation |

**Finance scenarios (min 4):**
1. Customer segmentation: RFM features, standardize before K-Means, interpret 3 clusters
2. Fraud detection: KNN with imbalanced classes (99% accuracy trap)
3. Credit card transactions: choose distance metric for mixed features
4. Bank branch clustering: interpret silhouette score, recommend K
5. Anomaly detection: compare KNN distance vs K-Means centroid distance for flagging outliers

**Key gaps to fix vs current combined quiz:**
- Raise from 20% L3+ to 55%+
- Add 4+ finance scenarios (currently 2 in combined)
- Add calculation questions (distance, centroid update)
- Add Evaluate (currently ZERO in combined)

---

### 5.5 L04: Random Forests (KEEP -- minor tune-up)

**Status:** Already upgraded. 40% L3+, 5/20 finance. Best quiz in the set.

**Tune-up only (if any):**
- Verify all 20 explanations reference specific slides
- Check Bloom classification accuracy
- No structural changes needed

**Current distribution:** L1=4, L2=8, L3=2, L4=4, L5=2
**Finance coverage:** 5/20 (SHAP loan denial, ECOA compliance, fraud detection, class imbalance, feature importance for credit)

**Action:** Mark as canonical. Add to inventory JSON. No rewrite.

> **Critic note:** L04's Bloom distribution (L1=20%, L3=10%) does not match the universal targets (L1<=15%, L3=25-30%), but is accepted as-is because it was the subject of a separate dedicated upgrade and is the quality benchmark for finance coverage (5/20 = 25%). MCQ format cannot meaningfully test Bloom L6 (Create).

---

### 5.6 L05: PCA & t-SNE (REWRITE)

**Finance case:** Portfolio risk decomposition, visualization (from manifest)
**Slide topics to cover:** Covariance matrix, eigendecomposition, scree plot, explained variance, reconstruction error, Kaiser criterion, centering/scaling, t-SNE perplexity, KL divergence, crowding problem, PCA vs t-SNE comparison, Swiss roll example
**Learning objectives:** L05-O1 (derive PCA from eigenvalues), L05-O2 (apply PCA/t-SNE), L05-O3 (interpret PCs in finance), L05-O4 (choose PCA vs t-SNE)

**Target Bloom distribution:**
| Level | Count | Questions (indicative) |
|-------|-------|----------------------|
| L1 Remember | 2 | PCA maximizes variance along PCs, t-SNE preserves local structure |
| L2 Understand | 5 | Why center data, eigenvalue = variance explained, scree plot elbow meaning, crowding problem in t-SNE, KL divergence as loss |
| L3 Apply | 6 | Compute explained variance ratio from eigenvalues, determine number of PCs from scree plot, compute reconstruction error for k PCs, Kaiser criterion application, project data point onto PC1, perplexity parameter selection |
| L4 Analyze | 4 | Interpret PC1 as "market factor" in portfolio, compare PCA vs t-SNE on Swiss roll, diagnose t-SNE artifacts (perplexity too low vs too high), analyze scree plot with no clear elbow |
| L5 Evaluate | 3 | Choose PCA vs t-SNE for portfolio factor analysis, recommend dimensionality reduction for 1000-feature dataset, judge whether t-SNE cluster separations are real or artifact |

**Finance scenarios (min 4):**
1. Portfolio risk: PC1 as market factor, PC2 as sector rotation -- interpret loadings
2. Stock return analysis: choose number of PCs to explain 80% variance
3. Customer visualization: t-SNE reveals 4 natural segments in transaction data -- are clusters real?
4. Risk model: 50 correlated risk factors -> PCA for feature reduction before regression
5. Fund classification: visualize fund embeddings with t-SNE, choose perplexity

**Key gaps to fix vs current:**
- Drop L1 from 9 to 2 (45% -> 10%)
- Add 3 Evaluate questions (currently ZERO)
- Add 4+ finance scenarios (currently 1)
- Add 4 more calculation questions
- Add "diagnose the artifact" question for t-SNE

---

### 5.7 L06: Embeddings & RL (REWRITE)

**Finance case:** Sentiment analysis, trading strategies (from manifest)
**Slide topics to cover:** One-hot vs dense embeddings, Word2Vec (Skip-gram, CBOW), cosine similarity, analogy arithmetic, negative sampling, FastText, FinBERT; MDP, policy, Q-function, Bellman equation, Q-learning update, epsilon-greedy, discount factor, DQN
**Learning objectives:** L06-O1 (explain embeddings), L06-O2 (implement Q-learning), L06-O3 (analyze embedding spaces), L06-O4 (design reward functions)

**Target Bloom distribution:**
| Level | Count | Questions (indicative) |
|-------|-------|----------------------|
| L1 Remember | 2 | MDP tuple components, Skip-gram prediction direction |
| L2 Understand | 5 | Why dense > one-hot, distributional hypothesis, Bellman equation meaning, exploration-exploitation tradeoff, discount factor effect on horizon |
| L3 Apply | 6 | Cosine similarity calculation, word analogy vector arithmetic, Q-table update for one step, epsilon-greedy action selection, negative sampling probability, reward signal calculation |
| L4 Analyze | 4 | Compare CBOW vs Skip-gram for rare words, analyze Q-table convergence (gamma too low), interpret embedding space clusters for financial terms, diagnose reward shaping problem |
| L5 Evaluate | 3 | Choose FinBERT vs general BERT for sentiment, design reward function for trading agent, recommend embedding approach for small financial corpus |

**Finance scenarios (min 5, given dual-topic breadth):**
1. Sentiment analysis: cosine similarity between "bullish" and "optimistic" embeddings
2. Financial NLP: FinBERT vs BERT for earnings call sentiment
3. Trading agent: design reward function (Sharpe ratio vs raw return vs drawdown penalty)
4. Portfolio rebalancing: MDP formulation (states = market regimes, actions = allocations)
5. Credit document analysis: word embeddings for "default", "delinquent", "bankruptcy" -- interpret clusters

**Key gaps to fix vs current:**
- Drop L1 from 8 to 2 (40% -> 10%)
- Add 4 Analyze questions (currently ZERO)
- Add 2 more Evaluate questions
- Completely rewrite RL section (Q11-16 was pure recall)
- Add 4 more finance scenarios (currently 1)
- Add calculation questions for cosine similarity and Q-table update

---

## 6. JSON Inventory Schema Design

### 6.1 File Location
`quizzes/quiz_inventory.json`

### 6.2 Schema

```json
{
  "$schema": "quiz_inventory_v1",
  "version": "1.0.0",
  "updated": "2026-03-XX",
  "quizzes": [
    {
      "id": "L01_canonical",
      "lecture": "L01",
      "title": "Linear Regression",
      "type": "canonical",
      "file": "docs/quiz/L01_linear_regression.html",
      "questions_count": 20,
      "duration_minutes": 25,
      "bloom_distribution": {
        "L1_remember": 2,
        "L2_understand": 6,
        "L3_apply": 6,
        "L4_analyze": 4,
        "L5_evaluate": 2
      },
      "finance_questions": 4,
      "calculation_questions": 6,
      "diagnose_failure_questions": 1,
      "topics_covered": [
        "OLS", "gradient_descent", "MSE", "R_squared",
        "regularization", "bias_variance", "cross_validation"
      ],
      "learning_objectives_tested": ["L01-O1", "L01-O2", "L01-O3", "L01-O4"],
      "quality_metrics": {
        "l3_plus_percent": 60,
        "finance_percent": 20,
        "slide_reference_coverage": 100
      },
      "status": "pending",
      "last_audit": null,
      "questions": [
        {
          "qid": "L01-Q01",
          "bloom_level": "L3_apply",
          "topic": "MSE_calculation",
          "finance_context": false,
          "slide_reference": "L01_overview, slide 12"
        }
      ]
    }
  ],
  "supplementary_quizzes": [
    {
      "id": "L03_knn_deep",
      "lecture": "L03",
      "title": "KNN (Deep Dive)",
      "type": "supplementary",
      "file": "docs/quiz/L03_knn.html",
      "questions_count": 20,
      "status": "complete"
    }
  ],
  "overview_quizzes": [
    {
      "id": "quiz1_overview",
      "lectures": ["L01", "L02"],
      "title": "Regression Methods",
      "type": "overview",
      "file": "docs/quiz/quiz1_regression.html",
      "questions_count": 15,
      "status": "complete"
    }
  ],
  "moodle_quizzes": [
    {
      "id": "moodle_quiz1",
      "lectures": ["L01", "L02"],
      "title": "Quiz 1: Regression Methods",
      "type": "moodle",
      "file": "quizzes/quiz1_topics_1_2.xml",
      "questions_count": 15,
      "status": "complete"
    }
  ]
}
```

### 6.3 Schema Design Decisions

1. **Separate arrays by quiz type** (canonical, supplementary, overview, moodle) for clarity
2. **Per-question metadata** in canonical quizzes only (supplementary just get summary counts)
3. **`bloom_distribution` object** enables automated audit scripts to verify targets
4. **`quality_metrics` summary** enables dashboard display without parsing all questions
5. **`slide_reference` per question** enforces the "every explanation cites slides" rule
6. **`status` field** uses same vocabulary as manifest.json: `pending`, `in_progress`, `complete`
7. **`last_audit` date** tracks when the quiz was last reviewed against Bloom targets

### 6.4 Integration with manifest.json

Update the existing `quizzes` array in `manifest.json` to:
- Point canonical quiz entries to `docs/quiz/L0X_*.html` (already done for most)
- Add `"type": "canonical"` field to distinguish from overview/moodle quizzes
- Add `"inventory_ref": "L01_canonical"` to link back to the detailed inventory
- Remove or mark the duplicate/fragmented L03 entries (keep only the canonical one as primary)

---

## 7. Task Flow and Dependencies

```
PHASE 1: Infrastructure (no quiz content changes)
  T1: Create quiz_inventory.json schema file
  T2: Update manifest.json quiz entries
  (T1 and T2 are independent)

PHASE 2: Quiz Rewrites (5 quizzes, sequential within each, parallel across)
  T3: Rewrite L01 quiz
  T4: Rewrite L02 quiz
  T5: Rewrite L03 quiz
  T6: Rewrite L05 quiz
  T7: Rewrite L06 quiz
  T8: Verify L04 quiz (minor tune-up only)
  (T3-T8 are independent of each other)
  (T3-T8 depend on T1 for inventory template)

PHASE 3: Integration
  T9: Populate quiz_inventory.json with all 6 canonical quizzes
  T10: Update docs/index.html quiz section
  T11: Update manifest.json with final quiz metadata
  (T9 depends on T3-T8)
  (T10 depends on T9)
  (T11 depends on T9)

PHASE 4: Verification
  T12: Bloom audit of all 6 canonical quizzes
  T13: KaTeX rendering test (open each HTML in browser)
  T14: Link integrity check (all quiz URLs work from index.html)
  (T12-T14 depend on T10)
```

---

## 8. Detailed TODOs

### T1: Create quiz_inventory.json
**File:** `quizzes/quiz_inventory.json`
**Action:** Create the JSON file with the schema from Section 6.2. Populate supplementary, overview, and moodle arrays immediately (those quizzes exist and won't change). Leave canonical array with skeleton entries (status: "pending").
**Acceptance:** Valid JSON, all 15 per-topic/overview quiz HTML files referenced (excluding quiz_template.html), schema matches Section 6.2.

### T2: Update manifest.json quiz entries
**File:** `manifest.json`
**Action:**
- Add `"type"` field to each quiz entry ("canonical", "supplementary", "overview", "moodle")
- Add `"inventory_ref"` field linking to quiz_inventory.json ID
- Ensure each L0X has exactly ONE canonical entry (remove duplicate L03 entries, keep L03 canonical pointing to `L03_knn_kmeans.html`)
- Mark supplementary quizzes as `"type": "supplementary"`
- ADD manifest entries for currently-unlisted supplementary quizzes: L03_knn.html, L03_kmeans.html, L03_knn_kmeans_accessible.html, L04_decision_trees.html, L04_ensemble_methods.html
**Acceptance:** Valid JSON, no duplicate canonical entries per lecture, all quiz files referenced (canonical + supplementary + overview + moodle).

### T3: Rewrite L01 Linear Regression Quiz
**File:** `docs/quiz/L01_linear_regression.html`
**Action:** Replace the `quizData.questions` array with 20 new questions matching Section 5.2 spec. Keep all HTML/CSS/JS unchanged. Only the JSON questions array changes.
**Slide sources to reference:**
- `slides/L01_Introduction_Linear_Regression/L01_overview.tex`
- `slides/L01_Introduction_Linear_Regression/L01_deepdive.tex`
**Acceptance criteria:**
- [ ] 20 questions, 4 options each
- [ ] Bloom: L1<=3, L2=6, L3=6, L4=4, L5=2 (allow +/-1)
- [ ] Finance: >=4 questions with house price / factor model / credit risk scenarios
- [ ] Calculations: >=4 (MSE, R-squared, GD step, Ridge shrinkage)
- [ ] 1 "diagnose the failure" question (learning curve interpretation)
- [ ] Every explanation references specific slide

### T4: Rewrite L02 Logistic Regression Quiz
**File:** `docs/quiz/L02_logistic_regression.html`
**Action:** Replace `quizData.questions` array with 20 new questions per Section 5.3.
**Slide sources:**
- `slides/L02_Logistic_Regression/L02_overview.tex`
- `slides/L02_Logistic_Regression/L02_deepdive.tex`
**Acceptance criteria:**
- [ ] 20 questions, 4 options each
- [ ] Bloom: L1<=3, L2=6, L3=6, L4=4, L5=2 (allow +/-1)
- [ ] Finance: >=4 (credit scoring, fraud detection, default prediction, loan approval)
- [ ] Calculations: >=4 (sigmoid, odds ratio, cross-entropy, precision/F1)
- [ ] 1 "diagnose the failure" question (threshold choice impact)
- [ ] Every explanation references specific slide

### T5: Rewrite L03 KNN & K-Means Quiz
**File:** `docs/quiz/L03_knn_kmeans.html`
**Action:** Replace `quizData.questions` array with 20 new questions per Section 5.4. Draw inspiration from accessible and standalone versions but write fresh content.
**Slide sources:**
- `slides/L03_KNN_KMeans/L03_overview.tex`
- `slides/L03_KNN_KMeans/L03_deepdive.tex`
**Acceptance criteria:**
- [ ] 20 questions, 4 options each
- [ ] Bloom: L1<=3, L2=5, L3=6, L4=5, L5=2 (allow +/-1)
- [ ] Finance: >=4 (customer segmentation, fraud, branch clustering, anomaly detection)
- [ ] Calculations: >=3 (Euclidean distance, centroid update, silhouette interpretation)
- [ ] 1 "diagnose the failure" question (99% accuracy trap or non-convex failure)
- [ ] Every explanation references specific slide
- [ ] Balanced KNN/K-Means split: 10 questions each (+/-2)

### T6: Rewrite L05 PCA & t-SNE Quiz
**File:** `docs/quiz/L05_pca_tsne.html`
**Action:** Replace `quizData.questions` array with 20 new questions per Section 5.6.
**Slide sources:**
- `slides/L05_PCA_tSNE/L05_overview.tex`
- `slides/L05_PCA_tSNE/L05_deepdive.tex`
**Acceptance criteria:**
- [ ] 20 questions, 4 options each
- [ ] Bloom: L1<=3, L2=5, L3=6, L4=4, L5=3 (allow +/-1)
- [ ] Finance: >=4 (portfolio PC interpretation, stock variance, customer visualization, risk model)
- [ ] Calculations: >=3 (explained variance ratio, Kaiser criterion, reconstruction error)
- [ ] 1 "diagnose the artifact" question (t-SNE perplexity artifacts)
- [ ] Every explanation references specific slide
- [ ] Balanced PCA/t-SNE split: ~12 PCA / 8 t-SNE (+/-2)

### T7: Rewrite L06 Embeddings & RL Quiz
**File:** `docs/quiz/L06_embeddings_rl.html`
**Action:** Replace `quizData.questions` array with 20 new questions per Section 5.7.
**Slide sources:**
- `slides/L06_Embeddings_RL/L06_overview.tex`
- `slides/L06_Embeddings_RL/L06_deepdive.tex`
**Acceptance criteria:**
- [ ] 20 questions, 4 options each
- [ ] Bloom: L1<=3, L2=5, L3=6, L4=4, L5=3 (allow +/-1)
- [ ] Finance: >=5 (sentiment, FinBERT, trading agent reward, MDP portfolio, credit docs)
- [ ] Calculations: >=3 (cosine similarity, Q-table update, epsilon-greedy selection)
- [ ] 1 "diagnose the failure" question (reward shaping or gamma problem)
- [ ] Every explanation references specific slide
- [ ] Balanced Embeddings/RL split: 10 each (+/-2)
- [ ] RL questions MUST NOT be pure recall (max 1 L1 for RL section)

### T8: Verify L04 Random Forests Quiz
**File:** `docs/quiz/L04_random_forests.html`
**Action:** Read all 20 questions. Verify:
- All explanations reference specific slides
- Bloom classifications are accurate
- Finance scenarios are factually correct
- KaTeX renders (no broken formulas)
**Acceptance:** Verification report with any minor corrections applied. If 0 issues, mark as canonical-verified.

### T9: Populate quiz_inventory.json
**File:** `quizzes/quiz_inventory.json`
**Action:** Fill in all canonical quiz entries with per-question metadata from T3-T8.
**Acceptance:** All 120 questions (6 x 20) have qid, bloom_level, topic, finance_context, slide_reference. All quality_metrics computed. All statuses = "complete".

### T10: Update docs/index.html
**File:** `docs/index.html`
**Action:**
- Reorganize quiz section: "Canonical Quizzes (6)" as primary section, "Deep Dive Quizzes" as secondary
- Update question counts in hero stats
- Remove L03_knn_kmeans_accessible from main listing (it becomes supplementary)
- Ensure all 6 canonical quizzes are prominently linked with consistent styling
- Keep deep/supplementary quizzes visible but visually secondary
**Acceptance:** All quiz links resolve, layout is clean, canonical quizzes are visually primary.

### T11: Update manifest.json final
**File:** `manifest.json`
**Action:** Final pass: update all quiz statuses, ensure `inventory_ref` fields are correct, update `course.updated` date.
**Acceptance:** Valid JSON, all statuses reflect completion.

### T12: Bloom Audit
**Action:** For each of 6 canonical quizzes, verify Bloom distribution against targets from Section 5.1.
**Method:** Count L1-L5 per quiz, compute percentages, flag any quiz outside tolerance (+/-1 per level).
**Acceptance:** All 6 quizzes within tolerance. Summary table produced.

### T13: KaTeX Rendering Test
**Action:** Open each of 6 canonical quiz HTML files in browser. Verify:
- All math renders (no raw LaTeX visible)
- Subscripts, superscripts, fractions display correctly
- Greek letters render
**Acceptance:** Zero rendering errors across all 6 quizzes.

### T14: Link Integrity Check
**Action:** From `docs/index.html`, click every quiz link. Verify:
- All 6 canonical quiz links work
- All supplementary quiz links work
- All overview quiz links work
- "Dashboard" link from each quiz returns to index.html
**Acceptance:** Zero broken links.

---

## 9. Commit Strategy

| Commit | Scope | Message |
|--------|-------|---------|
| C1 | T1, T2 | `Add quiz inventory JSON schema and update manifest quiz entries` |
| C2 | T3 | `Rewrite L01 linear regression quiz to MSc Bloom targets` |
| C3 | T4 | `Rewrite L02 logistic regression quiz to MSc Bloom targets` |
| C4 | T5 | `Rewrite L03 KNN/K-Means quiz to MSc Bloom targets` |
| C5 | T6 | `Rewrite L05 PCA/t-SNE quiz to MSc Bloom targets` |
| C6 | T7 | `Rewrite L06 embeddings/RL quiz to MSc Bloom targets` |
| C7 | T8, T9, T10, T11 | `Complete quiz inventory, verify L04, update dashboard` |

---

## 10. Success Criteria (Final Verification)

| Criterion | Measurement | Pass Threshold |
|-----------|-------------|----------------|
| Bloom quality | L3+ percentage across all 6 quizzes | >= 55% average (vs current 30%) |
| Finance coverage | Finance questions across all 6 quizzes | >= 20% per quiz (vs current 10%) |
| L1 reduction | L1 Remember across all 6 quizzes | <= 15% average (vs current 27%) |
| Evaluate presence | L5 questions across all 6 quizzes | >= 2 per quiz (vs current 0-1) |
| Calculation presence | Apply/calculation questions per quiz | >= 3 per quiz (vs current 0-6 varying) |
| Inventory completeness | quiz_inventory.json entries | 120 questions with full metadata |
| Rendering | KaTeX in all quizzes | Zero rendering errors |
| Links | All quiz URLs from index.html | Zero broken links |

---

## 11. Execution Notes

### Parallelization Opportunity
T3-T8 (the 5 rewrites + 1 verify) are fully independent and can run in parallel. Each touches exactly one HTML file with no shared state. This is the natural parallelism boundary.

However, per user preference for token efficiency, sequential execution by a single executor reading slide sources as it goes is recommended. The executor should:
1. Read the relevant overview.tex and deepdive.tex for the lecture
2. Draft 20 questions matching the spec
3. Replace only the `quizData.questions` array in the HTML file
4. Verify question count and option format

### Question Writing Guidelines for Executor
- **Distractors must be plausible** -- each wrong answer should represent a common misconception
- **Explanations must teach** -- not just "A is correct because A" but explain WHY other options are wrong
- **Finance scenarios must be specific** -- use dollar amounts, percentages, named financial instruments
- **Calculations must show work** -- the explanation should walk through the arithmetic step by step
- **Slide references format:** "As shown in L01 overview (OLS derivation slide): ..."
- **"Diagnose the failure" format:** Present a scenario with symptoms, ask student to identify the root cause
- **Question JSON format (for reference):**
  ```json
  {
      "id": 1,
      "question": "A bank's linear regression predicts loan defaults with training RMSE = $2,100 but test RMSE = $8,400. What does this gap indicate?",
      "options": {
          "A": "The model is underfitting -- it needs more features",
          "B": "The model is overfitting -- it memorized training noise",
          "C": "The test set has more outliers than training",
          "D": "RMSE is not a valid metric for this problem"
      },
      "correct": "B",
      "explanation": "As shown in L01 overview (bias-variance tradeoff slide): a large gap between training and test error is the hallmark of overfitting. The model has low bias but high variance."
  }
  ```

### File Touch Summary
| File | Action |
|------|--------|
| `quizzes/quiz_inventory.json` | CREATE |
| `manifest.json` | EDIT (quiz section only) |
| `docs/quiz/L01_linear_regression.html` | EDIT (quizData only) |
| `docs/quiz/L02_logistic_regression.html` | EDIT (quizData only) |
| `docs/quiz/L03_knn_kmeans.html` | EDIT (quizData only) |
| `docs/quiz/L05_pca_tsne.html` | EDIT (quizData only) |
| `docs/quiz/L06_embeddings_rl.html` | EDIT (quizData only) |
| `docs/quiz/L04_random_forests.html` | READ-ONLY (verify) |
| `docs/index.html` | EDIT (quiz section layout) |
| No other files touched | |
