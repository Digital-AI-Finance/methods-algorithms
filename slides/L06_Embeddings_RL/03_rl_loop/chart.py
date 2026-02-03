"""RL Agent-Environment Loop - Core RL interaction diagram"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLORANGE = '#FF7F0E'

CHART_METADATA = {
    'url': 'github.com/joerg-osterrieder/Methods_and_Algorithms'
}

fig, ax = plt.subplots(figsize=(10, 6))

# Draw Agent box
agent = mpatches.FancyBboxPatch((0.15, 0.55), 0.25, 0.25,
                                  boxstyle="round,pad=0.02,rounding_size=0.05",
                                  facecolor=MLBLUE, edgecolor='black', linewidth=2)
ax.add_patch(agent)
ax.text(0.275, 0.675, 'Agent', ha='center', va='center', fontsize=16,
        fontweight='bold', color='white')
ax.text(0.275, 0.60, '(Policy)', ha='center', va='center', fontsize=12, color='white')

# Draw Environment box
env = mpatches.FancyBboxPatch((0.60, 0.55), 0.25, 0.25,
                                boxstyle="round,pad=0.02,rounding_size=0.05",
                                facecolor=MLGREEN, edgecolor='black', linewidth=2)
ax.add_patch(env)
ax.text(0.725, 0.675, 'Environment', ha='center', va='center', fontsize=16,
        fontweight='bold', color='white')
ax.text(0.725, 0.60, '(Market)', ha='center', va='center', fontsize=12, color='white')

# Arrow: Action (Agent -> Environment)
ax.annotate('', xy=(0.60, 0.72), xytext=(0.40, 0.72),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=3))
ax.text(0.50, 0.78, 'Action $a_t$', ha='center', va='center', fontsize=13,
        fontweight='bold', color=MLORANGE)
ax.text(0.50, 0.72, '(buy/sell/hold)', ha='center', va='center', fontsize=10,
        color='gray')

# Arrow: State (Environment -> Agent, bottom path)
ax.annotate('', xy=(0.40, 0.40), xytext=(0.60, 0.40),
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=3,
                           connectionstyle='arc3,rad=-0.3'))
ax.text(0.50, 0.32, 'State $s_{t+1}$', ha='center', va='center', fontsize=13,
        fontweight='bold', color=MLPURPLE)
ax.text(0.50, 0.26, '(prices, portfolio)', ha='center', va='center', fontsize=10,
        color='gray')

# Arrow: Reward
ax.annotate('', xy=(0.40, 0.55), xytext=(0.60, 0.55),
            arrowprops=dict(arrowstyle='->', color='#D62728', lw=3))
ax.text(0.50, 0.48, 'Reward $r_t$', ha='center', va='center', fontsize=13,
        fontweight='bold', color='#D62728')
ax.text(0.50, 0.42, '(profit/loss)', ha='center', va='center', fontsize=10,
        color='gray')

# Time step annotation
ax.text(0.50, 0.12, 'At each time step t:', ha='center', va='center', fontsize=12,
        style='italic', color='gray')
ax.text(0.50, 0.06, 'Agent observes state, takes action, receives reward',
        ha='center', va='center', fontsize=11, color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Reinforcement Learning: Agent-Environment Interaction', fontsize=16,
             fontweight='bold', y=0.95)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 03_rl_loop/chart.pdf")
