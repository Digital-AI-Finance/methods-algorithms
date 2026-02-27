"""Similarity Heatmap - Cosine similarity from real GloVe embeddings"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 11, 'ytick.labelsize': 11, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

CHART_METADATA = {
    "title": "Similarity Heatmap",
    "description": "Cosine similarity matrix from real GloVe-50d embeddings",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/02_similarity_heatmap"
}

np.random.seed(42)
cache_path = Path(__file__).parent / 'similarity_cache.npy'

words = ['stock', 'equity', 'bond', 'risk', 'volatility', 'buy', 'sell', 'bullish', 'bearish']

try:
    import gensim.downloader as api
    from sklearn.metrics.pairwise import cosine_similarity
    model = api.load('glove-wiki-gigaword-50')
    vectors = np.array([model[w] for w in words])
    similarity = cosine_similarity(vectors)
    np.save(cache_path, similarity)
    print("Computed similarities from GloVe embeddings")
except Exception as e:
    print(f"gensim unavailable ({e}), using cached similarities")
    similarity = np.load(cache_path)

n = len(words)
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(similarity, cmap='RdYlGn', aspect='auto', vmin=0, vmax=1)

ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels(words, rotation=45, ha='right')
ax.set_yticklabels(words)

cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Cosine Similarity', fontsize=12)

for i in range(n):
    for j in range(n):
        ax.text(j, i, f'{similarity[i, j]:.2f}',
                ha='center', va='center', fontsize=8,
                color='white' if similarity[i, j] > 0.5 else 'black')

ax.set_title('Word Embedding Similarity (GloVe-50d)')

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_similarity_heatmap/chart.pdf")
