import numpy as np

# Define the parameters
num_states = 5
num_actions = 3
learning_rate = 0.1
discount_factor = 0.9

# Initialize the Q-table with zeros
q_table = np.zeros((num_states, num_actions))

# Define the reward matrix (optional)
reward_matrix = np.array([[0, 0, 0],
                          [0, 0, 100],
                          [0, 100, 0],
                          [0, 0, 0],
                          [0, 0, 0]])

# Q-learning algorithm
def q_learning(state, action, reward, next_state):
    current_q = q_table[state, action]
    max_next_q = np.max(q_table[next_state])
    new_q = current_q + learning_rate * (reward + discount_factor * max_next_q - current_q)
    q_table[state, action] = new_q

# Example of using the q_learning function
state = 1
action = 2
next_state = 2
reward = reward_matrix[state, action]
q_learning(state, action, reward, next_state)

# Display the Q-table
print(q_table)