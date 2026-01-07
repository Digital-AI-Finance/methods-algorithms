"""t-SNE Perplexity Effect - Different perplexity values"""
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

# Generate clustered data
n_per_cluster = 50
centers = [(-3, 0), (0, 3), (3, 0)]
colors = [MLBLUE, MLGREEN, MLRED]

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

perplexities = [5, 30, 100]
titles = ['Perplexity = 5\n(Local structure)',
          'Perplexity = 30\n(Balanced)',
          'Perplexity = 100\n(Global structure)']

for ax, perp, title in zip(axes, perplexities, titles):
    # Simulate t-SNE output with different perplexities
    # Low perplexity: tighter clusters, more separation
    # High perplexity: more spread, clusters merge

    spread_factor = 0.3 + (perp / 100) * 0.7
    separation = 3 - (perp / 100) * 1.5

    for i, (cx, cy) in enumerate(centers):
        n = n_per_cluster
        x = np.random.randn(n) * spread_factor + cx * separation / 3
        y = np.random.randn(n) * spread_factor + cy * separation / 3
        ax.scatter(x, y, c=colors[i], alpha=0.7, s=30)

    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    # Add box
    for spine in ax.spines.values():
        spine.set_linewidth(2)

fig.suptitle('t-SNE: Effect of Perplexity Parameter', fontsize=16, fontweight='bold', y=1.02)

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=c, label=f'Cluster {i+1}')
                   for i, c in enumerate(colors)]
fig.legend(handles=legend_elements, loc='center right', bbox_to_anchor=(1.12, 0.5))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04_tsne_perplexity/chart.pdf")
