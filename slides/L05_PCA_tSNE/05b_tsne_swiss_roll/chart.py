"""t-SNE on Swiss Roll - Runs ACTUAL sklearn t-SNE on Swiss roll data.
Demonstrates that t-SNE can unroll nonlinear manifold structure."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.datasets import make_swiss_roll

CHART_METADATA = {
    'title': 't-SNE on Swiss Roll',
    'description': 'Non-linear t-SNE successfully unrolls Swiss roll manifold',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/05b_tsne_swiss_roll'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Generate Swiss roll data using sklearn (same params as 05a)
X, color = make_swiss_roll(n_samples=1500, noise=0.5, random_state=42)

# Run ACTUAL t-SNE to reduce from 3D to 2D
tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=1000)
X_tsne = tsne.fit_transform(X)

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(X_tsne[:, 0], X_tsne[:, 1], c=color, cmap='viridis',
                     alpha=0.7, s=15, edgecolors='none')
ax.set_title('t-SNE Projection of Swiss Roll (Non-linear)\nManifold Structure Preserved',
             fontsize=16, fontweight='bold')
ax.set_xlabel('t-SNE Dimension 1', fontweight='bold')
ax.set_ylabel('t-SNE Dimension 2', fontweight='bold')
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
print("Chart saved: 05b_tsne_swiss_roll/chart.pdf")
