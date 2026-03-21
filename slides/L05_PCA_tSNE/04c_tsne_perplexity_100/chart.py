"""t-SNE with High Perplexity (100) - Runs ACTUAL sklearn t-SNE on blob data."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.datasets import make_blobs
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 't-SNE High Perplexity',
    'description': 'Perplexity=100 emphasizes global structure over local',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/04c_tsne_perplexity_100'
}


# Generate actual high-dimensional clustered data (same as 04a/04b for consistency)
X, y = make_blobs(n_samples=300, centers=4, n_features=10,
                  random_state=42, cluster_std=2.0)

# Run ACTUAL t-SNE with perplexity=100
tsne = TSNE(n_components=2, perplexity=100, random_state=42, n_iter=1000)
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

ax.set_title('t-SNE: Perplexity = 100\n(Focus on Global Structure)', fontsize=16, fontweight='bold')
ax.set_xlabel('t-SNE Dimension 1', fontweight='bold')
ax.set_ylabel('t-SNE Dimension 2', fontweight='bold')
ax.legend(loc='best', framealpha=0.9)
ax.grid(True, alpha=0.3)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 04c_tsne_perplexity_100/chart.pdf")
