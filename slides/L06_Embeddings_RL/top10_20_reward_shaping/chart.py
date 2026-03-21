"""Reward Shaping: Sparse vs Dense Rewards - Compares Q-learning training with sparse vs shaped rewards."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Reward Shaping: Sparse vs Dense Rewards",
    "description": "Compares Q-learning episode returns with sparse reward vs distance-based shaped reward",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_20_reward_shaping"
}


np.random.seed(42)

grid_size = 5
n_states = grid_size * grid_size
n_actions = 4
goal_state = 24
alpha_lr = 0.1
gamma = 0.95
epsilon = 0.15
n_episodes = 500

def manhattan_dist(state, goal, grid_size):
    r1, c1 = divmod(state, grid_size)
    r2, c2 = divmod(goal, grid_size)
    return abs(r1 - r2) + abs(c1 - c2)

def step(state, action, grid_size):
    row, col = divmod(state, grid_size)
    if action == 0: row = max(0, row - 1)
    elif action == 1: row = min(grid_size - 1, row + 1)
    elif action == 2: col = max(0, col - 1)
    elif action == 3: col = min(grid_size - 1, col + 1)
    return row * grid_size + col

def run_qlearning(shaped=False):
    np.random.seed(42)
    Q = np.zeros((n_states, n_actions))
    episode_returns = []
    for ep in range(n_episodes):
        state = 0
        total_reward = 0.0
        for _ in range(100):
            if np.random.rand() < epsilon:
                action = np.random.randint(n_actions)
            else:
                action = np.argmax(Q[state])
            next_state = step(state, action, grid_size)
            done = next_state == goal_state

            if done:
                reward = 10.0
            elif shaped:
                # Shaped: bonus for reducing distance to goal
                d_old = manhattan_dist(state, goal_state, grid_size)
                d_new = manhattan_dist(next_state, goal_state, grid_size)
                reward = -0.1 + 0.5 * (d_old - d_new)
            else:
                reward = -0.1  # sparse: only step penalty

            Q[state, action] += alpha_lr * (reward + gamma * np.max(Q[next_state]) * (1 - done) - Q[state, action])
            total_reward += reward
            state = next_state
            if done:
                break
        episode_returns.append(total_reward)
    return episode_returns

sparse_returns = run_qlearning(shaped=False)
shaped_returns = run_qlearning(shaped=True)

# Smooth with rolling window
window = 20
def smooth(x, w):
    return np.convolve(x, np.ones(w) / w, mode='valid')

sparse_smooth = smooth(sparse_returns, window)
shaped_smooth = smooth(shaped_returns, window)
episodes = np.arange(window - 1, n_episodes)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(episodes, sparse_smooth, color=MLRED, linewidth=2.5, label='Sparse reward')
ax.plot(episodes, shaped_smooth, color=MLBLUE, linewidth=2.5, label='Shaped reward')

# Light fill between
ax.fill_between(episodes, sparse_smooth, shaped_smooth, alpha=0.08, color=MLBLUE,
                where=shaped_smooth > sparse_smooth)

ax.set_title("Reward Shaping: Sparse vs Dense Rewards", fontsize=16, fontweight='bold')
ax.set_xlabel("Episode")
ax.set_ylabel("Episode Return (smoothed)")
ax.legend(loc='lower right', fontsize=12, framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_20_reward_shaping/chart.pdf")
