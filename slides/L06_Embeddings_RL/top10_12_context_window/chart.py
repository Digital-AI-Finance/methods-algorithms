"""Context Window Size vs Embedding Quality - Shows how context window size affects embedding quality."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Context Window Size vs Embedding Quality",
    "description": "Simulated effect of context window size on semantic similarity quality",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_12_context_window"
}


np.random.seed(42)

window_sizes = np.array([1, 2, 3, 5, 8, 12])
# Quality curve: rises fast, peaks around 5, slight decline after
quality = 1 - np.exp(-window_sizes / 2.0) - 0.02 * window_sizes
# Add slight noise for uncertainty band
quality_std = 0.03 + 0.01 * window_sizes

# Smooth curve for interpolation
w_smooth = np.linspace(1, 12, 100)
q_smooth = 1 - np.exp(-w_smooth / 2.0) - 0.02 * w_smooth

fig, ax = plt.subplots(figsize=(10, 6))

# Uncertainty band on smooth curve
q_smooth_std = 0.03 + 0.01 * w_smooth
ax.fill_between(w_smooth, q_smooth - q_smooth_std, q_smooth + q_smooth_std,
                color=MLBLUE, alpha=0.15, label='Uncertainty range')

# Smooth line
ax.plot(w_smooth, q_smooth, color=MLBLUE, linewidth=2.5, alpha=0.5)

# Data points
ax.plot(window_sizes, quality, color=MLBLUE, linewidth=2.5, marker='o', markersize=10,
        markerfacecolor='white', markeredgecolor=MLBLUE, markeredgewidth=2.5,
        label='Semantic similarity score', zorder=5)

# Highlight optimal region
best_idx = np.argmax(quality)
ax.axvline(x=window_sizes[best_idx], color=MLRED, linestyle='--', alpha=0.6, linewidth=1.5)
ax.annotate(f'Optimal: w={window_sizes[best_idx]}',
            (window_sizes[best_idx], quality[best_idx]),
            textcoords="offset points", xytext=(15, 10),
            fontsize=12, color=MLRED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MLRED))

ax.set_title("Context Window Size vs Embedding Quality", fontsize=16, fontweight='bold')
ax.set_xlabel("Context Window Size")
ax.set_ylabel("Semantic Similarity Score")
ax.set_xticks(window_sizes)
ax.legend(loc='lower right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_12_context_window/chart.pdf")
