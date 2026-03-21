"""Epsilon-Greedy Exploration vs Exploitation - 10-armed bandit comparison of epsilon strategies."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Epsilon-Greedy: Exploration vs Exploitation",
    "description": "Compares greedy, epsilon=0.1, and epsilon=0.5 on a 10-armed bandit",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_09_epsilon_greedy"
}


np.random.seed(42)

n_arms = 10
n_steps = 1000
true_means = np.random.randn(n_arms) + np.arange(n_arms) * 0.5

def run_bandit(epsilon, n_steps, true_means):
    n_arms = len(true_means)
    Q = np.zeros(n_arms)
    N = np.zeros(n_arms)
    rewards = np.zeros(n_steps)
    for t in range(n_steps):
        if np.random.rand() < epsilon:
            action = np.random.randint(n_arms)
        else:
            action = np.argmax(Q)
        reward = true_means[action] + np.random.randn()
        N[action] += 1
        Q[action] += (reward - Q[action]) / N[action]
        rewards[t] = reward
    # Cumulative average
    avg_rewards = np.cumsum(rewards) / (np.arange(n_steps) + 1)
    return avg_rewards

# Average over multiple runs for smoother curves
n_runs = 200
epsilons = [0.0, 0.1, 0.5]
colors = [MLRED, MLBLUE, MLORANGE]
labels = [r'$\epsilon = 0.0$ (greedy)', r'$\epsilon = 0.1$', r'$\epsilon = 0.5$']

fig, ax = plt.subplots(figsize=(10, 6))

for eps, color, label in zip(epsilons, colors, labels):
    all_avg = np.zeros((n_runs, n_steps))
    for run in range(n_runs):
        np.random.seed(42 + run)
        all_avg[run] = run_bandit(eps, n_steps, true_means)
    mean_avg = all_avg.mean(axis=0)
    ax.plot(range(n_steps), mean_avg, color=color, label=label, linewidth=2)

ax.set_title("Epsilon-Greedy: Exploration vs Exploitation", fontsize=16, fontweight='bold')
ax.set_xlabel("Steps")
ax.set_ylabel("Average Reward")
ax.legend(loc='lower right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_09_epsilon_greedy/chart.pdf")
