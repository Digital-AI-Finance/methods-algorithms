"""Cluster Centers Heatmap - K-Means cluster profiles as a feature heatmap."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "K-Means Cluster Profiles: Feature Centroids",
    "description": "Heatmap of cluster_centers_ showing feature values per cluster",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_16_cluster_centers_heatmap"
}


feature_names = ['Amount', 'Frequency', 'Recency', 'Duration', 'Count', 'Score']

X, _ = make_blobs(n_samples=500, n_features=6, centers=4, random_state=42)

km = KMeans(n_clusters=4, random_state=42, n_init=10)
km.fit(X)

centers = km.cluster_centers_

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(centers, cmap='coolwarm', aspect='auto')
ax.grid(False)

# Annotate cells
for i in range(centers.shape[0]):
    for j in range(centers.shape[1]):
        ax.text(j, i, f'{centers[i, j]:.2f}', ha='center', va='center',
                fontsize=12, fontweight='bold',
                color='white' if abs(centers[i, j]) > 3 else 'black')

ax.set_xticks(range(len(feature_names)))
ax.set_xticklabels(feature_names, rotation=30, ha='right')
ax.set_yticks(range(4))
ax.set_yticklabels([f'Cluster {i}' for i in range(4)])
ax.set_title('K-Means Cluster Profiles: Feature Centroids', fontweight='bold')

cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Centroid Value', fontsize=12)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_16_cluster_centers_heatmap/chart.pdf")
