"""Sigmoid Function - The logistic activation function"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    "title": "Sigmoid Function",
    "description": "Logistic activation function visualization",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L02_Logistic_Regression/01_sigmoid_function"
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

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-8, 8, 200)
y = sigmoid(z)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(z, y, color=MLPURPLE, linewidth=3, label=r'$\sigma(z) = \frac{1}{1 + e^{-z}}$')
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.7, linewidth=1.5)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axhline(y=1, color='gray', linestyle=':', alpha=0.7, linewidth=1.5)
ax.axvline(x=0, color='black', linewidth=0.5)

# Annotations
ax.annotate('Decision\nThreshold', xy=(0, 0.5), xytext=(2.5, 0.5),
            fontsize=12, ha='left', va='center',
            arrowprops=dict(arrowstyle='->', color='gray'))
ax.annotate('Predict 1', xy=(4, 0.85), fontsize=12, color=MLGREEN)
ax.annotate('Predict 0', xy=(-6, 0.15), fontsize=12, color=MLRED)

# Shade regions
ax.fill_between(z[z >= 0], 0, y[z >= 0], alpha=0.15, color=MLGREEN)
ax.fill_between(z[z <= 0], 0, y[z <= 0], alpha=0.15, color=MLRED)

ax.set_xlabel('z = w\'x + b')
ax.set_ylabel('Probability P(y=1|x)')
ax.set_title('Sigmoid (Logistic) Function')
ax.set_xlim(-8, 8)
ax.set_ylim(-0.05, 1.05)
ax.legend(loc='upper left', fontsize=14)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 01_sigmoid_function/chart.pdf")
