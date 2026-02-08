"""PCA on Swiss Roll - Runs ACTUAL sklearn PCA on Swiss roll data.
Demonstrates that linear PCA cannot unroll a nonlinear manifold."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.datasets import make_swiss_roll

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

# Generate Swiss roll data using sklearn
X, color = make_swiss_roll(n_samples=1500, noise=0.5, random_state=42)
# X has shape (1500, 3), color is the manifold parameter t

# Run ACTUAL PCA to reduce from 3D to 2D
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X)

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=color, cmap='viridis',
                     alpha=0.7, s=15, edgecolors='none')
ax.set_title('PCA Projection of Swiss Roll (Linear)\nStructure Overlaps -- Cannot Unroll Manifold',
             fontsize=16, fontweight='bold')
ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% var.)', fontweight='bold')
ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% var.)', fontweight='bold')
ax.grid(True, alpha=0.3)

cbar = fig.colorbar(scatter, ax=ax, shrink=0.8)
cbar.set_label('Position on Manifold', fontweight='bold')

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05a_pca_swiss_roll/chart.pdf")
