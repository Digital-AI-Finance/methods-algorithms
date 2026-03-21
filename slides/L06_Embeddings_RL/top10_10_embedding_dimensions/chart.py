"""Embedding Quality vs Dimensions - Shows how truncated embeddings preserve similarity structure."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Embedding Quality vs Number of Dimensions",
    "description": "Measures how truncated embeddings preserve pairwise cosine similarity structure",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_10_embedding_dimensions"
}


np.random.seed(42)

# Create "true" 50D embedding matrix with some structure
n_words = 20
full_dim = 50
# Create embeddings with a few dominant directions (realistic structure)
base = np.random.randn(n_words, 5) @ np.random.randn(5, full_dim)  # low-rank structure
noise = np.random.randn(n_words, full_dim) * 0.5
embeddings_full = base + noise

# Compute full cosine similarity
def cosine_sim_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-10)
    X_norm = X / norms
    return X_norm @ X_norm.T

full_sim = cosine_sim_matrix(embeddings_full)
# Extract upper triangle (no diagonal)
idx = np.triu_indices(n_words, k=1)
full_sim_vec = full_sim[idx]

# For each truncated dim, compute correlation with full sim
dims_to_test = [2, 5, 10, 15, 20, 30, 40, 50]
correlations = []

for d in dims_to_test:
    trunc = embeddings_full[:, :d]
    trunc_sim = cosine_sim_matrix(trunc)
    trunc_sim_vec = trunc_sim[idx]
    corr = np.corrcoef(full_sim_vec, trunc_sim_vec)[0, 1]
    correlations.append(corr)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(dims_to_test, correlations, color=MLBLUE, linewidth=2.5, marker='o', markersize=8,
        markerfacecolor='white', markeredgecolor=MLBLUE, markeredgewidth=2)

# Highlight the "diminishing returns" region
ax.axvspan(20, 50, alpha=0.08, color=MLGREEN)
ax.text(35, min(correlations) + 0.05, 'Diminishing\nreturns', fontsize=12,
        ha='center', color=MLGREEN, fontstyle='italic')

ax.set_title("Embedding Quality vs Number of Dimensions", fontsize=16, fontweight='bold')
ax.set_xlabel("Embedding Dimensions")
ax.set_ylabel("Similarity Preservation (Correlation)")
ax.set_ylim(0, 1.05)
ax.set_xticks(dims_to_test)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_10_embedding_dimensions/chart.pdf")
