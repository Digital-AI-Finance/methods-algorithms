"""Confusion Matrix - Classification results visualization"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from pathlib import Path

CHART_METADATA = {
    "title": "Confusion Matrix",
    "description": "Credit default prediction matrix with metrics",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/06_confusion_matrix"
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

# Generate data and compute confusion matrix with sklearn
X, y = make_classification(n_samples=500, n_features=10, n_informative=5,
                           weights=[0.85, 0.15], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = LogisticRegression(random_state=42, max_iter=1000).fit(X_train, y_train)
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

tn, fp, fn, tp = cm.ravel()

fig, ax = plt.subplots(figsize=(10, 6))

# Create heatmap
cmap_custom = plt.cm.Blues
im = ax.imshow(cm, cmap=cmap_custom, aspect='auto')

# Add text annotations
labels = [[f'TN\n(True Negative)\n{tn}', f'FP\n(False Positive)\n{fp}'],
          [f'FN\n(False Negative)\n{fn}', f'TP\n(True Positive)\n{tp}']]
colors = [['black', MLRED], [MLRED, 'white']]

for i in range(2):
    for j in range(2):
        ax.text(j, i, labels[i][j], ha='center', va='center',
                fontsize=13, color=colors[i][j], fontweight='bold')

# Axis labels
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['Predicted: No Default', 'Predicted: Default'])
ax.set_yticklabels(['Actual: No Default', 'Actual: Default'])
ax.set_xlabel('Predicted Label', fontsize=14)
ax.set_ylabel('Actual Label', fontsize=14)
ax.set_title('Confusion Matrix: Credit Default Prediction', fontsize=16)

# Add metrics box
total = tn + fp + fn + tp
accuracy = (tn + tp) / total
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

metrics_text = (f'Accuracy: {accuracy:.1%}\n'
                f'Precision: {precision:.1%}\n'
                f'Recall: {recall:.1%}\n'
                f'F1 Score: {f1:.2f}')
ax.text(1.35, 0.5, metrics_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='center',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

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
print("Chart saved: 06_confusion_matrix/chart.pdf")
