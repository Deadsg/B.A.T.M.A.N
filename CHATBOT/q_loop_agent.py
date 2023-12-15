import numpy as np

def q_loop_agent():
    pass

class QLearningAgent:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration-exploitation tradeoff
        self.q_table = np.zeros((n_states, n_actions))

    def choose_action(self, state):
        # Exploration-exploitation tradeoff
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.n_actions)  # Explore
        else:
            return np.argmax(self.q_table[state, :])  # Exploit

    def update_q_table(self, state, action, reward, next_state):
        # Q-table update formula
        current_q = self.q_table[state, action]
        max_future_q = np.max(self.q_table[next_state, :])
        new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * max_future_q)
        self.q_table[state, action] = new_q

def run_q_learning(agent, episodes=1000):
    for episode in range(episodes):
        state = np.random.choice(agent.n_states)  # Random initial state
        total_reward = 0

        while True:
            action = agent.choose_action(state)
            
            # Simulate a simple environment
            if state == 0 and action == 0:
                next_state, reward, done = 1, 1, False
            elif state == 1 and action == 1:
                next_state, reward, done = 2, 2, False
            else:
                next_state, reward, done = state, 0, True

            agent.update_q_table(state, action, reward, next_state)

            total_reward += reward
            state = next_state

            if done:
                break

        if episode % 100 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}")

# Example usage:
# Assume a simple environment with 5 states and 2 actions
num_states = 5
num_actions = 2

# Create Q-learning agent
q_agent = QLearningAgent(num_states, num_actions)

# Run Q-learning loop
run_q_learning(q_agent)
