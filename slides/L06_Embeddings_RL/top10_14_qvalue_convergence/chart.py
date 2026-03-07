"""Q-Value Convergence Over Episodes - Tracks Q-value for one state-action pair during Q-learning."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Q-Value Convergence Over Episodes",
    "description": "Tracks Q[start, right] convergence during Q-learning on a 4x4 gridworld",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_14_qvalue_convergence"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

# 4x4 gridworld Q-learning
grid_size = 4
n_states = grid_size * grid_size
n_actions = 4  # 0=up, 1=down, 2=left, 3=right
goal_state = n_states - 1  # bottom-right
alpha = 0.1
gamma = 0.95
epsilon = 0.1
n_episodes = 500

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

# Track Q[0, 3] (start state, right action)
track_state, track_action = 0, 3
q_history = []

for ep in range(n_episodes):
    state = 0
    for _ in range(100):  # max steps
        if np.random.rand() < epsilon:
            action = np.random.randint(n_actions)
        else:
            action = np.argmax(Q[state])
        next_state, reward, done = step(state, action, grid_size)
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) * (1 - done) - Q[state, action])
        state = next_state
        if done:
            break
    q_history.append(Q[track_state, track_action])

converged_value = q_history[-1]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(range(n_episodes), q_history, color=MLBLUE, linewidth=2, label='Q[start, right]')
ax.axhline(y=converged_value, color=MLRED, linestyle='--', linewidth=2,
           label=f'Converged value: {converged_value:.2f}', alpha=0.8)

ax.fill_between(range(n_episodes), q_history, alpha=0.1, color=MLBLUE)

ax.set_title("Q-Value Convergence Over Episodes", fontsize=16, fontweight='bold')
ax.set_xlabel("Episode")
ax.set_ylabel("Q-value")
ax.legend(loc='lower right', fontsize=12, framealpha=0.9)

# Annotate convergence region
ax.annotate('Convergence', xy=(400, converged_value * 0.98),
            fontsize=12, color=MLRED, fontstyle='italic')

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_14_qvalue_convergence/chart.pdf")
