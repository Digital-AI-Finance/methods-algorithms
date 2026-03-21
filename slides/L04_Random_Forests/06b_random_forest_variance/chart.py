"""Random Forest Variance - Reduced variance through ensemble averaging"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

# Chart metadata for QR code generation
CHART_METADATA = {
    'title': 'Random Forest Variance',
    'description': 'Reduced variance through ensemble averaging',
    'url': 'https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L04_Random_Forests/06b_random_forest_variance'
}


np.random.seed(42)

# Generate true function
x = np.linspace(0, 10, 200)
y_true = np.sin(x) + 0.5 * np.cos(2*x)

# Generate training data
n_train = 30
x_train = np.random.uniform(0, 10, n_train)
y_train = np.sin(x_train) + 0.5 * np.cos(2*x_train) + np.random.normal(0, 0.3, n_train)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot training data
ax.scatter(x_train, y_train, c=MLBLUE, s=60, alpha=0.7, label='Training data', zorder=5)
ax.plot(x, y_true, 'k--', linewidth=2.5, label='True function', alpha=0.6)

# Train actual Random Forest with bootstrap samples
all_preds = []
for i in range(50):
    idx = np.random.choice(n_train, n_train, replace=True)
    rf = RandomForestRegressor(n_estimators=1, max_depth=5, random_state=i)
    rf.fit(x_train[idx].reshape(-1, 1), y_train[idx])
    y_pred = rf.predict(x.reshape(-1, 1))
    all_preds.append(y_pred)

# Average prediction
y_rf = np.mean(all_preds, axis=0)
y_rf_std = np.std(all_preds, axis=0)

ax.fill_between(x, y_rf - y_rf_std, y_rf + y_rf_std,
                color=MLGREEN, alpha=0.25, label='Prediction uncertainty')
ax.plot(x, y_rf, color=MLGREEN, linewidth=3, label='Random Forest (50 trees)')

ax.set_xlabel('x', fontweight='bold')
ax.set_ylabel('y', fontweight='bold')
ax.set_title('Random Forest: Reduced Variance via Averaging', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=12)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2.5)
ax.grid(True, alpha=0.3)

# Add annotation
ax.annotate('Averaging reduces\nprediction variance',
            xy=(7, 1.5), fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='gray', alpha=0.8))

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: 06b_random_forest_variance/chart.pdf")
