"""Original Clusters - High-dimensional data shown in 2D projection"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Original Clusters',
    'description': 'High-dimensional cluster structure (showing 2 of 50 dimensions)',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/06a_original_clusters'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
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
colors_map = {0: MLBLUE, 1: MLGREEN, 2: MLRED}
color_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3']

# Original data (first 2 dims for visualization)
X_2d = np.vstack([centers_hd[i][:2] + np.random.randn(n_per_cluster, 2) * 0.5
                  for i in range(3)])

for i, (color, label) in enumerate(zip([MLBLUE, MLGREEN, MLRED], color_labels)):
    mask = labels == i
    ax.scatter(X_2d[mask, 0], X_2d[mask, 1], c=color, alpha=0.7, s=40, label=label)

ax.set_title('Original High-Dimensional Data\n(Showing 2 of 50 Dimensions - Clusters Overlap)', fontsize=16, fontweight='bold')
ax.set_xlabel('Dimension 1', fontweight='bold')
ax.set_ylabel('Dimension 2', fontweight='bold')
ax.legend(loc='upper right')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06a_original_clusters/chart.pdf")
