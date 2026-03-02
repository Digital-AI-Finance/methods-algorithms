# Work Plan: L04 Random Forests -- Mini-Lecture + Full Lecture + GH Pages

## Context

### Original Request
Create two standalone Beamer lectures on Random Forests (L04):
1. A 10-slide mini-lecture (`L04_rf_mini.tex`) following the interleaved arc WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT
2. A full-length technical lecture (`L04_rf_full.tex`) with ~31 frames, expanded arc, external Python charts, MSc-level depth
3. GitHub Pages: add both PDFs as download cards under L04 section in `docs/index.html`

### Research Findings

**Preamble source (EXACT COPY required):** Lines 1-99 of `slides/L03_KNN_KMeans/L03_knn_mini.tex`
- Includes: colortbl, pgfplots, algorithm, algorithmic, dfteal/dfred colors, compactlist, bottomnote, highlight, mathbold

**Structural model for mini-lecture:** `slides/L03_KNN_KMeans/L03_kmeans_mini.tex` (651 lines, 10 frames)
- Arc: WHY(TikZ comic) -> FEEL(text+prompt) -> WHAT(comparison table) -> CASE(step diagram) -> HOW(side-by-side) -> RISK(TikZ comic) -> WHERE(external chart) -> IMPACT(stakeholder map) -> SO WHAT(metaphor visual) -> ACT(activity frame)
- Two-column [T] layout on every frame: 0.55 + 0.42
- Question-style frametitles on every frame
- NO title page, 10 content frames only
- ONE external chart via `\includegraphics`

**Structural model for full-lecture:** `slides/L02_Logistic_Regression/L02_logreg_full.tex` (1641 lines, 31 frames)
- Frame 1: `\titlepage`
- Frame 2: XKCD opening comic (two-column with commentary)
- Frame 3: Learning objectives (numbered, Bloom's verbs)
- Frames 4-29: Content frames, NO `\section{}` commands, use `%% === SECTION N: NAME ===` comment markers
- Frame 30: Key Takeaways
- Frame 31: Closing (callback to opening comic)
- All chart frames use "What you see / Key pattern / Takeaway" format
- Two-column [T] layout: `\column{0.55\textwidth}` + `\column{0.42\textwidth}`

**Available L04 assets (8 chart PDFs):**
| Chart | Path (relative to L04 folder) | Best For |
|-------|-------------------------------|----------|
| Decision tree | `01_decision_tree/chart.pdf` | Full: tree foundations |
| Feature importance | `02_feature_importance/chart.pdf` | Full: MDI/permutation |
| Bootstrap | `03_bootstrap/chart.pdf` | Full: bagging concept |
| OOB error | `04_oob_error/chart.pdf` | Full: OOB convergence |
| Ensemble voting | `05_ensemble_voting/chart.pdf` | Mini: WHERE slide; Full: ensemble concept |
| Single tree variance | `06a_single_tree_variance/chart.pdf` | Full: variance problem |
| RF variance reduction | `06b_random_forest_variance/chart.pdf` | Full: variance solution |
| Decision flowchart | `07_decision_flowchart/chart.pdf` | Full: practical decision |

**Available XKCD images (for full lecture):**
- `images/1885_ensemble_model.png` -- XKCD #1885 "Ensemble Model"
- `images/1838_machine_learning.png` -- XKCD #1838 "Machine Learning"

**GH Pages current L04 section:** `docs/index.html` lines 215-236
- Currently has 4 cards: Overview PDF, Deep Dive PDF, Colab Notebook, Dataset
- Followed by 7 chart thumbnails
- Must add 2 new PDF download cards for mini and full lecture

---

## Work Objectives

### Core Objective
Produce two pedagogically complete, visually consistent Beamer lecture files for Random Forests that compile with 0 errors and 0 Overfull warnings, plus update GitHub Pages with download cards.

### Deliverables
1. `slides/L04_Random_Forests/L04_rf_mini.tex` -- 10-slide mini-lecture
2. `slides/L04_Random_Forests/L04_rf_full.tex` -- ~31-frame full lecture
3. Updated `docs/index.html` -- 2 new download cards in L04 section

### Definition of Done
- Both .tex files compile with `pdflatex -interaction=nonstopmode` producing 0 errors
- Both .tex files produce 0 "Overfull \hbox" warnings
- Mini has exactly 10 content frames (no title page)
- Full has title page + ~30 content frames (~31 total)
- All chart paths resolve correctly (relative to .tex location)
- GH Pages cards link to correct PDF paths
- Both files are fully self-contained (no \input, no \include)

---

## Must Have / Must NOT Have

### Must Have
- Preamble: exact copy of lines 1-99 from `L03_knn_mini.tex` (same packages, colors, commands)
- Mini: all 10 arc positions (WHY, FEEL, WHAT, CASE, HOW, RISK, WHERE, IMPACT, SO WHAT, ACT)
- Mini: question-style frametitles on every frame
- Mini: two-column [T] layout (0.55 + 0.42) on every frame
- Mini: TikZ comics on WHY and RISK slides
- Mini: ONE external chart (ensemble voting or feature importance recommended)
- Mini: `\bottomnote{}` on every frame
- Mini: 10 different visual types across 10 slides
- Full: title page (Frame 1)
- Full: XKCD #1885 opening comic (Frame 2) with CC BY-NC 2.5 attribution
- Full: Learning objectives frame with Bloom's verbs (Frame 3)
- Full: "What you see / Key pattern / Takeaway" format on chart frames
- Full: NO `\section{}` commands, use `%% === SECTION N: NAME ===` comment markers
- Full: All 8 chart PDFs included across relevant frames
- Full: Key Takeaways frame and Closing frame (callbacks to opening)
- Full: MSc-level math: Gini, entropy, information gain, variance reduction formula, OOB, MDI, permutation importance, boosting objective, SHAP
- Full: Finance domain: fraud detection with class imbalance, credit risk feature importance
- Both: `\begin{compactlist}` instead of raw `\begin{itemize}` for tight spacing
- Both: `block{Insight}` and `exampleblock` used per established convention
- Both: `\scriptsize` / `\footnotesize` font cascade for density control

### Must NOT Have
- Mini: NO title page frame
- Mini: NO `\section{}` commands
- Full: NO `\section{}` commands (use comment-block markers only)
- Neither file: NO `\input{}` or `\include{}` directives
- Neither file: NO lines exceeding Beamer text width (risk of Overfull)
- Neither file: NO more than 3-4 bullet points per compactlist (overflow risk)
- Neither file: NO unescaped special LaTeX characters in text
- GH Pages: NO changes outside the L04 section div

---

## Task Flow and Dependencies

```
TASK 1 (Mini .tex)  ─────────┐
                              ├──> TASK 3 (Compile both) ──> TASK 4 (GH Pages)
TASK 2 (Full .tex)  ─────────┘
```

Tasks 1 and 2 are independent and can be executed in parallel.
Task 3 depends on both 1 and 2.
Task 4 depends on Task 3 (need to confirm PDF filenames).

---

## Detailed TODOs

### TASK 1: Create L04_rf_mini.tex (10-slide mini-lecture)

**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\L04_rf_mini.tex`

**Preamble (lines 1-99):** Exact copy from `slides/L03_KNN_KMeans/L03_knn_mini.tex` lines 1-99, then change:
- `\title[Random Forests Mini-Lecture]{Random Forests}`
- `\subtitle{A 10-Slide Mini-Lecture}`
- Keep `\author{Methods and Algorithms}`, `\institute{MSc Data Science}`, `\date{}`

**Frame-by-frame specification:**

| # | Arc | Frametitle (question) | Visual Type | Content |
|---|-----|----------------------|-------------|---------|
| 1 | WHY | Why Would a Fraud Analyst Trust 500 Weak Detectors Over One Expert? | TikZ comic (dilemma) | LEFT: Dilemma -- single decision tree overfits, misses fraud patterns, high variance. One tree says "fraud" another says "legit" for same transaction. RIGHT: TikZ stick figures -- single tree (confident but wrong) vs crowd of small trees (collectively right). Wisdom of crowds metaphor. Insight block: RF combines many weak learners to produce a strong one -- variance drops without increasing bias. Bottomnote: Ensemble learning = combining imperfect models to produce reliable decisions. |
| 2 | FEEL | Polling the Room vs. Asking One Expert -- Which Do You Trust More? | Text-only with reflection prompt | LEFT: Think Before You Compute. Narrative about asking one friend vs polling 20 friends for a restaurant recommendation. One expert can be biased; many imperfect opinions average out noise. compactlist: How many friends would you ask? Did their biases cancel? Was the consensus more stable? `exampleblock{Reflection Prompt}`: "Think of a time you made a better decision by gathering multiple opinions. What made the aggregate better than any single opinion?" RIGHT: fcolorbox: "Pause and reflect: when you last chose a restaurant by asking friends, you were bagging human opinions." Bottomnote: Bootstrap aggregating (bagging) formalizes this intuition: sample, train, average. |
| 3 | WHAT | What Makes a Random Forest Different from Bagging, Boosting, and a Single Tree? | Comparison table | LEFT: Taxonomy table with columns: Property, RF, Bag, Boost, Tree. Rows: Sampling (bootstrap/all), Feature subset (sqrt(p)/all/all/all), Correlation (low/high/seq/n/a), Bias (low/low/low/low), Variance (low/med/low/high), Parallelizable (yes/yes/no/n/a). Insight block: RF adds feature randomization ON TOP of bagging to decorrelate trees -- that is the key innovation. RIGHT: 4 colored summary boxes (like K-Means mini slide 3). Bottomnote: Breiman (2001) showed feature randomization is what makes RF variance reduction superior to plain bagging. |
| 4 | CASE | How Does a Single Transaction Navigate 500 Trees to a Fraud Verdict? | TikZ step diagram / timeline | LEFT: One Transaction, 500 Votes. compactlist: Bootstrap sample 63.2% of training data per tree. At each split, consider only sqrt(p) random features. Each tree votes: fraud or legit. Majority vote determines final prediction. OOB samples validate without a test set. Insight block: Each tree sees different data AND different features -- this double randomness is the source of RF's power. RIGHT: TikZ flowchart (vertical): Bootstrap Sample -> Build Tree (sqrt(p) features) -> Predict -> diamond "500 trees?" -> yes: loop back -> no: Majority Vote -> Output. Bottomnote: 63.2% = 1 - (1-1/n)^n approaches 1 - 1/e for large n. |
| 5 | HOW | How Does Feature Randomization Kill the Correlation Between Trees? | Side-by-side architecture | LEFT: The Decorrelation Trick. compactlist: Bagging alone: if one feature dominates, all trees split on it at root -> trees are correlated -> averaging correlated estimators reduces variance slowly. RF fix: restrict each split to sqrt(p) random features -> different trees use different features -> correlation drops -> variance drops faster. Math: Var(avg) = rho*sigma^2 + (1-rho)/B * sigma^2. When rho is small, second term vanishes with more trees. Insight block: The variance formula reveals WHY: reducing rho (correlation) is more powerful than increasing B (tree count). RIGHT: TikZ side-by-side: TOP "Bagging" box with 3 identical trees all splitting on "income" (correlated). BOTTOM "RF" box with 3 trees splitting on "income", "tenure", "amount" (decorrelated). Arrow label: rho drops. Bottomnote: Var(RF) = rho*sigma^2 + (1-rho)*sigma^2/B -- the first term is the irreducible correlation floor. |
| 6 | RISK | What Happens When the Forest Memorizes Noise Instead of Signal? | TikZ comic (failure) | LEFT: Three Ways RF Can Still Fail. compactlist: Overfitting to noise: too many deep trees on small data. Feature leakage: a feature that encodes the label sneaks in -- all trees use it. Class imbalance: RF votes majority, so rare class (fraud) gets outvoted. Insight block: RF is robust but not invincible. Class imbalance is the #1 failure mode in fraud detection -- always check class distribution. RIGHT: TikZ -- RF stick figure surrounded by 3 danger signs: (1) small dataset with deep trees memorizing, (2) leaked feature with all trees pointing to it, (3) imbalanced pie chart (99% legit, 1% fraud) with RF saying "All legit!" Speech bubble from RF: "The majority is always right...right?" Bottomnote: Solutions: max_depth, min_samples_leaf, class_weight='balanced', SMOTE for resampling. |
| 7 | WHERE | Why Do So Many Fraud Teams Reach for Random Forests First? | External chart (PDF) | LEFT: RF as the Industry Default for Tabular Data. compactlist: Ensemble voting aggregates weak signals into strong detection. Feature importance reveals which transaction attributes matter most. OOB error provides free cross-validation. Scales to millions of transactions with parallel training. The chart shows how ensemble voting combines individual tree predictions. Insight block: RF owes its popularity to the same property as K-Means: simplest reasonable solution that works out of the box. RIGHT: `\includegraphics[width=\textwidth]{05_ensemble_voting/chart.pdf}`. Bottomnote: Kaggle surveys consistently rank RF/gradient boosting as top methods for tabular data. |
| 8 | IMPACT | Who Wins and Who Loses When Trees Replace Rules? | TikZ stakeholder map | LEFT: Stakeholder Analysis. compactlist: Winners: Fraud analysts (better detection rate), Risk managers (feature importance for audit), Data engineers (parallel training, easy deployment). Losers: Compliance officers (less interpretable than logistic regression), Customers flagged by opaque ensemble, Rule-based system maintainers (legacy rules obsoleted). Insight block: RF shifts fraud detection from human-crafted rules to data-driven patterns -- but the trade-off is a regulatory interpretability gap. RIGHT: TikZ stakeholder map with RF node at center. Arrows to: Fraud Team (detection up), Risk Mgr (feature audit), Compliance (explain?), Customer (flagged), Data Eng (scales). Use same actor style as K-Means mini. Bottomnote: ECOA and GDPR require adverse action explanations -- SHAP values help bridge the interpretability gap for RF. |
| 9 | SO WHAT | 3 Questions That Reveal Whether Random Forests Are the Right Tool | TikZ metaphor (balance scale) | LEFT: The Decision Framework. Numbered list: 1. Is your data tabular? If images/text, use deep learning. 2. Do you need probability calibration? RF probabilities are often poorly calibrated -- consider Platt scaling. 3. Must the model be fully interpretable? If yes, use logistic regression or a single tree. If all three pass: RF is a strong candidate. Insight block: No Free Lunch applies: RF excels on tabular, non-linear, feature-rich data but struggles with extrapolation, calibration, and full interpretability. RIGHT: TikZ balance scale (same structure as K-Means mini slide 9). Left pan (heavier, green): "Tabular", "Non-linear", "Feature-rich" blocks -> "Use RF". Right pan (lighter, red): "Images", "Extrapolate", "Full interp." blocks -> "Avoid RF". Bottomnote: When in doubt: start with RF as baseline, then try gradient boosting (XGBoost/LightGBM) for marginal improvement. |
| 10 | ACT | Can You Diagnose This Fraud Detection Model? | Activity frame with fill-in table | LEFT: The Scenario. A payment processor runs RF with 1000 trees on transaction data. Features: amount, time, merchant category, distance from home, device fingerprint. The model flags 2% of transactions as fraud, but the actual fraud rate is 0.1%. compactlist: Calculate the expected false positive rate. Which feature would you expect to rank highest in importance? If the model misses 40% of actual fraud, what would you change? Is OOB error a reliable estimate here? Why or why not? exampleblock Deliverable: Fill in the table and defend your answers. RIGHT: Fill-in table with rows: Precision estimate, Recall estimate, Top feature, Recommended fix, OOB reliability. Bottomnote: Hint: with 0.1% fraud rate and 2% flag rate, most flags are false positives -- precision matters more than accuracy. |

**Acceptance criteria:**
- Exactly 10 `\begin{frame}` / `\end{frame}` pairs (no title page)
- Every frame has `\frametitle{...}` with a question
- Every frame uses `\begin{columns}[T]` with 0.55 + 0.42 split
- Every frame ends with `\bottomnote{...}`
- Only frame 7 has `\includegraphics`
- TikZ comics on frames 1, 4, 5, 6, 8, 9 (6 TikZ frames)
- 9 distinct visual types plus 1 intentional repeat for emotional contrast: TikZ comic (dilemma), text+prompt, comparison table, step diagram, side-by-side, TikZ comic (failure -- different emotional register), external chart, stakeholder map, balance scale, activity table
- Block type mapping: slides 1,3,4,5,6,7,8,9 use `block{Insight}`; slides 2,10 use `exampleblock` (titled "Reflection Prompt" and "Deliverable" respectively)
- Compiles with 0 errors, 0 Overfull

---

### TASK 2: Create L04_rf_full.tex (~31-frame full lecture)

**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests\L04_rf_full.tex`

**Preamble (lines 1-99):** Exact copy from `L03_knn_mini.tex` lines 1-99, then change:
- `\title[L04: Random Forests Full Lecture]{L04: Random Forests}`
- `\subtitle{Full Lecture: Ensemble Learning, Variance Reduction, and Fraud Detection}`
- `\author{Methods and Algorithms}`
- `\institute{MSc Data Science}`
- `\date{}`

**Frame-by-frame specification:**

| # | Section Marker | Frametitle (question) | Type | Chart Used |
|---|----------------|----------------------|------|------------|
| 1 | OPENING | (title page) | `\titlepage` | -- |
| 2 | OPENING | The Ensemble Approach | XKCD comic | `images/1885_ensemble_model.png` |
| 3 | OPENING | Learning Objectives | Numbered list | -- |
| 4 | DECISION TREES | Why Would a Single Tree Overfit Every Dataset It Touches? | TikZ + text | -- |
| 5 | DECISION TREES | How Does a Tree Choose the Best Split? (Gini Impurity) | Math + text | -- |
| 6 | DECISION TREES | What Does Entropy Add Beyond Gini? | Math + table | -- |
| 7 | DECISION TREES | What Does a Trained Decision Tree Actually Look Like? | Chart | `01_decision_tree/chart.pdf` |
| 8 | BAGGING | Why Does Averaging Multiple Models Reduce Variance? | Math derivation | -- |
| 9 | BAGGING | How Does Bootstrap Sampling Create Diversity? | Chart | `03_bootstrap/chart.pdf` |
| 10 | BAGGING | What Happens to the 36.8% of Samples Left Out? | Chart | `04_oob_error/chart.pdf` |
| 11 | RANDOM FORESTS | What Is the One Trick That Makes Random Forests Better Than Bagging? | Math + TikZ | -- |
| 12 | RANDOM FORESTS | How Does Feature Randomization Reduce Tree Correlation? | Variance formula | -- |
| 13 | RANDOM FORESTS | How Do 500 Trees Vote on a Single Prediction? | Chart | `05_ensemble_voting/chart.pdf` |
| 14 | RANDOM FORESTS | Can You See the Variance Drop from One Tree to a Forest? | Chart (side-by-side) | `06a_single_tree_variance/chart.pdf` + `06b_random_forest_variance/chart.pdf` |
| 15 | RANDOM FORESTS | What Is the Random Forest Algorithm in Pseudocode? | Pseudocode (algorithmic) | -- |
| 16 | FEATURE IMPORTANCE | Which Features Matter Most? (Mean Decrease in Impurity) | Chart | `02_feature_importance/chart.pdf` |
| 17 | FEATURE IMPORTANCE | Why Can MDI Be Misleading, and What Is Permutation Importance? | Math + comparison | -- |
| 18 | FEATURE IMPORTANCE | How Do SHAP Values Explain Individual Predictions? | Math + TikZ | -- |
| 19 | BOOSTING | How Does Boosting Learn from Its Mistakes? | TikZ + text | -- |
| 20 | BOOSTING | What Is AdaBoost's Weight Update Rule? | Math derivation | -- |
| 21 | BOOSTING | How Does Gradient Boosting Minimize an Arbitrary Loss? | Math + pseudocode | -- |
| 22 | BOOSTING | What Makes XGBoost's Objective Function Special? | Math | -- |
| 23 | EVALUATION | When Does a Forest Fail Silently? | TikZ risk comic | -- |
| 24 | EVALUATION | How Do You Choose the Right Hyperparameters? | Table + guidelines | -- |
| 25 | FINANCE APPLICATION | How Do Fraud Teams Use Feature Importance for Transaction Monitoring? | Case study | -- |
| 26 | FINANCE APPLICATION | What Happens When 99.9% of Transactions Are Legitimate? | Imbalanced data | -- |
| 27 | FINANCE APPLICATION | When Should You Choose RF Over Logistic Regression? | Chart | `07_decision_flowchart/chart.pdf` |
| 28 | STAKEHOLDERS | Who Wins and Who Loses When Ensembles Replace Scorecards? | TikZ stakeholder map | -- |
| 29 | STAKEHOLDERS | Can Regulators Trust a Model Made of 500 Trees? | Fairness/ECOA/GDPR | -- |
| 30 | SUMMARY | Key Takeaways | Two-column summary | -- |
| 31 | SUMMARY | Until Next Time... | Closing callback to XKCD | -- |

**Detailed content notes for key frames:**

**Frame 2 (XKCD):** LEFT column: commentary on XKCD #1885 Ensemble Model. "The cartoon captures the absurdity -- and power -- of combining models. Today we build the math." RIGHT: `\includegraphics[height=0.55\textheight]{images/1885_ensemble_model.png}`. Bottomnote with CC BY-NC 2.5 attribution.

**Frame 3 (Learning Objectives):**
1. **Derive** the variance reduction formula for bagged estimators and analyze the role of tree correlation (Analyze)
2. **Evaluate** RF vs. gradient boosting using bias-variance tradeoff analysis (Evaluate)
3. **Analyze** feature importance using MDI, permutation importance, and SHAP values (Analyze)
4. **Apply** ensemble methods to fraud detection with class imbalance (Apply)
5. **Compare** RF, AdaBoost, gradient boosting, and XGBoost objective functions (Evaluate)

**Frame 5 (Gini):** Full derivation: G = 1 - sum(p_k^2). Binary case: G = 2p(1-p). Properties. Worked example with fraud data.

**Frame 6 (Entropy):** H = -sum(p_k log p_k). Information Gain = H(parent) - weighted sum H(children). Table comparing Gini vs Entropy properties.

**Frame 8 (Variance reduction):** Key derivation: Var(1/B * sum X_b) = rho*sigma^2 + (1-rho)/B * sigma^2. Show that when rho=1 (identical trees), averaging does nothing. When rho=0 (independent), variance = sigma^2/B.

**Frame 12 (Feature randomization):** sqrt(p) for classification, p/3 for regression. Why: forces trees to explore different features -> reduces rho -> faster variance reduction.

**Frame 14 (Variance comparison):** Two-column frame. LEFT describes what both charts show. RIGHT: Two stacked `\includegraphics` showing 06a and 06b side by side (each at `width=0.48\textwidth` or stacked vertically at `width=\textwidth` with reduced height).

**Frame 15 (Pseudocode):** Use `\begin{algorithmic}` environment. RF algorithm: FOR b=1..B: draw bootstrap sample, grow tree with random feature subset at each split, store tree. Predict: majority vote (classification) or average (regression).

**Frame 18 (SHAP):** Shapley value formula: phi_j = sum over S of [|S|!(p-|S|-1)!/p!] * [f(S union j) - f(S)]. Explain TreeSHAP polynomial-time algorithm.

**Frame 20 (AdaBoost):** Weight update: w_i <- w_i * exp(alpha_t * I(misclassified)). Alpha_t = 0.5 * ln((1-err_t)/err_t). Show how misclassified samples get higher weight.

**Frame 21 (Gradient Boosting):** Generic: f_m(x) = f_{m-1}(x) + eta * h_m(x) where h_m fits negative gradient residuals. For squared loss: residuals = y - f_{m-1}(x). For log loss: residuals = y - p_{m-1}(x).

**Frame 22 (XGBoost):** Objective: sum L(y_i, y_hat_i) + sum Omega(f_k) where Omega(f) = gamma*T + 0.5*lambda*||w||^2. Second-order Taylor expansion. Optimal leaf weight formula.

**Frame 26 (Class imbalance):** Fraud rate 0.1%. RF majority vote = always "legit". Solutions: class_weight='balanced', stratified bootstrap, SMOTE, cost-sensitive learning. Precision/recall tradeoff.

**Frame 30 (Key Takeaways):** Two-column. LEFT: Mathematical Foundation (Gini/entropy, variance reduction, OOB, feature importance). RIGHT: Practical Application (boosting comparison, fraud detection, class imbalance, SHAP for interpretability).

**Frame 31 (Closing):** Callback to XKCD #1885. "We opened with the absurdity of ensemble models. Now you know WHY 500 trees beat one: variance reduction through decorrelation." Preview L05: PCA and t-SNE.

**Acceptance criteria:**
- Frame 1 is `\titlepage`
- Frames 2-31 are content frames (~31 total)
- NO `\section{}` commands anywhere
- All 8 chart PDFs are included via `\includegraphics` with correct relative paths
- XKCD #1885 included with CC BY-NC 2.5 bottomnote
- All math typeset correctly (no missing $ delimiters)
- Pseudocode uses `algorithmic` environment
- All frames use two-column [T] layout with 0.55/0.42 split
- Every frame has `\bottomnote{}`
- Compiles with 0 errors, 0 Overfull

---

### TASK 3: Compile and Verify Both Files

**Commands (run from L04 folder):**
```bash
cd D:\Joerg\Research\slides\Methods_and_Algorithms\slides\L04_Random_Forests
pdflatex -interaction=nonstopmode L04_rf_mini.tex
pdflatex -interaction=nonstopmode L04_rf_full.tex
```

**Verification checks:**
1. Both produce .pdf files
2. `grep -c "Overfull" L04_rf_mini.log` returns 0
3. `grep -c "Overfull" L04_rf_full.log` returns 0
4. `grep -c "Error" L04_rf_mini.log` returns 0 (excluding false positives)
5. `grep -c "Error" L04_rf_full.log` returns 0
6. Mini PDF has exactly 10 pages
7. Full PDF has ~31 pages
8. All chart inclusions resolve (no "File not found" warnings)

**If Overfull warnings found:**
- Identify the offending frame
- Reduce text, shorten bullet points, or adjust column widths
- Recompile and re-verify

**Acceptance criteria:**
- 0 errors, 0 Overfull in both logs
- Both PDFs render correctly

---

### TASK 4: Update GitHub Pages (docs/index.html)

**File:** `D:\Joerg\Research\slides\Methods_and_Algorithms\docs\index.html`

**Location:** Inside the `<div id="L04" class="lesson-section l2">` section, within the first `<div class="cgrid">` block (lines 220-225).

**Action:** Add 2 new download cards AFTER the existing Deep Dive PDF card (line 222) and BEFORE the Colab Notebook card (line 223).

**New cards to insert:**
```html
<a class="ccard" href="slides/pdf/L04_rf_mini.pdf" download><div class="ccard-icon">PDF</div>Mini-Lecture PDF<div class="ccard-label">10-slide RF overview</div></a>
<a class="ccard" href="slides/pdf/L04_rf_full.pdf" download><div class="ccard-icon">PDF</div>Full Lecture PDF<div class="ccard-label">31-slide RF theory</div></a>
```

**Note:** The PDF files need to be copied to `docs/slides/pdf/` for the links to work. This is a deployment step that may happen separately.

**Acceptance criteria:**
- 2 new `<a class="ccard">` elements appear in L04 section
- Links point to `slides/pdf/L04_rf_mini.pdf` and `slides/pdf/L04_rf_full.pdf`
- Labels are descriptive: "Mini-Lecture PDF" / "Full Lecture PDF"
- No changes outside the L04 `<div>` block
- HTML remains valid (no unclosed tags)

---

## Commit Strategy

**Single commit after all 4 tasks complete:**

```
Add L04 Random Forests mini-lecture and full lecture

- L04_rf_mini.tex: 10-slide mini-lecture (WHY-FEEL-WHAT-CASE-HOW-RISK-WHERE-IMPACT-SO WHAT-ACT arc)
- L04_rf_full.tex: 31-frame full lecture with MSc-level depth (variance reduction, boosting, SHAP, fraud detection)
- docs/index.html: add download cards for both new PDFs under L04 section
```

**Files to stage:**
- `slides/L04_Random_Forests/L04_rf_mini.tex`
- `slides/L04_Random_Forests/L04_rf_full.tex`
- `docs/index.html`

---

## Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| Mini compiles clean | 0 errors, 0 Overfull in pdflatex log |
| Full compiles clean | 0 errors, 0 Overfull in pdflatex log |
| Mini frame count | Exactly 10 pages in PDF |
| Full frame count | ~31 pages in PDF |
| Mini arc completeness | All 10 arc positions present |
| Full chart coverage | All 8 chart PDFs included |
| Full XKCD attribution | CC BY-NC 2.5 in bottomnote |
| Full math depth | Gini, entropy, variance formula, OOB, SHAP, XGBoost objective all present |
| Full pseudocode | RF algorithm in algorithmic environment |
| GH Pages cards | 2 new cards visible in L04 section |
| Self-contained | No \input or \include in either file |
| Visual consistency | Same preamble, colors, layout as L02/L03 lectures |
