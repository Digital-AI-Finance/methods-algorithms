"""Cost-Complexity Pruning - Pruning path with train and CV accuracy"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    'title': 'Decision Tree: Cost-Complexity Pruning',
    'description': 'Train and cross-validation accuracy across pruning alphas',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/19_pruning_ccp'
}


# Generate dataset
X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Get pruning path
dt = DecisionTreeClassifier(random_state=42)
path = dt.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas

# Subsample if too many alphas
if len(ccp_alphas) > 50:
    indices = np.linspace(0, len(ccp_alphas) - 1, 40, dtype=int)
    ccp_alphas = ccp_alphas[indices]

train_accs = []
cv_means = []
cv_stds = []

for alpha in ccp_alphas:
    dt_pruned = DecisionTreeClassifier(ccp_alpha=alpha, random_state=42)
    dt_pruned.fit(X_train, y_train)
    train_accs.append(dt_pruned.score(X_train, y_train))
    cv = cross_val_score(dt_pruned, X_train, y_train, cv=5)
    cv_means.append(cv.mean())
    cv_stds.append(cv.std())

train_accs = np.array(train_accs)
cv_means = np.array(cv_means)
cv_stds = np.array(cv_stds)

# Find optimal alpha (highest CV accuracy)
best_idx = np.argmax(cv_means)
best_alpha = ccp_alphas[best_idx]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(ccp_alphas, train_accs, color=MLBLUE, linewidth=2.5, marker='o', markersize=4, label='Train accuracy')
ax.plot(ccp_alphas, cv_means, color=MLRED, linewidth=2.5, marker='s', markersize=4, label='CV accuracy (5-fold)')
ax.fill_between(ccp_alphas, cv_means - cv_stds, cv_means + cv_stds, color=MLRED, alpha=0.15)

# Mark optimal alpha
ax.axvline(x=best_alpha, color=MLGREEN, linestyle='--', linewidth=2, label=f'Optimal $\\alpha$ = {best_alpha:.4f}')

ax.set_xlabel('Cost-Complexity Parameter ($\\alpha$)', fontweight='bold')
ax.set_ylabel('Accuracy', fontweight='bold')
ax.set_title('Decision Tree: Cost-Complexity Pruning', fontsize=16, fontweight='bold')
ax.legend(loc='lower left', fontsize=11)
ax.grid(True, alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 19_pruning_ccp/chart.pdf")
