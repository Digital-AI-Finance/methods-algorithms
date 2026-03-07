# Plan: Top 10 Essential DT & RF Charts — Standalone Lecture

## Context

### Original Request
Create one standalone lecture with 10 Python-generated charts representing the most common, most useful visualizations for Decision Trees and Random Forests. All charts use synthetic data. Brainstorm what the top 10 charts should be. PLAN ONLY.

### Brainstorm: What Are the 10 Most Common/Useful DT & RF Charts?

Every ML textbook, Kaggle tutorial, and university course on DT/RF features a core set of visualizations. After surveying the pedagogical canon (ISL, ESL, Hastie/Tibshirani, scikit-learn docs, fast.ai, Hands-On ML):

| Rank | Chart | Why It's Essential | DT or RF |
|------|-------|--------------------|----------|
| 1 | **Decision Boundary (2D)** | The single most iconic DT visual — axis-aligned splits carving up feature space | DT |
| 2 | **Depth vs Train/Test Error** | The core bias-variance lesson: shallow=underfit, deep=overfit | DT |
| 3 | **DT Regression Step Function** | Shows piecewise-constant nature of DT vs smooth truth | DT |
| 4 | **Gini Impurity & Entropy vs p** | The mathematical heart of splitting criteria | DT |
| 5 | **Tree Structure Visualization** | The literal tree — nodes, splits, Gini values. THE most recognizable DT image in any textbook. | DT |
| 6 | **Feature Importance (RF)** | The #1 reason practitioners use RF — "which features matter?" | RF |
| 7 | **OOB Error Convergence vs n_trees** | The unique RF "free CV" story | RF |
| 8 | **DT vs RF Decision Boundary** | Side-by-side showing noisy DT vs smooth RF — the ensemble "aha moment" | Both |
| 9 | **Effect of max_features on RF** | The key RF hyperparameter — decorrelation sweet spot | RF |
| 10 | **Partial Dependence Plot** | How one feature affects predictions — the modern interpretability standard | RF |

### Why This Specific 10?

**Selection criteria:**
- **Frequency**: Appears in ≥3 major ML textbooks
- **DT/RF-specific**: Must be inherently about trees/forests (not generic to all classifiers)
- **Balance**: 5 DT-focused, 4 RF-focused, 1 both
- **Progression**: Builds from tree mechanics → overfitting → ensemble fix → interpretation
- **Synthetic data**: All can be generated with sklearn or numpy

### What Was Deliberately Excluded (and Why)

| Chart | Why Excluded |
|-------|-------------|
| Confusion matrix | Generic to ALL classifiers, not DT/RF-specific |
| ROC / PR curve | Same reason — applies to any classifier |
| SHAP waterfall | Important but specialized; not in most intro DT/RF lectures |
| Boosting (AdaBoost, GBM) | Different algorithm family — dilutes DT/RF focus |
| SMOTE visualization | Pre-processing, not DT/RF core |
| Bootstrap sampling scatter | Better taught as a diagram/schematic than a data plot |
| Permutation importance | Useful but MDI is more canonical in intro courses |

### Overlap with Existing Charts — Curated Reuse Strategy

**Critical design decision:** L04 already has 28 chart folders (01-27 + 06a/06b). Seven of the "top 10" canonical charts already exist as high-quality chart.py + chart.pdf files. Rather than creating near-identical duplicates, this lecture **reuses existing chart.pdf files** and creates **3 genuinely new charts** for concepts not yet visualized.

| Rank | Chart | Existing? | Action |
|------|-------|-----------|--------|
| C1 | Decision Boundary | `10_dt_decision_boundary/chart.pdf` | **REUSE** existing |
| C2 | Depth vs Error | `17_bias_variance_depth/chart.pdf` | **REUSE** existing |
| C3 | DT Regression Step | `16_regression_tree_mse/chart.pdf` | **REUSE** existing (shows MSE fit) |
| C4 | Gini vs Entropy | `11_gini_vs_entropy/chart.pdf` | **REUSE** existing |
| C5 | Tree Structure | None | **NEW** — `top10_05_tree_structure/chart.py` |
| C6 | Feature Importance | `02_feature_importance/chart.pdf` | **REUSE** existing |
| C7 | OOB Convergence | `27_rf_ntrees_convergence/chart.pdf` | **REUSE** existing |
| C8 | DT vs RF Boundary | None (06a/06b are separate, not side-by-side) | **NEW** — `top10_08_dt_vs_rf_boundary/chart.py` |
| C9 | max_features Effect | `18_rf_hyperparameter_maxfeatures/chart.pdf` | **REUSE** existing |
| C10 | Partial Dependence | None | **NEW** — `top10_10_partial_dependence/chart.py` |

**Rationale**: Creating 7 duplicate chart.py files that produce visually identical output to existing charts wastes effort and storage. The existing charts already follow the rcParams template and ML color palette. The 3 new charts fill genuine gaps: tree visualization, side-by-side boundary comparison, and partial dependence.

### File Structure

```
slides/L04_Random_Forests/
  L04_dt_rf_top10.tex                      # New standalone lecture
  top10_05_tree_structure/chart.py          # NEW: sklearn.tree.plot_tree
  top10_08_dt_vs_rf_boundary/chart.py       # NEW: side-by-side boundary
  top10_10_partial_dependence/chart.py       # NEW: PDP
```

The .tex file references existing chart.pdf paths for the 7 reused charts and the 3 new `top10_*/chart.pdf` paths.

---

## Work Objectives

### Core Objective
Create a self-contained Beamer lecture (L04_dt_rf_top10.tex) that curates the 10 most essential DT/RF visualizations: 7 reused from existing chart.pdf files + 3 newly created chart.py files.

### Deliverables

| # | Source | Folder/Path | Chart Description |
|---|--------|-------------|-------------------|
| C1 | REUSE | `10_dt_decision_boundary/chart.pdf` | 2D DT classification boundary on make_moons data |
| C2 | REUSE | `17_bias_variance_depth/chart.pdf` | Train/test error vs max_depth (1-20), bias-variance tradeoff |
| C3 | REUSE | `16_regression_tree_mse/chart.pdf` | DT regression piecewise-constant fit |
| C4 | REUSE | `11_gini_vs_entropy/chart.pdf` | Gini and entropy curves vs p |
| C5 | **NEW** | `top10_05_tree_structure/chart.py` | Actual tree rendered by sklearn.tree.plot_tree (depth=3, fraud features) |
| C6 | REUSE | `02_feature_importance/chart.pdf` | RF horizontal bar chart of feature importances |
| C7 | REUSE | `27_rf_ntrees_convergence/chart.pdf` | OOB + test error vs n_estimators |
| C8 | **NEW** | `top10_08_dt_vs_rf_boundary/chart.py` | Side-by-side (1x2 subplot): DT boundary (noisy) vs RF boundary (smooth) |
| C9 | REUSE | `18_rf_hyperparameter_maxfeatures/chart.pdf` | RF accuracy vs max_features |
| C10 | **NEW** | `top10_10_partial_dependence/chart.py` | Partial dependence plot for top 2 RF features |

### Lecture Structure (L04_dt_rf_top10.tex)

```
Slide 1:  Title — "Decision Trees & Random Forests: The 10 Essential Visuals"
Slide 2:  Opening XKCD cartoon (#1838, path: images/1838_machine_learning.png)
Slide 3:  Learning Objectives (3 bullets)
          --- PART 1: DECISION TREES ---
Slide 4:  C1 — Decision Boundary + "What do you see?" interpretation
Slide 5:  C4 — Gini & Entropy (the splitting math)
Slide 6:  C5 — Tree Structure (the actual tree, NEW)
Slide 7:  C3 — DT Regression Step Function
Slide 8:  C2 — Bias-Variance Tradeoff (the overfitting problem)
Slide 9:  Transition — "DTs overfit. How do we fix this?"
          --- PART 2: RANDOM FORESTS ---
Slide 10: C8 — DT vs RF Boundary (the ensemble aha moment, NEW)
Slide 11: C7 — OOB Error Convergence
Slide 12: C9 — max_features Effect
Slide 13: C6 — Feature Importance
Slide 14: C10 — Partial Dependence Plot (NEW)
Slide 15: Summary — "10 Charts You Should Know" (thumbnail grid or checklist)
Slide 16: Closing XKCD (#1885, path: images/1885_ensemble_model.png)
```

### Definition of Done
- All 3 new chart.py files run without error and produce chart.pdf
- All 7 reused chart.pdf files exist at their referenced paths
- L04_dt_rf_top10.tex compiles with 0 errors, 0 Overfull
- Every slide has a `\bottomnote{}`
- manifest.json updated with new .tex file and 3 new chart entries

---

## Guardrails

### Must Have
- New chart.py files follow exact rcParams template (font.size=14, figsize=(10,6), dpi=150)
- savefig uses dpi=300 (matching existing charts: rcParams sets figure.dpi=150 for screen, savefig overrides to 300 for print)
- ML color palette: MLPurple=#3333B2, MLBlue=#0066CC, MLOrange=#FF7F0E, MLGreen=#2CA02C, MLRed=#D62728
- Chart widths in tex: 0.65\textwidth (chart-only) or 0.55\textwidth (with text)
- Max 3-4 bullets per slide
- Beamer: Madrid theme, 8pt, 16:9
- Each new chart.py has CHART_METADATA dict and URL figtext
- Dependencies: numpy, matplotlib, scikit-learn only
- random_state=42 everywhere

### Must NOT Have
- No modifications to existing chart.py files or existing .tex files
- No boosting charts (pure DT/RF focus)
- No external datasets — synthetic only

### Subplot Exception
Chart C8 (DT vs RF boundary) uses `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))`. This is a deliberate pedagogical exception — the side-by-side comparison IS the point. figsize remains (10, 6) per guardrails; each subplot is (5, 6).

### XKCD Image Paths
- Opening: `images/1838_machine_learning.png` (already exists in L04 folder)
- Closing: `images/1885_ensemble_model.png` (already exists in L04 folder)

---

## Task Flow

```
Phase 1: Create 3 new chart.py files
  C5 → C8 → C10

Phase 2: Run chart.py files to generate chart.pdf

Phase 3: Verify 7 reused chart.pdf files exist

Phase 4: Create L04_dt_rf_top10.tex

Phase 5: Compile and validate (0 errors, 0 Overfull)

Phase 6: Update manifest.json
```

---

## Detailed Specifications for NEW Charts

### C5: `top10_05_tree_structure/chart.py`

**Purpose:** Show the actual tree structure — the most recognizable DT image in any textbook.

**Data:** `make_classification(n_samples=200, n_features=4, n_informative=3, random_state=42)`
**Feature names:** `['Amount', 'Frequency', 'Distance', 'Time']`
**Model:** `DecisionTreeClassifier(max_depth=3, random_state=42)`
**Plot:**
- Use `sklearn.tree.plot_tree(clf, feature_names=..., class_names=['Legit', 'Fraud'], filled=True, rounded=True, fontsize=10, ax=ax)`
- Color: override the default colormap — use MLGREEN for "Legit" majority and MLRED for "Fraud" majority nodes
- Title: "Decision Tree Structure (max_depth=3)"
- The tree should be readable at Beamer slide size (depth=3 keeps it manageable)

**Acceptance Criteria:**
- [ ] Uses sklearn.tree.plot_tree (not a manual diagram)
- [ ] Tree is readable at 0.65\textwidth
- [ ] Feature names and class names are meaningful (fraud context)
- [ ] chart.pdf generated

---

### C8: `top10_08_dt_vs_rf_boundary/chart.py`

**Purpose:** The visual "aha moment" for ensembles — noisy DT vs smooth RF.

**Data:** `make_moons(n_samples=300, noise=0.3, random_state=42)`
**Models:** DT(max_depth=None, random_state=42), RF(n_estimators=200, max_depth=None, random_state=42)
**Plot:** `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), sharey=True)`
- Left panel: DT contourf boundary (noisy, jagged)
  - `ax1.set_title("Single Decision Tree")`
  - Contour colors: MLBLUE (class 0) and MLORANGE (class 1), alpha=0.3
  - Scatter points colored by class
- Right panel: RF contourf boundary (smooth)
  - `ax2.set_title("Random Forest (200 Trees)")`
  - Same colormap and scatter
- Suptitle: "Ensemble Smoothing: One Tree vs Many"
- Meshgrid: np.meshgrid over feature range with step 0.02

**Acceptance Criteria:**
- [ ] Side-by-side clearly shows DT=jagged, RF=smooth
- [ ] Same data and colormap on both panels
- [ ] figsize=(10, 6) per guardrails
- [ ] chart.pdf generated

---

### C10: `top10_10_partial_dependence/chart.py`

**Purpose:** The modern interpretability standard — how one feature affects predictions.

**Data:** `make_classification(n_samples=1000, n_features=6, n_informative=4, random_state=42)`
**Feature names:** `['Amount', 'Frequency', 'Distance', 'Time', 'Device', 'Country']`
**Model:** `RandomForestClassifier(n_estimators=200, random_state=42)`
**Plot:**
- Use `sklearn.inspection.PartialDependenceDisplay.from_estimator()` for the top 2 features (by importance)
- Plot PDP curves on a single axis (2 lines, different colors)
- Alternatively: use `sklearn.inspection.partial_dependence()` manually and plot with matplotlib for more control
- Color: Feature 1 in MLBLUE, Feature 2 in MLORANGE
- y-axis: "Partial Dependence (probability shift)"
- x-axis: Feature value range
- Title: "Partial Dependence: How Features Affect Predictions"
- Add rug plot (tick marks) at bottom showing data distribution

**Acceptance Criteria:**
- [ ] Shows PDP for 2 features on same axes
- [ ] Rug plot shows data distribution
- [ ] Uses sklearn.inspection (not manual approximation)
- [ ] chart.pdf generated

---

## Commit Strategy

**Single commit:** "Add standalone DT/RF top-10 charts lecture with 3 new visualizations"
- Files: 3 new chart folders (chart.py + chart.pdf), L04_dt_rf_top10.tex, manifest.json

---

## Success Criteria

| Criterion | Metric |
|-----------|--------|
| 3 new charts generated | 3 chart.pdf files in top10_* folders |
| 7 reused charts accessible | All 7 existing chart.pdf paths valid |
| Lecture compiles clean | 0 errors, 0 Overfull |
| Template compliance | rcParams, ML colors, CHART_METADATA in 3 new charts |
| DT/RF-specific selection | No generic classifier charts (confusion matrix, ROC excluded) |
| Pedagogical flow | DT mechanics → overfitting → RF solution → interpretation |
| Standalone | Works without cross-referencing other L04 lectures |
