# notebooks/

<!-- Parent: ../AGENTS.md -->

**Generated**: 2026-01-25
**Purpose**: Hands-on Jupyter notebooks for each course topic (L01-L06) with implementations, exercises, and solutions

---

## Overview

This directory contains interactive Jupyter notebooks that accompany each lecture topic. Students use these notebooks to:
- Implement ML algorithms from scratch using NumPy
- Apply methods using scikit-learn
- Complete exercises with solutions
- Visualize results and interpret models

Notebooks are designed for **dual deployment**: local Jupyter and Google Colab.

---

## Key Files

| File | Topic | Status | Colab Link |
|------|-------|--------|------------|
| `L01_linear_regression.ipynb` | Linear Regression (OLS, Gradient Descent, Regularization) | Complete | [Open in Colab](https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L01_linear_regression.ipynb) |
| `L02_logistic_regression.ipynb` | Logistic Regression (Classification, ROC/AUC) | Complete | [Open in Colab](https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L02_logistic_regression.ipynb) |
| `L03_knn_kmeans.ipynb` | K-Nearest Neighbors & K-Means Clustering | Complete | [Open in Colab](https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L03_knn_kmeans.ipynb) |
| `L04_random_forests.ipynb` | Random Forests (Ensemble Learning) | Complete | [Open in Colab](https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L04_random_forests.ipynb) |
| `L05_pca_tsne.ipynb` | PCA & t-SNE (Dimensionality Reduction) | Complete | [Open in Colab](https://colab.research.google.com/github/Digital-AI-Finance/methods-algorithms/blob/master/notebooks/L05_pca_tsne.ipynb) |
| `L06_embeddings_rl.ipynb` | Word Embeddings & Reinforcement Learning | Pending | - |

**Source**: All notebooks follow the template structure defined in `../templates/notebook_template.ipynb`

---

## For AI Agents

### Notebook Structure

Each notebook follows this standard cell sequence (refer to template):

```
1. Title + Colab Badge
   - Include [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](URL)

2. Learning Objectives
   - 4 clear learning outcomes

3. Setup
   - Standard imports: numpy, pandas, matplotlib, sklearn
   - Set np.random.seed(42) for reproducibility
   - Configure matplotlib rcParams

4. Theory Recap
   - Brief review of lecture concepts
   - Key equations in LaTeX

5. Generate/Load Data
   - Try local path first: ../datasets/*.csv
   - Fallback to GitHub raw URL for Colab
   - Synthetic generation as final fallback

6. Implementation from Scratch
   - NumPy-only implementation
   - Step-by-step with comments
   - Include docstrings

7. scikit-learn Implementation
   - Use standard sklearn classes
   - Compare with scratch implementation
   - Train/test split

8. Visualization
   - Use matplotlib with course color palette
   - Clear labels and titles
   - Interpretation text

9. Exercises
   - 2-3 exercises with solutions
   - Range from basic to advanced
   - Include hints

10. Summary
    - Key takeaways (3-4 points)
```

### How to Use Notebooks

**Reading existing notebooks**:
```python
from nbformat import read

with open('notebooks/L01_linear_regression.ipynb', 'r', encoding='utf-8') as f:
    nb = read(f, as_version=4)

# Extract code cells
code_cells = [cell['source'] for cell in nb.cells if cell['cell_type'] == 'code']
```

**Validating notebooks**:
```bash
# Test execution (ensure all cells run without errors)
jupyter nbconvert --execute --to notebook notebooks/L01_linear_regression.ipynb

# Or use CLI validator
python infrastructure/course_cli.py validate notebooks
```

**Creating new notebooks**:
1. Copy `templates/notebook_template.ipynb`
2. Update placeholders: `{{TOPIC_ID}}`, `{{TOPIC_TITLE}}`
3. Add topic-specific content
4. Test execution locally and in Colab

### Critical Conventions

#### Data Loading Pattern

**ALWAYS use this fallback pattern** for Colab compatibility:

```python
import os

try:
    # Try local path first
    if os.path.exists('../datasets/housing_synthetic.csv'):
        df = pd.read_csv('../datasets/housing_synthetic.csv')
        print('Loaded dataset from local file')
    else:
        # Try GitHub URL for Colab
        url = 'https://raw.githubusercontent.com/Digital-AI-Finance/methods-algorithms/master/datasets/housing_synthetic.csv'
        df = pd.read_csv(url)
        print('Loaded dataset from GitHub')
except Exception as e:
    print(f'Could not load dataset: {e}')
    print('Generating synthetic data instead...')
    # Synthetic generation code here
```

#### Reproducibility

```python
# Set random seed at start of every notebook
np.random.seed(42)

# Use random_state parameter in sklearn
train_test_split(X, y, test_size=0.2, random_state=42)
Ridge(alpha=1.0, random_state=42)
```

#### Plotting Configuration

```python
# Standard plotting settings
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Use course color palette (from templates/chart_template.py)
COLORS = {
    'primary': '#3333B2',    # ML Purple
    'secondary': '#0066CC',  # ML Blue
    'accent': '#FF7F0E',     # ML Orange
    'success': '#2CA02C',    # ML Green
    'danger': '#D62728',     # ML Red
}
```

#### Exercise Format

```markdown
## Exercises

### Exercise 1: Implement RMSE
Write a function to compute RMSE from scratch.
```

```python
# SOLUTION: Implement RMSE from scratch
def rmse(y_true, y_pred):
    """Compute Root Mean Squared Error.

    Args:
        y_true: Actual target values
        y_pred: Predicted values

    Returns:
        float: RMSE value
    """
    # Implementation here
    pass
```

**Exercise guidelines**:
- Include docstrings with Args and Returns
- Provide hints if complex
- Test against sklearn equivalent
- Use `# SOLUTION:` prefix for solution cells

### Testing Requirements

**Before committing notebook changes**:

1. **Execute all cells**: `jupyter nbconvert --execute --to notebook notebooks/L0X_topic.ipynb`
2. **Check outputs**: Verify all cells executed without errors
3. **Test in Colab**: Upload to Colab and run end-to-end
4. **Validate data loading**: Ensure fallback pattern works
5. **Check links**: Verify GitHub raw URLs are correct

**Common errors to check**:
- Missing imports
- Undefined variables
- Dataset path errors (local vs Colab)
- Random seed not set
- Plots not displaying

### Notebook-Specific Notes

#### L01_linear_regression.ipynb
- **Dataset**: housing_synthetic.csv (200 samples, 4 features)
- **Key implementations**: Normal equation, gradient descent with convergence
- **Exercises**: RMSE from scratch, Ridge cross-validation
- **Special features**: Residual analysis, Q-Q plots, regularization comparison

#### L02_logistic_regression.ipynb
- **Dataset**: credit_synthetic.csv (classification task)
- **Key implementations**: Sigmoid function, log loss, decision boundary
- **Exercises**: ROC curve interpretation, threshold tuning
- **Special features**: Confusion matrix, precision-recall tradeoff

#### L03_knn_kmeans.ipynb
- **Dataset**: customers_synthetic.csv (clustering)
- **Key implementations**: KNN from scratch, K-Means with iteration visualization
- **Exercises**: Distance metrics comparison, elbow method
- **Special features**: Voronoi diagrams, silhouette scores

#### L04_random_forests.ipynb
- **Dataset**: credit_synthetic.csv (ensemble learning)
- **Key implementations**: Decision tree splitting, bootstrap sampling
- **Exercises**: Feature importance analysis, OOB error calculation
- **Special features**: Ensemble voting visualization

#### L05_pca_tsne.ipynb
- **Dataset**: portfolio_synthetic.csv (high-dimensional data)
- **Key implementations**: PCA from scratch, scree plot
- **Exercises**: Reconstruction error, component interpretation
- **Special features**: t-SNE perplexity comparison

#### L06_embeddings_rl.ipynb (Pending)
- **Dataset**: TBD (financial news text + trading environment)
- **Key implementations**: Word2Vec, Q-learning agent
- **Exercises**: TBD
- **Status**: Not yet implemented

### Dependencies

All notebooks require:

```python
# Core libraries
numpy >= 1.21.0
pandas >= 1.3.0
matplotlib >= 3.4.0
scikit-learn >= 1.0.0

# Optional (for specific notebooks)
scipy >= 1.7.0  # L01, L02 (stats functions)
seaborn >= 0.11.0  # (optional for enhanced plots)
```

**Colab pre-installed**: All dependencies are pre-installed in Google Colab.

---

## Updating Notebooks

### Adding New Exercise

```python
# 1. Add markdown cell with exercise description
"""
### Exercise 3: Custom Metric
Implement Mean Absolute Percentage Error (MAPE).
"""

# 2. Add code cell with solution
# SOLUTION: Implement MAPE
def mape(y_true, y_pred):
    """Compute Mean Absolute Percentage Error."""
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# 3. Test the implementation
mape_score = mape(y_test, y_pred_test)
print(f'MAPE: {mape_score:.2f}%')
```

### Modifying Existing Content

```bash
# 1. Read notebook
jupyter notebook notebooks/L01_linear_regression.ipynb

# 2. Make changes in Jupyter UI

# 3. Test execution: Kernel → Restart & Run All

# 4. Validate
python infrastructure/course_cli.py validate notebooks

# 5. Update manifest.json if structure changed
```

### Deploying to Colab

**GitHub repository must be public** for Colab badge links to work.

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/BRANCH/notebooks/L01_linear_regression.ipynb)
```

Replace `OWNER/REPO/BRANCH` with actual repository details.

---

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| `FileNotFoundError` for dataset | Incorrect path for local/Colab | Use fallback pattern with try/except |
| Kernel dies during execution | Out of memory (large dataset) | Reduce sample size or use chunking |
| Different results each run | Random seed not set | Add `np.random.seed(42)` to Setup |
| Plots not showing in Colab | Missing `plt.show()` | Colab auto-displays, but add for clarity |
| Import errors | Missing library | Add to requirements or use `!pip install` |

---

## Related Files

- **Parent hierarchy**: `../AGENTS.md` (project root)
- **Template source**: `../templates/notebook_template.ipynb`
- **Datasets**: `../datasets/*.csv` (synthetic data used in notebooks)
- **Slides**: `../slides/L0X_Topic/` (corresponding lecture materials)
- **Validators**: `infrastructure/validators/notebook_validator.py`
- **CLI**: `python infrastructure/course_cli.py validate notebooks`
