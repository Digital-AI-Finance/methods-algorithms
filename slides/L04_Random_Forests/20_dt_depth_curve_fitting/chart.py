"""Decision Tree: Effect of Depth on Curve Fitting"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.tree import DecisionTreeRegressor
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Decision Tree: Effect of Depth on Curve Fitting',
    'description': 'Shows how tree depth controls underfitting vs overfitting for a single decision tree regressor',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/20_dt_depth_curve_fitting'
}


np.random.seed(42)
n = 80
X_train = np.sort(np.random.uniform(0, 10, n))
y_true_func = lambda x: np.sin(1.5 * x) + 0.5 * np.cos(2 * x)
y_train = y_true_func(X_train) + np.random.normal(0, 0.3, n)

X_plot = np.linspace(0, 10, 500).reshape(-1, 1)
X_train_2d = X_train.reshape(-1, 1)

depths = [1, 3, 5, 10, None]
colors = [MLBLUE, MLGREEN, MLORANGE, MLRED, MLPURPLE]
labels = ['depth=1', 'depth=3', 'depth=5', 'depth=10', 'depth=unlimited']

fig, ax = plt.subplots()

ax.scatter(X_train, y_train, c='gray', alpha=0.4, s=20, zorder=1, label='Training data')
ax.plot(X_plot, y_true_func(X_plot.ravel()), 'k--', linewidth=1.5, label='True function', zorder=2)

predictions = {}
for depth, color, label in zip(depths, colors, labels):
    dt = DecisionTreeRegressor(max_depth=depth, random_state=42)
    dt.fit(X_train_2d, y_train)
    y_pred = dt.predict(X_plot)
    predictions[depth] = y_pred
    ax.plot(X_plot, y_pred, color=color, linewidth=1.8, label=label, zorder=3)

# Annotations
idx_mid = 250
ax.annotate('Underfitting', xy=(X_plot[idx_mid, 0], predictions[1][idx_mid]),
            xytext=(X_plot[idx_mid, 0] + 0.8, predictions[1][idx_mid] + 0.6),
            fontsize=12, color=MLBLUE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MLBLUE, lw=1.2))

idx_late = 400
ax.annotate('Overfitting', xy=(X_plot[idx_late, 0], predictions[None][idx_late]),
            xytext=(X_plot[idx_late, 0] - 1.5, predictions[None][idx_late] + 0.7),
            fontsize=12, color=MLPURPLE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=1.2))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(CHART_METADATA['title'])
ax.legend(loc='lower left', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 20_dt_depth_curve_fitting/chart.pdf")
