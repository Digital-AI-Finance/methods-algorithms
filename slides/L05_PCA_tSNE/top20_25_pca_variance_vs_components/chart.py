"""Silhouette Score vs Number of PCA Components."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Silhouette Score vs Number of PCA Components",
    "description": "Line plot of silhouette score vs PCA components with optimal k starred.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_25_pca_variance_vs_components"
}


np.random.seed(42)

# 5 blobs in 30D
X, labels = make_blobs(n_samples=600, n_features=30, centers=5,
                       cluster_std=2.0, random_state=42)

# Full-space silhouette (using true labels)
sil_full = silhouette_score(X, labels)

# Silhouette for each k components
k_values = list(range(2, 21))
sil_scores = []
for k in k_values:
    X_pca = PCA(n_components=k, random_state=42).fit_transform(X)
    sil = silhouette_score(X_pca, labels)
    sil_scores.append(sil)

sil_scores = np.array(sil_scores)

# Optimal k
best_idx = np.argmax(sil_scores)
best_k = k_values[best_idx]
best_sil = sil_scores[best_idx]

fig, ax = plt.subplots()

ax.plot(k_values, sil_scores, color=MLBLUE, linewidth=2.5, marker='o',
        markersize=6, markerfacecolor='white', markeredgecolor=MLBLUE,
        markeredgewidth=2, label='Silhouette score', zorder=3)

# Star at optimal
ax.plot(best_k, best_sil, marker='*', markersize=20, color=MLORANGE,
        markeredgecolor='black', markeredgewidth=0.5, zorder=4,
        label=f'Optimal: k={best_k} (sil={best_sil:.3f})')

# Full-space reference line
ax.axhline(y=sil_full, color=MLRED, linestyle='--', linewidth=2,
           label=f'Full 30D silhouette = {sil_full:.3f}')

ax.set_xlabel('Number of PCA Components ($k$)')
ax.set_ylabel('Silhouette Score')
ax.set_title('Silhouette Score vs Number of PCA Components')
ax.set_xticks(k_values[::2])
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray',
            ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
