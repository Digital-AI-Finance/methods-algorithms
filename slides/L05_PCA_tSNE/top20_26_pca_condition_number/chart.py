"""Condition Number vs Feature Correlation Strength - Shows how increasing pairwise correlation inflates condition number."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Condition Number vs Feature Correlation Strength",
    "description": "Scatter plot showing condition number (log scale) vs pairwise correlation strength, with severity thresholds.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_26_pca_condition_number"
}


np.random.seed(42)

p = 5
n_samples = 500
r_values = np.linspace(0, 0.99, 50)
condition_numbers = []

for r in r_values:
    # Build correlation matrix with pairwise correlation r
    corr = np.full((p, p), r)
    np.fill_diagonal(corr, 1.0)
    # Cholesky decomposition
    L = np.linalg.cholesky(corr)
    # Generate correlated data
    Z = np.random.randn(n_samples, p)
    X = Z @ L.T
    # Covariance eigenvalues
    cov = np.cov(X, rowvar=False)
    eigvals = np.linalg.eigvalsh(cov)
    eigvals = np.sort(eigvals)[::-1]
    cond = eigvals[0] / max(eigvals[-1], 1e-12)
    condition_numbers.append(cond)

condition_numbers = np.array(condition_numbers)

# Color by severity
colors = []
for c in condition_numbers:
    if c < 30:
        colors.append(MLGREEN)
    elif c < 1000:
        colors.append(MLORANGE)
    else:
        colors.append(MLRED)

fig, ax = plt.subplots()

ax.scatter(r_values, condition_numbers, c=colors, s=50, edgecolors='white', linewidths=0.5, zorder=3)
ax.set_yscale('log')

# Threshold lines
ax.axhline(y=30, color=MLORANGE, linestyle='--', linewidth=1.5, alpha=0.8)
ax.text(0.02, 35, 'Moderate (30)', fontsize=11, color=MLORANGE, va='bottom')

ax.axhline(y=1000, color=MLRED, linestyle='--', linewidth=1.5, alpha=0.8)
ax.text(0.02, 1200, 'Severe (1000)', fontsize=11, color=MLRED, va='bottom')

ax.set_xlabel('Pairwise Correlation Strength (r)')
ax.set_ylabel('Condition Number (log scale)')
ax.set_title('Condition Number vs Feature Correlation Strength')

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=MLGREEN, markersize=10, label='Low (< 30)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=MLORANGE, markersize=10, label='Moderate (30\u20131000)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=MLRED, markersize=10, label='Severe (> 1000)'),
]
ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
