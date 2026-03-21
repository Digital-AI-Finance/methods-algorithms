"""Eigenvalue Decay: Correlated vs Uncorrelated Features."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Eigenvalue Decay: Correlated vs Uncorrelated Features",
    "description": "Two overlaid semilogy curves comparing eigenvalue decay from correlated (r=0.7) vs uncorrelated features.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_36_pca_correlation_effect"
}


np.random.seed(42)

n_samples = 500
n_features = 10

# Correlated features: off-diagonal = 0.7, diagonal = 1.0
corr_matrix = np.full((n_features, n_features), 0.7)
np.fill_diagonal(corr_matrix, 1.0)
L_corr = np.linalg.cholesky(corr_matrix)
X_corr = np.random.randn(n_samples, n_features) @ L_corr.T

# Uncorrelated features: independent standard normals
X_uncorr = np.random.randn(n_samples, n_features)

# PCA on both
pca_corr = PCA().fit(X_corr)
pca_uncorr = PCA().fit(X_uncorr)

components = np.arange(1, n_features + 1)

fig, ax = plt.subplots()
ax.semilogy(components, pca_corr.explained_variance_, color=MLPURPLE, marker='o',
            linewidth=2.5, markersize=8, label='Correlated (r = 0.7)')
ax.semilogy(components, pca_uncorr.explained_variance_, color=MLORANGE, marker='s',
            linewidth=2.5, markersize=8, linestyle='--', label='Uncorrelated')

ax.set_xlabel('Principal Component')
ax.set_ylabel('Eigenvalue (log scale)')
ax.set_title('Eigenvalue Decay: Correlated vs Uncorrelated Features')
ax.set_xticks(components)
ax.legend(frameon=True, fancybox=True, shadow=True)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
