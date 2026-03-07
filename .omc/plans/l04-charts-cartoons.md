# Plan: L04 Charts & Cartoons Enrichment

## Context

### Original Request
Add many more charts and cartoons to the L04 (Decision Trees & Random Forests) lecture. Specifically:
1. Effect of tree depth on curve fitting for Decision Trees
2. Effect of tree depth on curve fitting for Random Forests
3. Additional charts filling visual gaps across all four .tex files
4. More TikZ cartoons for engagement

### Current State
- **20 existing chart folders** (01-19, with 06a/06b split)
- **6 .tex files**: L04_overview.tex (25 slides), L04_deepdive.tex (42+10 appendix slides), L04_dt_full.tex (25 slides), L04_rf_full.tex (31 slides), L04_dt_mini.tex, L04_rf_mini.tex
- **Scope note:** L04_dt_mini.tex and L04_rf_mini.tex are abbreviated prerequisite lectures and are explicitly OUT OF SCOPE for this plan. They can be updated in a follow-up pass if needed.
- **2 XKCD images**: #1838 (Machine Learning), #1885 (Ensemble Model)
- Chart pattern: matplotlib with rcParams, ML color palette, figsize=(10,6), single figure per chart.py, output to chart.pdf

### Research Findings (from tex file analysis)
**Visual gap analysis across all four files:**

| .tex File | Slides | Charts Used | Text-Only Slides (no visual) | Gap |
|-----------|--------|-------------|------------------------------|-----|
| L04_overview.tex | 25 | 5 (01,03,05,07,17) + 2 XKCD = 7 visuals | 16 text-only | HIGH |
| L04_deepdive.tex | 52 | 11 (02,04,06a,06b,13,14,15,16,17,18,19) + 1 XKCD = 12 visuals | 39 text-only | HIGH |
| L04_dt_full.tex | 25 | 7 (01,08,09,10,11,12,16) + 1 XKCD + 1 TikZ = 9 visuals | 14 text-only | MEDIUM |
| L04_rf_full.tex | 31 | 12 (01,02,03,04,05,06a,06b,07,13,14,15,18) + 2 XKCD + 5 TikZ = 19 visuals | 10 text-only | MEDIUM |

**Key content areas with NO chart support:**
- Tree depth effect on curve fitting (DT) -- REQUESTED
- Tree depth effect on curve fitting (RF) -- REQUESTED
- Bagging variance reduction (formula slide, no visual)
- RF algorithm pseudocode (text-only)
- SHAP values (formula-only, no waterfall/beeswarm plot)
- Class imbalance / precision-recall (text-only, no ROC/PR curve)
- RF vs Boosting comparison (text-only, no visual comparison)
- Correlation effect on ensemble variance (formula, no visual)
- SMOTE/resampling (text-only, no visual)
- Concept drift / silent failures (text-only)

---

## Work Objectives

### Core Objective
Enrich L04 with 8 new Python charts and 4 new TikZ cartoons, filling the most impactful visual gaps and delivering the two specifically requested depth-effect charts.

### Deliverables

| # | Type | Folder/Location | Description |
|---|------|-----------------|-------------|
| 1 | chart.py | `20_dt_depth_curve_fitting/` | **DT depth effect on curve fitting** -- sinusoidal data with DTs at depth=1,3,5,10,None showing underfit-to-overfit progression |
| 2 | chart.py | `21_rf_depth_curve_fitting/` | **RF depth effect on curve fitting** -- same data, RF at depth=1,3,5,10,None showing smoother, more robust fits at every depth |
| 3 | chart.py | `22_correlation_variance_surface/` | **Ensemble variance vs rho and B** -- heatmap or 3D surface showing how Var(f_bar) = rho*sigma^2 + (1-rho)*sigma^2/B changes with rho (0-1) and B (1-500) |
| 4 | chart.py | `23_precision_recall_curve/` | **Precision-Recall curve for fraud detection** -- PR curve with AUC-PR, showing threshold effect on precision vs recall for imbalanced data |
| 5 | chart.py | `24_shap_waterfall/` | **SHAP waterfall plot** -- waterfall chart showing per-feature SHAP contributions for a single fraud prediction (synthetic data, using shap library or manual bars) |
| 6 | chart.py | `25_bagging_vs_boosting/` | **Bagging vs Boosting conceptual comparison** -- side-by-side showing parallel (bagging) vs sequential (boosting) error reduction curves |
| 7 | chart.py | `26_smote_visualization/` | **SMOTE resampling** -- scatter plot showing original imbalanced data vs SMOTE-augmented data with synthetic minority points highlighted |
| 8 | chart.py | `27_rf_ntrees_convergence/` | **RF error convergence vs n_estimators** -- OOB error and test error vs number of trees (10 to 500), showing diminishing returns and convergence plateau |
| 9 | TikZ | L04_overview.tex | **Bagging Pipeline Cartoon** -- visual showing data flowing through bootstrap sampling into parallel trees and into a voting box |
| 10 | TikZ | L04_deepdive.tex | **Gradient Descent in Function Space** -- cartoon showing "stepping downhill" in loss landscape with each boosting round |
| 11 | TikZ | L04_dt_full.tex | **Closing Cartoon** -- "The Tree That Learned Too Much" -- a comically deep tree with absurd splits (e.g., "Is it Tuesday?", "Did the user blink?") ending in a confused leaf |
| 12 | TikZ | L04_rf_full.tex | **Closing Cartoon** -- "The Forest Parliament" -- cartoon of diverse trees debating and voting, with a banner reading "Majority Rules" |

### Definition of Done
- All 8 chart.py files run without error and produce chart.pdf
- All 4 TikZ cartoons compile cleanly within their .tex files
- Each new chart is included in at least one .tex file with appropriate `\includegraphics` and `\bottomnote`
- Zero Overfull warnings in all four .tex files after integration
- manifest.json updated with all new chart entries

---

## Guardrails

### Must Have
- Charts 20 and 21 (depth curve fitting for DT and RF) are the **top priority**
- All chart.py files follow the exact rcParams template from existing charts
- ML color palette used consistently: MLPurple=#3333B2, MLBlue=#0066CC, MLOrange=#FF7F0E, MLGreen=#2CA02C, MLRed=#D62728
- figsize=(10,6), dpi=150, font.size=14
- ONE figure per chart.py (no subplots)
- Chart widths in tex: 0.55\textwidth (with text) or 0.65\textwidth (chart-only slide)
- Max 3-4 bullets per slide
- XKCD attribution format: `\bottomnote{XKCD \#NNNN by Randall Munroe (CC BY-NC 2.5)}`
- TikZ cartoons must use defined ML colors (mlpurple, mlblue, mlorange, mlgreen, mlred)

### Must NOT Have
- No subplots -- each chart is exactly ONE figure
- No new Python dependencies beyond numpy, matplotlib, scikit-learn, scipy (shap library is optional; if used for chart 24, provide a fallback using manual bar chart)
- No modifications to existing chart.py files
- No removal of existing slides or charts
- No changes to the Beamer preamble or template structure EXCEPT: adding `\usetikzlibrary{arrows.meta,positioning,shapes.callouts,shapes.geometric,decorations.pathreplacing}` to L04_overview.tex and L04_deepdive.tex (required for TikZ cartoons T9 and T10; the _full files already have this line)
- No XKCD images downloaded without explicit permission (TikZ cartoons only for new cartoons)

---

## Task Flow

```
Phase 1: Priority Charts (DT/RF depth)
  T1 -> T2 (sequential: RF chart references DT chart for visual consistency)

Phase 2: Supporting Charts (parallel)
  T3, T4, T5, T6, T7, T8 (all independent)

Phase 3: TikZ Cartoons (parallel)
  T9, T10, T11, T12 (all independent)

Phase 4: Integration
  T13 (integrate all into .tex files, sequential)

Phase 5: Validation
  T14 (compile all .tex files, verify zero Overfull)

Phase 6: Manifest
  T15 (update manifest.json)
```

---

## Detailed TODOs

### T1: Create `20_dt_depth_curve_fitting/chart.py`
**Priority: HIGHEST**

Create a chart showing how a Decision Tree fits a noisy sinusoidal curve at different depths.

**Specification:**
- Generate noisy sinusoidal data: `y = sin(1.5*x) + 0.5*cos(2*x) + noise` on x in [0, 10], n=80 training points
- Fit DecisionTreeRegressor at depths: 1, 3, 5, 10, None (unlimited)
- Plot: scatter of training data (gray dots), true function (black dashed), and 5 colored lines for each depth
- Colors: depth=1 (MLBlue), depth=3 (MLGreen), depth=5 (MLOrange), depth=10 (MLRed), depth=None (MLPurple)
- Legend with depth labels
- Title: "Decision Tree: Effect of Depth on Curve Fitting"
- Annotations: "Underfitting" near depth=1 line, "Overfitting" near depth=None line
- Use same seed (random_state=42) for reproducibility

**Acceptance Criteria:**
- [ ] chart.py runs and produces chart.pdf
- [ ] Shows clear progression from underfit (smooth) to overfit (jagged)
- [ ] All 5 depth levels clearly distinguishable
- [ ] Follows rcParams template exactly

---

### T2: Create `21_rf_depth_curve_fitting/chart.py`
**Priority: HIGHEST**

Create a chart showing how a Random Forest fits the same noisy sinusoidal curve at different depths.

**Specification:**
- Use IDENTICAL data generation as T1 (same seed, same function, same noise)
- Fit RandomForestRegressor(n_estimators=200) at depths: 1, 3, 5, 10, None
- Plot: scatter of training data (gray dots), true function (black dashed), and 5 colored lines
- Same color scheme as T1 for direct visual comparison
- Title: "Random Forest: Effect of Depth on Curve Fitting"
- Key visual difference from T1: RF lines should be SMOOTHER at every depth level, especially depth=None which should closely track the true function instead of memorizing noise
- Annotation: "Smooth even at max depth" near depth=None line

**Acceptance Criteria:**
- [ ] chart.py runs and produces chart.pdf
- [ ] RF curves visibly smoother than DT curves at equivalent depths
- [ ] depth=None RF closely approximates true function (low variance)
- [ ] Same data as T1 for direct comparison

---

### T3: Create `22_correlation_variance_surface/chart.py`
**Priority: HIGH**

Visualize the ensemble variance formula: Var = rho*sigma^2 + (1-rho)*sigma^2/B.

**Specification:**
- Create a heatmap (imshow or pcolormesh) with:
  - x-axis: B (number of trees) from 1 to 500
  - y-axis: rho (correlation) from 0.0 to 1.0
  - Color: normalized variance Var/sigma^2
- Add contour lines at key variance levels (0.1, 0.2, 0.5, 0.8)
- Mark the "sweet spot" region where rho < 0.2 and B > 100
- Title: "Ensemble Variance: Correlation vs Number of Trees"
- Colorbar labeled "Var / sigma^2"

**Acceptance Criteria:**
- [ ] Heatmap clearly shows that low rho matters more than high B
- [ ] Sweet spot region visually highlighted
- [ ] Follows rcParams template

**Target .tex files:** L04_deepdive.tex (after the bagging variance reduction slide), L04_rf_full.tex (after frame 12)

---

### T4: Create `23_precision_recall_curve/chart.py`
**Priority: HIGH**

Show Precision-Recall tradeoff for imbalanced fraud detection.

**Specification:**
- Generate imbalanced classification data: 95% legitimate, 5% fraud (n=2000)
- Train a RandomForestClassifier with class_weight='balanced'
- Plot PR curve using sklearn.metrics.precision_recall_curve
- Shade the AUC-PR area
- Mark the point where F1 is maximized with a star
- Add a horizontal dashed line at precision = fraud_rate (baseline)
- Title: "Precision-Recall Curve: Fraud Detection"
- Annotate AUC-PR value on the plot

**Acceptance Criteria:**
- [ ] PR curve shows realistic tradeoff
- [ ] AUC-PR clearly labeled
- [ ] Baseline (random classifier) shown for reference

**Target .tex files:** L04_overview.tex (after fraud detection slide 17), L04_deepdive.tex (after slide 35), L04_rf_full.tex (after frame 26)

---

### T5: Create `24_shap_waterfall/chart.py`
**Priority: MEDIUM**

Show per-feature SHAP-style contributions for a single prediction.

**Specification:**
- DO NOT require the `shap` library -- create a manual waterfall bar chart
- Use synthetic but realistic feature names: Transaction Amount, Distance from Home, Time of Day, Merchant Category, Card Present, Customer Age, Frequency (24h)
- Use synthetic SHAP values that tell a story: Amount (+0.32), Distance (+0.18), Time (+0.08), Merchant (-0.05), Card Present (-0.03), Age (-0.02), Frequency (+0.15)
- Horizontal waterfall chart: start from base value, accumulate positive (red) and negative (green) contributions
- Final prediction marked with a vertical line
- Title: "SHAP Waterfall: Why Was This Transaction Flagged?"

**Acceptance Criteria:**
- [ ] No dependency on shap library
- [ ] Waterfall clearly shows positive (fraud-pushing) and negative (fraud-reducing) contributions
- [ ] Feature names readable

**Target .tex files:** L04_deepdive.tex (after SHAP slide 24), L04_rf_full.tex (after frame 18)

---

### T6: Create `25_bagging_vs_boosting/chart.py`
**Priority: MEDIUM**

Visual comparison of bagging (RF) vs boosting error reduction.

**Specification:**
- Two line plots on the same axes:
  - Bagging (RF): test error decreases smoothly with n_estimators (variance reduction)
  - Boosting (GradientBoosting): test error decreases more aggressively but with risk of increase at high iterations
- Train both on same dataset (make_classification, n=500, n_features=10)
- Use staged_predict for GradientBoosting to get per-iteration test error
- For RF per-iteration error: loop from n_estimators=1 to N, incrementing by 1 each iteration with warm_start=True, recording oob_score_ at each step. NOTE: warm_start adds trees incrementally but you must manually set n_estimators and refit each iteration.
- For GradientBoosting: use staged_predict() which is straightforward
- RF line in MLBlue, Boosting line in MLOrange
- Annotate "variance reduction" near RF curve, "bias reduction" near boosting curve
- Title: "Bagging vs Boosting: Error Reduction Strategies"

**Acceptance Criteria:**
- [ ] Both curves on same axes for direct comparison
- [ ] Boosting potentially overfits at high iterations (visible uptick)
- [ ] RF converges monotonically (never overfits by adding trees)

**Target .tex files:** L04_overview.tex (after RF vs Boosting slide 19), L04_deepdive.tex (after slide 30)

---

### T7: Create `26_smote_visualization/chart.py`
**Priority: MEDIUM**

Visualize SMOTE resampling effect on imbalanced data.

**Specification:**
- Generate 2D imbalanced data: 200 majority class, 20 minority class (using make_classification with weights=[0.9, 0.1])
- Apply SMOTE manually (linear interpolation between random minority point pairs -- do NOT require imblearn). Optional: use imblearn if installed, but default implementation must be manual.
- Plot two panels... NO -- single figure rule. Plot on ONE axis:
  - Original majority points: MLBlue, alpha=0.5
  - Original minority points: MLRed, filled circles
  - SMOTE-generated synthetic points: MLOrange, stars or diamonds
- Title: "SMOTE: Synthetic Minority Oversampling"
- Annotate the interpolation lines between original minority points and their synthetic neighbors (show 3-4 example lines)

**Acceptance Criteria:**
- [ ] Single figure (no subplots)
- [ ] Clear distinction between original and synthetic minority points
- [ ] If imblearn unavailable, implement simple linear interpolation manually

**Target .tex files:** L04_overview.tex (after slide 18), L04_deepdive.tex (after slide 36)

---

### T8: Create `27_rf_ntrees_convergence/chart.py`
**Priority: MEDIUM**

Show how RF error converges as n_estimators increases.

**Specification:**
- Train RF on make_classification data, varying n_estimators from 1 to 500
- Plot OOB error (primary, solid line) and test error (secondary, dashed line) vs n_estimators
- Use warm_start=True for efficiency: loop from n_estimators=10 to 500 in increments (e.g., steps of 10), setting n_estimators and calling fit() each iteration. Record oob_score_ (set oob_score=True) at each step.
- Mark the "diminishing returns" point where improvement < 0.1% per additional tree
- Shade the "recommended range" (100-300 trees)
- Title: "Random Forest: Error Convergence vs Number of Trees"

**Acceptance Criteria:**
- [ ] Both OOB and test error shown
- [ ] Clear convergence behavior visible
- [ ] Recommended range highlighted

**Target .tex files:** L04_deepdive.tex (after hyperparameter slide 17), L04_rf_full.tex (after hyperparameter frame)

---

### T9: TikZ Cartoon -- Bagging Pipeline (L04_overview.tex)
**Priority: LOW**

Insert after the Bootstrap Aggregating slide (slide 10, around line 267).

**Description:** A pipeline diagram showing:
- Left: "Training Data" box
- Middle: 3 bootstrap sample boxes with arrows splitting from data
- Right: 3 tree icons (triangles) growing from samples
- Far right: "Vote!" box collecting predictions
- Arrows connecting the flow
- Style: playful, using ML colors

**Acceptance Criteria:**
- [ ] Compiles cleanly in L04_overview.tex
- [ ] Fits within 0.65\textwidth
- [ ] Uses mlpurple, mlblue, mlorange colors

---

### T10: TikZ Cartoon -- Gradient Descent in Function Space (L04_deepdive.tex)
**Priority: LOW**

Insert after the Gradient Boosting slide (around line 775).

**Description:** A cartoon landscape with:
- Wavy "loss surface" drawn as a curve
- A stick figure (or ball) taking steps downhill
- Each step labeled "Tree 1", "Tree 2", "Tree 3"
- Steps get smaller (representing learning rate shrinkage)
- Caption: "Each tree takes one step downhill in the loss landscape"

**Acceptance Criteria:**
- [ ] Compiles cleanly in L04_deepdive.tex
- [ ] Conveys gradient descent intuition visually

---

### T11: TikZ Cartoon -- "The Tree That Learned Too Much" (L04_dt_full.tex)
**Priority: LOW**

Replace or supplement the closing slide (slide 25, around line 898).

**Description:** A comically deep decision tree with absurd splits:
- Root: "Is income > $50k?" (sensible)
- Level 2: "Is debt ratio > 0.4?" (sensible)
- Level 3: "Is it a Tuesday?" (ridiculous)
- Level 4: "Did the applicant blink twice?" (absurd)
- Leaf: "CONFUSED" with a question mark
- Caption: "When overfitting goes too far"

**Acceptance Criteria:**
- [ ] Clearly communicates overfitting concept with humor
- [ ] Compiles cleanly
- [ ] Fits within slide dimensions

---

### T12: TikZ Cartoon -- "The Forest Parliament" (L04_rf_full.tex)
**Priority: LOW**

Add as a new closing cartoon slide before the final "Until Next Time" frame (before line 1404).

**Description:** Five tree-shaped figures sitting around a semicircular table:
- Each tree has a different "opinion" speech bubble: "Fraud!", "Legit!", "Fraud!", "Fraud!", "Legit!"
- A gavel or banner in the center: "Majority Rules: FRAUD (3-2)"
- Trees colored differently to represent diversity
- Caption: "Democracy in the forest: majority vote wins"

**Acceptance Criteria:**
- [ ] Conveys voting/ensemble concept with humor
- [ ] Compiles cleanly
- [ ] Five distinct trees visible

---

### T13: Integration -- Insert Charts and Cartoons into .tex Files
**Priority: HIGH (depends on T1-T12)**

For each new chart and cartoon, add the appropriate `\begin{frame}` block into the target .tex file(s).

**Integration map:**

| Chart/Cartoon | L04_overview.tex | L04_deepdive.tex | L04_dt_full.tex | L04_rf_full.tex |
|---------------|------------------|-------------------|-----------------|-----------------|
| 20 (DT depth) | After slide 9 (line ~252) | After slide 10 (line ~281, after pruning chart frame) | After slide 18 (line ~673) | -- |
| 21 (RF depth) | After slide 12 (line ~308) | After slide 26 (line ~653) | -- | After frame 14 (line ~633) |
| 22 (corr/var) | -- | After slide 14 (line ~380) | -- | After frame 12 (line ~568) |
| 23 (PR curve) | After slide 17 (line ~398) | After slide 35 (line ~873) | -- | After frame 26 (line ~1243) |
| 24 (SHAP) | -- | After slide 24 (line ~609) | -- | After frame 18 (line ~801) |
| 25 (bag vs boost) | After slide 19 (line ~437) | After slide 30 (line ~725) | -- | -- |
| 26 (SMOTE) | After slide 18 (line ~416) | After slide 36 (line ~898) | -- | -- |
| 27 (ntrees) | -- | After slide 17 (line ~450) | -- | After frame 15 (line ~679) |
| T9 (TikZ bagging) | After slide 10 (line ~267) | -- | -- | -- |
| T10 (TikZ grad desc) | -- | After slide 32 (line ~775) | -- | -- |
| T11 (TikZ overfit tree) | -- | -- | Closing area (line ~898) | -- |
| T12 (TikZ parliament) | -- | -- | -- | Before frame 31 (line ~1404) |

**Slide frame template for chart-only slides:**
```latex
\begin{frame}[t]{Title Here}
\begin{center}
\includegraphics[width=0.65\textwidth]{XX_folder_name/chart.pdf}
\end{center}
\bottomnote{Caption text here}
\end{frame}
```

**Slide frame template for chart + text slides:**
```latex
\begin{frame}[t]{Title Here}
\begin{columns}[T]
\begin{column}{0.55\textwidth}
\small
[Bullet points]
\end{column}
\begin{column}{0.42\textwidth}
\includegraphics[width=\textwidth]{XX_folder_name/chart.pdf}
\end{column}
\end{columns}
\bottomnote{Caption text here}
\end{frame}
```

**Acceptance Criteria:**
- [ ] Each chart appears in at least one .tex file
- [ ] No duplicate chart usage (each chart used purposefully)
- [ ] Slide titles are question-format where appropriate (matching existing L04 style)
- [ ] Every slide has a `\bottomnote{}`

---

### T14: Compile and Validate All .tex Files
**Priority: HIGH (depends on T13)**

```bash
cd slides/L04_Random_Forests
for f in L04_overview.tex L04_deepdive.tex L04_dt_full.tex L04_rf_full.tex; do
  pdflatex -interaction=nonstopmode "$f"
  pdflatex -interaction=nonstopmode "$f"  # second pass for references
done
```

Then grep for Overfull warnings:
```bash
grep -c "Overfull" *.log
```

**Acceptance Criteria:**
- [ ] All four .tex files compile with 0 errors
- [ ] 0 Overfull \hbox or \vbox warnings
- [ ] PDFs open correctly and new slides are visible

---

### T15: Update manifest.json
**Priority: MEDIUM (depends on T1-T8)**

Add entries for all 8 new chart folders under L04's charts array.

**Acceptance Criteria:**
- [ ] All 8 new charts listed with status "complete"
- [ ] Paths are correct relative to slides/L04_Random_Forests/

---

## Commit Strategy

**Commit 1:** "Add 8 new L04 charts: depth curve fitting (DT/RF), correlation-variance surface, PR curve, SHAP waterfall, bagging-vs-boosting, SMOTE visualization, ntrees convergence"
- Files: all 8 new chart folders (chart.py + chart.pdf each)

**Commit 2:** "Add TikZ cartoons and integrate all new visuals into L04 slide decks"
- Files: L04_overview.tex, L04_deepdive.tex, L04_dt_full.tex, L04_rf_full.tex

**Commit 3:** "Update manifest.json with 8 new L04 chart entries"
- Files: manifest.json

---

## Success Criteria

| Criterion | Metric |
|-----------|--------|
| Priority charts delivered | Charts 20 and 21 (DT/RF depth) exist and run |
| Visual coverage improved | Each .tex file gains at least 2 new visuals |
| Chart quality | All charts follow template, use ML palette, single figure |
| Compilation clean | 0 errors, 0 Overfull across all 4 .tex files |
| Cartoons effective | Each cartoon reinforces a teaching point, not just decoration |
| Manifest updated | All new charts tracked in manifest.json |

---

## Summary Statistics (Post-Plan)

| .tex File | Current Visuals | New Charts | New TikZ | Total Visuals After |
|-----------|----------------|------------|----------|---------------------|
| L04_overview.tex | 5 charts + 2 XKCD = 7 | +5 (20,21,23,25,26) | +1 (T9) | 13 |
| L04_deepdive.tex | 11 charts + 1 XKCD = 12 | +8 (20,21,22,23,24,25,26,27) | +1 (T10) | 21 |
| L04_dt_full.tex | 7 charts + 1 XKCD + 1 TikZ = 9 | +1 (20) | +1 (T11) | 11 |
| L04_rf_full.tex | 12 charts + 2 XKCD + 5 TikZ = 19 | +5 (21,22,23,24,27) | +1 (T12) | 25 |
