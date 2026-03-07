"""Random Forest: Confusion Matrix (Fraud Detection)"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

CHART_METADATA = {
    'title': 'Random Forest: Confusion Matrix (Fraud Detection)',
    'description': '2x2 confusion matrix heatmap for imbalanced fraud detection',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/top10_14_confusion_matrix'
}

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

X, y = make_classification(n_samples=1000, n_features=10, weights=[0.9, 0.1], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
total = cm.sum()

# Color map: correct predictions green-ish, errors red-ish
cell_colors = np.array([
    ['#c8e6c9', '#ffcdd2'],  # TN (light green), FP (light red)
    ['#ffcdd2', '#2e7d32'],  # FN (light red), TP (dark green)
])

fig, ax = plt.subplots(figsize=(10, 6))

ax.imshow(np.zeros_like(cm), cmap='Greys', alpha=0)  # blank canvas

for i in range(2):
    for j in range(2):
        # Draw colored rectangle
        rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor=cell_colors[i][j], edgecolor='white', linewidth=3)
        ax.add_patch(rect)
        # Text: count + percentage
        count = cm[i, j]
        pct = count / total * 100
        text_color = 'white' if (i == 1 and j == 1) else 'black'
        ax.text(j, i, f'{count}\n({pct:.1f}%)', ha='center', va='center',
                fontsize=18, fontweight='bold', color=text_color)

class_names = ['Legitimate', 'Fraud']
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(class_names, fontsize=14)
ax.set_yticklabels(class_names, fontsize=14)
ax.set_xlabel("Predicted", fontsize=14, fontweight='bold')
ax.set_ylabel("Actual", fontsize=14, fontweight='bold')
ax.set_title("Random Forest: Confusion Matrix (Fraud Detection)", fontsize=16, fontweight='bold')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(1.5, -0.5)
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: top10_14_confusion_matrix/chart.pdf")
