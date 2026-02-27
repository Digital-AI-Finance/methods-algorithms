"""Word Embedding Space - 2D visualization of real GloVe word vectors"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

CHART_METADATA = {
    "title": "Word Embedding Space",
    "description": "2D PCA projection of real GloVe-50d word embeddings",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/01_word_embedding_space"
}

np.random.seed(42)
cache_path = Path(__file__).parent / 'embedding_cache.npz'

# Load real GloVe embeddings via gensim (with offline fallback)
words = ['stock', 'equity', 'share', 'bond', 'dividend',
         'risk', 'volatility', 'hedge', 'loss', 'exposure',
         'buy', 'sell', 'trade', 'invest', 'hold',
         'bullish', 'bearish', 'positive', 'negative', 'neutral']

word_clusters = {
    'Financial': (['stock', 'equity', 'share', 'bond', 'dividend'], MLBLUE),
    'Risk': (['risk', 'volatility', 'hedge', 'loss', 'exposure'], MLRED),
    'Action': (['buy', 'sell', 'trade', 'invest', 'hold'], MLGREEN),
    'Sentiment': (['bullish', 'bearish', 'positive', 'negative', 'neutral'], MLORANGE),
}

try:
    import gensim.downloader as api
    from sklearn.decomposition import PCA
    model = api.load('glove-wiki-gigaword-50')
    vectors = np.array([model[w] for w in words])
    pca = PCA(n_components=2, random_state=42)
    coords = pca.fit_transform(vectors)
    np.savez(cache_path, coords=coords, words=words)
    print("Loaded GloVe embeddings via gensim")
except Exception as e:
    print(f"gensim unavailable ({e}), using cached embeddings")
    data = np.load(cache_path, allow_pickle=True)
    coords = data['coords']

word_to_coord = {w: coords[i] for i, w in enumerate(words)}

fig, ax = plt.subplots(figsize=(10, 6))

for cluster, (word_list, color) in word_clusters.items():
    xs = [word_to_coord[w][0] for w in word_list]
    ys = [word_to_coord[w][1] for w in word_list]
    ax.scatter(xs, ys, c=color, s=100, label=cluster, alpha=0.7)
    for word in word_list:
        ax.annotate(word, word_to_coord[word], fontsize=10,
                    xytext=(5, 5), textcoords='offset points')

# Draw semantic relationships
ax.annotate('', xy=word_to_coord['sell'], xytext=word_to_coord['buy'],
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
ax.annotate('', xy=word_to_coord['bearish'], xytext=word_to_coord['bullish'],
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

ax.set_xlabel('PCA Dimension 1')
ax.set_ylabel('PCA Dimension 2')
ax.set_title('Word Embedding Space (GloVe-50d, Finance Domain)')
ax.legend(loc='best')
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 01_word_embedding_space/chart.pdf")
