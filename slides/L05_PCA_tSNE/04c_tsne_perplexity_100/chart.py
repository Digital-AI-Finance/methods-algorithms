"""t-SNE with High Perplexity (100) - Focus on global structure"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 't-SNE High Perplexity',
    'description': 'Perplexity=100 emphasizes global structure over local',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/04c_tsne_perplexity_100'
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

# Generate clustered data
n_per_cluster = 50
centers = [(-3, 0), (0, 3), (3, 0)]
colors = [MLBLUE, MLGREEN, MLRED]

fig, ax = plt.subplots(figsize=(10, 6))

perplexity = 100
# High perplexity: more spread, clusters may merge
spread_factor = 0.3 + (perplexity / 100) * 0.7
separation = 3 - (perplexity / 100) * 1.5

for i, (cx, cy) in enumerate(centers):
    n = n_per_cluster
    x = np.random.randn(n) * spread_factor + cx * separation / 3
    y = np.random.randn(n) * spread_factor + cy * separation / 3
    ax.scatter(x, y, c=colors[i], alpha=0.7, s=50, label=f'Cluster {i+1}')

ax.set_title('t-SNE: Perplexity = 100\n(Focus on Global Structure)', fontsize=16, fontweight='bold')
ax.set_xlabel('t-SNE Dimension 1', fontweight='bold')
ax.set_ylabel('t-SNE Dimension 2', fontweight='bold')
ax.legend(loc='upper right')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04c_tsne_perplexity_100/chart.pdf")
