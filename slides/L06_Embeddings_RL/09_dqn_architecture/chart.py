import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse, Rectangle

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
    'title': 'Deep Q-Network Architecture for Trading',
    'description': 'DQN architecture showing state input, neural network layers, Q-value outputs, experience replay buffer, and target network for reinforcement learning in trading',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/09_dqn_architecture'
}

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# State input
state_box = FancyBboxPatch((0.3, 2.5), 1.4, 1.2, boxstyle="round,pad=0.05",
                           edgecolor=MLPURPLE, facecolor=MLLAVENDER, linewidth=2)
ax.add_patch(state_box)
ax.text(1.0, 3.5, 'State s', ha='center', va='center', fontsize=11, weight='bold')
ax.text(1.0, 3.15, '[prices,', ha='center', va='center', fontsize=8)
ax.text(1.0, 2.95, 'RSI,', ha='center', va='center', fontsize=8)
ax.text(1.0, 2.75, 'position]', ha='center', va='center', fontsize=8)

# Neural network layers
layer_x = [2.5, 3.5, 4.5]
layer_sizes = [128, 64, 32]
for i, (x, size) in enumerate(zip(layer_x, layer_sizes)):
    layer_box = FancyBboxPatch((x, 2.3), 0.7, 1.6, boxstyle="round,pad=0.03",
                               edgecolor=MLBLUE, facecolor='lightblue', linewidth=2)
    ax.add_patch(layer_box)
    ax.text(x + 0.35, 3.1, f'Layer {i+1}', ha='center', va='center', fontsize=8)
    ax.text(x + 0.35, 2.8, f'({size})', ha='center', va='center', fontsize=7,
            style='italic')

    # Connections
    if i == 0:
        arrow = FancyArrowPatch((1.7, 3.1), (x, 3.1), arrowstyle='->',
                               mutation_scale=15, linewidth=1.5, color=MLPURPLE)
    else:
        arrow = FancyArrowPatch((layer_x[i-1] + 0.7, 3.1), (x, 3.1), arrowstyle='->',
                               mutation_scale=15, linewidth=1.5, color=MLBLUE)
    ax.add_patch(arrow)

# Neural network label
ax.text(3.5, 4.3, 'DQN (θ)', ha='center', va='center', fontsize=10,
        weight='bold', color=MLBLUE)

# Q-value outputs
q_values = ['Q(s, buy)', 'Q(s, hold)', 'Q(s, sell)']
colors = [MLGREEN, MLORANGE, MLRED]
for i, (q_val, color) in enumerate(zip(q_values, colors)):
    y = 3.7 - i * 0.6
    output_box = FancyBboxPatch((6.0, y - 0.2), 1.3, 0.4, boxstyle="round,pad=0.03",
                                edgecolor=color, facecolor='white', linewidth=1.5)
    ax.add_patch(output_box)
    ax.text(6.65, y, q_val, ha='center', va='center', fontsize=9, weight='bold')

    # Arrow from last layer to output
    arrow = FancyArrowPatch((5.2, 3.1), (6.0, y), arrowstyle='->',
                           mutation_scale=12, linewidth=1.2, color=color)
    ax.add_patch(arrow)

# Action selection arrow
action_arrow = FancyArrowPatch((7.3, 3.1), (8.5, 3.1), arrowstyle='->',
                              mutation_scale=20, linewidth=2, color='black')
ax.add_patch(action_arrow)
ax.text(7.9, 3.4, 'argmax', ha='center', va='bottom', fontsize=9, style='italic')
ax.text(9.0, 3.1, 'Action', ha='left', va='center', fontsize=10, weight='bold')

# Experience replay buffer (bottom left)
# Draw cylinder shape
ellipse_top = Ellipse((1.0, 1.3), 1.2, 0.3, edgecolor=MLORANGE,
                      facecolor='lightyellow', linewidth=2)
ax.add_patch(ellipse_top)
rect = Rectangle((0.4, 0.5), 1.2, 0.8, edgecolor=MLORANGE,
                 facecolor='lightyellow', linewidth=2)
ax.add_patch(rect)
ellipse_bottom = Ellipse((1.0, 0.5), 1.2, 0.3, edgecolor=MLORANGE,
                         facecolor='lightyellow', linewidth=2)
ax.add_patch(ellipse_bottom)

ax.text(1.0, 0.9, 'Experience', ha='center', va='center', fontsize=9, weight='bold')
ax.text(1.0, 0.6, 'Replay', ha='center', va='center', fontsize=9, weight='bold')

# Arrow from buffer to network
buffer_arrow = FancyArrowPatch((1.0, 1.6), (2.5, 2.5), arrowstyle='->',
                              mutation_scale=15, linewidth=1.5, color=MLORANGE,
                              linestyle='--')
ax.add_patch(buffer_arrow)
ax.text(1.8, 2.0, 'sample\nmini-batch', ha='center', va='center',
        fontsize=8, color=MLORANGE)

# Target network (bottom right)
target_box = FancyBboxPatch((6.0, 0.5), 1.5, 0.9, boxstyle="round,pad=0.05",
                            edgecolor=MLPURPLE, facecolor='white', linewidth=2,
                            linestyle='--')
ax.add_patch(target_box)
ax.text(6.75, 1.0, 'Target', ha='center', va='center', fontsize=9, weight='bold')
ax.text(6.75, 0.75, 'Network (θ⁻)', ha='center', va='center', fontsize=8)

# Arrow from main network to target network
target_arrow = FancyArrowPatch((4.5, 2.3), (6.5, 1.4), arrowstyle='->',
                              mutation_scale=15, linewidth=1.5, color=MLPURPLE,
                              linestyle='--')
ax.add_patch(target_arrow)
ax.text(5.5, 1.8, 'periodic\ncopy', ha='center', va='center',
        fontsize=8, color=MLPURPLE)

# Loss function annotation (top)
loss_text = r"$L = (r + \gamma \max_{a'} Q(s',a';\theta^-) - Q(s,a;\theta))^2$"
ax.text(5.0, 5.2, loss_text, ha='center', va='center', fontsize=11,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black', linewidth=1.5))
ax.text(5.0, 5.7, 'Loss Function', ha='center', va='center', fontsize=9,
        weight='bold', style='italic')

# Title
ax.text(5.0, 0.1, CHART_METADATA['title'], ha='center', va='center',
        fontsize=16, weight='bold')

# Save figure
plt.tight_layout()
plt.savefig('D:/Joerg/Research/slides/Methods_and_Algorithms/slides/L06_Embeddings_RL/09_dqn_architecture/chart.pdf',
            bbox_inches='tight', dpi=150)
print(f"Chart saved: {CHART_METADATA['title']}")
plt.close()
