import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

# Set random seed
np.random.seed(42)

# Configure matplotlib for Beamer display
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13,
    'legend.fontsize': 13,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

# Color palette
MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLLAVENDER = '#ADADE0'

# Chart metadata
CHART_METADATA = {
    'title': 'Negative Sampling: Binary Classification Instead of Full Softmax',
    'description': 'Illustration of negative sampling in Word2Vec showing target word, positive context sample, and multiple negative samples with binary classification objectives',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/10_negative_sampling'
}

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Target word (center)
target_box = FancyBboxPatch((4.0, 2.5), 2.0, 1.0, boxstyle="round,pad=0.1",
                            edgecolor=MLORANGE, facecolor='lightyellow', linewidth=3)
ax.add_patch(target_box)
ax.text(5.0, 3.0, 'stock', ha='center', va='center', fontsize=18,
        weight='bold', color=MLORANGE)
ax.text(5.0, 2.3, '(target word)', ha='center', va='top', fontsize=9,
        style='italic')

# Positive context word (top right)
pos_box = FancyBboxPatch((7.5, 4.0), 1.5, 0.7, boxstyle="round,pad=0.05",
                         edgecolor=MLGREEN, facecolor='lightgreen', linewidth=2.5)
ax.add_patch(pos_box)
ax.text(8.25, 4.35, 'market', ha='center', va='center', fontsize=13,
        weight='bold', color=MLGREEN)
ax.text(8.25, 3.8, 'P(+) → 1', ha='center', va='top', fontsize=9,
        weight='bold', color=MLGREEN)

# Arrow from target to positive
arrow_pos = FancyArrowPatch((6.0, 3.2), (7.5, 4.2), arrowstyle='->',
                           mutation_scale=20, linewidth=2.5, color=MLGREEN)
ax.add_patch(arrow_pos)
ax.text(6.7, 3.9, 'positive\nsample', ha='center', va='center', fontsize=8,
        color=MLGREEN, weight='bold')

# Negative samples (bottom right)
negative_words = ['piano', 'dog', 'blue', 'chair']
for i, word in enumerate(negative_words):
    y = 2.6 - i * 0.55
    neg_box = FancyBboxPatch((7.5, y - 0.25), 1.5, 0.5, boxstyle="round,pad=0.03",
                             edgecolor=MLRED, facecolor='mistyrose', linewidth=1.5)
    ax.add_patch(neg_box)
    ax.text(8.25, y, word, ha='center', va='center', fontsize=10, color=MLRED)

    # Arrow from target to negative
    arrow_neg = FancyArrowPatch((6.0, 2.9), (7.5, y), arrowstyle='->',
                               mutation_scale=15, linewidth=1.2, color=MLRED,
                               linestyle='--')
    ax.add_patch(arrow_neg)

ax.text(8.25, 0.5, 'P(+) → 0', ha='center', va='center', fontsize=9,
        weight='bold', color=MLRED)
ax.text(6.5, 1.2, 'negative\nsamples', ha='center', va='center', fontsize=8,
        color=MLRED, weight='bold')

# Corpus/sliding window (left side)
corpus_box = FancyBboxPatch((0.3, 4.0), 2.5, 1.2, boxstyle="round,pad=0.05",
                            edgecolor=MLBLUE, facecolor='lightblue', linewidth=2)
ax.add_patch(corpus_box)
ax.text(1.55, 4.9, 'Corpus', ha='center', va='center', fontsize=11, weight='bold')
ax.text(1.55, 4.5, '"...the stock market..."', ha='center', va='center',
        fontsize=8, style='italic')
ax.text(1.55, 4.2, 'Sliding window', ha='center', va='center', fontsize=8)

# Arrow from corpus to target
corpus_arrow = FancyArrowPatch((2.8, 4.5), (4.0, 3.3), arrowstyle='->',
                              mutation_scale=20, linewidth=2, color=MLBLUE)
ax.add_patch(corpus_arrow)

# Objective function annotation (bottom)
formula_text = r"$\log \sigma(\mathbf{v}'_{context} \cdot \mathbf{v}_{target}) + \sum_{i=1}^{k} \log \sigma(-\mathbf{v}'_{neg_i} \cdot \mathbf{v}_{target})$"
ax.text(5.0, 1.5, 'Objective:', ha='center', va='center', fontsize=10,
        weight='bold', style='italic')
ax.text(5.0, 1.0, formula_text, ha='center', va='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                  edgecolor='black', linewidth=1))

# Efficiency note (top left)
efficiency_box = FancyBboxPatch((0.3, 2.0), 2.5, 1.0, boxstyle="round,pad=0.05",
                                edgecolor='gray', facecolor='whitesmoke',
                                linewidth=1, linestyle='--')
ax.add_patch(efficiency_box)
ax.text(1.55, 2.7, 'Efficiency Gain:', ha='center', va='center',
        fontsize=9, weight='bold')
ax.text(1.55, 2.4, 'k+1 samples', ha='center', va='center', fontsize=8)
ax.text(1.55, 2.15, 'instead of |V|', ha='center', va='center', fontsize=8)
ax.text(1.55, 1.9, '(k ≈ 5-20)', ha='center', va='center', fontsize=7,
        style='italic')

# Title
ax.text(5.0, 0.3, CHART_METADATA['title'], ha='center', va='center',
        fontsize=15, weight='bold')

# Save figure
plt.tight_layout()
plt.savefig('D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L06_Embeddings_RL/10_negative_sampling/chart.pdf',
            bbox_inches='tight', dpi=150)
print(f"Chart saved: {CHART_METADATA['title']}")
plt.close()
