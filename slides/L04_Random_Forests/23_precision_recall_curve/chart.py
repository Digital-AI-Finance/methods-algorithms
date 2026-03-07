"""Precision-Recall Curve: Fraud Detection"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, auc

CHART_METADATA = {
    'title': 'Precision-Recall Curve: Fraud Detection',
    'description': 'PR curve for an RF classifier on imbalanced fraud detection data with AUC-PR and F1-optimal point',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/23_precision_recall_curve'
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

X, y = make_classification(n_samples=2000, n_features=10, n_informative=5,
                           n_redundant=2, weights=[0.95, 0.05],
                           random_state=42, flip_y=0.01)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

rf = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
rf.fit(X_train, y_train)
y_scores = rf.predict_proba(X_test)[:, 1]

precision, recall, thresholds = precision_recall_curve(y_test, y_scores)
pr_auc = auc(recall, precision)

# F1-optimal point
f1_scores = 2 * (precision[:-1] * recall[:-1]) / (precision[:-1] + recall[:-1] + 1e-10)
best_idx = np.argmax(f1_scores)
best_precision = precision[best_idx]
best_recall = recall[best_idx]
best_f1 = f1_scores[best_idx]

fraud_rate = y_test.mean()

fig, ax = plt.subplots()

ax.fill_between(recall, precision, alpha=0.15, color=MLBLUE)
ax.plot(recall, precision, color=MLBLUE, linewidth=2.0, label=f'RF (AUC-PR = {pr_auc:.3f})')

ax.plot(best_recall, best_precision, marker='*', markersize=18, color=MLORANGE, zorder=5,
        label=f'Best F1 = {best_f1:.2f}')
ax.annotate(f'F1 = {best_f1:.2f}\n(P={best_precision:.2f}, R={best_recall:.2f})',
            xy=(best_recall, best_precision),
            xytext=(best_recall - 0.25, best_precision - 0.15),
            fontsize=11, fontweight='bold', color=MLORANGE,
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=1.2))

ax.axhline(y=fraud_rate, color='gray', linestyle='--', linewidth=1.2, alpha=0.7,
           label=f'Baseline (fraud rate = {fraud_rate:.2f})')

ax.set_xlabel('Recall')
ax.set_ylabel('Precision')
ax.set_title(CHART_METADATA['title'])
ax.set_xlim([0, 1.02])
ax.set_ylim([0, 1.05])
ax.legend(loc='upper right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 23_precision_recall_curve/chart.pdf")
