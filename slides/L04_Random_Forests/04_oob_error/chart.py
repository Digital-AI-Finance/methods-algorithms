"""Out-of-Bag Error - OOB vs Test Error comparison"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from pathlib import Path

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'OOB Error Estimation',
    'description': 'Out-of-bag error convergence with tree count',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/04_oob_error'
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
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

np.random.seed(42)

# Generate classification data with sklearn
X, y = make_classification(n_samples=500, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Compute OOB and test error for increasing number of trees
n_trees_range = list(range(10, 501, 10))
oob_errors = []
test_errors = []
train_errors = []

for n in n_trees_range:
    rf = RandomForestClassifier(n_estimators=n, oob_score=True, random_state=42)
    rf.fit(X_train, y_train)
    oob_errors.append(1 - rf.oob_score_)
    test_errors.append(1 - rf.score(X_test, y_test))
    train_errors.append(1 - rf.score(X_train, y_train))

n_trees_arr = np.array(n_trees_range)
oob_errors = np.array(oob_errors)
test_errors = np.array(test_errors)
train_errors = np.array(train_errors)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(n_trees_arr, train_errors, color=MLGREEN, linewidth=2, label='Training Error', alpha=0.8)
ax.plot(n_trees_arr, oob_errors, color=MLBLUE, linewidth=2.5, label='OOB Error')
ax.plot(n_trees_arr, test_errors, color=MLRED, linewidth=2, linestyle='--', label='Test Error')

# Highlight convergence region
ax.axvspan(200, 500, alpha=0.1, color='gray')
ax.text(350, max(oob_errors) * 0.95, 'Stable Region', fontsize=11, ha='center', style='italic', color='gray')

# Add horizontal line at final OOB error
final_oob = np.mean(oob_errors[-5:])
ax.axhline(y=final_oob, color=MLBLUE, linestyle=':', alpha=0.5)
ax.text(505, final_oob, f'{final_oob:.1%}', fontsize=10, va='center', color=MLBLUE)

ax.set_xlabel('Number of Trees', fontweight='bold')
ax.set_ylabel('Error Rate', fontweight='bold')
ax.set_title('Out-of-Bag Error vs Number of Trees', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', framealpha=0.9)

ax.set_xlim(0, 520)
y_max = max(max(oob_errors), max(test_errors)) * 1.3
ax.set_ylim(0, y_max)
ax.grid(True, alpha=0.3)

# Format y-axis as percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0%}'))

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 04_oob_error/chart.pdf")
