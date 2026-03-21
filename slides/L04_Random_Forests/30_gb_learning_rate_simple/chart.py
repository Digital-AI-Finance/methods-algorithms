import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Learning Rate: Slow and Steady Wins',
    'description': 'Test MSE curves for 3 learning rates (0.5, 0.1, 0.01) showing optimal stopping points and overfitting zone',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/30_gb_learning_rate_simple'
}

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Data
X, y = make_regression(n_samples=200, n_features=5, noise=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

n_est = 300
configs = [
    (0.5,  MLRED,   'lr=0.5'),
    (0.1,  MLGREEN, 'lr=0.1'),
    (0.01, MLBLUE,  'lr=0.01'),
]

fig, ax = plt.subplots(figsize=(10, 6))

overfitting_start = None

for lr, color, label in configs:
    gbr = GradientBoostingRegressor(
        n_estimators=n_est, learning_rate=lr, max_depth=3, random_state=42
    )
    gbr.fit(X_train, y_train)
    test_mse = [mean_squared_error(y_test, pred)
                for pred in gbr.staged_predict(X_test)]

    iters = np.arange(1, n_est + 1)
    ax.plot(iters, test_mse, color=color, linewidth=2, label=label)

    # Mark minimum
    best_n = int(np.argmin(test_mse)) + 1
    best_mse = test_mse[best_n - 1]
    ax.plot(best_n, best_mse, marker='*', color=color, markersize=14, zorder=5)
    ax.annotate(f'Best at {best_n} trees',
                xy=(best_n, best_mse),
                xytext=(best_n + 15, best_mse + 200),
                fontsize=10, color=color,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.2))

    # Track overfitting start for lr=0.5 (first time test MSE exceeds its min by 5%)
    if lr == 0.5:
        overfitting_start = best_n

# Shade overfitting region for lr=0.5
if overfitting_start:
    ax.axvspan(overfitting_start, n_est, color='red', alpha=0.08, label='Overfitting zone (lr=0.5)')

ax.set_xlabel('Number of Trees')
ax.set_ylabel('Test MSE')
ax.set_title('Learning Rate: Slow and Steady Wins')
ax.legend(loc='upper right', fontsize=12)

ax.text(0.03, 0.96,
        'Lower LR → more trees needed,\nbut better generalization',
        transform=ax.transAxes, fontsize=12,
        va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.85))

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
