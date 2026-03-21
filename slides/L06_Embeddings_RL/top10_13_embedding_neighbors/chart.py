"""Nearest Neighbors in Embedding Space - Query word with 5 nearest neighbors in 2D PCA projection."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from scipy.spatial.distance import cdist
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Nearest Neighbors in Embedding Space",
    "description": "Query word with 5 nearest neighbors in PCA-projected synthetic embeddings",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_13_embedding_neighbors"
}


np.random.seed(42)

# Define semantic clusters with synthetic 20D embeddings
dim = 20
financial_words = ['bank', 'stock', 'bond', 'loan', 'credit', 'fund', 'trade', 'yield', 'asset', 'risk']
tech_words = ['code', 'data', 'cloud', 'server', 'byte', 'pixel', 'algorithm', 'neural', 'chip', 'model']
nature_words = ['river', 'tree', 'mountain', 'forest', 'ocean', 'lake', 'valley', 'cliff', 'meadow', 'creek']

all_words = financial_words + tech_words + nature_words
n_words = len(all_words)

# Create cluster centers
center_fin = np.random.randn(dim) * 2
center_tech = np.random.randn(dim) * 2
center_nat = np.random.randn(dim) * 2

# Generate embeddings around cluster centers
embeddings = np.zeros((n_words, dim))
for i in range(10):
    embeddings[i] = center_fin + np.random.randn(dim) * 0.8       # financial
    embeddings[10 + i] = center_tech + np.random.randn(dim) * 0.8 # tech
    embeddings[20 + i] = center_nat + np.random.randn(dim) * 0.8  # nature

# PCA to 2D
pca = PCA(n_components=2, random_state=42)
coords = pca.fit_transform(embeddings)

# Query word: "bank" (index 0)
query_idx = 0
dists = cdist(embeddings[query_idx:query_idx+1], embeddings, metric='cosine')[0]
dists[query_idx] = np.inf  # exclude self
neighbor_idxs = np.argsort(dists)[:5]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot by cluster
cluster_colors = [MLBLUE] * 10 + [MLORANGE] * 10 + [MLPURPLE] * 10
cluster_labels = ['Financial', 'Technology', 'Nature']

for cluster_start, color, label in [(0, MLBLUE, 'Financial'), (10, MLORANGE, 'Technology'), (20, MLPURPLE, 'Nature')]:
    idxs = range(cluster_start, cluster_start + 10)
    ax.scatter(coords[list(idxs), 0], coords[list(idxs), 1],
               c=color, s=60, alpha=0.6, label=label, edgecolors='white', linewidth=0.5)

# Draw lines to nearest neighbors
for ni in neighbor_idxs:
    ax.plot([coords[query_idx, 0], coords[ni, 0]],
            [coords[query_idx, 1], coords[ni, 1]],
            color=MLGREEN, linewidth=2, alpha=0.7, zorder=3)

# Highlight query word
ax.scatter(coords[query_idx, 0], coords[query_idx, 1],
           c=MLRED, s=250, marker='*', zorder=6, edgecolors='darkred', linewidth=0.5,
           label='Query: "bank"')

# Label all points
for i, word in enumerate(all_words):
    fontweight = 'bold' if i == query_idx or i in neighbor_idxs else 'normal'
    alpha = 1.0 if i == query_idx or i in neighbor_idxs else 0.7
    ax.annotate(word, (coords[i, 0], coords[i, 1]),
                textcoords="offset points", xytext=(5, 5),
                fontsize=8, alpha=alpha, fontweight=fontweight)

ax.set_title("Nearest Neighbors in Embedding Space", fontsize=16, fontweight='bold')
ax.set_xlabel("First Principal Component")
ax.set_ylabel("Second Principal Component")
ax.legend(loc='best', fontsize=11, framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_13_embedding_neighbors/chart.pdf")
