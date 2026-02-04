"""Similarity Heatmap - Cosine similarity between word embeddings"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 11, 'ytick.labelsize': 11, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

CHART_METADATA = {
    "title": "Similarity Heatmap",
    "description": "Cosine similarity matrix between word embeddings",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/02_similarity_heatmap"
}

np.random.seed(42)

fig, ax = plt.subplots(figsize=(10, 8))

# Words for comparison
words = ['stock', 'equity', 'bond', 'risk', 'volatility', 'buy', 'sell', 'bullish', 'bearish']

# Simulated similarity matrix (based on semantic relationships)
n = len(words)
similarity = np.eye(n)

# Set realistic similarities
pairs = {
    ('stock', 'equity'): 0.85, ('stock', 'bond'): 0.45, ('stock', 'risk'): 0.35,
    ('stock', 'buy'): 0.40, ('stock', 'sell'): 0.38, ('stock', 'bullish'): 0.30,
    ('equity', 'bond'): 0.50, ('equity', 'risk'): 0.32, ('bond', 'risk'): 0.40,
    ('risk', 'volatility'): 0.82, ('risk', 'sell'): 0.25, ('volatility', 'bearish'): 0.35,
    ('buy', 'sell'): 0.72, ('buy', 'bullish'): 0.55, ('sell', 'bearish'): 0.52,
    ('bullish', 'bearish'): 0.70, ('equity', 'buy'): 0.35, ('bond', 'buy'): 0.30,
    ('risk', 'bearish'): 0.45, ('volatility', 'sell'): 0.28, ('stock', 'volatility'): 0.38
}

for (w1, w2), sim in pairs.items():
    i, j = words.index(w1), words.index(w2)
    similarity[i, j] = sim
    similarity[j, i] = sim

# Fill remaining with low random similarities
for i in range(n):
    for j in range(i+1, n):
        if similarity[i, j] == 0:
            similarity[i, j] = np.random.uniform(0.1, 0.25)
            similarity[j, i] = similarity[i, j]

im = ax.imshow(similarity, cmap='RdYlGn', aspect='auto', vmin=0, vmax=1)

ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels(words, rotation=45, ha='right')
ax.set_yticklabels(words)

# Add colorbar
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Cosine Similarity', fontsize=12)

# Add text annotations
for i in range(n):
    for j in range(n):
        text = ax.text(j, i, f'{similarity[i, j]:.2f}',
                       ha='center', va='center', fontsize=8,
                       color='white' if similarity[i, j] > 0.5 else 'black')

ax.set_title('Word Embedding Similarity Matrix')

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_similarity_heatmap/chart.pdf")
