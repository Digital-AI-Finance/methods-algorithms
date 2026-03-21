"""Embedding Dimensionality: Variance per Component - PCA on synthetic embeddings showing explained variance."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Embedding Dimensionality: Variance per Component",
    "description": "PCA explained variance on synthetic word embeddings with realistic low-rank structure",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_18_embedding_pca_variance"
}


np.random.seed(42)

# Create synthetic embedding matrix with realistic structure
n_words = 100
full_dim = 50

# A few dominant semantic directions + noise
n_dominant = 5
dominant_dirs = np.random.randn(n_dominant, full_dim)
# Give each direction a different scale (first few are strongest)
scales = np.array([3.0, 2.5, 2.0, 1.5, 1.0])
word_coeffs = np.random.randn(n_words, n_dominant)
structured = (word_coeffs * scales) @ dominant_dirs
noise = np.random.randn(n_words, full_dim) * 0.5
embeddings = structured + noise

# Run PCA
n_components = 20
pca = PCA(n_components=n_components, random_state=42)
pca.fit(embeddings)

var_ratio = pca.explained_variance_ratio_
cumulative = np.cumsum(var_ratio)

fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for individual variance
components = np.arange(1, n_components + 1)
bars = ax.bar(components, var_ratio, color=MLBLUE, alpha=0.7, label='Individual', edgecolor='white')

# Cumulative line on same axis
ax2 = ax.twinx()
ax2.grid(False)
ax2.plot(components, cumulative, color=MLRED, linewidth=2.5, marker='s', markersize=6,
         markerfacecolor='white', markeredgecolor=MLRED, markeredgewidth=2,
         label='Cumulative')
ax2.set_ylabel("Cumulative Explained Variance", color=MLRED)
ax2.tick_params(axis='y', labelcolor=MLRED)
ax2.set_ylim(0, 1.05)

# 90% threshold line
ax2.axhline(y=0.9, color=MLRED, linestyle=':', alpha=0.5, linewidth=1.5)
ax2.text(n_components - 1, 0.91, '90%', fontsize=11, color=MLRED, alpha=0.7)

ax.set_title("Embedding Dimensionality: Variance per Component", fontsize=16, fontweight='bold')
ax.set_xlabel("Component")
ax.set_ylabel("Explained Variance Ratio", color=MLBLUE)
ax.tick_params(axis='y', labelcolor=MLBLUE)
ax.set_xticks(components)

# Combined legend
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=12, framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_18_embedding_pca_variance/chart.pdf")
