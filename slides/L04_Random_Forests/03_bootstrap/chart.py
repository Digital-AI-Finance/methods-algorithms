"""Bootstrap Sampling - Bagging visualization"""
import matplotlib.pyplot as plt

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'Bootstrap Sampling',
    'description': 'Sampling with replacement visualization',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/03_bootstrap'
}
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

np.random.seed(42)

fig, ax = plt.subplots(figsize=(10, 6))

# Original dataset (left)
original_x = 0.12
original_y = 0.5
box_width = 0.15
box_height = 0.7

# Draw original dataset
rect = FancyBboxPatch((original_x - box_width/2, original_y - box_height/2),
                       box_width, box_height,
                       boxstyle="round,pad=0.02,rounding_size=0.02",
                       facecolor=MLBLUE, edgecolor='black', linewidth=2, alpha=0.8)
ax.add_patch(rect)
ax.text(original_x, original_y + box_height/2 + 0.05, 'Original\nDataset',
        ha='center', va='bottom', fontsize=12, fontweight='bold')

# Draw data points in original
n_points = 10
for i in range(n_points):
    y = original_y - box_height/2 + 0.05 + i * (box_height - 0.1) / (n_points - 1)
    ax.plot(original_x, y, 'o', color='white', markersize=8, markeredgecolor='black')
    ax.text(original_x + 0.02, y, str(i+1), fontsize=10, va='center', color='white', fontweight='bold')

# Bootstrap samples (right side)
bootstrap_positions = [(0.4, 0.75), (0.6, 0.75), (0.8, 0.75)]
sample_colors = [MLGREEN, MLORANGE, MLRED]
sample_labels = ['Tree 1', 'Tree 2', 'Tree 3']
sample_indices = [
    [1, 3, 3, 5, 7, 8, 8, 10],  # Bootstrap sample 1
    [2, 2, 4, 6, 6, 7, 9, 10],  # Bootstrap sample 2
    [1, 1, 3, 4, 5, 8, 9, 9],   # Bootstrap sample 3
]

for (x, y), color, label, indices in zip(bootstrap_positions, sample_colors, sample_labels, sample_indices):
    # Draw bootstrap sample box
    small_width = 0.12
    small_height = 0.4
    rect = FancyBboxPatch((x - small_width/2, y - small_height/2),
                           small_width, small_height,
                           boxstyle="round,pad=0.02,rounding_size=0.02",
                           facecolor=color, edgecolor='black', linewidth=2, alpha=0.7)
    ax.add_patch(rect)
    ax.text(x, y + small_height/2 + 0.03, f'Bootstrap\nSample',
            ha='center', va='bottom', fontsize=10)

    # Draw sampled points
    for i, idx in enumerate(indices):
        py = y - small_height/2 + 0.03 + i * (small_height - 0.06) / (len(indices) - 1)
        ax.plot(x, py, 'o', color='white', markersize=6, markeredgecolor='black')
        ax.text(x, py, str(idx), fontsize=10, ha='center', va='center', fontweight='bold')

    # Arrow from original to sample
    ax.annotate('', xy=(x - small_width/2 - 0.02, y),
                xytext=(original_x + box_width/2 + 0.02, original_y + 0.1),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5,
                               connectionstyle='arc3,rad=0.1'))

# Tree boxes below bootstrap samples
for (x, y), color, label in zip(bootstrap_positions, sample_colors, sample_labels):
    tree_y = 0.25
    tree_width = 0.12
    tree_height = 0.15

    rect = FancyBboxPatch((x - tree_width/2, tree_y - tree_height/2),
                           tree_width, tree_height,
                           boxstyle="round,pad=0.02,rounding_size=0.02",
                           facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, tree_y, label, ha='center', va='center', fontsize=11,
            fontweight='bold', color='white')

    # Arrow from sample to tree
    ax.annotate('', xy=(x, tree_y + tree_height/2 + 0.02),
                xytext=(x, y - 0.4/2 - 0.02),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

# Text annotations
ax.text(0.5, 0.05, 'Each tree trained on ~63% unique samples (with replacement)',
        ha='center', fontsize=11, style='italic', color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Bootstrap Aggregating (Bagging)', fontsize=16, fontweight='bold', y=0.98)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 03_bootstrap/chart.pdf")
