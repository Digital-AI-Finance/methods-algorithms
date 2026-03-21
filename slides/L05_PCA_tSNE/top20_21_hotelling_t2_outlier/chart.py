"""Hotelling T-squared Outlier Detection in PC Space."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.stats import chi2
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Hotelling T-squared Outlier Detection in PC Space",
    "description": "Scatter of PC1 vs PC2 colored by Hotelling T2 with 95%/99% confidence ellipses.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_21_hotelling_t2_outlier"
}


np.random.seed(42)

# Generate data: 200 normal + 10 outliers
X_normal = np.random.multivariate_normal([0, 0], [[3, 1], [1, 2]], size=200)
X_outliers = np.random.multivariate_normal([6, 6], [[0.3, 0], [0, 0.3]], size=10)
X = np.vstack([X_normal, X_outliers])

# PCA via eigen decomposition
mean = X.mean(axis=0)
X_centered = X - mean
cov_mat = np.cov(X_centered, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eigh(cov_mat)
# Sort descending
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Project onto PCs
scores = X_centered @ eigenvectors

# Hotelling T2: sum of (score_k / sqrt(eigenvalue_k))^2
T2 = np.sum((scores / np.sqrt(eigenvalues))**2, axis=1)

# Confidence ellipse radii from chi2
chi2_95 = chi2.ppf(0.95, 2)
chi2_99 = chi2.ppf(0.99, 2)

fig, ax = plt.subplots()

sc = ax.scatter(scores[:, 0], scores[:, 1], c=T2, cmap='YlOrRd',
                edgecolors='gray', linewidth=0.3, s=40, zorder=3)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Hotelling $T^2$')

# Draw confidence ellipses (radii = sqrt(eigenvalue_k * chi2_threshold))
for threshold, label, ls in [(chi2_95, '95% confidence', '--'), (chi2_99, '99% confidence', ':')]:
    width = 2 * np.sqrt(eigenvalues[0] * threshold)
    height = 2 * np.sqrt(eigenvalues[1] * threshold)
    ellipse = patches.Ellipse((0, 0), width, height, fill=False,
                               edgecolor=MLPURPLE, linewidth=2, linestyle=ls,
                               label=label, zorder=2)
    ax.add_patch(ellipse)

ax.set_xlabel('PC1 Score')
ax.set_ylabel('PC2 Score')
ax.set_title('Hotelling $T^2$ Outlier Detection in PC Space')
ax.legend(loc='upper left')
ax.set_aspect('equal', adjustable='datalim')

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray',
            ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
