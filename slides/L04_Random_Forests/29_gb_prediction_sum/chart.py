import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'How GBM Builds Its Prediction: One Tree at a Time',
    'description': 'Stacked bar chart decomposing a GBM prediction into initial value plus 5 tree contributions for x=4',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/29_gb_prediction_sum'
}

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor

# Data
x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([3, 7, 5, 9, 2, 8], dtype=float)
X = x.reshape(-1, 1)

# Target point
x_query = np.array([[4.0]])
y_true = 9.0

# Fit GBR with 5 estimators
lr = 0.3
gbr = GradientBoostingRegressor(
    n_estimators=5, learning_rate=lr, max_depth=2, random_state=42
)
gbr.fit(X, y)

# Extract contributions
f0 = gbr.init_.predict(x_query)[0]  # initial prediction (mean)
tree_contribs = []
for est in gbr.estimators_.ravel():
    contrib = lr * est.predict(x_query)[0]
    tree_contribs.append(contrib)

all_contribs = [f0] + tree_contribs
labels = ['f_0'] + [f'Tree {i+1}' for i in range(5)]
seg_colors = ['#808080', MLBLUE, MLGREEN, MLORANGE, MLPURPLE, MLRED]

fig, ax = plt.subplots(figsize=(10, 6))

# Build stacked bar
bottom = 0.0
bar_x = 0.4
bar_width = 0.5
for val, lbl, col in zip(all_contribs, labels, seg_colors):
    ax.bar(bar_x, val, bar_width, bottom=bottom,
           color=col, label=f'{lbl}: {val:+.3f}', edgecolor='white', linewidth=0.5)
    # Annotate segment center
    center = bottom + val / 2
    ax.text(bar_x, center, f'{val:+.3f}',
            ha='center', va='center', fontsize=11,
            color='white', fontweight='bold')
    bottom += val

total = sum(all_contribs)

# True value line
ax.axhline(y_true, color=MLRED, linestyle='--', linewidth=2, label=f'y_true = {y_true}')

# Summary text
ax.text(bar_x + bar_width / 2 + 0.1, total / 2,
        f'y_hat = f_0 + lr*h_1 + lr*h_2 + ...\n     = {total:.2f}',
        ha='left', va='center', fontsize=12,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.85))

ax.set_xlim(0, 1.5)
ax.set_xticks([bar_x])
ax.set_xticklabels(['x = 4'])
ax.set_ylabel('Predicted value')
ax.set_title('How GBM Builds Its Prediction: One Tree at a Time')
ax.legend(loc='lower right', fontsize=11, ncol=2)
ax.grid(axis='x', visible=False)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
