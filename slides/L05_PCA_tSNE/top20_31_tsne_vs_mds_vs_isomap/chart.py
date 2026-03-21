"""Trustworthiness: t-SNE vs MDS vs Isomap - Grouped bar comparison."""
import matplotlib.pyplot as plt
import numpy as np
import time
from pathlib import Path
from sklearn.datasets import make_moons
from sklearn.manifold import TSNE, MDS, Isomap, trustworthiness
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'templates'))
from chart_style import apply_style, COLORS, MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLLAVENDER
apply_style()

CHART_METADATA = {
    "title": "Trustworthiness: t-SNE vs MDS vs Isomap",
    "description": "Grouped bar chart comparing trustworthiness and runtime of three manifold methods on make_moons embedded in 10D.",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L05_PCA_tSNE/top20_31_tsne_vs_mds_vs_isomap"
}


np.random.seed(42)

# Data: make_moons in 10D (2 real + 8 noise dims)
X_2d, y = make_moons(n_samples=600, noise=0.05, random_state=42)
X_noise = np.random.RandomState(42).randn(600, 8) * 0.5
X = np.hstack([X_2d, X_noise])

# Run each method and measure time + trustworthiness
methods = {
    't-SNE': TSNE(n_components=2, random_state=42),
    'MDS': MDS(n_components=2, random_state=42, normalized_stress='auto'),
    'Isomap': Isomap(n_components=2),
}

names = []
trust_scores = []
runtimes = []
colors = [MLPURPLE, MLBLUE, MLGREEN]

for name, model in methods.items():
    t0 = time.time()
    X_emb = model.fit_transform(X)
    elapsed = time.time() - t0
    t_score = trustworthiness(X, X_emb, n_neighbors=10)
    names.append(name)
    trust_scores.append(t_score)
    runtimes.append(elapsed)

fig, ax = plt.subplots()

x_pos = np.arange(len(names))
bars = ax.bar(x_pos, trust_scores, width=0.5, color=colors, edgecolor='white', linewidth=1.5)

# Label each bar with exact value and runtime
for i, (bar, score, rt) in enumerate(zip(bars, trust_scores, runtimes)):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.008,
            f'{score:.3f}', ha='center', va='bottom', fontsize=14, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.035,
            f'{rt:.2f}s', ha='center', va='bottom', fontsize=11, color='gray')

ax.set_xticks(x_pos)
ax.set_xticklabels(names)
ax.set_ylabel('Trustworthiness (k=10)')
ax.set_ylim(0, 1.12)
ax.set_title('Trustworthiness: t-SNE vs MDS vs Isomap')
ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.3, linewidth=0.8)

plt.figtext(0.99, 0.01, CHART_METADATA['url'], fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
