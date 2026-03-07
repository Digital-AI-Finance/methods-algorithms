"""Optimal vs Random Policy in Gridworld - Visualizes learned optimal path vs random walk on 5x5 grid."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Optimal vs Random Policy in Gridworld",
    "description": "Compares Q-learning optimal trajectory with random walk on a 5x5 gridworld",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_19_gridworld_trajectory"
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

grid_size = 5
n_states = grid_size * grid_size
n_actions = 4  # 0=up, 1=down, 2=left, 3=right
goal = (4, 4)
walls = [(1, 1), (2, 3), (3, 1)]  # obstacle positions
wall_states = [r * grid_size + c for r, c in walls]

def step(state, action):
    row, col = divmod(state, grid_size)
    if action == 0: row = max(0, row - 1)
    elif action == 1: row = min(grid_size - 1, row + 1)
    elif action == 2: col = max(0, col - 1)
    elif action == 3: col = min(grid_size - 1, col + 1)
    next_state = row * grid_size + col
    if next_state in wall_states:
        next_state = state  # bounce back
    reward = 10.0 if next_state == goal[0] * grid_size + goal[1] else -0.1
    done = next_state == goal[0] * grid_size + goal[1]
    return next_state, reward, done

# Q-learning
Q = np.zeros((n_states, n_actions))
alpha, gamma, epsilon = 0.1, 0.95, 0.1

for ep in range(1000):
    state = 0
    for _ in range(200):
        if np.random.rand() < epsilon:
            action = np.random.randint(n_actions)
        else:
            action = np.argmax(Q[state])
        ns, r, done = step(state, action)
        Q[state, action] += alpha * (r + gamma * np.max(Q[ns]) * (1 - done) - Q[state, action])
        state = ns
        if done:
            break

# Extract optimal trajectory
def get_optimal_path(Q, start=0, max_steps=20):
    path = [start]
    state = start
    for _ in range(max_steps):
        action = np.argmax(Q[state])
        ns, _, done = step(state, action)
        path.append(ns)
        state = ns
        if done:
            break
    return path

# Random trajectory
def get_random_path(start=0, max_steps=20):
    np.random.seed(123)
    path = [start]
    state = start
    for _ in range(max_steps):
        action = np.random.randint(n_actions)
        ns, _, done = step(state, action)
        path.append(ns)
        state = ns
        if done:
            break
    return path

optimal_path = get_optimal_path(Q)
random_path = get_random_path(max_steps=len(optimal_path))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw grid
for i in range(grid_size + 1):
    ax.axhline(y=i, color='gray', linewidth=0.5, alpha=0.5)
    ax.axvline(x=i, color='gray', linewidth=0.5, alpha=0.5)

# Fill walls
for r, c in walls:
    ax.add_patch(plt.Rectangle((c, grid_size - 1 - r), 1, 1, facecolor='gray', alpha=0.4, edgecolor='gray'))
    ax.text(c + 0.5, grid_size - 1 - r + 0.5, 'Wall', ha='center', va='center', fontsize=9, color='gray')

# Draw random path (behind optimal)
def draw_path(path, color, label, linewidth, alpha_val, offset=0.0):
    for i in range(len(path) - 1):
        r1, c1 = divmod(path[i], grid_size)
        r2, c2 = divmod(path[i + 1], grid_size)
        x1, y1 = c1 + 0.5 + offset, grid_size - 1 - r1 + 0.5 + offset
        x2, y2 = c2 + 0.5 + offset, grid_size - 1 - r2 + 0.5 + offset
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=linewidth, alpha=alpha_val))
    # Label only first segment for legend
    r1, c1 = divmod(path[0], grid_size)
    ax.plot([], [], color=color, linewidth=linewidth, alpha=alpha_val, label=label)

draw_path(random_path, MLRED, 'Random policy', 1.5, 0.35, offset=0.05)
draw_path(optimal_path, MLGREEN, 'Optimal policy', 3.0, 0.9, offset=-0.05)

# Mark start and goal
ax.plot(0.5, grid_size - 0.5, 'o', color=MLBLUE, markersize=18, zorder=5)
ax.text(0.5, grid_size - 0.5, 'S', ha='center', va='center', fontsize=12, fontweight='bold', color='white', zorder=6)
ax.plot(goal[1] + 0.5, grid_size - 1 - goal[0] + 0.5, '*', color=MLGREEN, markersize=25, zorder=5,
        markeredgecolor='darkgreen', markeredgewidth=0.5)
ax.text(goal[1] + 0.5, grid_size - 1 - goal[0] + 0.15, 'G', ha='center', va='center', fontsize=10,
        fontweight='bold', color='darkgreen', zorder=6)

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_aspect('equal')
ax.set_title("Optimal vs Random Policy in Gridworld", fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12, framealpha=0.9)
ax.set_xticks([])
ax.set_yticks([])

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_19_gridworld_trajectory/chart.pdf")
