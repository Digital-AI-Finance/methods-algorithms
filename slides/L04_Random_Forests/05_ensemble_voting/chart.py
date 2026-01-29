"""Ensemble Voting - How trees combine predictions"""
import matplotlib.pyplot as plt

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'Ensemble Voting',
    'description': 'Majority voting aggregation process',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/05_ensemble_voting'
}
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle
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

fig, ax = plt.subplots(figsize=(10, 6))

# Input sample
input_x, input_y = 0.1, 0.5
rect = FancyBboxPatch((input_x - 0.06, input_y - 0.08), 0.12, 0.16,
                       boxstyle="round,pad=0.02,rounding_size=0.02",
                       facecolor=MLBLUE, edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(input_x, input_y, 'New\nSample', ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')

# Trees
n_trees = 5
tree_x = 0.35
tree_spacing = 0.15
predictions = ['Fraud', 'Normal', 'Fraud', 'Fraud', 'Normal']
tree_colors = [MLRED, MLGREEN, MLRED, MLRED, MLGREEN]

for i in range(n_trees):
    y = 0.85 - i * tree_spacing

    # Arrow from input to tree
    ax.annotate('', xy=(tree_x - 0.07, y),
                xytext=(input_x + 0.06, input_y + (0.4 - i * 0.2) * 0.1),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

    # Tree box
    rect = FancyBboxPatch((tree_x - 0.06, y - 0.05), 0.12, 0.1,
                           boxstyle="round,pad=0.02,rounding_size=0.02",
                           facecolor=MLPURPLE, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(tree_x, y, f'Tree {i+1}', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Arrow from tree to prediction
    ax.annotate('', xy=(0.53, y), xytext=(tree_x + 0.06, y),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

    # Prediction box
    pred_x = 0.6
    rect = FancyBboxPatch((pred_x - 0.06, y - 0.04), 0.12, 0.08,
                           boxstyle="round,pad=0.01,rounding_size=0.01",
                           facecolor=tree_colors[i], edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(pred_x, y, predictions[i], ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

# Aggregation box
agg_x, agg_y = 0.78, 0.5
rect = FancyBboxPatch((agg_x - 0.07, agg_y - 0.12), 0.14, 0.24,
                       boxstyle="round,pad=0.02,rounding_size=0.02",
                       facecolor=MLORANGE, edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(agg_x, agg_y + 0.05, 'Majority', ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')
ax.text(agg_x, agg_y - 0.05, 'Vote', ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')

# Arrows from predictions to aggregation
for i in range(n_trees):
    y = 0.85 - i * tree_spacing
    ax.annotate('', xy=(agg_x - 0.07, agg_y + (2-i) * 0.03),
                xytext=(0.66, y),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

# Final prediction
final_x = 0.93
ax.annotate('', xy=(final_x - 0.05, agg_y), xytext=(agg_x + 0.07, agg_y),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))

rect = FancyBboxPatch((final_x - 0.05, agg_y - 0.06), 0.1, 0.12,
                       boxstyle="round,pad=0.02,rounding_size=0.02",
                       facecolor=MLRED, edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(final_x, agg_y, 'FRAUD', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white')

# Vote count annotation
ax.text(0.78, 0.18, 'Fraud: 3/5 (60%)\nNormal: 2/5 (40%)',
        ha='center', fontsize=10, style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray'))

ax.set_xlim(0, 1)
ax.set_ylim(0.1, 0.95)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Ensemble Voting (Classification)', fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05_ensemble_voting/chart.pdf")
