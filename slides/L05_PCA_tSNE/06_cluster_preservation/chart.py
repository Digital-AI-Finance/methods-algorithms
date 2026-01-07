"""Cluster Preservation - How well do projections preserve cluster structure?"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'
MLGRAY = '#808080'

np.random.seed(42)

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# Generate high-dimensional data with clusters
n_per_cluster = 100
n_dims = 50

# Cluster centers in high-dim space
centers_hd = [np.random.randn(n_dims) * 3 for _ in range(3)]
labels = np.repeat([0, 1, 2], n_per_cluster)
colors_map = {0: MLBLUE, 1: MLGREEN, 2: MLRED}
colors = [colors_map[l] for l in labels]

# Original data (first 2 dims for visualization)
X_2d = np.vstack([centers_hd[i][:2] + np.random.randn(n_per_cluster, 2) * 0.5
                  for i in range(3)])

# Ax1: Original High-D (just showing 2 dims)
ax1 = axes[0]
ax1.scatter(X_2d[:, 0], X_2d[:, 1], c=colors, alpha=0.7, s=30)
ax1.set_title('Original (2 of 50 dims)\nClusters overlap', fontsize=12, fontweight='bold')
ax1.set_xlabel('Dim 1')
ax1.set_ylabel('Dim 2')

# Ax2: PCA projection
ax2 = axes[1]
# Simulate PCA - finds directions of max variance (may not separate clusters well)
# Random projection that preserves some structure
pca_x = X_2d[:, 0] * 0.8 + X_2d[:, 1] * 0.2 + np.random.randn(300) * 0.3
pca_y = X_2d[:, 0] * 0.2 - X_2d[:, 1] * 0.8 + np.random.randn(300) * 0.3
ax2.scatter(pca_x, pca_y, c=colors, alpha=0.7, s=30)
ax2.set_title('PCA Projection\nSome separation', fontsize=12, fontweight='bold')
ax2.set_xlabel('PC1')
ax2.set_ylabel('PC2')

# Ax3: t-SNE projection
ax3 = axes[2]
# Simulate t-SNE - preserves local neighborhood (clusters well-separated)
tsne_centers = [(-3, 0), (2, 3), (2, -3)]
tsne_x = np.concatenate([tsne_centers[i][0] + np.random.randn(n_per_cluster) * 0.4
                          for i in range(3)])
tsne_y = np.concatenate([tsne_centers[i][1] + np.random.randn(n_per_cluster) * 0.4
                          for i in range(3)])
ax3.scatter(tsne_x, tsne_y, c=colors, alpha=0.7, s=30)
ax3.set_title('t-SNE Projection\nClear separation', fontsize=12, fontweight='bold')
ax3.set_xlabel('t-SNE 1')
ax3.set_ylabel('t-SNE 2')

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=MLBLUE, label='Cluster 1'),
                   Patch(facecolor=MLGREEN, label='Cluster 2'),
                   Patch(facecolor=MLRED, label='Cluster 3')]
fig.legend(handles=legend_elements, loc='center right', bbox_to_anchor=(1.08, 0.5))

fig.suptitle('Cluster Preservation in Dimensionality Reduction',
             fontsize=16, fontweight='bold', y=1.02)

for ax in axes:
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06_cluster_preservation/chart.pdf")
