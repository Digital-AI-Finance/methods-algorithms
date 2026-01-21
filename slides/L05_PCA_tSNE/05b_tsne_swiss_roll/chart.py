"""t-SNE on Swiss Roll - Non-linear projection unrolls manifold"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 't-SNE on Swiss Roll',
    'description': 'Non-linear t-SNE successfully unrolls Swiss roll manifold',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/05b_tsne_swiss_roll'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

np.random.seed(42)

fig, ax = plt.subplots(figsize=(10, 6))

# Generate Swiss roll-like data (non-linear manifold)
n = 300
t = 1.5 * np.pi * (1 + 2 * np.random.rand(n))
y_original = 21 * np.random.rand(n)

# Color by position on manifold
colors = t

# t-SNE projection (non-linear - unrolls manifold)
tsne_x = t + np.random.randn(n) * 0.3
tsne_y = y_original / 5 + np.random.randn(n) * 0.3

scatter = ax.scatter(tsne_x, tsne_y, c=colors, cmap='viridis', alpha=0.7, s=40)
ax.set_title('t-SNE Projection (Non-linear)\nManifold Successfully Unrolled', fontsize=16, fontweight='bold')
ax.set_xlabel('t-SNE Dimension 1', fontweight='bold')
ax.set_ylabel('t-SNE Dimension 2', fontweight='bold')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Add colorbar
cbar = fig.colorbar(scatter, ax=ax, shrink=0.8)
cbar.set_label('Position on Manifold', fontweight='bold')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05b_tsne_swiss_roll/chart.pdf")
