"""t-SNE with Low Perplexity (5) - Focus on local structure
Runs ACTUAL sklearn t-SNE on high-dimensional blob data."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.datasets import make_blobs

CHART_METADATA = {
    'title': 't-SNE Low Perplexity',
    'description': 'Perplexity=5 focuses on very local neighborhood structure',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/04a_tsne_perplexity_5'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLLAVENDER = '#ADADE0'

# Generate actual high-dimensional clustered data
X, y = make_blobs(n_samples=300, centers=4, n_features=10,
                  random_state=42, cluster_std=2.0)

# Run ACTUAL t-SNE with perplexity=5
tsne = TSNE(n_components=2, perplexity=5, random_state=42, n_iter=1000)
X_embedded = tsne.fit_transform(X)

# Plot with course colors
cluster_colors = [MLBLUE, MLORANGE, MLGREEN, MLRED]
cluster_names = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4']

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(4):
    mask = y == i
    ax.scatter(X_embedded[mask, 0], X_embedded[mask, 1],
               c=cluster_colors[i], alpha=0.7, s=50, label=cluster_names[i],
               edgecolors='white', linewidths=0.3)

ax.set_title('t-SNE: Perplexity = 5\n(Focus on Local Structure)', fontsize=16, fontweight='bold')
ax.set_xlabel('t-SNE Dimension 1', fontweight='bold')
ax.set_ylabel('t-SNE Dimension 2', fontweight='bold')
ax.legend(loc='best', framealpha=0.9)
ax.grid(True, alpha=0.3)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04a_tsne_perplexity_5/chart.pdf")
