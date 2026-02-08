"""Policy Visualization - Q-Learning Trained Trading Policy"""
import matplotlib.pyplot as plt
import numpy as np
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
MLRED = '#D62728'
MLORANGE = '#FF7F0E'

CHART_METADATA = {
    "title": "Q-Learning Trained Trading Policy",
    "description": "Trading policy learned via Q-learning based on RSI and momentum",
    "url": "https://github.com/Digital-AI-Finance/methods-algorithms/tree/master/slides/L06_Embeddings_RL/06_policy_viz"
}

np.random.seed(42)

# Q-learning parameters
N_RSI_BINS = 10
N_MOM_BINS = 10
N_ACTIONS = 3  # Buy (0), Hold (1), Sell (2)
ALPHA = 0.1  # learning rate
GAMMA = 0.95  # discount factor
EPSILON = 0.1  # exploration rate
N_EPISODES = 5000
MAX_STEPS = 50

# Discretize state space
rsi_bins = np.linspace(0, 100, N_RSI_BINS + 1)
mom_bins = np.linspace(-5, 5, N_MOM_BINS + 1)

def discretize_state(rsi, momentum):
    """Convert continuous state to discrete bin indices"""
    rsi_idx = np.digitize(rsi, rsi_bins) - 1
    mom_idx = np.digitize(momentum, mom_bins) - 1
    rsi_idx = np.clip(rsi_idx, 0, N_RSI_BINS - 1)
    mom_idx = np.clip(mom_idx, 0, N_MOM_BINS - 1)
    return rsi_idx, mom_idx

def compute_reward(action, momentum, prev_position, transaction_cost=0.02):
    """
    Reward function:
    - Positive reward for buying when momentum > 0, selling when momentum < 0
    - Transaction cost for changing position
    - Small penalty for holding in wrong direction
    """
    # action: 0=Buy, 1=Hold, 2=Sell
    # Convert to position: Buy=1, Hold=prev, Sell=-1
    if action == 0:  # Buy
        new_position = 1
    elif action == 2:  # Sell
        new_position = -1
    else:  # Hold
        new_position = prev_position

    # Position aligns with momentum = positive reward
    alignment_reward = new_position * momentum * 0.5

    # Transaction cost if position changed
    cost = transaction_cost if new_position != prev_position else 0

    return alignment_reward - cost

class TradingEnvironment:
    """Simple trading environment with RSI and momentum dynamics"""
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset to random initial state"""
        self.rsi = np.random.uniform(20, 80)
        self.momentum = np.random.uniform(-3, 3)
        self.position = 0  # Start neutral
        self.step_count = 0
        return self.rsi, self.momentum

    def step(self, action):
        """Execute action and return next state, reward, done"""
        self.step_count += 1

        # Compute reward
        reward = compute_reward(action, self.momentum, self.position)

        # Update position
        if action == 0:  # Buy
            self.position = 1
        elif action == 2:  # Sell
            self.position = -1
        # action == 1 (Hold) keeps current position

        # Evolve state with mean reversion dynamics
        # RSI reverts toward 50, momentum reverts toward 0
        self.rsi += np.random.normal(0, 5) + (50 - self.rsi) * 0.1
        self.rsi = np.clip(self.rsi, 0, 100)

        self.momentum += np.random.normal(0, 0.8) - self.momentum * 0.15
        self.momentum = np.clip(self.momentum, -5, 5)

        done = self.step_count >= MAX_STEPS

        return self.rsi, self.momentum, reward, done

# Initialize Q-table
Q = np.zeros((N_RSI_BINS, N_MOM_BINS, N_ACTIONS))

# Train Q-learning
env = TradingEnvironment()
episode_rewards = []

print("Training Q-learning agent...")
for episode in range(N_EPISODES):
    rsi, momentum = env.reset()
    total_reward = 0

    for step in range(MAX_STEPS):
        # Get current state
        rsi_idx, mom_idx = discretize_state(rsi, momentum)

        # Epsilon-greedy action selection
        if np.random.random() < EPSILON:
            action = np.random.randint(N_ACTIONS)
        else:
            action = np.argmax(Q[rsi_idx, mom_idx])

        # Take action
        next_rsi, next_momentum, reward, done = env.step(action)
        total_reward += reward

        # Update Q-value
        next_rsi_idx, next_mom_idx = discretize_state(next_rsi, next_momentum)
        best_next_action = np.argmax(Q[next_rsi_idx, next_mom_idx])
        td_target = reward + GAMMA * Q[next_rsi_idx, next_mom_idx, best_next_action]
        Q[rsi_idx, mom_idx, action] += ALPHA * (td_target - Q[rsi_idx, mom_idx, action])

        rsi = next_rsi
        momentum = next_momentum

        if done:
            break

    episode_rewards.append(total_reward)

    if (episode + 1) % 1000 == 0:
        avg_reward = np.mean(episode_rewards[-1000:])
        print(f"Episode {episode + 1}/{N_EPISODES}, Avg Reward: {avg_reward:.2f}")

print("Training complete!")

# Extract learned policy for visualization
rsi_viz = np.linspace(0, 100, 100)
momentum_viz = np.linspace(-5, 5, 100)
RSI, MOM = np.meshgrid(rsi_viz, momentum_viz)

policy_grid = np.zeros_like(RSI)
for i in range(len(momentum_viz)):
    for j in range(len(rsi_viz)):
        rsi_idx, mom_idx = discretize_state(rsi_viz[j], momentum_viz[i])
        best_action = np.argmax(Q[rsi_idx, mom_idx])
        # Map: 0=Buy -> 1, 1=Hold -> 0, 2=Sell -> -1
        if best_action == 0:
            policy_grid[i, j] = 1  # Buy
        elif best_action == 2:
            policy_grid[i, j] = -1  # Sell
        else:
            policy_grid[i, j] = 0  # Hold

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Plot policy regions
im = ax.contourf(RSI, MOM, policy_grid, levels=[-1.5, -0.5, 0.5, 1.5],
                  colors=[MLRED, 'lightgray', MLGREEN], alpha=0.6)

# Add contour lines
ax.contour(RSI, MOM, policy_grid, levels=[-0.5, 0.5], colors='black', linewidths=2)

# Find representative points for labels
sell_mask = policy_grid < -0.5
hold_mask = (policy_grid >= -0.5) & (policy_grid <= 0.5)
buy_mask = policy_grid > 0.5

if np.any(sell_mask):
    sell_coords = np.where(sell_mask)
    sell_center = (RSI[sell_coords].mean(), MOM[sell_coords].mean())
    ax.text(sell_center[0], sell_center[1], 'SELL', fontsize=14, fontweight='bold',
            color=MLRED, ha='center', va='center')

if np.any(hold_mask):
    hold_coords = np.where(hold_mask)
    hold_center = (RSI[hold_coords].mean(), MOM[hold_coords].mean())
    ax.text(hold_center[0], hold_center[1], 'HOLD', fontsize=14, fontweight='bold',
            color='gray', ha='center', va='center')

if np.any(buy_mask):
    buy_coords = np.where(buy_mask)
    buy_center = (RSI[buy_coords].mean(), MOM[buy_coords].mean())
    ax.text(buy_center[0], buy_center[1], 'BUY', fontsize=14, fontweight='bold',
            color=MLGREEN, ha='center', va='center')

ax.set_xlabel('RSI (Relative Strength Index)')
ax.set_ylabel('Price Momentum (%)')
ax.set_title('Q-Learning Trained Trading Policy')
ax.grid(True, alpha=0.3)

# Add URL annotation
plt.figtext(0.99, 0.01, CHART_METADATA['url'],
            fontsize=7, color='gray', ha='right', va='bottom', alpha=0.7)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight')
plt.close()
print("Chart saved: 06_policy_viz/chart.pdf")
