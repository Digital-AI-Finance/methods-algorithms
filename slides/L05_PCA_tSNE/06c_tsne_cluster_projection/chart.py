"""t-SNE Cluster Projection - Runs ACTUAL sklearn t-SNE on MNIST digits.
Shows that t-SNE provides clear cluster separation."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

CHART_METADATA = {
    'title': 't-SNE Cluster Projection',
    'description': 't-SNE 2D projection shows clear cluster separation on digits data',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/06c_tsne_cluster_projection'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Color palette for 10 digit classes
colors = ['#3333B2', '#0066CC', '#FF7F0E', '#2CA02C', '#D62728',
          '#ADADE0', '#8B4513', '#FF69B4', '#808080', '#000000']

# Load ACTUAL high-dimensional data
digits = load_digits()
X, y = digits.data, digits.target

# Best practice: PCA first to 30 dims, then t-SNE
pca = PCA(n_components=30, random_state=42)
X_pca = pca.fit_transform(X)

# Run ACTUAL t-SNE
tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=1000)
X_tsne = tsne.fit_transform(X_pca)

fig, ax = plt.subplots(figsize=(10, 6))

for digit in range(10):
    mask = y == digit
    ax.scatter(X_tsne[mask, 0], X_tsne[mask, 1], c=colors[digit], label=str(digit),
               s=15, alpha=0.7, edgecolors='none')

ax.set_title('t-SNE Projection of MNIST Digits\n(Clear Cluster Separation -- Local Structure Preserved)',
             fontsize=16, fontweight='bold')
ax.set_xlabel('t-SNE Dimension 1', fontweight='bold')
ax.set_ylabel('t-SNE Dimension 2', fontweight='bold')
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=11,
          title='Digit', title_fontsize=12, markerscale=2)
ax.grid(True, alpha=0.3)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06c_tsne_cluster_projection/chart.pdf")
