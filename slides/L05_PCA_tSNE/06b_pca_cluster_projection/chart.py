"""PCA Cluster Projection - Linear projection preserves global structure"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'PCA Cluster Projection',
    'description': 'PCA 2D projection shows some cluster separation',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/06b_pca_cluster_projection'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

fig, ax = plt.subplots(figsize=(10, 6))

# Generate high-dimensional data with clusters
n_per_cluster = 100
n_dims = 50

# Cluster centers in high-dim space
centers_hd = [np.random.randn(n_dims) * 3 for _ in range(3)]
labels = np.repeat([0, 1, 2], n_per_cluster)
color_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3']

# Original data (first 2 dims)
X_2d = np.vstack([centers_hd[i][:2] + np.random.randn(n_per_cluster, 2) * 0.5
                  for i in range(3)])

# Simulate PCA projection - finds directions of max variance
pca_x = X_2d[:, 0] * 0.8 + X_2d[:, 1] * 0.2 + np.random.randn(300) * 0.3
pca_y = X_2d[:, 0] * 0.2 - X_2d[:, 1] * 0.8 + np.random.randn(300) * 0.3

for i, (color, label) in enumerate(zip([MLBLUE, MLGREEN, MLRED], color_labels)):
    mask = labels == i
    ax.scatter(pca_x[mask], pca_y[mask], c=color, alpha=0.7, s=40, label=label)

ax.set_title('PCA Projection\n(Some Cluster Separation - Global Structure)', fontsize=16, fontweight='bold')
ax.set_xlabel('Principal Component 1', fontweight='bold')
ax.set_ylabel('Principal Component 2', fontweight='bold')
ax.legend(loc='upper right')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06b_pca_cluster_projection/chart.pdf")
