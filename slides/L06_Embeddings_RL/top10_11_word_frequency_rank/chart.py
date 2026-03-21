"""Zipf's Law: Word Frequency vs Rank - Log-log plot of synthetic word frequencies following Zipf distribution."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Zipf's Law: Word Frequency vs Rank",
    "description": "Log-log plot showing synthetic word frequencies following Zipf distribution",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_11_word_frequency_rank"
}


np.random.seed(42)

# Generate synthetic word frequencies following Zipf's law
n_words = 10000
alpha = 1.0
C = 1e6
ranks = np.arange(1, n_words + 1)
# True Zipf frequencies with noise
frequencies = C / (ranks ** alpha)
# Add realistic noise (multiplicative)
noise = np.exp(np.random.randn(n_words) * 0.15)
frequencies_noisy = frequencies * noise

log_ranks = np.log10(ranks)
log_freqs = np.log10(frequencies_noisy)
log_freqs_true = np.log10(frequencies)

fig, ax = plt.subplots(figsize=(10, 6))

# Scatter of noisy data
ax.scatter(log_ranks, log_freqs, c=MLBLUE, alpha=0.3, s=4, rasterized=True)

# Theoretical Zipf line
ax.plot(log_ranks, log_freqs_true, color=MLRED, linewidth=2.5, linestyle='--',
        label=r"Zipf's law: $f \propto 1/r^{\alpha}$, $\alpha=1.0$")

# Annotate a few example words
example_words = {1: 'the', 2: 'of', 3: 'and', 10: 'in', 100: 'world', 1000: 'umbrella'}
for rank, word in example_words.items():
    idx = rank - 1
    ax.annotate(f'"{word}"', (log_ranks[idx], log_freqs[idx]),
                textcoords="offset points", xytext=(12, 5),
                fontsize=10, color=MLPURPLE, fontstyle='italic')

ax.set_title("Zipf's Law: Word Frequency vs Rank", fontsize=16, fontweight='bold')
ax.set_xlabel("log$_{10}$(Rank)")
ax.set_ylabel("log$_{10}$(Frequency)")
ax.legend(loc='upper right', fontsize=12, framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_11_word_frequency_rank/chart.pdf")
