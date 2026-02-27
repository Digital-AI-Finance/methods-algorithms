"""ROC Curve - Receiver Operating Characteristic"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from pathlib import Path

CHART_METADATA = {
    "title": "ROC Curve",
    "description": "Receiver Operating Characteristic comparison",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/04_roc_curve"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

np.random.seed(42)

# Generate data and fit logistic regression with sklearn
X, y = make_classification(n_samples=500, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = LogisticRegression(random_state=42, max_iter=1000).fit(X_train, y_train)
fpr_good, tpr_good, _ = roc_curve(y_test, clf.predict_proba(X_test)[:, 1])
auc_good = auc(fpr_good, tpr_good)

# Medium model: use fewer features
clf_med = LogisticRegression(random_state=42, max_iter=1000).fit(X_train[:, :3], y_train)
fpr_medium, tpr_medium, _ = roc_curve(y_test, clf_med.predict_proba(X_test[:, :3])[:, 1])
auc_medium = auc(fpr_medium, tpr_medium)

# Poor model: use single noisy feature
clf_poor = LogisticRegression(random_state=42, max_iter=1000).fit(X_train[:, 5:6], y_train)
fpr_poor, tpr_poor, _ = roc_curve(y_test, clf_poor.predict_proba(X_test[:, 5:6])[:, 1])
auc_poor = auc(fpr_poor, tpr_poor)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot ROC curves
ax.plot(fpr_good, tpr_good, color=MLGREEN, linewidth=3,
        label=f'Good Model (AUC = {auc_good:.2f})')
ax.plot(fpr_medium, tpr_medium, color=MLORANGE, linewidth=3,
        label=f'Medium Model (AUC = {auc_medium:.2f})')
ax.plot(fpr_poor, tpr_poor, color=MLRED, linewidth=3,
        label=f'Poor Model (AUC = {auc_poor:.2f})')

# Random classifier line
ax.plot([0, 1], [0, 1], color='gray', linewidth=2, linestyle='--',
        label='Random (AUC = 0.50)')

# Fill AUC area for good model
ax.fill_between(fpr_good, 0, tpr_good, alpha=0.15, color=MLGREEN)

# Annotations
ax.annotate('AUC Area', xy=(0.6, 0.4), fontsize=12, color=MLGREEN)
ax.annotate('', xy=(0.3, 0.7), xytext=(0.3, 0.3),
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=2))
ax.text(0.35, 0.5, 'Better', fontsize=11, color=MLPURPLE, rotation=90, va='center')

ax.set_xlabel('False Positive Rate (FPR)')
ax.set_ylabel('True Positive Rate (TPR)')
ax.set_title('ROC Curves: Model Comparison')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

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
print("Chart saved: 04_roc_curve/chart.pdf")
