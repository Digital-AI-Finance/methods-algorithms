"""Decision Boundary - 2D classification visualization"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Decision Boundary",
    "description": "Linear classification boundary with probability contours",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/02_decision_boundary"
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

np.random.seed(42)

# Generate two-class data
n_samples = 100
class0_x = np.random.randn(n_samples, 2) * 0.8 + np.array([-1.5, -1])
class1_x = np.random.randn(n_samples, 2) * 0.8 + np.array([1.5, 1])

fig, ax = plt.subplots(figsize=(10, 6))

# Plot data points
ax.scatter(class0_x[:, 0], class0_x[:, 1], c=MLRED, s=60, alpha=0.7,
           label='Class 0 (No Default)', edgecolors='white', linewidth=0.5)
ax.scatter(class1_x[:, 0], class1_x[:, 1], c=MLGREEN, s=60, alpha=0.7,
           label='Class 1 (Default)', edgecolors='white', linewidth=0.5)

# Decision boundary (learned weights simulation)
x_line = np.linspace(-4, 4, 100)
# w0 + w1*x1 + w2*x2 = 0 -> x2 = -(w0 + w1*x1)/w2
w0, w1, w2 = -0.2, 1, 1  # simulated weights
y_line = -(w0 + w1 * x_line) / w2

ax.plot(x_line, y_line, color=MLPURPLE, linewidth=3, linestyle='--',
        label='Decision Boundary')

# Shade regions
xx, yy = np.meshgrid(np.linspace(-4, 4, 100), np.linspace(-4, 4, 100))
Z = 1 / (1 + np.exp(-(w0 + w1*xx + w2*yy)))
ax.contourf(xx, yy, Z, levels=[0, 0.5, 1], colors=[MLRED, MLGREEN], alpha=0.1)

ax.set_xlabel('Feature 1 (e.g., Income)')
ax.set_ylabel('Feature 2 (e.g., Debt Ratio)')
ax.set_title('Logistic Regression Decision Boundary')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_decision_boundary/chart.pdf")
