"""KNN Confusion Matrix - 3-class confusion matrix heatmap."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "KNN Confusion Matrix (k=7, 3-Class)",
    "description": "Confusion matrix heatmap for 3-class KNN classification",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L03_KNN_KMeans/top10_20_knn_confusion_matrix"
}


X, y = make_classification(n_samples=800, n_features=8, n_informative=5,
                           n_classes=3, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                     random_state=42)

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
class_names = ['Low Risk', 'Medium Risk', 'High Risk']

fig, ax = plt.subplots(figsize=(10, 6))

im = ax.imshow(cm, interpolation='nearest', cmap='Blues')
ax.grid(False)

# Annotate cells
thresh = cm.max() / 2.0
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, f'{cm[i, j]}', ha='center', va='center',
                fontsize=18, fontweight='bold',
                color='white' if cm[i, j] > thresh else 'black')

ax.set_xticks(range(len(class_names)))
ax.set_xticklabels(class_names)
ax.set_yticks(range(len(class_names)))
ax.set_yticklabels(class_names)
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
ax.set_title('KNN Confusion Matrix (k=7, 3-Class)', fontweight='bold')

cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Count', fontsize=12)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_20_knn_confusion_matrix/chart.pdf")
