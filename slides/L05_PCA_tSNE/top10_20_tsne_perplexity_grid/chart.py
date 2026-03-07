"""t-SNE Perplexity Grid - 2x2 subplot showing t-SNE with perplexity 5, 15, 30, 100."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.datasets import make_blobs

CHART_METADATA = {
    "title": "t-SNE: Effect of Perplexity",
    "description": "2x2 grid showing t-SNE embeddings at four perplexity values",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_20_tsne_perplexity_grid"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

cluster_colors = [MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE]

X, y = make_blobs(n_samples=300, n_features=10, centers=5, random_state=42)

perplexities = [5, 15, 30, 100]
fig, axes = plt.subplots(2, 2, figsize=(10, 6))
axes = axes.ravel()

for idx, perp in enumerate(perplexities):
    tsne = TSNE(n_components=2, perplexity=perp, random_state=42, learning_rate='auto')
    X_emb = tsne.fit_transform(X)

    for cls in range(5):
        mask = y == cls
        axes[idx].scatter(X_emb[mask, 0], X_emb[mask, 1], c=cluster_colors[cls],
                          alpha=0.6, s=18, edgecolors='none')

    axes[idx].set_title(f'Perplexity = {perp}', fontsize=13)
    axes[idx].set_xticks([])
    axes[idx].set_yticks([])

fig.suptitle('t-SNE: Effect of Perplexity', fontsize=16, fontweight='bold', y=0.98)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_20_tsne_perplexity_grid/chart.pdf")
