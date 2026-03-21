"""Learned Q-Table: State-Action Values - Heatmap of full Q-table after Q-learning on 5x5 gridworld."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Learned Q-Table: State-Action Values",
    "description": "Heatmap of Q-table after Q-learning on a 5x5 gridworld",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_15_state_action_heatmap"
}


np.random.seed(42)

# 5x5 gridworld Q-learning
grid_size = 5
n_states = grid_size * grid_size
n_actions = 4  # 0=up, 1=down, 2=left, 3=right
goal_state = 24  # bottom-right
alpha = 0.1
gamma = 0.95
epsilon = 0.1
n_episodes = 2000

Q = np.zeros((n_states, n_actions))

def step(state, action, grid_size):
    row, col = divmod(state, grid_size)
    if action == 0:  # up
        row = max(0, row - 1)
    elif action == 1:  # down
        row = min(grid_size - 1, row + 1)
    elif action == 2:  # left
        col = max(0, col - 1)
    elif action == 3:  # right
        col = min(grid_size - 1, col + 1)
    next_state = row * grid_size + col
    reward = 10.0 if next_state == goal_state else -0.1
    done = next_state == goal_state
    return next_state, reward, done

for ep in range(n_episodes):
    state = np.random.randint(n_states - 1)  # random start (not goal)
    for _ in range(200):
        if np.random.rand() < epsilon:
            action = np.random.randint(n_actions)
        else:
            action = np.argmax(Q[state])
        next_state, reward, done = step(state, action, grid_size)
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) * (1 - done) - Q[state, action])
        state = next_state
        if done:
            break

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(Q, cmap='YlOrRd', aspect='auto')
ax.grid(False)

# Annotate cells with Q-values
for i in range(n_states):
    for j in range(n_actions):
        val = Q[i, j]
        color = 'white' if val > (Q.max() * 0.6) else 'black'
        ax.text(j, i, f'{val:.1f}', ha='center', va='center', fontsize=6, color=color)

ax.set_xticks(range(n_actions))
ax.set_xticklabels(['Up', 'Down', 'Left', 'Right'])
ax.set_ylabel("State")
ax.set_xlabel("Action")
ax.set_yticks(range(0, n_states, 5))
ax.set_title("Learned Q-Table: State-Action Values", fontsize=16, fontweight='bold')

cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Q-value', fontsize=12)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_15_state_action_heatmap/chart.pdf")
