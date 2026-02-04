"""Policy Visualization - Trading policy based on state"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

CHART_METADATA = {
    "title": "Policy Visualization",
    "description": "Optimal policy arrows for grid world navigation",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/06_policy_viz"
}

np.random.seed(42)

fig, ax = plt.subplots(figsize=(10, 6))

# State space: RSI (x) vs Price Momentum (y)
rsi = np.linspace(0, 100, 50)
momentum = np.linspace(-5, 5, 50)
RSI, MOM = np.meshgrid(rsi, momentum)

# Policy: action = f(RSI, momentum)
# Buy when: RSI < 30 (oversold) OR momentum > 2
# Sell when: RSI > 70 (overbought) OR momentum < -2
# Hold otherwise

def policy(rsi, mom):
    """Returns: -1 (sell), 0 (hold), 1 (buy)"""
    if rsi < 30 or mom > 2:
        return 1  # Buy
    elif rsi > 70 or mom < -2:
        return -1  # Sell
    else:
        return 0  # Hold

# Vectorized policy
policy_grid = np.zeros_like(RSI)
for i in range(len(momentum)):
    for j in range(len(rsi)):
        policy_grid[i, j] = policy(rsi[j], momentum[i])

# Plot policy regions
cmap = plt.cm.RdYlGn
im = ax.contourf(RSI, MOM, policy_grid, levels=[-1.5, -0.5, 0.5, 1.5],
                  colors=[MLRED, 'lightgray', MLGREEN], alpha=0.6)

# Add contour lines
ax.contour(RSI, MOM, policy_grid, levels=[-0.5, 0.5], colors='black', linewidths=2)

# Labels for regions
ax.text(85, 3, 'SELL', fontsize=14, fontweight='bold', color=MLRED,
        ha='center', va='center')
ax.text(50, 0, 'HOLD', fontsize=14, fontweight='bold', color='gray',
        ha='center', va='center')
ax.text(15, -3, 'BUY', fontsize=14, fontweight='bold', color=MLGREEN,
        ha='center', va='center')
ax.text(50, 3.5, 'BUY\n(high momentum)', fontsize=10, color=MLGREEN,
        ha='center', va='center')
ax.text(50, -3.5, 'SELL\n(low momentum)', fontsize=10, color=MLRED,
        ha='center', va='center')

# Mark thresholds
ax.axvline(x=30, color='black', linestyle='--', alpha=0.5, linewidth=1.5)
ax.axvline(x=70, color='black', linestyle='--', alpha=0.5, linewidth=1.5)
ax.axhline(y=2, color='black', linestyle='--', alpha=0.5, linewidth=1.5)
ax.axhline(y=-2, color='black', linestyle='--', alpha=0.5, linewidth=1.5)

ax.text(30, -4.7, 'RSI=30\n(oversold)', fontsize=9, ha='center', va='top')
ax.text(70, -4.7, 'RSI=70\n(overbought)', fontsize=9, ha='center', va='top')

ax.set_xlabel('RSI (Relative Strength Index)')
ax.set_ylabel('Price Momentum (%)')
ax.set_title('Learned Trading Policy: Action based on State')
ax.grid(True, alpha=0.3)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06_policy_viz/chart.pdf")
