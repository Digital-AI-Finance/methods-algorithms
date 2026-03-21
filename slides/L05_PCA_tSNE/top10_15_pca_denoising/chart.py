"""PCA Denoising - Recovering signal from noise using low-rank PCA reconstruction."""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "PCA Denoising: Recovering Signal from Noise",
    "description": "Three-line plot comparing clean signal, noisy data, and PCA-reconstructed signal",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top10_15_pca_denoising"
}


np.random.seed(42)
n_samples = 200
n_features = 10
t = np.linspace(0, 4 * np.pi, n_samples)

X_clean = np.zeros((n_samples, n_features))
for j in range(n_features):
    X_clean[:, j] = np.sin(t + j * 0.5) + 0.5 * np.cos(2 * t + j * 0.3)

X_noisy = X_clean + np.random.normal(0, 0.5, X_clean.shape)

pca = PCA(n_components=3, random_state=42)
X_low = pca.fit_transform(X_noisy)
X_reconstructed = pca.inverse_transform(X_low)

feat = 0
fig, ax = plt.subplots()
ax.plot(t, X_clean[:, feat], color=MLGREEN, linestyle='--', linewidth=2, label='Original (clean)', zorder=3)
ax.plot(t, X_noisy[:, feat], color=MLRED, alpha=0.3, linewidth=1, label='Noisy', zorder=1)
ax.plot(t, X_reconstructed[:, feat], color=MLBLUE, linewidth=2.5, label='PCA reconstructed (3 PCs)', zorder=2)

ax.set_xlabel('Sample Index')
ax.set_ylabel('Feature Value')
ax.set_title('PCA Denoising: Recovering Signal from Noise')
ax.legend(loc='upper right', framealpha=0.9)

plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart saved: top10_15_pca_denoising/chart.pdf")
