"""Explained Variance vs Classification Accuracy - PCA component selection guide."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Explained Variance vs Classification Accuracy",
    "description": "Line plot of logistic regression CV accuracy vs PCA components with cumulative variance annotations.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_35_explained_var_vs_accuracy"
}


np.random.seed(42)

# Data
X, y = make_classification(n_samples=800, n_features=30, n_informative=8, random_state=42)

# Full PCA to get explained variance ratios
pca_full = PCA(random_state=42).fit(X)
cumvar = np.cumsum(pca_full.explained_variance_ratio_)

k_values = list(range(2, 26))
accuracies = []

for k in k_values:
    X_pca = PCA(n_components=k, random_state=42).fit_transform(X)
    scores = cross_val_score(LogisticRegression(max_iter=1000), X_pca, y, cv=5)
    accuracies.append(scores.mean())

fig, ax = plt.subplots()

ax.plot(k_values, accuracies, 'o-', color=MLPURPLE, linewidth=2.5, markersize=6, label='5-fold CV Accuracy')

# Accuracy plateau: where improvement < 0.5% over next 3 steps
plateau_acc = max(accuracies)
plateau_k = None
for i in range(len(accuracies) - 2):
    if all((plateau_acc - accuracies[i + j]) < 0.01 for j in range(3)):
        plateau_k = k_values[i]
        break

if plateau_k is not None:
    ax.axhline(y=accuracies[k_values.index(plateau_k)], color='gray', linestyle='--',
               alpha=0.5, linewidth=1.5, label=f'Plateau ({accuracies[k_values.index(plateau_k)]:.3f})')

# Annotate cumulative variance at k=5,10,15,20
annotate_ks = [5, 10, 15, 20]
for ak in annotate_ks:
    idx = k_values.index(ak)
    cv_ratio = cumvar[ak - 1]  # 0-indexed
    ax.annotate(f'{cv_ratio:.0%} var',
                xy=(ak, accuracies[idx]),
                xytext=(ak + 1.2, accuracies[idx] - 0.025),
                fontsize=10, color=MLBLUE,
                arrowprops=dict(arrowstyle='->', color=MLBLUE, lw=1.2))

ax.set_xlabel('Number of PCA Components (k)')
ax.set_ylabel('Logistic Regression Accuracy (5-fold CV)')
ax.set_ylim(0.5, 1.0)
ax.set_title('Explained Variance vs Classification Accuracy')
ax.legend(loc='lower right', framealpha=0.9)
ax.grid(axis='y', alpha=0.3)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
