"""Line chart: train vs test error as max_depth increases."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

depths = range(1, 21)
train_errors = []
test_errors = []

for d in depths:
    clf = DecisionTreeClassifier(max_depth=d, random_state=42)
    clf.fit(X_train, y_train)
    train_errors.append(1 - clf.score(X_train, y_train))
    test_errors.append(1 - clf.score(X_test, y_test))

best_depth = depths[np.argmin(test_errors)]

fig, ax = plt.subplots()
ax.plot(depths, train_errors, 'o-', color=MLBLUE, linewidth=2, markersize=5, label='Train Error')
ax.plot(depths, test_errors, 's-', color=MLORANGE, linewidth=2, markersize=5, label='Test Error')
ax.axvline(best_depth, color=MLRED, linestyle='--', linewidth=1.5, alpha=0.7,
           label=f'Best Depth = {best_depth}')

# Annotations
ax.text(2.5, max(test_errors) * 0.85, "Underfitting", fontsize=13, color=MLPURPLE,
        fontweight='bold', ha='center')
ax.text(17, max(test_errors) * 0.85, "Overfitting", fontsize=13, color=MLRED,
        fontweight='bold', ha='center')

ax.set_xlabel("Max Depth")
ax.set_ylabel("Classification Error")
ax.set_title("Decision Tree: Train vs Test Error by Depth")
ax.legend(loc='upper right')
ax.set_xticks(range(1, 21, 2))

plt.tight_layout()
fig.savefig(Path(__file__).parent / "chart.pdf", bbox_inches='tight')
plt.close(fig)
print("09_dt_overfitting/chart.pdf created")
