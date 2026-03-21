"""Gradient Boosting Residuals - First residual fit visualization"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Gradient Boosting: First Residual Fit',
    'description': 'Visualization of gradient boosting first residual correction',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/14_gradient_boosting_residuals'
}


np.random.seed(42)

# Generate 1D data
n = 100
x = np.sort(np.random.uniform(0, 2 * np.pi, n))
y = np.sin(x) + np.random.normal(0, 0.3, n)

# Fit GBR with 1 estimator
gbr = GradientBoostingRegressor(n_estimators=1, max_depth=3, learning_rate=0.5, random_state=42)
gbr.fit(x.reshape(-1, 1), y)

# Smooth prediction curve
x_plot = np.linspace(0, 2 * np.pi, 300)
y_pred = gbr.predict(x_plot.reshape(-1, 1))
y_mean = y.mean()

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x, y, c=MLBLUE, s=40, alpha=0.6, label='Data points', zorder=5)
ax.axhline(y=y_mean, color=MLRED, linestyle='--', linewidth=2, label=f'Initial prediction (mean = {y_mean:.2f})')
ax.plot(x_plot, y_pred, color=MLGREEN, linewidth=3, label='After 1st tree correction')

ax.set_xlabel('x', fontweight='bold')
ax.set_ylabel('y', fontweight='bold')
ax.set_title('Gradient Boosting: First Residual Fit', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)

# Annotate
ax.annotate('Mean prediction\n(before boosting)',
            xy=(5.5, y_mean), xytext=(5.5, y_mean + 0.6),
            fontsize=10, ha='center', color=MLRED,
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=1.5))
ax.annotate('Tree corrects\nresiduals',
            xy=(1.5, 0.8), fontsize=10, ha='center', color=MLGREEN,
            bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='gray', alpha=0.8))

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 14_gradient_boosting_residuals/chart.pdf")
