"""
Chart 13: Cross-Validation - Finding Optimal K Neighbors
Train vs validation accuracy curves with overfitting/underfitting zones.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False, 'axes.spines.right': False,
})

COLORS = {
    'purple': '#3333B2', 'blue': '#0066CC', 'orange': '#FF7F0E',
    'green': '#2CA02C', 'red': '#D62728', 'lavender': '#ADADE0', 'gray': '#808080',
}

np.random.seed(42)

# Generate synthetic classification data
X, y = make_classification(n_samples=300, n_features=10, n_informative=5,
                           n_redundant=2, n_classes=2, random_state=42,
                           flip_y=0.1)

k_values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
train_scores = []
val_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    # Training accuracy (fit on all, predict on all)
    knn.fit(X, y)
    train_scores.append(knn.score(X, y))
    # Validation accuracy (5-fold CV)
    cv_scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
    val_scores.append(cv_scores.mean())

train_scores = np.array(train_scores)
val_scores = np.array(val_scores)

# Find optimal K
best_idx = np.argmax(val_scores)
best_k = k_values[best_idx]
best_acc = val_scores[best_idx]

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 6))

# Shaded zones
ax.axvspan(0, 6, alpha=0.05, color=COLORS['red'], zorder=0)
ax.axvspan(14, 20, alpha=0.05, color=COLORS['orange'], zorder=0)
ax.text(2.5, 0.72, 'Overfitting\nzone', fontsize=11, color=COLORS['red'],
        ha='center', alpha=0.8)
ax.text(17.5, 0.72, 'Underfitting\nzone', fontsize=11, color=COLORS['orange'],
        ha='center', alpha=0.8)

# Training accuracy line
ax.plot(k_values, train_scores, 'o-', color=COLORS['gray'], linewidth=2.0,
        markersize=7, label='Training accuracy', zorder=3)

# Validation accuracy line
ax.plot(k_values, val_scores, 's-', color=COLORS['blue'], linewidth=2.0,
        markersize=7, label='Validation accuracy (5-fold CV)', zorder=3)

# Optimal K (green star)
ax.scatter(best_k, best_acc, color=COLORS['green'], s=300, marker='*',
           zorder=5, edgecolors='black', linewidths=0.8,
           label=f'Optimal K={best_k} ({best_acc:.2f})')

# Annotate optimal
ax.annotate(f'Best: K={best_k}\nAcc={best_acc:.2f}',
            xy=(best_k, best_acc),
            xytext=(best_k + 3, best_acc + 0.02),
            fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=COLORS['green'], alpha=0.9),
            arrowprops=dict(arrowstyle='->', color=COLORS['green'], lw=1.5),
            zorder=6)

ax.set_xlabel('K (Number of Neighbors)')
ax.set_ylabel('Accuracy')
ax.set_title('Cross-Validation: Finding Optimal K Neighbors')
ax.set_xticks(k_values)
ax.set_ylim(0.70, 1.02)
ax.set_xlim(0, 20)
ax.legend(loc='upper right', framealpha=0.9)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(Path(__file__).parent / 'chart.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to: {output_path}")
