"""Trustworthiness Across Neighborhood Sizes - Comparing t-SNE, PCA, Isomap."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE, Isomap, trustworthiness
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Trustworthiness Across Neighborhood Sizes",
    "description": "Three-line plot comparing trustworthiness of t-SNE, PCA, and Isomap across varying k values.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_34_trustworthiness_vs_k"
}


np.random.seed(42)

# Data: 5 blobs in 20D, 500 samples
X, y = make_blobs(n_samples=500, n_features=20, centers=5, random_state=42)

k_values = [5, 10, 15, 20, 30, 50, 75, 100]

# Compute embeddings once
X_tsne = TSNE(n_components=2, random_state=42).fit_transform(X)
X_pca = PCA(n_components=2, random_state=42).fit_transform(X)
X_iso = Isomap(n_components=2).fit_transform(X)

trust_tsne = [trustworthiness(X, X_tsne, n_neighbors=k) for k in k_values]
trust_pca = [trustworthiness(X, X_pca, n_neighbors=k) for k in k_values]
trust_iso = [trustworthiness(X, X_iso, n_neighbors=k) for k in k_values]

fig, ax = plt.subplots()

ax.plot(k_values, trust_tsne, 'o-', color=MLPURPLE, linewidth=2.5, markersize=7, label='t-SNE')
ax.plot(k_values, trust_pca, 's-', color=MLBLUE, linewidth=2.5, markersize=7, label='PCA')
ax.plot(k_values, trust_iso, '^-', color=MLGREEN, linewidth=2.5, markersize=7, label='Isomap')

ax.set_xlabel('Neighborhood Size (k)')
ax.set_ylabel('Trustworthiness')
ax.set_ylim(0.7, 1.0)
ax.set_title('Trustworthiness Across Neighborhood Sizes')
ax.legend(loc='lower left', framealpha=0.9)
ax.grid(axis='y', alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
