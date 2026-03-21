# Plan: 5 Ultra-Simple Gradient Boosting Visuals

## Context

**Request:** 5 new chart.py visualizations explaining gradient boosting simply and intuitively, with concrete numerical examples.

**Location:** `slides/L04_Random_Forests/` (charts 28-32)

**Existing boosting charts (avoid overlap):**
- `13_adaboost_staged_error/` -- AdaBoost train vs test error across rounds
- `14_gradient_boosting_residuals/` -- First residual fit (sine wave + mean + 1 tree correction)
- `15_boosting_learning_rate/` -- Test error convergence for lr=0.01, 0.1, 1.0
- `25_bagging_vs_boosting/` -- RF vs GBM test error curves

**Differentiation from existing charts:**
- Chart 14 shows ONE iteration on a sine wave. New chart 28 shows 3 iterations on simple integer data with a table.
- Chart 15 shows learning rate convergence. New chart 30 reframes as "how many trees you need" with annotated zones.
- Chart 25 shows error curves. New chart 31 is a DIAGRAM (no data), showing parallel vs sequential visually.

## Chart Style Template (mandatory for all 5)

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': '...',
    'description': '...',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/XX_name'
}
```

- `fig, ax = plt.subplots(figsize=(10, 6))`
- Save: `plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')`
- `ax.grid(False)` for diagrams (charts 31, 32). Keep grid for data plots (28, 29, 30).
- Use `plt.figtext(0.99, 0.01, CHART_METADATA['url'], ...)` for URL watermark.

## Deliverables

5 chart folders, each containing `chart.py` + generated `chart.pdf`.

## Definition of Done

- All 5 chart.py scripts run without errors
- All 5 produce chart.pdf
- Each chart is self-explanatory with title, annotations, and concrete numbers
- No subplots -- single figure per chart
- Consistent style via chart_style.py

---

## TODO 1: Chart 28 -- Fitting Residuals Step by Step

**Path:** `slides/L04_Random_Forests/28_gb_residual_steps/chart.py`

**Concept:** The core gradient boosting idea -- each tree fits the residuals of the previous ensemble.

**Visualization:** A single figure showing 4 horizontal "rows" as a visual walkthrough using ax.text and colored markers. Use matplotlib to create a clean annotated diagram (not a data plot).

**Concrete data (hardcoded, 6 data points):**
```
x =      [1,   2,   3,   4,   5,   6]
y_true = [3.0, 7.0, 5.0, 9.0, 2.0, 8.0]
```

**Layout (top to bottom on single axes):**
1. **Row 1 -- "Step 0: Initial Prediction"**: Show y_true as blue dots. Show f_0 = mean(y) = 5.67 as a horizontal dashed red line. Label: "f_0 = mean = 5.67"
2. **Row 2 -- "Step 1: Residuals"**: Show residuals r_1 = y - f_0 = [-2.67, 1.33, -0.67, 3.33, -3.67, 2.33] as orange bars. Label each bar with its value.
3. **Row 3 -- "Step 1: Tree fits residuals"**: Show h_1(x) predictions (use a simple decision stump: if x<=3 then -0.67, else 0.67 -- approximate). Show as green step function.
4. **Row 4 -- "Updated prediction"**: f_1 = f_0 + 0.1 * h_1(x). Show new predictions vs y_true. Show reduced residuals.

**Implementation approach:** Use a single axes with y-offset sections. Use `ax.text()` for labels, `ax.barh()` or `ax.bar()` for residuals, scatter for data points. Use `ax.axhspan()` with light backgrounds to separate the rows visually.

**Alternatively (simpler):** Plot the actual 1D regression across 3 iterations. X-axis = x values (1-6), Y-axis = y values. Show:
- Blue dots: true y values
- Red dashed line: f_0 = mean
- Green line: f_1 = f_0 + lr*h_1 (after 1 tree)
- Orange line: f_2 = f_1 + lr*h_2 (after 2 trees)
- Purple line: f_3 = f_2 + lr*h_3 (after 3 trees)
- Use `sklearn.ensemble.GradientBoostingRegressor` with n_estimators=1,2,3 and lr=0.3
- Annotate each line with the iteration number and MSE
- Add a text box: "Each tree corrects what the previous ensemble got wrong"

**Use the simpler alternative approach.** It is cleaner and more intuitive.

**Acceptance criteria:**
- Shows true data as scatter, mean line, and 3 progressive fit lines
- Each line labeled with iteration number
- MSE annotation decreasing per iteration
- Text box explaining the core idea

---

## TODO 2: Chart 29 -- Prediction as Sum of Weak Learners

**Path:** `slides/L04_Random_Forests/29_gb_prediction_sum/chart.py`

**Concept:** The final GBM prediction is the sum of initial prediction plus learning_rate * each tree's output.

**Visualization:** Stacked bar chart for ONE data point showing how contributions add up.

**Concrete example (hardcoded):**
Pick x=4 (where y_true=9.0). Train a GBM with 5 trees (lr=0.3, max_depth=1) on the 6-point dataset from TODO 1. Extract each tree's prediction for x=4 using `gbr.estimators_`.

**Layout:**
- Single horizontal stacked bar (or vertical stacked bar) showing:
  - Base: f_0 = mean = 5.67 (gray)
  - Tree 1 contribution: lr * h_1(4) (blue)
  - Tree 2 contribution: lr * h_2(4) (green)
  - Tree 3 contribution: lr * h_3(4) (orange)
  - Tree 4 contribution: lr * h_4(4) (purple)
  - Tree 5 contribution: lr * h_5(4) (red)
- Horizontal dashed line at y_true = 9.0
- Annotate each segment with its numerical value
- Title: "GBM Prediction = Initial + Sum of Tree Contributions"
- Subtitle/text: "y_hat = f_0 + lr*h_1(x) + lr*h_2(x) + ... = {final_value:.2f}"

**Implementation:** Use `ax.bar()` with `bottom` parameter for stacking. Extract tree predictions via:
```python
gbr = GradientBoostingRegressor(n_estimators=5, learning_rate=0.3, max_depth=1, random_state=42)
gbr.fit(X, y)
contributions = [gbr.init_.predict(X_point)[0]]  # f_0
for tree in gbr.estimators_.flatten():
    contributions.append(0.3 * tree.predict(X_point)[0])
```

**Acceptance criteria:**
- Stacked bar shows f_0 + 5 tree contributions
- Each segment labeled with its value
- Target line at y_true = 9.0
- Final prediction value annotated
- Formula shown as text on chart

---

## TODO 3: Chart 30 -- Learning Rate: Slow and Steady Wins

**Path:** `slides/L04_Random_Forests/30_gb_learning_rate_simple/chart.py`

**Concept:** Lower learning rate needs more trees but generalizes better. Ultra-simple version with annotated zones.

**Differentiation from chart 15:** Chart 15 shows raw test error curves. This chart uses a simple synthetic regression problem (not classification), adds annotated "zones" (underfitting / sweet spot / overfitting), and marks the optimal stopping point for each LR.

**Visualization:** Line plot, X = number of trees (1-300), Y = test MSE.

**Data:** Use `make_regression` with n_samples=200, noise=20. Train/test split 70/30. Three GBR models: lr=0.5, lr=0.1, lr=0.01. Use `staged_predict` to get MSE at each iteration.

**Layout:**
- 3 curves: lr=0.5 (MLRED), lr=0.1 (MLGREEN), lr=0.01 (MLBLUE)
- Mark minimum test MSE point on each curve with a star marker
- Annotate each star: "Best at N trees"
- Add vertical shaded region where lr=0.5 overfits (test MSE rising) in light red
- Text box: "Lower learning rate = more trees needed, but better generalization"
- Title: "Learning Rate: Slow and Steady Wins"

**Acceptance criteria:**
- 3 clearly distinct curves
- Minimum marked with star on each
- Overfitting region shaded for high LR
- Text box with takeaway message
- Uses regression (MSE), not classification (differentiates from chart 15)

---

## TODO 4: Chart 31 -- GBM vs Random Forest: Sequential vs Parallel

**Path:** `slides/L04_Random_Forests/31_gb_vs_rf_diagram/chart.py`

**Concept:** RF builds trees independently (parallel), GBM builds sequentially (each corrects errors).

**Differentiation from chart 25:** Chart 25 shows error curves. This is a DIAGRAM with no data -- purely conceptual.

**Visualization:** A side-by-side diagram using matplotlib patches, arrows, and text. NO grid (`ax.grid(False)`, `ax.axis('off')`).

**Layout (left half = RF, right half = GBM):**

LEFT SIDE -- "Random Forest":
- Title at top: "Random Forest" in MLBLUE
- Subtitle: "Trees built independently"
- 3 tree boxes (rectangles) labeled "Tree 1", "Tree 2", "Tree 3" arranged vertically
- All 3 start from a single "Training Data" box at top (arrows going down in parallel)
- All 3 feed into a "Majority Vote / Average" box at bottom (arrows going down)
- Arrow from average box to "Final Prediction"

RIGHT SIDE -- "Gradient Boosting":
- Title at top: "Gradient Boosting" in MLORANGE
- Subtitle: "Trees built sequentially"
- "Training Data" box at top
- Arrow down to "Tree 1" box
- Arrow from Tree 1 to "Residuals 1" (small text)
- Arrow from Residuals 1 to "Tree 2" box
- Arrow from Tree 2 to "Residuals 2"
- Arrow from Residuals 2 to "Tree 3" box
- All trees feed into "Weighted Sum" box at bottom
- Arrow to "Final Prediction"

Use `matplotlib.patches.FancyBboxPatch` for boxes, `ax.annotate` with arrowprops for arrows.

**Acceptance criteria:**
- Two clearly separated sections (RF left, GBM right)
- RF shows parallel structure, GBM shows sequential chain
- "Residuals" labeled between GBM trees
- No data, purely diagrammatic
- ax.grid(False) and ax.axis('off')

---

## TODO 5: Chart 32 -- Train vs Test Error: When to Stop

**Path:** `slides/L04_Random_Forests/32_gb_early_stopping/chart.py`

**Concept:** As you add more trees, training error keeps dropping but test error eventually rises. Early stopping catches the sweet spot.

**Visualization:** Classic train/test error plot with annotated early stopping point.

**Data:** Use `make_regression` with n_samples=300, noise=15, n_features=10. Train GBR with n_estimators=500, lr=0.1, max_depth=3. Use `staged_predict` for both train and test MSE.

**Layout:**
- Blue line: training MSE (keeps decreasing)
- Red line: test MSE (decreases then rises)
- Vertical dashed green line at the minimum of test MSE = early stopping point
- Left of green line: light green shaded region labeled "Underfitting zone"
- Right of green line: light red shaded region labeled "Overfitting zone"
- Star marker at the minimum test MSE point
- Annotation arrow pointing to star: "Early stopping here\nTest MSE = {value:.2f}\nn_trees = {n}"
- Text box: "More trees always reduce training error, but test error rises after the sweet spot"
- Title: "Gradient Boosting: When to Stop Adding Trees"

**Acceptance criteria:**
- Train error monotonically decreasing
- Test error shows U-shape (decrease then increase)
- Early stopping point clearly marked
- Under/overfitting zones shaded
- Annotation with exact MSE value and tree count

---

## Task Flow

All 5 charts are independent -- can be built in any order or in parallel.

```
TODO 1 (chart 28) ─┐
TODO 2 (chart 29) ─┤
TODO 3 (chart 30) ─┼─> Verify all 5 run ─> Commit
TODO 4 (chart 31) ─┤
TODO 5 (chart 32) ─┘
```

## Verification Step

After all 5 charts are created, run each one:
```bash
cd D:/Joerg/Research/slides/Methods_and_Algorithms
python slides/L04_Random_Forests/28_gb_residual_steps/chart.py
python slides/L04_Random_Forests/29_gb_prediction_sum/chart.py
python slides/L04_Random_Forests/30_gb_learning_rate_simple/chart.py
python slides/L04_Random_Forests/31_gb_vs_rf_diagram/chart.py
python slides/L04_Random_Forests/32_gb_early_stopping/chart.py
```

Verify each produces `chart.pdf` without errors.

## Commit Strategy

Single commit after all 5 pass verification:
```
Add 5 ultra-simple gradient boosting explanation charts (28-32)
```

Files to commit:
- `slides/L04_Random_Forests/28_gb_residual_steps/chart.py`
- `slides/L04_Random_Forests/28_gb_residual_steps/chart.pdf`
- `slides/L04_Random_Forests/29_gb_prediction_sum/chart.py`
- `slides/L04_Random_Forests/29_gb_prediction_sum/chart.pdf`
- `slides/L04_Random_Forests/30_gb_learning_rate_simple/chart.py`
- `slides/L04_Random_Forests/30_gb_learning_rate_simple/chart.pdf`
- `slides/L04_Random_Forests/31_gb_vs_rf_diagram/chart.py`
- `slides/L04_Random_Forests/31_gb_vs_rf_diagram/chart.pdf`
- `slides/L04_Random_Forests/32_gb_early_stopping/chart.py`
- `slides/L04_Random_Forests/32_gb_early_stopping/chart.pdf`

## Success Criteria

- [ ] 5 chart.py files created in correct directories
- [ ] All 5 run without errors and produce chart.pdf
- [ ] Each chart explains ONE gradient boosting concept
- [ ] Each uses concrete numbers (not abstract)
- [ ] Each is self-explanatory (title + annotations + labels)
- [ ] Consistent style via chart_style.py
- [ ] No overlap with existing charts 13, 14, 15, 25
