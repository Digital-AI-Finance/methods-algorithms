"""TD(0) Learning: Value Estimates Over Episodes - Tracks value convergence on a 5-state chain."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "TD(0) Learning: Value Estimates Over Episodes",
    "description": "Value function convergence on a 5-state chain with TD(0)",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_17_td_learning_update"
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

# 5-state chain: S0 -> S1 -> S2 -> S3 -> S4 (terminal, reward=1)
n_states = 5
gamma = 0.9
alpha = 0.05
n_episodes = 200

# True values: V(Si) = gamma^(4-i) for state i (0-3), V(S4) = 0 (terminal)
true_values = np.array([gamma**4, gamma**3, gamma**2, gamma**1])

V = np.zeros(n_states)  # V[4] stays 0 (terminal)
history = {i: [] for i in range(4)}

for ep in range(n_episodes):
    state = 0  # always start at S0
    while state < 4:  # S4 is terminal
        next_state = state + 1
        reward = 1.0 if next_state == 4 else 0.0
        # TD(0) update
        V[state] += alpha * (reward + gamma * V[next_state] - V[state])
        state = next_state
    # Record current estimates
    for i in range(4):
        history[i].append(V[i])

fig, ax = plt.subplots(figsize=(10, 6))

colors = [MLBLUE, MLORANGE, MLGREEN, MLRED]
labels = [f'V(S{i})' for i in range(4)]

for i, (color, label) in enumerate(zip(colors, labels)):
    ax.plot(range(n_episodes), history[i], color=color, linewidth=2, label=label)
    # True value dashed line
    ax.axhline(y=true_values[i], color=color, linestyle='--', alpha=0.4, linewidth=1.5)

# Add true value annotations on the right
for i, color in enumerate(colors):
    ax.text(n_episodes + 3, true_values[i], f'True: {true_values[i]:.3f}',
            fontsize=10, color=color, va='center')

ax.set_title("TD(0) Learning: Value Estimates Over Episodes", fontsize=16, fontweight='bold')
ax.set_xlabel("Episode")
ax.set_ylabel("Estimated Value")
ax.legend(loc='center right', fontsize=12, framealpha=0.9)
ax.set_xlim(-5, n_episodes + 50)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_17_td_learning_update/chart.pdf")
