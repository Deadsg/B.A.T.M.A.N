import numpy as np

class GridWorldEnvironment:
    def __init__(self, grid_size=(5, 5), start=(0, 0), goal=(4, 4), obstacles=[]):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.state = start

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):
        x, y = self.state

        if action == 0:  # Move up
            y = max(y - 1, 0)
        elif action == 1:  # Move down
            y = min(y + 1, self.grid_size[1] - 1)
        elif action == 2:  # Move left
            x = max(x - 1, 0)
        elif action == 3:  # Move right
            x = min(x + 1, self.grid_size[0] - 1)

        if (x, y) in self.obstacles:
            reward = -1  # Negative reward for hitting an obstacle
            done = False
        elif (x, y) == self.goal:
            reward = 10  # Positive reward for reaching the goal
            done = True
        else:
            reward = -0.1  # Small negative reward for each step taken
            done = False

        self.state = (x, y)
        return self.state, reward, done