"""PPO Training Curve on CartPole-v1 - Realistic synthetic data."""
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


np.random.seed(42)

# Generate realistic PPO CartPole training curve
# X: timesteps in thousands (0 to 50)
n_points = 500
timesteps = np.linspace(0, 50, n_points)

# Sigmoid-like rise: starts ~20, rises steeply 10-20k, plateaus ~475-500 by 30k
base_curve = 20 + 480 / (1 + np.exp(-0.25 * (timesteps - 15)))

# Add noise that decreases as training progresses (early episodes are noisier)
noise_scale = 120 * np.exp(-0.06 * timesteps) + 15
raw_rewards = base_curve + np.random.randn(n_points) * noise_scale
raw_rewards = np.clip(raw_rewards, 0, 500)

# Rolling average (window=25)
window = 25
rolling_avg = np.convolve(raw_rewards, np.ones(window) / window, mode='same')
# Fix edges
rolling_avg[:window // 2] = np.mean(raw_rewards[:window])
rolling_avg[-window // 2:] = np.mean(raw_rewards[-window:])

# Rolling std for shaded region
rolling_std = np.array([
    np.std(raw_rewards[max(0, i - window // 2):i + window // 2 + 1])
    for i in range(n_points)
])

fig, ax = plt.subplots()

# Raw episode rewards (noisy, light)
ax.scatter(timesteps, raw_rewards, s=4, color=MLBLUE, alpha=0.3, label='Episode Reward', zorder=2)

# Shaded variance region
ax.fill_between(timesteps, rolling_avg - rolling_std, np.minimum(rolling_avg + rolling_std, 500),
                color=MLBLUE, alpha=0.15, zorder=3)

# Rolling average (smooth, thick)
ax.plot(timesteps, rolling_avg, color=MLBLUE, linewidth=2.5, label='Rolling Average', zorder=4)

# Solved line
ax.axhline(y=500, color=MLGREEN, linestyle='--', linewidth=1.5, zorder=5)
ax.text(51, 500, 'Solved!', color=MLGREEN, fontsize=13, fontweight='bold',
        va='center', ha='left')

ax.set_xlabel('Timestep (thousands)')
ax.set_ylabel('Episode Reward')
ax.set_title('PPO Training on CartPole-v1')
ax.set_xlim(0, 50)
ax.set_ylim(0, 540)
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.pdf')
plt.savefig(output_path, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Saved: {output_path}")
