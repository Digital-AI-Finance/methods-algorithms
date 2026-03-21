import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Gradient Boosting: Fitting Residuals Step by Step',
    'description': 'Shows how gradient boosting iteratively fits residuals, with MSE decreasing across 3 iterations on 6 data points',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/28_gb_residual_steps'
}

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor

# Data
x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([3, 7, 5, 9, 2, 8], dtype=float)
X = x.reshape(-1, 1)

# Smooth x for line plotting
x_smooth = np.linspace(0.5, 6.5, 300).reshape(-1, 1)

fig, ax = plt.subplots(figsize=(10, 6))

# True scatter
ax.scatter(x, y, color=MLBLUE, zorder=5, s=80, label='True y', edgecolors='white')

# f_0 = mean(y)
f0 = np.mean(y)
ax.axhline(f0, color='red', linestyle='--', linewidth=2,
           label=f'f_0 = mean = {f0:.2f}')

# Colors and labels for iterations 1-3
iter_colors = [MLGREEN, MLORANGE, MLPURPLE]
iter_labels = ['Iter 1', 'Iter 2', 'Iter 3']

for n_est, color, label in zip([1, 2, 3], iter_colors, iter_labels):
    gbr = GradientBoostingRegressor(
        n_estimators=n_est, learning_rate=0.3, max_depth=3, random_state=42
    )
    gbr.fit(X, y)
    y_pred = gbr.predict(x_smooth)
    y_pred_train = gbr.predict(X)
    mse = np.mean((y - y_pred_train) ** 2)
    ax.plot(x_smooth, y_pred, color=color, linewidth=2,
            label=f'{label}, MSE={mse:.2f}')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Gradient Boosting: Fitting Residuals Step by Step')
ax.legend(loc='upper right', fontsize=12)

# Text box
ax.text(0.03, 0.08,
        'Each tree corrects what\nthe previous ensemble got wrong',
        transform=ax.transAxes,
        fontsize=12, va='bottom',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.85))

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
