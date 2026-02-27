"""Regularization Comparison - Ridge vs Lasso Coefficient Paths"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from pathlib import Path

# QuantLet branding metadata
CHART_METADATA = {
    "title": "Ridge vs Lasso Regularization",
    "description": "Coefficient shrinkage paths comparing Ridge and Lasso",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L01_Introduction_Linear_Regression/06_regularization_comparison"
}

# Chart settings for Beamer
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

# Colors
MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

# Generate multi-feature data and compute coefficient paths with sklearn
np.random.seed(42)
X_multi = np.random.randn(100, 6)
y_multi = X_multi @ np.array([3, -2, 0, 0, 1, -1]) + np.random.normal(0, 1, 100)
alphas = np.logspace(-2, 3, 50)

ridge_coefs = np.array([Ridge(alpha=a).fit(X_multi, y_multi).coef_ for a in alphas])
lasso_coefs = np.array([Lasso(alpha=a, max_iter=10000).fit(X_multi, y_multi).coef_ for a in alphas])

n_coefs = X_multi.shape[1]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Ridge paths (solid lines)
colors = [MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE, '#888888']
for j in range(n_coefs):
    ax.plot(np.log10(alphas), ridge_coefs[:, j], '-', color=colors[j], linewidth=2,
            label=f'Feature {j+1} (Ridge)' if j < 2 else None, alpha=0.8)

# Plot Lasso paths (dashed lines)
for j in range(n_coefs):
    ax.plot(np.log10(alphas), lasso_coefs[:, j], '--', color=colors[j], linewidth=2,
            label=f'Feature {j+1} (Lasso)' if j < 2 else None, alpha=0.8)

# Zero line
ax.axhline(y=0, color='gray', linestyle='-', linewidth=1, alpha=0.5)

# Labels
ax.set_xlabel(r'$\log_{10}(\alpha)$ (Regularization Strength)')
ax.set_ylabel('Coefficient Value')
ax.set_title('Ridge vs Lasso: Coefficient Shrinkage')
ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3)

# Add annotation
ax.annotate('Ridge: smooth shrinkage\nLasso: sparse solutions',
            xy=(-1, -0.5), fontsize=11, color='gray',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06_regularization_comparison/chart.pdf")
