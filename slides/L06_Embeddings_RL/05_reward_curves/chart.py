"""Reward Curves - Learning progress in RL"""
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

# Episode numbers
episodes = np.arange(0, 501, 10)

# Simulated reward curves for different agents
# Q-learning (basic)
q_learning = -50 + 45 * (1 - np.exp(-episodes / 150)) + np.random.randn(len(episodes)) * 5
q_learning = np.clip(q_learning, -60, 10)

# Deep Q-Network (DQN) - learns faster, higher asymptote
dqn = -50 + 55 * (1 - np.exp(-episodes / 100)) + np.random.randn(len(episodes)) * 4
dqn = np.clip(dqn, -60, 15)

# Random agent (baseline)
random_agent = -30 + np.random.randn(len(episodes)) * 8

# Plot curves
ax.plot(episodes, random_agent, color='gray', linewidth=2, alpha=0.7,
        label='Random (baseline)', linestyle='--')
ax.plot(episodes, q_learning, color=MLBLUE, linewidth=2.5,
        label='Q-Learning', alpha=0.8)
ax.plot(episodes, dqn, color=MLGREEN, linewidth=2.5,
        label='Deep Q-Network', alpha=0.8)

# Add smoothed trend lines
from scipy.ndimage import gaussian_filter1d
ax.plot(episodes, gaussian_filter1d(q_learning, sigma=3), color=MLBLUE,
        linewidth=3, linestyle='-')
ax.plot(episodes, gaussian_filter1d(dqn, sigma=3), color=MLGREEN,
        linewidth=3, linestyle='-')

# Annotations
ax.axhline(y=0, color='black', linestyle=':', alpha=0.5)
ax.text(510, 0, 'Break-even', fontsize=10, va='center', color='gray')

ax.set_xlabel('Episode')
ax.set_ylabel('Average Reward (per episode)')
ax.set_title('RL Training: Cumulative Reward vs Episode')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 520)

# Add phases annotation
ax.axvspan(0, 100, alpha=0.1, color=MLRED, label='Exploration phase')
ax.axvspan(100, 300, alpha=0.1, color=MLORANGE)
ax.axvspan(300, 500, alpha=0.1, color=MLGREEN)
ax.text(50, -55, 'Exploration', fontsize=10, ha='center', color=MLRED)
ax.text(200, -55, 'Learning', fontsize=10, ha='center', color=MLORANGE)
ax.text(400, -55, 'Convergence', fontsize=10, ha='center', color=MLGREEN)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 05_reward_curves/chart.pdf")
