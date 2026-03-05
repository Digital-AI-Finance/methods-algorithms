# Plan: L04 Simple Visual Notebooks (Decision Trees + Random Forests)

## Task
Create two simple, visual-heavy Jupyter notebooks for L04: one for Decision Trees, one for Random Forests. Follow the L03 split-notebook pattern (`L03_knn.ipynb`, `L03_kmeans.ipynb`). Update GH Pages with links.

## Current State

### Existing L04 Notebook
- `notebooks/L04_random_forests.ipynb` — 25 cells, comprehensive, covers both DT and RF together, uses fraud detection dataset (1000 samples, 8 features), includes exercises with solutions, feature importance, OOB error, ROC curves, confusion matrices

### L03 Split Pattern (template)
- `notebooks/L03_knn_kmeans.ipynb` — combined (like existing L04)
- `notebooks/L03_knn.ipynb` — visual-heavy, simple, 19 cells, uses `make_classification(n_features=2)` for 2D visualization, ML color palette, 8 visuals
- `notebooks/L03_kmeans.ipynb` — visual-heavy, simple, same pattern

### GH Pages (docs/index.html)
- L03 section: 3 notebook links (Combined, KNN, K-Means) with labels "Visual-heavy KNN" etc.
- L04 section (line 261): 1 notebook link ("Colab Notebook")
- Hero stat (line 126): `<b>8</b><small>Notebooks</small>` — will become 10 after adding 2

---

## Proposed New Notebooks

### 1. `notebooks/L04_dt.ipynb` — Decision Trees (Visual-Heavy)

**Target**: ~18 cells (8 markdown + 10 code), ~8 visuals, simple 2D data

**Structure**:

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | MD | Title + Colab badge + 4 learning objectives | — |
| 2 | Code | Setup: imports, ML palette, rcParams, seed | — |
| 3 | MD | "1. Generate Data" | — |
| 4 | Code | `make_classification(n_samples=200, n_features=2, n_redundant=0, random_state=42)`, train/test split, scatter plot of 2D data | Visual 1: Scatter plot |
| 5 | MD | "2. How a Decision Tree Splits" | — |
| 6 | Code | Fit `DecisionTreeClassifier(max_depth=2)`, plot decision boundary with data overlay, annotate split lines | Visual 2: Decision boundary (depth=2) |
| 7 | Code | `plot_tree()` of the depth-2 tree with feature names, filled colors | Visual 3: Tree structure |
| 8 | MD | "3. Effect of Tree Depth" | — |
| 9 | Code | 3-panel: decision boundaries for max_depth=1, 3, None (full) — shows bias-variance tradeoff visually | Visual 4: Depth comparison (3 panels) |
| 10 | Code | Train/test accuracy vs max_depth (1–15), two lines, shade underfitting/overfitting zones | Visual 5: Bias-variance curve |
| 11 | MD | "4. Gini Impurity" | — |
| 12 | Code | Plot Gini = 2p(1-p) and Entropy = -p*log(p)-(1-p)*log(1-p) curves for p in [0,1], annotate pure/impure | Visual 6: Gini vs Entropy curves |
| 13 | MD | "5. Regression Trees" | — |
| 14 | Code | 1D regression data (sin + noise), fit depth-1 and depth-5 trees, plot predictions as step functions vs true curve | Visual 7: Regression tree predictions |
| 15 | MD | "6. Pruning with Cost-Complexity" | — |
| 16 | Code | Train/CV accuracy vs ccp_alpha, mark optimal alpha | Visual 8: Pruning curve |
| 17 | MD | Summary: 4 bullet points | — |

**Design principles**:
- ALL data is 2D (2 features) for easy scatter/boundary visualization
- NO fraud dataset, NO 8 features — keep it simple
- ML color palette throughout (MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE)
- Every code cell either produces a visual or prints 2-3 lines of output
- No exercises (this is "visual-heavy simple", not the main exercises notebook)

### 2. `notebooks/L04_rf.ipynb` — Random Forests (Visual-Heavy)

**Target**: 19 cells (7 markdown + 12 code), 9 visuals, same 2D data pattern

**Structure**:

| # | Type | Content | Visual? |
|---|------|---------|---------|
| 1 | MD | Title + Colab badge + 4 learning objectives | — |
| 2 | Code | Setup: imports, ML palette, rcParams, seed | — |
| 3 | MD | "1. The Problem with Single Trees" | — |
| 4 | Code | Train 5 trees on different bootstrap samples, overlay all 5 decision boundaries → shows HIGH VARIANCE | Visual 1: 5 different tree boundaries |
| 5 | MD | "2. Bootstrap Sampling" | — |
| 6 | Code | Show original dataset and 3 bootstrap samples side-by-side, highlight which points are sampled (some repeated, some missing) | Visual 2: Bootstrap visualization |
| 7 | MD | "3. Random Forest: Averaging Reduces Variance" | — |
| 8 | Code | Decision boundary from RF (n_estimators=100) — smooth, stable, overlaid with data | Visual 3: RF boundary (smooth) |
| 9 | Code | Compare single tree boundary vs RF boundary side-by-side | Visual 4: Tree vs RF (2 panels) |
| 10 | MD | "4. How Many Trees?" | — |
| 11 | Code | OOB error vs n_estimators (1–200), show convergence | Visual 5: OOB error curve |
| 12 | MD | "5. Feature Importance" | — |
| 13 | Code | Use `make_classification(n_features=8, n_informative=4)` for this one cell, horizontal bar chart of MDI importance | Visual 6: Feature importance bars |
| 14 | MD | "6. Boosting: Sequential Correction" | — |
| 15 | Code | AdaBoost staged train/test error curve (matching chart 13 from slides) | Visual 7: AdaBoost convergence |
| 16 | Code | GradientBoosting test error for 3 learning rates (matching chart 15) | Visual 8: Learning rate effect |
| 17 | MD | "7. Random Forest vs Boosting" | — |
| 18 | Code | Bar chart comparing test accuracy of: single tree, RF(100), AdaBoost(50), GBR(100) on the 2D dataset | Visual 9: Model comparison |
| 19 | MD | Summary: 4 bullet points | — |

**Design principles**:
- Same 2D dataset as DT notebook for consistency (except feature importance cell)
- Bootstrap visualization is key — students must SEE how sampling works
- Side-by-side comparisons (tree vs RF) are the core teaching tool
- Boosting included because it's part of L04 lecture content
- No exercises

---

## GH Pages Updates

### docs/index.html changes

1. **Hero stat** (line 126): `<b>8</b><small>Notebooks</small>` → `<b>10</b><small>Notebooks</small>`

2. **L04 section** (around line 261): Add 2 new notebook links AFTER the existing Colab Notebook link:
```html
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L04_dt.ipynb" target="_blank"><div class="ccard-icon">NB</div>DT Notebook<div class="ccard-label">Visual-heavy DT</div></a>
<a class="ccard" href="https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L04_rf.ipynb" target="_blank"><div class="ccard-icon">NB</div>RF Notebook<div class="ccard-label">Visual-heavy RF</div></a>
```

3. **Relabel existing notebook** (line 261): Change "Colab Notebook" to "Combined Notebook" and label to "DT + RF Combined" (matching L03 pattern)

### manifest.json changes

Add 2 new notebook entries to the L04 assets. Currently L04 has:
```json
"notebook": {
    "file": "notebooks/L04_random_forests.ipynb",
    "status": "complete"
}
```

Add two new keys alongside the existing `"notebook"` key:
```json
"notebook_dt": {
    "file": "notebooks/L04_dt.ipynb",
    "status": "complete"
},
"notebook_rf": {
    "file": "notebooks/L04_rf.ipynb",
    "status": "complete"
}
```
Note: L03 split notebooks are NOT tracked in manifest.json, so this is a new addition for L04.

---

## Implementation Steps

### Step 1: Create `notebooks/L04_dt.ipynb`
- 18 cells as specified above
- Use `make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2, flip_y=0.1, random_state=42)` for the main dataset
- ML color palette, figsize=(10,6), font.size=12
- Colab badge URL: `https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L04_dt.ipynb`
- 8 visuals, no exercises, no fraud dataset

### Step 2: Create `notebooks/L04_rf.ipynb`
- 19 cells as specified above
- Same `make_classification` dataset (with `flip_y=0.1`) for consistency
- ML color palette, figsize=(10,6), font.size=12
- Colab badge URL: `https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L04_rf.ipynb`
- 9 visuals, no exercises, no fraud dataset

### Step 3: Test both notebooks
- Run all cells in both notebooks to verify they execute without errors
- Verify all visuals render correctly

### Step 4: Update docs/index.html
- Hero stat: 8 → 10 notebooks
- L04 section: relabel existing + add 2 new notebook cards
- Follow L03 pattern exactly

### Step 5: Update manifest.json
- Add 2 new notebook entries for L04

### Step 6: Git commit and push

---

## Acceptance Criteria

1. `notebooks/L04_dt.ipynb` exists with ~18 cells and ~8 visuals
2. `notebooks/L04_rf.ipynb` exists with ~19 cells and ~8-9 visuals
3. Both notebooks use ML color palette (MLBLUE #0066CC, MLORANGE #FF7F0E, etc.)
4. Both notebooks use 2D data for visualization (no complex multi-feature datasets except feature importance)
5. Both notebooks execute without errors
6. Both notebooks have Colab badges with correct URLs
7. No exercises — these are "visual-heavy simple" notebooks
8. docs/index.html hero stat updated (8 → 10 notebooks)
9. docs/index.html L04 section has 3 notebook links (Combined, DT, RF)
10. manifest.json updated with 2 new entries
11. Changes committed and pushed to master

---

## Risk Assessment

| Risk | Mitigation |
|---|---|
| 2D data may not show RF advantage clearly | Use `flip_y=0.1` to add noise — RF should outperform single tree |
| Bootstrap visualization may be confusing | Use color-coding: sampled=solid, not-sampled=faded, duplicates=highlighted |
| Too many cells for "simple" | Hard cap at 19 cells per notebook — if approaching limit, merge cells |
| Boosting section in RF notebook may feel out of place | Frame it as "From Bagging to Boosting" to connect concepts |

---

PLAN_READY: .omc/plans/l04-simple-notebooks.md
