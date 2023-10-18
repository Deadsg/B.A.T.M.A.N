import numpy as np
import gym

def reinforcement_learing():
# Create the FrozenLake environment
env = gym.make('FrozenLake-v1')

# Q-learning parameters
num_episodes = 1000
learning_rate = 0.1
discount_factor = 0.99

# Initialize the Q-table with zeros (state-action values)
num_states = env.observation_space.n
num_actions = env.action_space.n
Q = np.zeros((num_states, num_actions))

# Exploration settings
epsilon = 0.5
min_epsilon = 0.01
decay_rate = 0.995

# Q-learning algorithm
for episode in range(num_episodes):
    state = env.reset()
    done = False
    
    while not done:
        # Exploration vs. exploitation (epsilon-greedy)
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(Q[state, :])  # Exploit
        
        # Take the chosen action
        next_state, reward, done, _ = env.step(action)
        
        # Update Q-value using the Q-learning update rule
        Q[state, action] = (1 - learning_rate) * Q[state, action] + \
                           learning_rate * (reward + discount_factor * np.max(Q[next_state, :]))
        
        # Transition to the next state
        state = next_state
    
    # Decay epsilon to reduce exploration over time
    epsilon = max(min_epsilon, epsilon * decay_rate)

# Evaluate the trained Q-table
num_episodes_eval = 100
total_rewards = 0

for _ in range(num_episodes_eval):
    state = env.reset()
    done = False
    
    while not done:
        action = np.argmax(Q[state, :])  # Exploit
        next_state, reward, done, _ = env.step(action)
        total_rewards += reward
        state = next_state

average_reward = total_rewards / num_episodes_eval
print(f"Average reward over {num_episodes_eval} episodes: {average_reward}")