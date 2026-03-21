"""KNN Regression - Effect of k on smoothness of KNN regression on sine curve."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.neighbors import KNeighborsRegressor
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "KNN Regression: Effect of k on Smoothness",
    "description": "KNN regression with k=1, 5, 20 on noisy sine data",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_13_knn_regression"
}


np.random.seed(42)
X_train = np.sort(np.random.uniform(0, 2 * np.pi, 200)).reshape(-1, 1)
y_train = np.sin(X_train.ravel()) + np.random.normal(0, 0.3, 200)

X_test = np.linspace(0, 2 * np.pi, 500).reshape(-1, 1)
y_true = np.sin(X_test.ravel())

fig, ax = plt.subplots(figsize=(10, 6))

# Scatter noisy data
ax.scatter(X_train, y_train, c='gray', alpha=0.3, s=15, label='Noisy data')

# True curve
ax.plot(X_test, y_true, 'k--', linewidth=2, alpha=0.7, label='True sin(x)')

# KNN regression for different k values
configs = [(1, MLRED, 'k=1 (overfitting)'), (5, MLBLUE, 'k=5 (good fit)'),
           (20, MLORANGE, 'k=20 (too smooth)')]

for k, color, label in configs:
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    ax.plot(X_test, y_pred, color=color, linewidth=2.5, label=label)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('KNN Regression: Effect of k on Smoothness', fontweight='bold')
ax.legend(loc='upper right', framealpha=0.9)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_13_knn_regression/chart.pdf")
