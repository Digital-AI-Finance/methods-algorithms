"""Regularization Comparison - Ridge vs Lasso Coefficient Paths

Note: The Lasso coefficient path uses a simplified soft-thresholding formula
for visualization purposes. The actual Lasso solution involves coordinate
descent optimization, but the visual behavior is qualitatively similar.
"""
import matplotlib.pyplot as plt
import numpy as np
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

# Generate coefficient paths for different lambda values
np.random.seed(42)
lambdas = np.logspace(-3, 2, 50)

# True coefficients (some large, some small)
true_coefs = np.array([3.0, 2.0, 0.5, 0.1, -1.5])
n_coefs = len(true_coefs)

# Ridge: coefficients shrink smoothly toward zero
ridge_paths = np.zeros((len(lambdas), n_coefs))
for i, lam in enumerate(lambdas):
    shrinkage = 1 / (1 + lam)
    ridge_paths[i] = true_coefs * shrinkage

# Lasso: some coefficients go to exactly zero
lasso_paths = np.zeros((len(lambdas), n_coefs))
for i, lam in enumerate(lambdas):
    soft_threshold = np.sign(true_coefs) * np.maximum(np.abs(true_coefs) - lam * 0.3, 0)
    lasso_paths[i] = soft_threshold

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Ridge paths (solid lines)
colors = [MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE]
for j in range(n_coefs):
    ax.plot(np.log10(lambdas), ridge_paths[:, j], '-', color=colors[j], linewidth=2,
            label=f'Feature {j+1} (Ridge)' if j < 2 else None, alpha=0.8)

# Plot Lasso paths (dashed lines)
for j in range(n_coefs):
    ax.plot(np.log10(lambdas), lasso_paths[:, j], '--', color=colors[j], linewidth=2,
            label=f'Feature {j+1} (Lasso)' if j < 2 else None, alpha=0.8)

# Zero line
ax.axhline(y=0, color='gray', linestyle='-', linewidth=1, alpha=0.5)

# Labels
ax.set_xlabel(r'$\log_{10}(\lambda)$ (Regularization Strength)')
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
