<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-25 | Updated: 2026-01-25 -->

# L02_Logistic_Regression/

**Parent**: [../AGENTS.md](../AGENTS.md) (slides/)

## Purpose

Lesson 2 introduces logistic regression for binary classification with credit scoring as the motivating finance case. Students learn sigmoid functions, maximum likelihood estimation, and evaluation metrics (ROC, precision-recall).

## Finance Case

**Problem**: Banks need to predict loan defaults with probability estimates for risk-based pricing. Logistic regression provides interpretable odds ratios (e.g., "Each $10k income increase reduces default odds by 15%") required by Basel regulations.

**Key Decision**: When to use logistic regression vs random forests for credit scoring.

## Learning Objectives

1. **Understand**: Derive logistic regression from maximum likelihood estimation
2. **Apply**: Implement binary classification with gradient descent
3. **Analyze**: Interpret odds ratios for business decisions (e.g., feature impact on default probability)
4. **Evaluate**: Choose classification thresholds using ROC and precision-recall curves

## Files

| File | Purpose | Slides |
|------|---------|--------|
| `L02_overview.tex` | Overview slides with 7 charts | ~17 |
| `L02_deepdive.tex` | Deep dive with MLE derivation | ~30 |
| `L02_instructor_guide.md` | Teaching guide with PMSP breakdown | - |

## Charts

All charts follow the naming convention `XX_descriptive_name/` and output `chart.pdf`:

| Chart | Directory | Description | Key Visual |
|-------|-----------|-------------|------------|
| 01 | `01_sigmoid_function/` | Logistic curve | Sigmoid transformation from log-odds to probability |
| 02 | `02_decision_boundary/` | Classification boundary | Linear decision boundary in 2D feature space |
| 03 | `03_log_loss/` | Cross-entropy loss | Loss function shape for binary classification |
| 04 | `04_roc_curve/` | ROC curve and AUC | True positive rate vs false positive rate |
| 05 | `05_precision_recall/` | Precision-recall curve | Trade-off for imbalanced datasets |
| 06 | `06_confusion_matrix/` | Classification matrix | TP, FP, TN, FN visualization |
| 07 | `07_decision_flowchart/` | When to use logistic regression | Flowchart for algorithm selection |

## Chart Technical Details

**Standard settings** (same as L01):
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
- MLOrange: #FF7F0E (decision boundary)
- MLGreen: #2CA02C (positive class, true positives)
- MLRed: #D62728 (false positives, errors)

## Building Charts

```bash
# Build all charts for L02 (from project root)
python infrastructure/course_cli.py build charts --topic L02

# Build single chart manually
cd slides/L02_Logistic_Regression/01_sigmoid_function
python chart.py

# Verify all charts generated
python infrastructure/course_cli.py validate charts --topic L02
```

## LaTeX Compilation

```bash
# Compile overview slides (from L02 directory)
cd slides/L02_Logistic_Regression
pdflatex -interaction=nonstopmode L02_overview.tex

# Compile deep dive slides
pdflatex -interaction=nonstopmode L02_deepdive.tex

# Clean auxiliary files
mkdir temp 2>nul & move *.aux *.log *.nav *.out *.snm *.toc temp/

# Build via CLI (from project root)
python infrastructure/course_cli.py build slides --topic L02
```

## PMSP Structure

The instructor guide breaks down the 3-hour session:

| Phase | Duration | Content |
|-------|----------|---------|
| **Problem** | 15 min | Credit scoring motivation, cost of false positives vs negatives |
| **Method** | 45 min | Sigmoid function, MLE derivation, log-loss |
| **Solution** | 45 min | NumPy implementation, threshold selection, sklearn comparison |
| **Practice** | 75 min | Jupyter notebook `L02_logistic_regression.ipynb` with credit data |

## Key Concepts

- **Sigmoid Function**: σ(z) = 1/(1 + e^(-z)) maps real line to [0,1]
- **Log-Loss**: -[y log(p) + (1-y) log(1-p)] for binary cross-entropy
- **Odds Ratios**: exp(β) interpretation (e.g., β=0.15 → 16% increase in odds per unit)
- **ROC Curve**: Shows trade-off between TPR and FPR across thresholds
- **Precision-Recall**: Better for imbalanced classes (e.g., 5% default rate)

## Decision Framework

**When to use Logistic Regression**:
- Binary classification with interpretability required
- Probability estimates needed (e.g., risk-based pricing)
- Linear decision boundary acceptable
- Regulatory compliance (explainable model)

**When NOT to use**:
- Non-linear decision boundaries (use trees/kernels)
- Multi-class with complex interactions (use neural nets)
- Very high-dimensional sparse data (use specialized methods)

## Common Pitfalls

1. **Class Imbalance**: Must use stratified sampling or adjust class weights
2. **Threshold Selection**: Default 0.5 may not be optimal for business costs
3. **Feature Scaling**: Always standardize features for gradient descent
4. **Multicollinearity**: Coefficients become unstable (use Ridge regularization)

## Testing Checklist

- [ ] All 7 chart.py scripts generate chart.pdf
- [ ] L02_overview.tex compiles without errors
- [ ] L02_deepdive.tex compiles without errors
- [ ] ZERO "Overfull \hbox" warnings in LaTeX output
- [ ] ROC curve shows AUC > 0.5 (better than random)
- [ ] Confusion matrix sums to total sample size

## Related Assets

- **Notebook**: `notebooks/L02_logistic_regression.ipynb`
- **Dataset**: `datasets/credit_synthetic.csv` (features: income, age, debt_ratio; target: default)
- **Quiz**: `quizzes/quiz1_topics_1_2.xml` (covers L01 + L02)
- **Template**: `templates/beamer_template.tex`, `templates/chart_template.py`

## Prerequisites

Students should know:
- L01 (linear regression, gradient descent)
- Probability basics (conditional probability, Bayes' theorem)
- Calculus (chain rule for backpropagation)

## Next Lesson

→ [L03_KNN_KMeans/AGENTS.md](../L03_KNN_KMeans/AGENTS.md) - Instance-based learning and clustering
