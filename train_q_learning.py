import collections

import numpy as np

q_data = collections.defaultdict(list)

# add data to q_data
for key, value in data.items():
    q_data[key].append(value)

# access data from q_data
if key in q_data:
    for value in q_data[key]:
        print(value)

class QLearning:
    def __init__(self, state_space_size, action_space_size, learning_rate, discount_factor):
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = np.zeros((state_space_size, action_space_size))

    def train(self, state, action, reward, next_state):
        q_value = self.q_table[state]