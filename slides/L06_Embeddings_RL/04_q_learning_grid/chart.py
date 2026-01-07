"""Q-Learning Grid World - Visualization of Q-values in a simple environment"""
import matplotlib.pyplot as plt
import numpy as np
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

np.random.seed(42)

fig, ax = plt.subplots(figsize=(10, 6))

# 4x4 grid world
grid_size = 4

# Q-values for each state (showing max Q-value)
# Higher values near goal (bottom-right), negative near trap (position 1,2)
q_values = np.array([
    [0.3, 0.4, 0.5, 0.6],
    [0.4, 0.5, -0.8, 0.7],  # Trap at (1,2)
    [0.5, 0.6, 0.7, 0.85],
    [0.6, 0.7, 0.85, 1.0]   # Goal at (3,3)
])

# Draw grid
for i in range(grid_size + 1):
    ax.axhline(y=i, color='black', linewidth=1)
    ax.axvline(x=i, color='black', linewidth=1)

# Color cells by Q-value
for i in range(grid_size):
    for j in range(grid_size):
        q = q_values[i, j]
        if q < 0:
            color = MLRED
            alpha = min(abs(q), 1)
        else:
            color = MLGREEN
            alpha = min(q, 1) * 0.8

        rect = plt.Rectangle((j, grid_size - 1 - i), 1, 1,
                              facecolor=color, alpha=alpha, edgecolor='none')
        ax.add_patch(rect)

        # Add Q-value text
        ax.text(j + 0.5, grid_size - 0.5 - i, f'{q:.2f}',
                ha='center', va='center', fontsize=11, fontweight='bold',
                color='white' if abs(q) > 0.4 else 'black')

# Mark special states
# Start state
ax.text(0.5, grid_size - 0.15, 'START', ha='center', va='top', fontsize=9,
        color='gray', fontweight='bold')
# Goal state
ax.text(3.5, 0.15, 'GOAL', ha='center', va='bottom', fontsize=9,
        color='white', fontweight='bold')
# Trap state
ax.text(2.5, 2.15, 'TRAP', ha='center', va='bottom', fontsize=9,
        color='white', fontweight='bold')

# Draw optimal policy arrows
arrows = [
    ((0, 3), 'right'), ((1, 3), 'right'), ((2, 3), 'down'), ((3, 3), 'down'),
    ((0, 2), 'right'), ((1, 2), 'down'),  # Skip trap
    ((0, 1), 'right'), ((1, 1), 'right'), ((3, 1), 'down'),
    ((0, 0), 'right'), ((1, 0), 'right'), ((2, 0), 'right')
]

arrow_offset = 0.5
arrow_len = 0.3
for (x, y), direction in arrows:
    y_plot = grid_size - 1 - y
    if direction == 'right':
        ax.annotate('', xy=(x + arrow_offset + arrow_len, y_plot + 0.5),
                    xytext=(x + arrow_offset - arrow_len, y_plot + 0.5),
                    arrowprops=dict(arrowstyle='->', color='black', lw=2))
    elif direction == 'down':
        ax.annotate('', xy=(x + 0.5, y_plot + arrow_offset - arrow_len),
                    xytext=(x + 0.5, y_plot + arrow_offset + arrow_len),
                    arrowprops=dict(arrowstyle='->', color='black', lw=2))

ax.set_xlim(-0.1, grid_size + 0.1)
ax.set_ylim(-0.1, grid_size + 0.1)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Q-Learning: Grid World with Learned Q-Values', fontsize=16,
             fontweight='bold', y=1.02)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLGREEN, alpha=0.8, label='High Q-value (good)'),
    Patch(facecolor=MLRED, alpha=0.8, label='Negative Q-value (bad)')
]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.0, 0.0))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04_q_learning_grid/chart.pdf")
