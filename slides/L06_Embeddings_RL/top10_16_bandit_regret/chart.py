"""Cumulative Regret: Comparing Exploration Strategies - Random vs Epsilon-Greedy vs UCB on 10-armed bandit."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Cumulative Regret: Comparing Exploration Strategies",
    "description": "Compares Random, Epsilon-Greedy, and UCB cumulative regret on a 10-armed bandit",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/top10_16_bandit_regret"
}


np.random.seed(42)

n_arms = 10
n_steps = 2000
n_runs = 100
true_means = np.random.randn(n_arms) + np.arange(n_arms) * 0.3
optimal_reward = true_means.max()

def run_random(n_steps, true_means):
    regrets = np.zeros(n_steps)
    for t in range(n_steps):
        action = np.random.randint(len(true_means))
        reward = true_means[action] + np.random.randn()
        regrets[t] = optimal_reward - true_means[action]
    return np.cumsum(regrets)

def run_epsilon_greedy(n_steps, true_means, epsilon=0.1):
    n_arms = len(true_means)
    Q = np.zeros(n_arms)
    N = np.zeros(n_arms)
    regrets = np.zeros(n_steps)
    for t in range(n_steps):
        if np.random.rand() < epsilon:
            action = np.random.randint(n_arms)
        else:
            action = np.argmax(Q)
        reward = true_means[action] + np.random.randn()
        N[action] += 1
        Q[action] += (reward - Q[action]) / N[action]
        regrets[t] = optimal_reward - true_means[action]
    return np.cumsum(regrets)

def run_ucb(n_steps, true_means, c=2.0):
    n_arms = len(true_means)
    Q = np.zeros(n_arms)
    N = np.zeros(n_arms)
    regrets = np.zeros(n_steps)
    for t in range(n_steps):
        if t < n_arms:
            action = t  # try each arm once
        else:
            ucb_values = Q + c * np.sqrt(np.log(t) / (N + 1e-10))
            action = np.argmax(ucb_values)
        reward = true_means[action] + np.random.randn()
        N[action] += 1
        Q[action] += (reward - Q[action]) / N[action]
        regrets[t] = optimal_reward - true_means[action]
    return np.cumsum(regrets)

# Average over runs
strategies = [
    ('Random', run_random, {}, MLRED),
    (r'$\epsilon$-Greedy ($\epsilon$=0.1)', run_epsilon_greedy, {'epsilon': 0.1}, MLBLUE),
    ('UCB (c=2)', run_ucb, {'c': 2.0}, MLGREEN),
]

fig, ax = plt.subplots(figsize=(10, 6))

for name, func, kwargs, color in strategies:
    all_regrets = np.zeros((n_runs, n_steps))
    for run in range(n_runs):
        np.random.seed(42 + run)
        all_regrets[run] = func(n_steps, true_means, **kwargs)
    mean_regret = all_regrets.mean(axis=0)
    ax.plot(range(n_steps), mean_regret, color=color, linewidth=2.5, label=name)

ax.set_title("Cumulative Regret: Comparing Exploration Strategies", fontsize=16, fontweight='bold')
ax.set_xlabel("Steps")
ax.set_ylabel("Cumulative Regret")
ax.legend(loc='upper left', fontsize=12, framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_16_bandit_regret/chart.pdf")
