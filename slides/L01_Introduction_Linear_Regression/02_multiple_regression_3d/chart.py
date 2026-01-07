"""Multiple Regression 3D Surface - Price vs Size and Bedrooms"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

# Chart settings for Beamer
plt.rcParams.update({
    'font.size': 12, 'axes.labelsize': 12, 'axes.titlesize': 14,
    'xtick.labelsize': 11, 'ytick.labelsize': 11, 'legend.fontsize': 11,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

# Colors
MLPURPLE = '#3333B2'
MLORANGE = '#FF7F0E'
MLBLUE = '#0066CC'

# Generate synthetic data
np.random.seed(42)
n = 100
size = np.random.uniform(50, 200, n)
bedrooms = np.random.randint(1, 6, n)
noise = np.random.normal(0, 20000, n)
price = 30000 + 1800 * size + 25000 * bedrooms + noise

# Create regression surface
size_grid = np.linspace(50, 200, 30)
bed_grid = np.linspace(1, 5, 30)
SIZE, BED = np.meshgrid(size_grid, bed_grid)
PRICE = 30000 + 1800 * SIZE + 25000 * BED

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(SIZE, BED, PRICE/1000, alpha=0.5, cmap='viridis')

# Plot data points
ax.scatter(size, bedrooms, price/1000, c=MLORANGE, s=30, alpha=0.8)

# Labels
ax.set_xlabel('Size (sqm)')
ax.set_ylabel('Bedrooms')
ax.set_zlabel('Price (thousands $)')
ax.set_title('Multiple Regression: Price = f(Size, Bedrooms)')

# Adjust view angle
ax.view_init(elev=20, azim=45)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 02_multiple_regression_3d/chart.pdf")
