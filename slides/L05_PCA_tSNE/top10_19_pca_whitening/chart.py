"""PCA Whitening - 1x3 subplot showing original, PCA, and whitened PCA transforms."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "PCA Whitening: Decorrelation and Scaling",
    "description": "Three-panel comparison of original, PCA-transformed, and whitened data",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_19_pca_whitening"
}


np.random.seed(42)
X = np.random.multivariate_normal([0, 0], [[3, 2], [2, 2]], 300)

pca_no_whiten = PCA(n_components=2, whiten=False, random_state=42)
X_pca = pca_no_whiten.fit_transform(X)

pca_whiten = PCA(n_components=2, whiten=True, random_state=42)
X_white = pca_whiten.fit_transform(X)

lim = 7
fig, axes = plt.subplots(1, 3, figsize=(10, 6))

axes[0].scatter(X[:, 0], X[:, 1], c=MLBLUE, alpha=0.4, s=15, edgecolors='none')
axes[0].set_title('Original Data', fontsize=14)
axes[0].set_aspect('equal')
axes[0].set_xlim(-lim, lim)
axes[0].set_ylim(-lim, lim)
axes[0].set_xlabel('X1')
axes[0].set_ylabel('X2')

axes[1].scatter(X_pca[:, 0], X_pca[:, 1], c=MLORANGE, alpha=0.4, s=15, edgecolors='none')
axes[1].set_title('PCA (no whitening)', fontsize=14)
axes[1].set_aspect('equal')
axes[1].set_xlim(-lim, lim)
axes[1].set_ylim(-lim, lim)
axes[1].set_xlabel('PC1')
axes[1].set_ylabel('PC2')

axes[2].scatter(X_white[:, 0], X_white[:, 1], c=MLGREEN, alpha=0.4, s=15, edgecolors='none')
axes[2].set_title('PCA (whitened)', fontsize=14)
axes[2].set_aspect('equal')
axes[2].set_xlim(-lim, lim)
axes[2].set_ylim(-lim, lim)
axes[2].set_xlabel('WPC1')
axes[2].set_ylabel('WPC2')

fig.suptitle('PCA Whitening: Decorrelation and Scaling', fontsize=16, fontweight='bold', y=0.98)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_19_pca_whitening/chart.pdf")
