"""t-SNE Cluster Projection - Non-linear projection preserves local structure"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 't-SNE Cluster Projection',
    'description': 't-SNE 2D projection shows clear cluster separation',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/06c_tsne_cluster_projection'
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

# Generate clustered data
n_per_cluster = 100
labels = np.repeat([0, 1, 2], n_per_cluster)
color_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3']

# Simulate t-SNE - preserves local neighborhood (clusters well-separated)
tsne_centers = [(-3, 0), (2, 3), (2, -3)]
tsne_x = np.concatenate([tsne_centers[i][0] + np.random.randn(n_per_cluster) * 0.4
                          for i in range(3)])
tsne_y = np.concatenate([tsne_centers[i][1] + np.random.randn(n_per_cluster) * 0.4
                          for i in range(3)])

for i, (color, label) in enumerate(zip([MLBLUE, MLGREEN, MLRED], color_labels)):
    mask = labels == i
    ax.scatter(tsne_x[mask], tsne_y[mask], c=color, alpha=0.7, s=40, label=label)

ax.set_title('t-SNE Projection\n(Clear Cluster Separation - Local Structure)', fontsize=16, fontweight='bold')
ax.set_xlabel('t-SNE Dimension 1', fontweight='bold')
ax.set_ylabel('t-SNE Dimension 2', fontweight='bold')
ax.legend(loc='upper right')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06c_tsne_cluster_projection/chart.pdf")
