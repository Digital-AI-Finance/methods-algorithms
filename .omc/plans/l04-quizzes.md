# Plan: L04 Topic-Split Quizzes — 20 DT + 20 RF/Boosting + GH Pages

## Task
Create two topic-specific deep quizzes for L04, following the L03 pattern (L03 has combined + KNN-deep + K-Means-deep). Push to GH Pages.

## Current State

**Existing L04 quiz:**
- `docs/quiz/L04_random_forests.html` — 20 questions (4 DT-specific, 16 RF-specific)
- Title: "Quiz 4: Random Forests"
- Linked in index.html line 379

**L03 pattern (reference):**
- `L03_knn_kmeans.html` — combined (20q)
- `L03_knn_kmeans_accessible.html` — accessible (20q)
- `L03_knn.html` — KNN deep (20q)
- `L03_kmeans.html` — K-Means deep (20q)

**Gap:** L04 has only 1 combined quiz. Missing DT-deep and RF/boosting-deep topic-split quizzes.

**Scope note:** L03 also has an accessible quiz variant (`L03_knn_kmeans_accessible.html`). An L04 accessible quiz is OUT OF SCOPE for this plan — the user's request focuses on topic-split deep quizzes. Accessible variant can be added later if needed.

## Deliverables

1. **`docs/quiz/L04_decision_trees.html`** — 20 DT-specific deep questions (NEW)
2. **`docs/quiz/L04_ensemble_methods.html`** — 20 RF + boosting deep questions (NEW)
3. **`docs/index.html`** — Updated hero stats, sidebar nav, quiz cards
4. **Git commit + push** to deploy to GH Pages

---

## Part 1: DT Deep Quiz (20 questions)

### Source Content (from L04_dt_full.tex, L04_dt_mini.tex, L04_deepdive.tex DT sections)

| # | Topic | Source |
|---|-------|--------|
| 1 | What is a decision tree (plain English definition) | dt_full:190, dt_mini:194 |
| 2 | Gini SPLIT comparison: which of two splits produces lower weighted Gini (NOT single-node calc like existing Q1) | dt_full:315, dt_mini:255 |
| 3 | Gini worked example with 3+ classes (multi-class, NOT binary like existing Q1) | dt_full:346, chart 08 |
| 4 | Entropy: compare entropy of two different distributions (NOT 50/50 calc like existing Q2) | dt_full:380 |
| 5 | Information gain: compare two candidate splits and pick the best (NOT simple subtraction like existing Q3) | dt_full:410 |
| 6 | Gini vs entropy: when they disagree, practical difference | dt_full:380, chart 11 |
| 7 | Feature space partitioning: axis-aligned splits only | dt_full:449, chart 10 |
| 8 | Non-linear separability: XOR pattern requires multiple splits | dt_full:267, chart 12 |
| 9 | CART recursive partitioning: predict NEXT split from pseudocode (NOT definition like existing Q4) | dt_full:475, deepdive:CART |
| 10 | Stopping rules: max_depth, min_samples_split, min_samples_leaf | dt_full:503 |
| 11 | Tree interpretation: path from root to leaf = decision rule | dt_full:536 |
| 12 | Feature importance (MDI) from a single tree | dt_full:571 |
| 13 | Overfitting: max_depth=None memorizes training data | dt_full:611, dt_mini:284 |
| 14 | Training vs test accuracy gap as depth increases | dt_full:649, chart 09 |
| 15 | Pruning: pre-pruning (early stopping) vs post-pruning (cost-complexity) | deepdive:pruning |
| 16 | Regression trees: MSE split criterion with worked example | dt_full:676, deepdive:197 |
| 17 | DT advantages: interpretability, no scaling, handles mixed types | dt_full:715 |
| 18 | DT disadvantages: instability, axis-aligned bias, greedy | dt_full:715 |
| 19 | DT vs logistic regression: when to use which | dt_full:745 |
| 20 | Regulatory interpretability: ECOA adverse action and DT transparency | dt_mini:358, dt_full:745 |

### Question Design Rules
- Every question tests reasoning ("What would happen if..."), not memorization
- At least 4 questions involve numerical calculation (Gini, entropy, IG, MSE)
- Distractors are plausible common misconceptions
- Explanations cite specific slide concepts and show arithmetic
- KaTeX for all math formulas
- Bloom's taxonomy level 3-5 (Apply, Analyze, Evaluate)
- Zero overlap with existing L04_random_forests.html questions. Existing Q1-Q4 cover: Q1=single-node Gini calc (60/40), Q2=single-node entropy (50/50=1.0), Q3=simple IG subtraction (0.9-0.4=0.5), Q4=recursive partitioning definition. New DT questions must test HIGHER Bloom levels (comparison, evaluation, application) on these same concepts, NOT repeat calculations.

---

## Part 2: RF + Boosting Deep Quiz (20 questions)

### Source Content (from L04_rf_full.tex, L04_rf_mini.tex, L04_deepdive.tex RF+boosting sections)

| # | Topic | Source |
|---|-------|--------|
| 1 | Bootstrap sampling: sampling with replacement, 63.2% unique samples | deepdive:12-14, rf_full:415 |
| 2 | Bagging: why averaging reduces variance (Law of Large Numbers) | deepdive:12, rf_full:bagging |
| 3 | OOB error: why ~36.8% samples are left out, used as validation | deepdive:28-29, rf_full:447 |
| 4 | Two sources of randomness in RF: bootstrap + feature subsetting | rf_full:11, rf_mini:4-5 |
| 5 | sqrt(p) rule for classification, p/3 for regression | deepdive:15, rf_full:classification |
| 6 | Variance formula: ρσ² + (1-ρ)/B·σ² worked example | deepdive:13-14, rf_full:8 |
| 7 | Effect of max_features on tree correlation ρ | deepdive:17-19, rf_full:hyperparams |
| 8 | When adding more trees stops helping (ρσ² floor) | deepdive:variance proof |
| 9 | RF pseudocode: step-by-step algorithm | deepdive:16, rf_full:15 |
| 10 | MDI vs permutation importance: bias toward high-cardinality | rf_full:16-17 |
| 11 | SHAP values: per-prediction explanation for regulatory compliance | deepdive:24, rf_full:18 |
| 12 | AdaBoost: sequential training, α_t = ½ ln((1-ε)/ε) worked example | deepdive:31, rf_full:20 |
| 13 | AdaBoost sample weight update: upweight misclassified | deepdive:AdaBoost |
| 14 | Gradient boosting: fitting pseudo-residuals, shrinkage/learning rate | deepdive:32, rf_full:21 |
| 15 | XGBoost: Taylor expansion, regularization term Ω | deepdive:33, rf_full:22 |
| 16 | XGBoost split gain formula: worked example | deepdive:738 |
| 17 | Boosting vs bagging: sequential vs parallel, variance vs bias | deepdive:30, overview:19-20 |
| 18 | RF hyperparameters: n_estimators, max_depth, max_features tuning | deepdive:17-19 |
| 19 | Class imbalance: class_weight='balanced', SMOTE timing | rf_full:25-26 |
| 20 | RF limitations: cannot extrapolate, memory-heavy, less interpretable | rf_full:advantages/limitations |

### Question Design Rules
- Same rules as DT quiz above
- At least 3 questions involve worked numerical examples (variance formula, AdaBoost α, XGBoost gain)
- Questions on boosting test conceptual understanding, not just formula recall
- Zero overlap with existing L04_random_forests.html questions AND zero overlap with DT quiz

---

## Part 3: index.html Updates

### 3A. Hero Stats
Current stats (from last deployment):
- PDFs: 31
- Quiz Questions: needs counting

Count ALL quiz questions:
- L01 (20) + L02 (20) + L03 combined (20) + L03 accessible (20) + L03 KNN (20) + L03 K-Means (20) + L04 combined (20) + L05 (20) + L06 (20) = 180 per-lesson
- Q1 (15) + Q2 (15) + Q3 (15) = 45 cross-topic
- Total before: 225

After adding 2 new quizzes (+40):
- Per-lesson: 180 → 220
- Total: 225 → 265

Update hero stat for Quiz Questions: **265**

### 3B. Sidebar Navigation
After line 110 (`L04 Random Forests` entry), add:
```html
<li><a href="#per-lesson-quizzes">L04 Decision Trees (Deep)</a></li>
<li><a href="#per-lesson-quizzes">L04 Ensemble Methods (Deep)</a></li>
```

### 3C. Per-Lesson Quizzes Section
After the existing L04_random_forests.html card (line 379), add:
```html
<a class="lcard" href="quiz/L04_decision_trees.html" style="border-left:3px solid #FF7F0E;background:linear-gradient(135deg,#f5f3ff,#ede9fe)"><span class="lcard-num" style="background:#8b5cf6;color:white">L04</span><span class="lcard-title">Decision Trees (Deep)</span><div style="font-size:9px;color:#7c3aed;margin-top:4px;font-weight:600">20 questions</div></a>
<a class="lcard" href="quiz/L04_ensemble_methods.html" style="border-left:3px solid #FF7F0E;background:linear-gradient(135deg,#f5f3ff,#ede9fe)"><span class="lcard-num" style="background:#8b5cf6;color:white">L04</span><span class="lcard-title">Ensemble Methods (Deep)</span><div style="font-size:9px;color:#7c3aed;margin-top:4px;font-weight:600">20 questions</div></a>
```

### 3D. Per-Lesson Quizzes Section Header
Update question count: `Per-Lesson Quizzes (180 questions)` → `Per-Lesson Quizzes (220 questions)` (180 current + 40 new).

---

## Part 4: HTML Structure

Both quiz files copy HTML/CSS/JS verbatim from `docs/quiz/L04_random_forests.html`:
- **Same**: CSS variables, styles, KaTeX loading, `waitForKaTeX(renderMath)` pattern, three-column grid, results card, `initQuiz()` / `renderQuestions()` / `handleAnswer()` JS
- **Changed per file**:
  - `<title>`: "Quiz 4: Decision Trees | Methods & Algorithms" / "Quiz 4: Ensemble Methods | Methods & Algorithms"
  - `.nav-title`: "Quiz 4: Decision Trees" / "Quiz 4: Ensemble Methods"
  - `.quiz-title`: same
  - `quizData.questions`: 20 new questions (JSON array)
  - Progress badge: `0/20`

**KaTeX rendering**: `renderMath()` targets `.q-text`, `.option-text`, `.feedback` elements (NOT `document.body`). `waitForKaTeX(renderMath)` called at end of `<body>`. Copy this pattern exactly from existing file.

---

## Part 5: Git & Deployment

1. `git add docs/quiz/L04_decision_trees.html docs/quiz/L04_ensemble_methods.html docs/index.html`
2. `git commit -m "Add L04 DT and ensemble deep quizzes, update GH Pages"`
3. `git push origin master`

---

## Acceptance Criteria

1. `docs/quiz/L04_decision_trees.html` exists with exactly 20 questions
2. `docs/quiz/L04_ensemble_methods.html` exists with exactly 20 questions
3. All 20 DT questions reference DT content from dt_full, dt_mini, deepdive DT sections
4. All 20 ensemble questions reference RF/boosting content from rf_full, rf_mini, deepdive RF/boosting sections
5. Zero question overlap between the two new quizzes
6. Zero question overlap with existing `L04_random_forests.html` (20 questions)
7. At least 4 calculation questions per quiz (Gini, entropy, IG, MSE / variance, AdaBoost α, XGBoost gain)
8. KaTeX renders correctly (waitForKaTeX pattern, renderMath on specific elements)
9. `docs/index.html` hero stat updated: 265 Quiz Questions
10. `docs/index.html` has quiz cards for both new quizzes
11. `docs/index.html` sidebar has entries for both new quizzes
12. All changes committed and pushed to master
13. No broken links in index.html

---

PLAN_READY: .omc/plans/l04-quizzes.md
