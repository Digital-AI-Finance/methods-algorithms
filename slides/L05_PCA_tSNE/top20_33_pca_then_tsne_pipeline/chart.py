"""PCA + t-SNE Pipeline Result (Pre-reduced to 50D) - Speedup demonstration."""
import matplotlib.pyplot as plt
import numpy as np
import time
from pathlib import Path
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, trustworthiness
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "PCA + t-SNE Pipeline Result (Pre-reduced to 50D)",
    "description": "Scatter plot of PCA(50) then t-SNE result with timing comparison annotation.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_33_pca_then_tsne_pipeline"
}


np.random.seed(42)

# Data: 5 blobs, 800 samples, 500D (10 informative + 490 noise)
X_info, y = make_blobs(n_samples=800, n_features=10, centers=5, random_state=42)
X_noise = np.random.RandomState(42).randn(800, 490) * 0.3
X = np.hstack([X_info, X_noise])

cluster_colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED]

# Direct t-SNE on 500D
t0 = time.time()
X_direct = TSNE(n_components=2, random_state=42).fit_transform(X)
time_direct = time.time() - t0
trust_direct = trustworthiness(X, X_direct, n_neighbors=10)

# PCA(50) + t-SNE pipeline
t0 = time.time()
X_pca50 = PCA(n_components=50, random_state=42).fit_transform(X)
X_pipeline = TSNE(n_components=2, random_state=42).fit_transform(X_pca50)
time_pipeline = time.time() - t0
trust_pipeline = trustworthiness(X, X_pipeline, n_neighbors=10)

speedup = time_direct / time_pipeline if time_pipeline > 0 else 1.0

fig, ax = plt.subplots()

for c in range(5):
    mask = y == c
    ax.scatter(X_pipeline[mask, 0], X_pipeline[mask, 1],
               c=cluster_colors[c], s=20, alpha=0.7, edgecolors='none',
               label=f'Cluster {c}')

# Annotation box with comparison
textstr = (f'Direct t-SNE on 500D: {time_direct:.1f}s  (trust={trust_direct:.3f})\n'
           f'PCA(50) + t-SNE:      {time_pipeline:.1f}s  (trust={trust_pipeline:.3f})\n'
           f'Speedup: {speedup:.1f}x')
props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='gray', alpha=0.9)
ax.text(0.03, 0.97, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props, family='monospace')

ax.set_xlabel('t-SNE Dimension 1')
ax.set_ylabel('t-SNE Dimension 2')
ax.set_title('PCA + t-SNE Pipeline Result (Pre-reduced to 50D)')
ax.legend(loc='lower right', markerscale=2, framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
