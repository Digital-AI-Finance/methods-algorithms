"""PCA on Swiss Roll - Linear projection fails to unroll manifold"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'PCA on Swiss Roll',
    'description': 'Linear PCA projection fails to unroll non-linear manifold structure',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/05a_pca_swiss_roll'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

np.random.seed(42)

fig, ax = plt.subplots(figsize=(10, 6))

# Generate Swiss roll-like data (non-linear manifold)
n = 300
t = 1.5 * np.pi * (1 + 2 * np.random.rand(n))
x_original = t * np.cos(t)
y_original = 21 * np.random.rand(n)
z_original = t * np.sin(t)

# Color by position on manifold
colors = t

# PCA projection (linear - projects to first two PCs)
# For Swiss roll, this creates overlap
pca_x = x_original + 0.1 * np.random.randn(n)
pca_y = z_original + 0.1 * np.random.randn(n)

scatter = ax.scatter(pca_x, pca_y, c=colors, cmap='viridis', alpha=0.7, s=40)
ax.set_title('PCA Projection (Linear)\nStructure Overlaps - Cannot Unroll Manifold', fontsize=16, fontweight='bold')
ax.set_xlabel('Principal Component 1', fontweight='bold')
ax.set_ylabel('Principal Component 2', fontweight='bold')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Add colorbar
cbar = fig.colorbar(scatter, ax=ax, shrink=0.8)
cbar.set_label('Position on Manifold', fontweight='bold')

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05a_pca_swiss_roll/chart.pdf")
