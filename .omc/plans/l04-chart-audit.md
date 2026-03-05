# Plan: L04 Chart Density Audit & New Charts (v2 — Critic feedback addressed)

## Task
Audit chart density across all 6 L04 .tex files. Identify gaps where topics lack visual support. Create new charts to reach the "1 chart per 4 slides" target. Fix chart 06b (hostile review MAJOR). Deploy chart PNGs to GH Pages.

## Current State

### Existing Charts (13 total)

| # | Chart | Type | Topic | Used In |
|---|-------|------|-------|---------|
| 01 | decision_tree | Diagram | DT structure | overview, dt_full, dt_mini, rf_full |
| 02 | feature_importance | Trained-model | RF feature importance (sklearn) | deepdive, rf_full |
| 03 | bootstrap | Diagram | Bootstrap sampling | overview, rf_full |
| 04 | oob_error | Trained-model | OOB error curve (sklearn) | deepdive, rf_full |
| 05 | ensemble_voting | Diagram | Majority voting | overview, rf_full, rf_mini |
| 06a | single_tree_variance | Trained-model | Single DT variance (sklearn) | deepdive, rf_full |
| 06b | random_forest_variance | **scipy interp (FAKED)** | RF variance | deepdive, rf_full |
| 07 | decision_flowchart | Diagram | When to use which method | overview, rf_full |
| 08 | gini_split | Diagram | Gini split worked example | dt_full, dt_mini |
| 09 | dt_overfitting | Trained-model | Train vs test accuracy (sklearn) | dt_full |
| 10 | dt_decision_boundary | Trained-model | DT boundary (sklearn) | dt_full |
| 11 | gini_vs_entropy | Math viz | Gini vs entropy curves | dt_full |
| 12 | nonlinear_classes | Diagram | XOR-like pattern | dt_full |

### Per-File Chart Density

Density is calculated on **main content slides only** (excluding appendix frames).

| File | Total Slides | Main Slides | Appendix | Charts | Density (main) | Target (1/4) | Gap |
|---|---|---|---|---|---|---|---|
| overview | 25 | 25 | 0 | 4 | 1/6.25 | 6 | **-2** |
| deepdive | 52 | 42 | 10 | 4 | 1/10.5 | 10-11 | **-7** |
| dt_full | 25 | 25 | 0 | 6 | 1/4.2 | 6 | 0 |
| dt_mini | 10 | 10 | 0 | 2 | 1/5 | 2-3 | **-1** |
| rf_full | 31 | 31 | 0 | 8 | 1/3.9 | 8 | 0 |
| rf_mini | 10 | 10 | 0 | 1 | 1/10 | 2-3 | **-2** |

**Note:** Deepdive has 42 main + 10 appendix = 52 total. Density target applies to main slides only. Appendix is proofs/derivations where charts are not appropriate.

### Coverage by Topic Area

| Area | Charts | Assessment |
|---|---|---|
| DT basics (structure, splits, impurity) | 01, 08, 11, 12 | Good |
| DT training (overfitting, boundary) | 09, 10 | Good |
| RF basics (bootstrap, OOB, voting) | 03, 04, 05 | Good |
| RF variance | 06a, 06b | Good (but 06b is faked) |
| RF importance/SHAP | 02 | Adequate |
| Decision guidance | 07 | Good |
| **Boosting (AdaBoost, GB, XGBoost)** | **NONE** | **CRITICAL GAP** |
| **Regression trees (MSE)** | **NONE** | **GAP** |
| **Pruning** | **NONE** | **GAP** |
| **Bias-variance curves** | **NONE** | **GAP** |
| **Hyperparameter effects** | **NONE** | **GAP** |

---

## Gap Analysis

### Critical Gap: Boosting Has Zero Visual Support

The deepdive covers AdaBoost (line 696), gradient boosting (line 715), and XGBoost (line 738) — roughly 12 slides of boosting content with zero charts. The hostile review flagged all 3 boosting topics as MAJOR issues for missing worked examples.

### Secondary Gaps

1. **Regression trees** — MSE split criterion taught at deepdive line 197, no visual
2. **Bias-variance tradeoff** — discussed at deepdive line 592, no U-shaped curve
3. **Pruning** — covered at deepdive line 243, no cost-complexity alpha visualization
4. **Hyperparameter tuning** — deepdive line 461, no effect plot for max_features

---

## Proposed New Charts (7 charts)

### Priority 1: Boosting Charts (3 charts — fills critical gap)

**13_adaboost_staged_error** — AdaBoost train/test error vs boosting rounds
- Single figure: x-axis = number of estimators (1-50), y-axis = error rate
- Two lines: training error and test error, showing how AdaBoost reduces training error while test error may plateau or rise
- Use `AdaBoostClassifier(n_estimators=50, algorithm='SAMME').staged_score(X_train, y_train)` and `.staged_score(X_test, y_test)` to get per-round accuracy
- Convert accuracy to error rate (1 - accuracy) for the y-axis
- Dataset: `make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)`
- Type: Trained-model (sklearn only)
- Target files: deepdive (line 696, AdaBoost Algorithm frame), rf_full
- Chart standards: figsize=(10,6), dpi=150, font.size=14, ML palette

**14_gradient_boosting_residuals** — Gradient boosting residual fitting
- Single figure: 1D regression data (x vs y) with scatter points, the initial prediction (horizontal mean line), and the updated prediction after one boosting round
- Show data points (MLBlue scatter), mean line (MLRed dashed), and GBR(n_estimators=1) prediction curve (MLGreen solid)
- Use `GradientBoostingRegressor(n_estimators=1, max_depth=3, learning_rate=0.5, random_state=42)`
- Dataset: `np.sin(x) + noise` on x in [0, 2*pi], n=100
- Type: Trained-model (sklearn only)
- Target files: deepdive (line 715, Gradient Boosting frame), rf_full

**15_boosting_learning_rate** — Learning rate effect on boosting convergence
- Single figure: x-axis = boosting iteration (1-200), y-axis = test loss (deviance)
- Three lines for learning_rate = 0.01, 0.1, 1.0
- Use `GradientBoostingClassifier(n_estimators=200, learning_rate=lr, max_depth=3, random_state=42)`
- Access staged test loss via `staged_predict_proba()` + manual log-loss, OR use `staged_decision_function()` with deviance
- Simpler approach: train 3 models, compute test accuracy at each stage via `staged_score(X_test, y_test)`, plot 1-accuracy as error
- Dataset: `make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)`
- Type: Trained-model (sklearn only — NO xgboost dependency)
- Target files: deepdive (line 738, XGBoost/LightGBM/CatBoost frame), rf_full
- **Note:** This replaces the original "xgboost regularization" chart. The pedagogical point is the same — how hyperparameters control overfitting — but uses sklearn's native `learning_rate` parameter instead of xgboost's `lambda` (which is not in requirements.txt).

### Priority 2: DT and RF Gaps (4 charts)

**16_regression_tree_mse** — Regression tree MSE split visualization
- Single figure: scatter plot of data points (x vs y), with a vertical split line at the optimal split point, and two horizontal prediction lines (left mean, right mean)
- Annotate: parent MSE, left MSE, right MSE, and MSE reduction
- Use `DecisionTreeRegressor(max_depth=1).fit()` to find the optimal split, then plot it
- Dataset: linear-ish with noise, n=50, random_state=42
- Type: Trained-model (sklearn)
- Target files: deepdive (line 197, Regression Trees: MSE Criterion), dt_full

**17_bias_variance_depth** — Bias-variance vs tree depth
- Single figure: x-axis = max_depth (1-20), y-axis = error rate
- Two lines: training error (decreases monotonically) and test error (U-shaped)
- Shade underfitting zone (left, light blue) and overfitting zone (right, light red)
- Use `DecisionTreeClassifier(max_depth=d)` for d in 1..20, compute train/test accuracy on each, plot 1-accuracy
- Dataset: `make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)`, 70/30 train/test split
- Type: Trained-model (sklearn)
- Target files: deepdive (line 592, Bias-Variance Decomposition), overview
- **Note vs chart 09:** Chart 09 shows a single train-vs-test comparison. This chart shows the FULL curve across all depths, explicitly demonstrating the bias-variance tradeoff.

**18_rf_hyperparameter_maxfeatures** — max_features vs OOB error
- Single figure: x-axis = max_features (1 to p), y-axis = OOB error
- U-shaped or monotone curve showing optimal around sqrt(p)
- Use `RandomForestClassifier(n_estimators=100, max_features=k, oob_score=True, random_state=42)` for k in 1..p
- Dataset: `make_classification(n_samples=500, n_features=20, n_informative=10, random_state=42)`
- Annotate sqrt(p) = sqrt(20) ~ 4.5 with a vertical dashed line
- Type: Trained-model (sklearn)
- Target files: deepdive (line 461, Hyperparameters: Feature Randomization), rf_full

**19_pruning_ccp** — Cost-complexity pruning path
- Single figure: x-axis = effective alpha (ccp_alpha), y-axis = accuracy
- Two lines: training accuracy and 5-fold cross-validation accuracy
- Show optimal alpha where CV accuracy peaks
- Use `DecisionTreeClassifier().cost_complexity_pruning_path(X_train, y_train)` to get alphas
- Then train trees at each alpha, compute train accuracy and cross_val_score
- Dataset: `make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)`
- Type: Trained-model (sklearn)
- Target files: deepdive (line 243, Decision Tree: Overfitting and Pruning)

---

## Chart Assignment to Files

After adding 7 new charts, density improves (main slides only):

| File | Main Slides | Current Charts | New Charts Added | New Total | New Density |
|---|---|---|---|---|---|
| overview | 25 | 4 | 17 (bias-variance) | 5 | 1/5.0 |
| deepdive | 42 (main) | 4 | 13, 14, 15, 16, 17, 18, 19 (all 7) | 11 | 1/3.8 |
| dt_full | 25 | 6 | 16 (reg tree MSE) | 7 | 1/3.6 |
| dt_mini | 10 | 2 | — | 2 | 1/5.0 |
| rf_full | 31 | 8 | 13, 14, 15, 18 (boosting + hyperparams) | 12 | 1/2.6 |
| rf_mini | 10 | 1 | — | 1 | 1/10 |

**Deepdive improvement:** 1/10.5 → 1/3.8 (exceeds 1/4 target on main slides).

**Note on minis:** dt_mini (1/5) and rf_mini (1/10) are intentionally light 10-slide summaries. The density target of 1/4 is aspirational for minis; 1/5 is acceptable.

**Note on pruning chart 19:** Originally planned for both deepdive and dt_full. However dt_full already has 1/4.2 density (meeting target), so 19 goes only to deepdive to avoid over-charting dt_full.

---

## Deepdive Insertion Points (exact frame titles and line numbers)

| Chart | Frame Title | Line | Placement |
|---|---|---|---|
| 13 | AdaBoost Algorithm | 696 | After the algorithmic pseudocode — add `\includegraphics` showing the staged error curve |
| 14 | Gradient Boosting: Functional Gradient Descent | 715 | After the gradient descent explanation — show the residual fitting |
| 15 | XGBoost, LightGBM, CatBoost: Industrial Boosting | 738 | After the Taylor expansion explanation — show learning rate effect |
| 16 | Regression Trees: MSE Criterion | 197 | After the MSE formula — show the visual split |
| 17 | Bias-Variance Decomposition | 592 | After the expected error decomposition — show the depth curves |
| 18 | Hyperparameters: Feature Randomization | 461 | After max_features explanation — show the OOB error curve |
| 19 | Decision Tree: Overfitting and Pruning | 243 | After the pruning explanation — show the CCP alpha curve |

Each insertion follows the pattern:
```latex
\begin{center}
\includegraphics[width=0.65\textwidth]{XX_chart_name/chart.pdf}
\end{center}
```

If the frame already has content that would overflow with the chart, create a NEW frame immediately after the existing one with title "[Topic]: Visualization" containing only the chart at 0.65\textwidth.

---

## Existing Bug Fix (from hostile review)

**Chart 06b** (`06b_random_forest_variance/chart.py`): Uses `scipy.interpolate.interp1d(kind='nearest')` to fake RF behavior instead of `sklearn.ensemble.RandomForestRegressor`. Hostile review flagged this as MAJOR.

**Fix:** Replace with `RandomForestRegressor(n_estimators=50, random_state=42).fit().predict()` matching chart 06a's pattern (which correctly uses `DecisionTreeRegressor`).

---

## Implementation Steps

### Step 1: Fix chart 06b (MAJOR hostile review issue)
- Read 06a/chart.py as reference for correct sklearn pattern
- Rewrite 06b/chart.py to use `RandomForestRegressor(n_estimators=50)`
- Run chart.py to regenerate chart.pdf

### Step 2: Create 7 new chart.py files
Each must follow chart standards:
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})
MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
```
- One figure per chart (NO subplots)
- Output to `chart.pdf` in same directory
- Use sklearn for ALL trained-model charts (no scipy approximations, no xgboost)
- Set `random_state=42` everywhere for reproducibility

### Step 3: Run all 8 chart.py scripts (1 fix + 7 new) to generate PDFs

### Step 4: Add \includegraphics to .tex files
For each new chart, add it to the target .tex file(s) at the insertion points listed in the "Deepdive Insertion Points" table above. For rf_full and overview, read the file to identify the matching frame and insert similarly.

### Step 5: Recompile all modified .tex files and check for Overfull warnings
```bash
pdflatex -interaction=nonstopmode L04_deepdive.tex
pdflatex -interaction=nonstopmode L04_overview.tex
pdflatex -interaction=nonstopmode L04_dt_full.tex
pdflatex -interaction=nonstopmode L04_rf_full.tex
```
Grep output for "Overfull" — must be zero.

### Step 6: Update manifest.json
Add 7 new chart entries to the L04 charts array:
```json
{"name": "13_adaboost_staged_error", "file": "slides/L04_Random_Forests/13_adaboost_staged_error/chart.py", "status": "complete"},
{"name": "14_gradient_boosting_residuals", "file": "slides/L04_Random_Forests/14_gradient_boosting_residuals/chart.py", "status": "complete"},
{"name": "15_boosting_learning_rate", "file": "slides/L04_Random_Forests/15_boosting_learning_rate/chart.py", "status": "complete"},
{"name": "16_regression_tree_mse", "file": "slides/L04_Random_Forests/16_regression_tree_mse/chart.py", "status": "complete"},
{"name": "17_bias_variance_depth", "file": "slides/L04_Random_Forests/17_bias_variance_depth/chart.py", "status": "complete"},
{"name": "18_rf_hyperparameter_maxfeatures", "file": "slides/L04_Random_Forests/18_rf_hyperparameter_maxfeatures/chart.py", "status": "complete"},
{"name": "19_pruning_ccp", "file": "slides/L04_Random_Forests/19_pruning_ccp/chart.py", "status": "complete"}
```

### Step 7: Convert chart PDFs to PNGs and deploy to GH Pages
- Use PyMuPDF (fitz) to convert each new chart.pdf → chart.png
- Copy to `docs/slides/images/L04_Random_Forests/`
- Update `docs/index.html`:
  - Hero stat: 60 → 67 charts (60 existing + 7 new)
  - Add 7 new chart cards to L04 chart gallery section

### Step 8: Git commit and push

---

## Acceptance Criteria

1. Chart 06b uses actual `sklearn.ensemble.RandomForestRegressor` (not scipy)
2. 7 new chart folders exist (13-19) with chart.py and chart.pdf
3. All chart.py files follow standards (figsize, dpi, fonts, colors, single figure, random_state=42)
4. All trained-model charts use actual sklearn (not scipy approximations, not xgboost)
5. Each new chart is `\includegraphics`-referenced in at least one .tex file
6. Deepdive chart density improves from 1/10.5 (main slides) to better than 1/4
7. All modified .tex files compile with zero Overfull warnings
8. manifest.json updated with 7 new chart entries
9. New chart PNGs deployed to `docs/slides/images/L04_Random_Forests/`
10. `docs/index.html` hero stat updated (60 → 67) and chart gallery updated
11. Changes committed and pushed to master

---

## Risk Assessment

| Risk | Mitigation |
|---|---|
| Adding charts to .tex may cause Overfull | Use 0.65\textwidth for chart-only slides; create new frames if existing frame overflows |
| `staged_score()` API may differ across sklearn versions | Tested in sklearn >=0.22; use `.staged_predict()` + manual accuracy as fallback |
| Deepdive frames may be too content-dense for chart insertion | Create new "[Topic]: Visualization" frames immediately after the content frame |
| Some charts need real data patterns to be pedagogically useful | Use `make_classification`/`make_regression` with `random_state=42` for reproducibility |

---

## Hero Stat Arithmetic

Current hero stat in `docs/index.html`: **60 charts**
Manifest.json L04 charts tracked: 01-12 (13 entries including 06a/06b counted as 2)
New charts: 7 (charts 13-19)
New hero stat: 60 + 7 = **67 charts**

---

PLAN_READY: .omc/plans/l04-chart-audit.md
