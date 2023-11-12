import agi
import cagi
import Acronyminterpreter
import ai_expander
import Batman
import openai
import re
import sys
import numpy as np

openai.api_key = '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'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.6
    )
    return response.choices[0].text.strip()

class AI_Agent:
    def __init__(self):
        self.actions = ['defend', 'infiltrate']
        self.state = 0

    # Defend the system or infiltrate target
    def act(self):
        if self.state == 0:
            action = random.choice(self.actions)
            if action == 'defend':
                self.state = 1
            elif action == 'infiltrate':
                self.state = 2
            return action
        elif self.state == 1:
            action = 'defend'

class QLearningAgent:
    def __init__(self, num_actions, alpha=0.5, gamma=0.9, epsilon=0.1):
        self.q_table = np.zeros(num_actions)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            action = np.random.choice(len(self.q_table))
        else:
            action = np.argmax(self.q_table)
        return action

    def update_q_table(self, action, reward):
        self.q_table[action] = (1 - self.alpha) * self.q_table[action] + \
                               self.alpha * (reward + self.gamma * np.max(self.q_table))

def train_Q_learning(agent, num_episodes, get_next_state_reward):
    for episode in range(num_episodes):
        state = np.random.randint(0, len(agent.q_table))
        while True:
            action = agent.choose_action(state)
            next_state, reward, done = get_next_state_reward(state, action)
            agent.update_q_table(action, reward)
            state = next_state
            if done:
                break

def get_next_state_reward(state, action):
    # Replace this with your environment logic
    next_state = state + 1
    reward = action * 2
    done = state >= 9
    return next_state, reward, done

if __name__ == "__main__":
    num_actions = 5  # Placeholder for the number of discrete actions
    q_learning_agent = QLearningAgent(num_actions)

    num_episodes = 1000  # Adjust as needed
    #train_Q_learning(q_learning_agent, num_episodes, get_next_state_reward)

    # The Q-table has been updated after training
    print("Updated Q-table:")
    print(q_learning_agent.q_table)

class Bot:
    def __init__(self):
        self.training_data = []

    def collect_data(self, data):
        self.training_data.append(data)

    def write_data_to_file(self, filename):
        with open(filename, 'w') as f:
            for data in self.training_data:
                f.write(f"{data}\n")

    def chat(self, user_input):
        prompt = f"You: {user_input}\nBATMAN_AI:"
        bot_response = generate_response(prompt)

        # Include the bot's response in the training data for self-learning
        self.collect_data(f"{prompt}\n{bot_response}")

        print(f"BATMAN_AI: {bot_response}")


def main():
    bot = Bot()

    print("Welcome to the bot training interface!")
    while True:
        print("\n1. Add training data")
        print("2. Write training data to file")
        print("3. Chat")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the training data: ")
            bot.collect_data(data)
        elif choice == '2':
            filename = input("Enter the filename: ")
            bot.write_data_to_file(filename)
            print(f"Training data written to {filename}")
        elif choice == '3':
            # Enter chat mode
            while True:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    break
                bot.chat(user_input)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def command_processor(command):
    #check if command is a valid command
    if re.search(r'^[a-zA-Z]+\s[a-zA-Z]+$', command):
        #split command into two parts
        cmd_parts = command.split(' ')
        #process command
        if cmd_parts[0] == 'greet':
            print('Hello!')
        elif cmd_parts[0] == 'exit':
            sys.exit()
        else:
            print('Command not recognized.')

def q_learning_agent():

    class QLearningAgent:
        def __init__(self, states, actions, alpha=0.5, gamma=0.9, epsilon=0.1):
            self.states = states
            self.actions = actions
            self.q_table = np.zeros((states, actions))
            self.alpha = alpha
            self.gamma = gamma
            self.epsilon = epsilon

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            action = np.argmax(self.q_table[state, :])
        return action

    def update_q_table(self, state, action, reward, next_state):
        predict = self.q_table[state, action]
        target = reward + self.gamma * np.max(self.q_table[next_state, :])
        self.q_table[state, action] = self.q_table[state, action] + self.alpha * (target - predict)


