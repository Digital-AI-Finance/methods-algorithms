import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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
    'title': 'Skip-gram Architecture: Predict Context from Target',
    'description': 'Neural network architecture diagram showing Skip-gram model components: input one-hot vector, embedding layer, and softmax output layer for context prediction',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/08_skipgram_architecture'
}

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Input layer (one-hot vector)
input_box = FancyBboxPatch((0.5, 2.2), 1.5, 1.6, boxstyle="round,pad=0.05",
                           edgecolor=MLPURPLE, facecolor=MLLAVENDER, linewidth=2)
ax.add_patch(input_box)
ax.text(1.25, 3.5, 'Input', ha='center', va='center', fontsize=12, weight='bold')
ax.text(1.25, 3.0, 'One-hot', ha='center', va='center', fontsize=10)
ax.text(1.25, 2.7, 'Vector', ha='center', va='center', fontsize=10)
ax.text(1.25, 2.4, '(size V)', ha='center', va='center', fontsize=9, style='italic')

# Sliding window illustration (top)
window_y = 5.0
words = ['...', 'of', 'the', 'stock', 'market', 'in', '...']
for i, word in enumerate(words):
    x = 0.5 + i * 0.6
    if word == 'stock':
        color = MLORANGE
        weight = 'bold'
    else:
        color = 'black'
        weight = 'normal'
    ax.text(x, window_y, word, ha='center', va='center', fontsize=10,
            color=color, weight=weight)
ax.text(2.5, 5.5, 'Target word', ha='center', va='bottom', fontsize=9,
        color=MLORANGE, style='italic')

# Hidden layer (embedding matrix)
hidden_box = FancyBboxPatch((3.5, 2.2), 1.5, 1.6, boxstyle="round,pad=0.05",
                            edgecolor=MLBLUE, facecolor='lightblue', linewidth=2)
ax.add_patch(hidden_box)
ax.text(4.25, 3.5, 'Hidden', ha='center', va='center', fontsize=12, weight='bold')
ax.text(4.25, 3.0, 'Embedding', ha='center', va='center', fontsize=10)
ax.text(4.25, 2.7, 'Layer', ha='center', va='center', fontsize=10)
ax.text(4.25, 2.4, '(size d)', ha='center', va='center', fontsize=9, style='italic')

# Output layer (softmax)
output_box = FancyBboxPatch((6.5, 2.2), 1.5, 1.6, boxstyle="round,pad=0.05",
                            edgecolor=MLGREEN, facecolor='lightgreen', linewidth=2)
ax.add_patch(output_box)
ax.text(7.25, 3.5, 'Output', ha='center', va='center', fontsize=12, weight='bold')
ax.text(7.25, 3.0, 'Softmax', ha='center', va='center', fontsize=10)
ax.text(7.25, 2.7, 'Context', ha='center', va='center', fontsize=10)
ax.text(7.25, 2.4, '(size V)', ha='center', va='center', fontsize=9, style='italic')

# Context predictions (right side)
context_words = ['the', 'market']
for i, word in enumerate(context_words):
    y = 3.8 - i * 0.8
    ax.text(8.8, y, f'P({word}|stock)', ha='left', va='center', fontsize=9,
            color=MLGREEN)

# Arrows between layers
arrow1 = FancyArrowPatch((2.0, 3.0), (3.5, 3.0), arrowstyle='->',
                        mutation_scale=20, linewidth=2, color=MLPURPLE)
ax.add_patch(arrow1)
ax.text(2.75, 3.4, 'Input Embeddings W', ha='center', va='bottom',
        fontsize=9, weight='bold', color=MLPURPLE)

arrow2 = FancyArrowPatch((5.0, 3.0), (6.5, 3.0), arrowstyle='->',
                        mutation_scale=20, linewidth=2, color=MLBLUE)
ax.add_patch(arrow2)
ax.text(5.75, 3.4, "Output Embeddings W'", ha='center', va='bottom',
        fontsize=9, weight='bold', color=MLBLUE)

arrow3 = FancyArrowPatch((8.0, 3.0), (8.6, 3.0), arrowstyle='->',
                        mutation_scale=20, linewidth=2, color=MLGREEN)
ax.add_patch(arrow3)

# Window size annotation
ax.annotate('', xy=(3.7, 5.0), xytext=(1.3, 5.0),
            arrowprops=dict(arrowstyle='<->', lw=1.5, color='gray'))
ax.text(2.5, 4.6, 'Window size = 2', ha='center', va='top',
        fontsize=9, style='italic', color='gray')

# Title
ax.text(5.0, 0.3, CHART_METADATA['title'], ha='center', va='center',
        fontsize=16, weight='bold')

# Save figure
plt.tight_layout()
plt.savefig('D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L06_Embeddings_RL/08_skipgram_architecture/chart.pdf',
            bbox_inches='tight', dpi=150)
print(f"Chart saved: {CHART_METADATA['title']}")
plt.close()
