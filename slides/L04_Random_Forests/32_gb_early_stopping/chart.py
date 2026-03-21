import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'When to Stop Adding Trees',
    'description': 'Train vs test MSE showing overfitting after the early stopping point with annotated zones',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/32_gb_early_stopping'
}

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Data
X, y = make_regression(n_samples=300, n_features=10, noise=15, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

n_est = 500
gbr = GradientBoostingRegressor(
    n_estimators=n_est, learning_rate=0.1, max_depth=3, random_state=42
)
gbr.fit(X_train, y_train)

train_mse = [mean_squared_error(y_train, pred)
             for pred in gbr.staged_predict(X_train)]
test_mse  = [mean_squared_error(y_test, pred)
             for pred in gbr.staged_predict(X_test)]

iters = np.arange(1, n_est + 1)
best_n = int(np.argmin(test_mse)) + 1
best_val = test_mse[best_n - 1]

fig, ax = plt.subplots(figsize=(10, 6))

# Shaded regions
ax.axvspan(1, best_n, alpha=0.10, color='green', label='Learning')
ax.axvspan(best_n, n_est, alpha=0.10, color='red', label='Overfitting')

# MSE curves
ax.plot(iters, train_mse, color=MLBLUE, linewidth=2, label='Train MSE')
ax.plot(iters, test_mse,  color=MLRED,  linewidth=2, label='Test MSE')

# Early stopping line
ax.axvline(best_n, color=MLGREEN, linestyle='--', linewidth=2,
           label=f'Early stop (n={best_n})')

# Star at minimum test MSE
ax.plot(best_n, best_val, marker='*', color=MLGREEN, markersize=16, zorder=6)

# Annotation arrow
ax.annotate(f'Stop here!\nTest MSE = {best_val:.1f}\nn_trees = {best_n}',
            xy=(best_n, best_val),
            xytext=(best_n + 45, best_val + (max(test_mse) - best_val) * 0.45),
            fontsize=11, color=MLGREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2.0))

ax.set_xlabel('Number of Trees')
ax.set_ylabel('MSE')
ax.set_title('When to Stop Adding Trees')
ax.legend(loc='upper right', fontsize=12)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
