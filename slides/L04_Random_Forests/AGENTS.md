<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-02-07 -->

# L04_Random_Forests/

**Parent**: [../AGENTS.md](../AGENTS.md) (slides/)

## Purpose

Lesson 4 introduces ensemble methods with fraud detection as the motivating finance case. Students learn decision trees, bagging, feature randomization, and how to interpret feature importance for business insights.

## Finance Case

**Problem**: Banks need robust fraud detection models that identify which features (transaction amount, merchant type, location) drive predictions. Random forests provide non-linear decision boundaries and built-in feature importance.

**Key Decision**: When to use random forests vs logistic regression for fraud detection.

## Learning Objectives

1. **Understand**: Explain bagging (bootstrap aggregating) and feature randomization
2. **Apply**: Build decision trees and random forests from scratch
3. **Analyze**: Interpret feature importance for business insights (e.g., "Amount is most predictive")
4. **Evaluate**: Tune hyperparameters using out-of-bag (OOB) error

## Files

| File | Purpose | Slides |
|------|---------|--------|
| `L04_overview.tex` | Overview slides with 8 charts | ~17 |
| `L04_deepdive.tex` | Deep dive with Gini impurity derivation | ~30 |
| `L04_instructor_guide.md` | Teaching guide with PMSP breakdown | - |

## Charts

All charts follow the naming convention `XX_descriptive_name/` and output `chart.pdf`:

| Chart | Directory | Description | Key Visual |
|-------|-----------|-------------|------------|
| 01 | `01_decision_tree/` | Single tree structure | Binary tree with split conditions and leaf predictions |
| 02 | `02_feature_importance/` | Feature ranking | Bar chart showing Gini importance by feature |
| 03 | `03_bootstrap/` | Bootstrap sampling | Visualization of sampling with replacement |
| 04 | `04_oob_error/` | OOB error curve | Out-of-bag error vs number of trees |
| 05 | `05_ensemble_voting/` | Majority voting | How multiple trees combine predictions |
| 06a | `06a_single_tree_variance/` | Single tree predictions | High variance across different data samples |
| 06b | `06b_random_forest_variance/` | Random forest predictions | Reduced variance through ensemble |
| 07 | `07_decision_flowchart/` | When to use random forests | Flowchart for algorithm selection |

Note: Also includes `images/` subdirectory for XKCD cartoons and supporting visuals.

## Chart Technical Details

**Standard settings** (same as L01-L03):
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})
```

**Color palette**:
- MLPurple: #3333B2 (structure)
- MLBlue: #0066CC (negative class)
- MLOrange: #FF7F0E (positive class, important features)
- MLGreen: #2CA02C (correct predictions)
- MLRed: #D62728 (fraud class, errors)

## Building Charts

```bash
# Build all charts for L04 (from project root)
python infrastructure/course_cli.py build charts --topic L04

# Build single chart manually
cd slides/L04_Random_Forests/01_decision_tree
python chart.py

# Verify all charts generated
python infrastructure/course_cli.py validate charts --topic L04
```

## LaTeX Compilation

```bash
# Compile overview slides (from L04 directory)
cd slides/L04_Random_Forests
pdflatex -interaction=nonstopmode L04_overview.tex

# Compile deep dive slides
pdflatex -interaction=nonstopmode L04_deepdive.tex

# Clean auxiliary files
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/

# Build via CLI (from project root)
python infrastructure/course_cli.py build slides --topic L04
```

## PMSP Structure

The instructor guide breaks down the 3-hour session:

| Phase | Duration | Content |
|-------|----------|---------|
| **Problem** | 15 min | Fraud detection motivation, interpretability vs accuracy trade-off |
| **Method** | 45 min | Decision trees (Gini/entropy), bagging, feature randomization |
| **Solution** | 45 min | NumPy tree implementation, sklearn RandomForest, feature importance |
| **Practice** | 75 min | Jupyter notebook `L04_random_forests.ipynb` with transaction data |

## Key Concepts

- **Decision Trees**: Recursive partitioning using Gini impurity or entropy
- **Gini Impurity**: 1 - Σ(p_i²) measures node purity
- **Bagging**: Bootstrap aggregating reduces variance by averaging predictions
- **Feature Randomization**: Selecting random subset of features at each split decorrelates trees
- **Feature Importance**: Mean decrease in impurity (MDI) across all trees
- **Out-of-Bag Error**: 0.632 bootstrap estimator (NOT LOOCV) - each tree's error on samples not in its bootstrap

## Major Additions (Feb 2026 Hostile Review Remediation)

This topic received **MAJOR MSc-level enhancements** in February 2026:

### New Content Blocks
1. **Boosting Section** (4 frames):
   - AdaBoost algorithm (Freund & Schapire 1997)
   - Gradient Boosting framework (Friedman 2001)
   - Modern variants: XGBoost (Chen & Guestrin 2016), LightGBM, CatBoost
   - Boosting in finance applications (credit scoring, fraud detection)

2. **CART Pseudocode**:
   - Full algorithmic environment using algorithm/algorithmic packages
   - Based on Breiman et al. 1984 specification
   - Recursive partitioning with stopping criteria

3. **SHAP Values** (Lundberg & Lee 2017):
   - Shapley value formula for feature attribution
   - TreeSHAP fast computation method
   - Interpretation for business insights

4. **Class Imbalance Treatment** (2 frames):
   - Class weights (cost-sensitive learning)
   - Sampling techniques (SMOTE, ADASYN)
   - Finance context: fraud detection (1:1000 ratio typical)

5. **Statistical Inference**:
   - Permutation-based feature importance tests
   - Bootstrap confidence intervals for predictions
   - Hypothesis testing for feature relevance

6. **Variance Derivation**:
   - Formal proof showing bagging reduces variance
   - Includes correlation term: Var(avg) = σ²/B + ρσ²(B-1)/B
   - Explains why feature randomization helps (reduces ρ)

### Corrections
- **OOB Error**: Changed from incorrect "LOOCV" description to correct "0.632 bootstrap estimator"
- **MDI Formula**: Added formal mathematical definition
- **Learning Objectives**: Rewritten to Bloom's Level 4-5 (Derive, Evaluate, Analyze, Critique)

### New Slides
- **Key Equations Frame** (Overview): Gini impurity, variance reduction, decorrelation effect
- **LaTeX Packages**: Now requires `algorithm` and `algorithmic` for pseudocode rendering

## Decision Framework

**When to use Random Forests**:
- Tabular data with mixed feature types
- Feature importance needed for business insights
- Non-linear relationships expected
- Robust to outliers and missing values

**When NOT to use**:
- Very high-dimensional sparse data (e.g., text)
- Interpretability of individual predictions required
- Real-time predictions with strict latency (many trees slow)
- Extrapolation beyond training data range

## Common Pitfalls

1. **Class Imbalance**: Use `class_weight='balanced'` or SMOTE
2. **Too Many Trees**: OOB error plateaus around 100-500 trees (diminishing returns)
3. **Max Depth**: Too deep → overfitting, too shallow → underfitting (use OOB to tune)
4. **Feature Importance Bias**: Biased toward high-cardinality features (use permutation importance)

## Hyperparameter Tuning

| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| `n_estimators` | More trees → lower variance | 100-500 |
| `max_depth` | Depth limit → controls overfitting | 10-30 |
| `min_samples_split` | Min samples to split → smoothing | 2-10 |
| `max_features` | Features per split → decorrelation | sqrt(n), log2(n) |

## Testing Checklist

- [ ] All 8 chart.py scripts generate chart.pdf
- [ ] L04_overview.tex compiles without errors
- [ ] L04_deepdive.tex compiles without errors
- [ ] ZERO "Overfull \hbox" warnings in LaTeX output
- [ ] Feature importance sums to 1.0
- [ ] OOB error converges to stable value

## Related Assets

- **Notebook**: `notebooks/L04_random_forests.ipynb`
- **Dataset**: `datasets/transactions_synthetic.csv` (features: amount, merchant_type, location; target: fraud)
- **Quiz**: `quizzes/quiz2_topics_3_4.xml` (covers L03 + L04)
- **Template**: `templates/beamer_template.tex`, `templates/chart_template.py`

## Prerequisites

Students should know:
- L01 (bias-variance tradeoff)
- L02 (classification metrics)
- Decision tree basics (splitting criteria)

## Next Lesson

→ [L05_PCA_tSNE/AGENTS.md](../L05_PCA_tSNE/AGENTS.md) - Dimensionality reduction for visualization
