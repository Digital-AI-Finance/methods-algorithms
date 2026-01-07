"""Bias-Variance Tradeoff - Single tree vs Random Forest"""
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

# Generate true function
x = np.linspace(0, 10, 200)
y_true = np.sin(x) + 0.5 * np.cos(2*x)

# Generate training data
n_train = 30
x_train = np.random.uniform(0, 10, n_train)
y_train = np.sin(x_train) + 0.5 * np.cos(2*x_train) + np.random.normal(0, 0.3, n_train)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Left: Single Decision Tree (high variance)
ax1 = axes[0]
ax1.scatter(x_train, y_train, c=MLBLUE, s=50, alpha=0.7, label='Training data', zorder=5)
ax1.plot(x, y_true, 'k--', linewidth=2, label='True function', alpha=0.5)

# Simulate multiple single tree predictions (high variance)
for i in range(5):
    # Each tree fits differently to bootstrap sample
    idx = np.random.choice(n_train, n_train, replace=True)
    x_boot = x_train[idx]
    y_boot = y_train[idx]

    # Simple piecewise approximation (simulating tree)
    from scipy.interpolate import interp1d
    sort_idx = np.argsort(x_boot)
    f = interp1d(x_boot[sort_idx], y_boot[sort_idx], kind='nearest',
                 fill_value='extrapolate')
    y_pred = f(x)
    ax1.plot(x, y_pred, color=MLRED, alpha=0.4, linewidth=1)

ax1.plot([], [], color=MLRED, alpha=0.6, linewidth=2, label='Individual trees')
ax1.set_xlabel('x', fontweight='bold')
ax1.set_ylabel('y', fontweight='bold')
ax1.set_title('Single Trees\n(High Variance)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper right', fontsize=10)
ax1.set_xlim(0, 10)
ax1.set_ylim(-2, 2.5)
ax1.grid(True, alpha=0.3)

# Right: Random Forest (reduced variance)
ax2 = axes[1]
ax2.scatter(x_train, y_train, c=MLBLUE, s=50, alpha=0.7, label='Training data', zorder=5)
ax2.plot(x, y_true, 'k--', linewidth=2, label='True function', alpha=0.5)

# Simulate Random Forest prediction (average of trees)
all_preds = []
for i in range(50):
    idx = np.random.choice(n_train, n_train, replace=True)
    x_boot = x_train[idx]
    y_boot = y_train[idx]

    from scipy.interpolate import interp1d
    sort_idx = np.argsort(x_boot)
    f = interp1d(x_boot[sort_idx], y_boot[sort_idx], kind='nearest',
                 fill_value='extrapolate')
    y_pred = f(x)
    all_preds.append(y_pred)

# Average prediction
y_rf = np.mean(all_preds, axis=0)
y_rf_std = np.std(all_preds, axis=0)

ax2.fill_between(x, y_rf - y_rf_std, y_rf + y_rf_std,
                  color=MLGREEN, alpha=0.2, label='Prediction std')
ax2.plot(x, y_rf, color=MLGREEN, linewidth=3, label='Random Forest')

ax2.set_xlabel('x', fontweight='bold')
ax2.set_ylabel('y', fontweight='bold')
ax2.set_title('Random Forest\n(Reduced Variance)', fontsize=14, fontweight='bold')
ax2.legend(loc='upper right', fontsize=10)
ax2.set_xlim(0, 10)
ax2.set_ylim(-2, 2.5)
ax2.grid(True, alpha=0.3)

plt.suptitle('Bias-Variance: Averaging Reduces Variance', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06_bias_variance/chart.pdf")
