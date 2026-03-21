"""RLHF Pipeline: 3-stage horizontal flowchart for L06 deepdive."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-0.5, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Box definitions: (x_center, label, subtitle, color)
boxes = [
    (1.5, 'Stage 1:\nSupervised\nFine-Tuning', 'Train on text corpus',   MLPURPLE),
    (5.0, 'Stage 2:\nReward\nModel',            'Humans rank outputs',    MLBLUE),
    (8.5, 'Stage 3:\nPPO\nOptimization',        'RL fine-tunes LLM',     MLORANGE),
]

box_w, box_h = 2.2, 1.8
y_center = 3.0

for x, label, subtitle, color in boxes:
    rect = mpatches.FancyBboxPatch(
        (x - box_w / 2, y_center - box_h / 2), box_w, box_h,
        boxstyle='round,pad=0.15', facecolor=color, edgecolor='white',
        linewidth=2, alpha=0.92
    )
    ax.add_patch(rect)
    # Main label
    ax.text(x, y_center + 0.1, label, ha='center', va='center',
            fontsize=13, fontweight='bold', color='white')
    # Subtitle below box (italic gray)
    ax.text(x, y_center - box_h / 2 - 0.3, subtitle, ha='center', va='top',
            fontsize=10, color='#444444', style='italic')

# Arrows between boxes
arrow_props = dict(arrowstyle='->', lw=2.5, color='#555555')
for i in range(len(boxes) - 1):
    x_start = boxes[i][0] + box_w / 2 + 0.05
    x_end = boxes[i + 1][0] - box_w / 2 - 0.05
    ax.annotate('', xy=(x_end, y_center), xytext=(x_start, y_center),
                arrowprops=arrow_props)

# Output arrow after last box
x_out_start = boxes[-1][0] + box_w / 2 + 0.05
ax.annotate('', xy=(x_out_start + 1.0, y_center), xytext=(x_out_start, y_center),
            arrowprops=arrow_props)
ax.text(x_out_start + 1.15, y_center, 'Aligned\nLLM', ha='left', va='center',
        fontsize=13, fontweight='bold', color='#333333')

# Step numbers above each box
for i, (x, _, _, _) in enumerate(boxes):
    ax.text(x, y_center + box_h / 2 + 0.2, f'Step {i + 1}',
            ha='center', va='bottom', fontsize=9, color='#888888', fontweight='bold')

# Data input labels below subtitles
inputs = ['Demonstration\ndata', 'Comparison\ndata', 'PPO policy\ngradient']
for i, (x, _, _, _) in enumerate(boxes):
    ax.text(x, y_center - box_h / 2 - 0.85, inputs[i], ha='center', va='top',
            fontsize=9, color='#999999', style='italic')

# Title
ax.text(5.25, 5.4, 'RLHF: How ChatGPT Learned to Be Helpful',
        ha='center', va='center', fontsize=16, fontweight='bold', color='#333333')

plt.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.pdf')
plt.savefig(out, bbox_inches='tight', pad_inches=0.1, facecolor='white')
plt.close()
print(f'Saved: {out}')
