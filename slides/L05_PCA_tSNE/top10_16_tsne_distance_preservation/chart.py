"""t-SNE Distance Preservation - Original vs embedded pairwise distances."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.datasets import make_blobs
from sklearn.metrics import pairwise_distances

CHART_METADATA = {
    "title": "t-SNE Distance Preservation",
    "description": "Scatter of original pairwise distances vs t-SNE embedded distances",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_16_tsne_distance_preservation"
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

X, y = make_blobs(n_samples=200, n_features=10, centers=4, random_state=42)

tsne = TSNE(n_components=2, random_state=42, perplexity=30, learning_rate='auto')
X_emb = tsne.fit_transform(X)

dist_orig = pairwise_distances(X)
dist_emb = pairwise_distances(X_emb)

np.random.seed(42)
n = len(X)
triu_idx = np.triu_indices(n, k=1)
all_pairs = len(triu_idx[0])
sample_idx = np.random.choice(all_pairs, size=min(500, all_pairs), replace=False)
d_orig = dist_orig[triu_idx[0][sample_idx], triu_idx[1][sample_idx]]
d_emb = dist_emb[triu_idx[0][sample_idx], triu_idx[1][sample_idx]]

fig, ax = plt.subplots()
ax.scatter(d_orig, d_emb, alpha=0.1, s=15, c=MLBLUE, edgecolors='none')

max_val = max(d_orig.max(), d_emb.max())
ax.plot([0, d_orig.max()], [0, d_emb.max() * d_orig.max() / d_orig.max()],
        color=MLRED, linestyle='--', linewidth=2, label='Perfect preservation', alpha=0.8)

ax.set_xlabel('Original Distance')
ax.set_ylabel('Embedded Distance')
ax.set_title('t-SNE Distance Preservation')
ax.legend(loc='upper left', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_16_tsne_distance_preservation/chart.pdf")
