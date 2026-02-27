"""Decision Boundary - 2D classification visualization"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from pathlib import Path

CHART_METADATA = {
    "title": "Decision Boundary",
    "description": "Linear classification boundary with probability contours",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/02_decision_boundary"
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

# Generate two-class data and fit LogisticRegression with sklearn
X, y = make_classification(n_samples=200, n_features=2, n_redundant=0,
                           n_clusters_per_class=1, random_state=42)
clf = LogisticRegression(random_state=42).fit(X, y)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot data points
mask0 = y == 0
mask1 = y == 1
ax.scatter(X[mask0, 0], X[mask0, 1], c=MLRED, s=60, alpha=0.7,
           label='Class 0 (No Default)', edgecolors='white', linewidth=0.5)
ax.scatter(X[mask1, 0], X[mask1, 1], c=MLGREEN, s=60, alpha=0.7,
           label='Class 1 (Default)', edgecolors='white', linewidth=0.5)

# Decision boundary from fitted model
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1].reshape(xx.shape)
ax.contourf(xx, yy, Z, levels=[0, 0.5, 1], colors=[MLRED, MLGREEN], alpha=0.1)

# Plot the decision boundary line
w = clf.coef_[0]
b = clf.intercept_[0]
x_line = np.linspace(x_min, x_max, 100)
y_line = -(b + w[0] * x_line) / w[1]
ax.plot(x_line, y_line, color=MLPURPLE, linewidth=3, linestyle='--',
        label='Decision Boundary')

ax.set_xlabel('Feature 1 (e.g., Income)')
ax.set_ylabel('Feature 2 (e.g., Debt Ratio)')
ax.set_title('Logistic Regression Decision Boundary')
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

# Add URL annotation
ax.text(0.99, 0.01, CHART_METADATA['url'],
        transform=ax.transAxes,
        fontsize=7,
        color='gray',
        ha='right',
        va='bottom',
        alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_decision_boundary/chart.pdf")
