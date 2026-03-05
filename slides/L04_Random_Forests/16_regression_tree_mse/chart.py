"""Regression Tree MSE Split - Visualization of MSE split criterion"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from pathlib import Path

CHART_METADATA = {
    'title': 'Regression Tree: MSE Split Criterion',
    'description': 'Visualization of how a regression tree splits using MSE',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/16_regression_tree_mse'
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

# Generate data
n = 50
x = np.sort(np.random.uniform(0, 10, n))
y = 0.5 * x + np.random.normal(0, 1.5, n)

# Fit depth-1 tree
dt = DecisionTreeRegressor(max_depth=1, random_state=42)
dt.fit(x.reshape(-1, 1), y)

# Extract split threshold
threshold = dt.tree_.threshold[0]
left_mask = x <= threshold
right_mask = x > threshold
left_mean = y[left_mask].mean()
right_mean = y[right_mask].mean()

# Compute MSE
parent_mse = np.mean((y - y.mean())**2)
left_mse = np.mean((y[left_mask] - left_mean)**2)
right_mse = np.mean((y[right_mask] - right_mean)**2)
n_left = left_mask.sum()
n_right = right_mask.sum()
weighted_mse = (n_left * left_mse + n_right * right_mse) / n
reduction = parent_mse - weighted_mse

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x, y, c=MLBLUE, s=50, alpha=0.7, label='Data points', zorder=5)
ax.axvline(x=threshold, color=MLPURPLE, linestyle='--', linewidth=2.5, label=f'Split at x = {threshold:.2f}')

# Left and right means
ax.hlines(left_mean, x[left_mask].min() - 0.2, threshold, color=MLGREEN, linewidth=3, label=f'Left mean = {left_mean:.2f}')
ax.hlines(right_mean, threshold, x[right_mask].max() + 0.2, color=MLORANGE, linewidth=3, label=f'Right mean = {right_mean:.2f}')

ax.set_xlabel('x', fontweight='bold')
ax.set_ylabel('y', fontweight='bold')
ax.set_title('Regression Tree: MSE Split Criterion', fontsize=16, fontweight='bold')
ax.legend(loc='upper left', fontsize=11)
ax.grid(True, alpha=0.3)

# MSE annotations
text = f'Parent MSE = {parent_mse:.2f}\nLeft MSE = {left_mse:.2f}\nRight MSE = {right_mse:.2f}\nReduction = {reduction:.2f}'
ax.text(0.97, 0.97, text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', edgecolor='gray', alpha=0.9))

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 16_regression_tree_mse/chart.pdf")
