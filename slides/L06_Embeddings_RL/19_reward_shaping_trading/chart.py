"""Reward Shaping: Impact on Trading Agent Learning -- line chart with confidence bands."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()


np.random.seed(42)
episodes = np.arange(1000)

# Raw P&L reward: slow, noisy convergence
raw_base = 2.0 / (1 + np.exp(-0.005 * (episodes - 600)))
raw_noise = np.random.normal(0, 0.8, 1000)
raw_returns = raw_base + raw_noise

# Risk-adjusted (Sharpe-like): faster, smoother convergence
adj_base = 5.0 / (1 + np.exp(-0.008 * (episodes - 350)))
adj_noise = np.random.normal(0, 0.35, 1000)
adj_returns = adj_base + adj_noise

# Smooth with rolling window of 30
window = 30
raw_smooth = pd.Series(raw_returns).rolling(window, min_periods=1).mean().values
adj_smooth = pd.Series(adj_returns).rolling(window, min_periods=1).mean().values
raw_std = pd.Series(raw_returns).rolling(window, min_periods=1).std().fillna(0).values
adj_std = pd.Series(adj_returns).rolling(window, min_periods=1).std().fillna(0).values

fig, ax = plt.subplots(figsize=(10, 6))

# Confidence bands
ax.fill_between(episodes, raw_smooth - raw_std, raw_smooth + raw_std,
                color=MLRED, alpha=0.15, zorder=1)
ax.fill_between(episodes, adj_smooth - adj_std, adj_smooth + adj_std,
                color=MLGREEN, alpha=0.15, zorder=1)

# Smoothed curves
ax.plot(episodes, raw_smooth, color=MLRED, linewidth=2.5, label='Raw P&L Reward', zorder=3)
ax.plot(episodes, adj_smooth, color=MLGREEN, linewidth=2.5,
        label='Risk-Adjusted Reward (Sharpe)', zorder=3)

ax.set_xlabel('Training Episode')
ax.set_ylabel('Cumulative Reward')
ax.set_title('Reward Shaping: Impact on Trading Agent Learning',
             fontsize=16, fontweight='bold', pad=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='lower right', framealpha=0.9)
ax.grid(alpha=0.2, zorder=0)

plt.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.pdf')
plt.savefig(out, bbox_inches='tight', pad_inches=0.1, facecolor='white')
plt.close()
print(f'Saved: {out}')
