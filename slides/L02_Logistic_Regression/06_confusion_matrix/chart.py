"""Confusion Matrix - Classification results visualization"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Confusion Matrix",
    "description": "Credit default prediction matrix with metrics",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/06_confusion_matrix"
}

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

# Confusion matrix values (credit scoring example)
# [TN, FP]
# [FN, TP]
cm = np.array([[850, 50],   # Actual Negative: TN=850, FP=50
               [30, 70]])    # Actual Positive: FN=30, TP=70

fig, ax = plt.subplots(figsize=(10, 6))

# Create heatmap
cmap_custom = plt.cm.Blues
im = ax.imshow(cm, cmap=cmap_custom, aspect='auto')

# Add text annotations
labels = [['TN\n(True Negative)\n850', 'FP\n(False Positive)\n50'],
          ['FN\n(False Negative)\n30', 'TP\n(True Positive)\n70']]
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
accuracy = (850 + 70) / 1000
precision = 70 / (70 + 50)
recall = 70 / (70 + 30)
f1 = 2 * precision * recall / (precision + recall)

metrics_text = (f'Accuracy: {accuracy:.1%}\n'
                f'Precision: {precision:.1%}\n'
                f'Recall: {recall:.1%}\n'
                f'F1 Score: {f1:.2f}')
ax.text(1.35, 0.5, metrics_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='center',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06_confusion_matrix/chart.pdf")
