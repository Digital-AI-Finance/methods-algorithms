"""t-SNE Convergence Over Iterations - Shows t-SNE at 250, 500, and 1000 iterations."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.datasets import make_blobs

CHART_METADATA = {
    "title": "t-SNE Convergence Over Iterations",
    "description": "Three-panel view of t-SNE embedding at different iteration counts",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_13_tsne_iterations"
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

cluster_colors = [MLBLUE, MLORANGE, MLGREEN, MLRED]

X, y = make_blobs(n_samples=300, n_features=10, centers=4, random_state=42)

iter_values = [250, 500, 1000]
fig, axes = plt.subplots(1, 3, figsize=(10, 6))

for idx, n_iter in enumerate(iter_values):
    tsne = TSNE(n_components=2, n_iter=n_iter, learning_rate='auto',
                random_state=42, perplexity=30)
    X_emb = tsne.fit_transform(X)

    for cls in range(4):
        mask = y == cls
        axes[idx].scatter(X_emb[mask, 0], X_emb[mask, 1], c=cluster_colors[cls],
                          alpha=0.6, s=20, edgecolors='none')

    axes[idx].set_title(f'{n_iter} iterations', fontsize=14)
    axes[idx].set_xticks([])
    axes[idx].set_yticks([])

fig.suptitle('t-SNE Convergence Over Iterations', fontsize=16, fontweight='bold', y=0.98)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_13_tsne_iterations/chart.pdf")
