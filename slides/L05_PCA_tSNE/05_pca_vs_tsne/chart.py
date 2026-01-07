"""PCA vs t-SNE Comparison - Linear vs Non-linear embeddings"""
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

np.random.seed(42)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Generate Swiss roll-like data (non-linear manifold)
n = 300
t = 1.5 * np.pi * (1 + 2 * np.random.rand(n))
x_original = t * np.cos(t)
y_original = 21 * np.random.rand(n)
z_original = t * np.sin(t)

# Color by position on manifold
colors = t

# PCA projection (linear - projects to first two PCs)
ax1 = axes[0]
# PCA would project along directions of max variance
# For Swiss roll, this creates overlap
pca_x = x_original + 0.1 * np.random.randn(n)
pca_y = z_original + 0.1 * np.random.randn(n)

scatter1 = ax1.scatter(pca_x, pca_y, c=colors, cmap='viridis', alpha=0.7, s=30)
ax1.set_title('PCA (Linear)\nStructure Overlaps', fontsize=14, fontweight='bold')
ax1.set_xlabel('PC1', fontweight='bold')
ax1.set_ylabel('PC2', fontweight='bold')
ax1.set_aspect('equal')

# t-SNE projection (non-linear - unrolls manifold)
ax2 = axes[1]
# t-SNE would unroll the manifold
tsne_x = t + np.random.randn(n) * 0.3
tsne_y = y_original / 5 + np.random.randn(n) * 0.3

scatter2 = ax2.scatter(tsne_x, tsne_y, c=colors, cmap='viridis', alpha=0.7, s=30)
ax2.set_title('t-SNE (Non-linear)\nManifold Unrolled', fontsize=14, fontweight='bold')
ax2.set_xlabel('t-SNE 1', fontweight='bold')
ax2.set_ylabel('t-SNE 2', fontweight='bold')
ax2.set_aspect('equal')

# Add colorbar
cbar = fig.colorbar(scatter2, ax=axes.ravel().tolist(), shrink=0.8)
cbar.set_label('Position on Manifold', fontweight='bold')

fig.suptitle('PCA vs t-SNE: Linear vs Non-linear Dimensionality Reduction',
             fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05_pca_vs_tsne/chart.pdf")
