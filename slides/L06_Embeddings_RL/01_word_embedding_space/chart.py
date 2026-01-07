"""Word Embedding Space - 2D visualization of word vectors"""
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

fig, ax = plt.subplots(figsize=(10, 6))

# Simulated 2D word embeddings (after dimensionality reduction)
# Finance-related words clustered by concept
words = {
    # Financial terms (cluster 1)
    'stock': (2.1, 1.8), 'equity': (2.5, 2.0), 'share': (2.3, 1.5),
    'bond': (1.8, 2.2), 'dividend': (2.0, 2.5),
    # Risk terms (cluster 2)
    'risk': (-1.5, 1.2), 'volatility': (-1.8, 0.8), 'hedge': (-1.2, 1.5),
    'exposure': (-1.6, 1.8), 'loss': (-2.0, 1.0),
    # Action terms (cluster 3)
    'buy': (0.5, -1.5), 'sell': (0.8, -1.8), 'trade': (0.2, -1.2),
    'invest': (1.0, -1.4), 'hold': (0.6, -2.0),
    # Sentiment (cluster 4)
    'bullish': (-0.5, -1.0), 'bearish': (-0.8, -0.7), 'positive': (-0.3, -0.5),
    'negative': (-1.0, -0.3), 'neutral': (-0.6, -1.5)
}

# Colors by cluster
cluster_colors = {
    'Financial': MLBLUE,
    'Risk': MLRED,
    'Action': MLGREEN,
    'Sentiment': MLORANGE
}

word_clusters = {
    'Financial': ['stock', 'equity', 'share', 'bond', 'dividend'],
    'Risk': ['risk', 'volatility', 'hedge', 'exposure', 'loss'],
    'Action': ['buy', 'sell', 'trade', 'invest', 'hold'],
    'Sentiment': ['bullish', 'bearish', 'positive', 'negative', 'neutral']
}

# Plot each cluster
for cluster, word_list in word_clusters.items():
    xs = [words[w][0] for w in word_list]
    ys = [words[w][1] for w in word_list]
    ax.scatter(xs, ys, c=cluster_colors[cluster], s=100, label=cluster, alpha=0.7)
    for word in word_list:
        ax.annotate(word, words[word], fontsize=10,
                    xytext=(5, 5), textcoords='offset points')

# Draw some relationships
ax.annotate('', xy=words['sell'], xytext=words['buy'],
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
ax.annotate('', xy=words['bearish'], xytext=words['bullish'],
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

ax.set_xlabel('Embedding Dimension 1')
ax.set_ylabel('Embedding Dimension 2')
ax.set_title('Word Embedding Space (Finance Domain)')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='gray', linewidth=0.5)
ax.axvline(x=0, color='gray', linewidth=0.5)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 01_word_embedding_space/chart.pdf")
