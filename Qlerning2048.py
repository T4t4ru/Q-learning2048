import numpy as np
import random
import tensorflow as tf
import os

class QLearningAgent:
    def __init__(self, num_states, num_actions, learning_rate, discount_factor, exploration_prob):
        self.q_table = np.zeros((num_states, num_actions))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob

    def choose_action(self, state):
        if random.random() < self.exploration_prob:
            return random.randint(0, 3)
        return np.argmax(self.q_table[state])

    @tf.function
    def train_q_learning(self, state, action, new_state, reward):
        q_target = reward + self.discount_factor * tf.reduce_max(self.q_table[new_state])
        with tf.GradientTape() as tape:
            q_predicted = self.q_table[state][action]
            loss = tf.square(q_target - q_predicted)
        gradients = tape.gradient(loss, [self.q_table])
        self.q_table[state][action].assign_sub(self.learning_rate * gradients[0][state][action])


class BoardGame:
    def __init__(self, initial_board, agent):
        self.initial_board = initial_board
        self.agent = agent

    def play_episodes(self, num_episodes):
        for episode in range(num_episodes):
            state = self.get_state_representation(self.initial_board)
            done = False

            while not done:
                action = self.agent.choose_action(state)
                new_board = self.perform_action(copy.deepcopy(state), action)  
                new_state = self.get_state_representation(new_board)
                reward = self.calculate_reward(new_board)
                self.agent.train_q_learning(state, action, new_state, reward)
                state = new_state
                done = self.check_game_over(new_board)

    def evaluate_agent(self):
        state = self.get_state_representation(self.initial_board)
        num_moves = 0

        while not self.check_game_over(state):
            action = np.argmax(self.agent.q_table[state])
            new_board = self.perform_action(copy.deepcopy(state), action)
            state = self.get_state_representation(new_board)
            num_moves += 1

        print(f"Min to Win: {num_moves}")

num_actions = 4
learning_rate = 0.1
discount_factor = 0.9
exploration_prob = 0.2
num_episodes = 1000000

agent = QLearningAgent(num_states, num_actions, learning_rate, discount_factor, exploration_prob)
game = BoardGame(initial_board, agent)

game.play_episodes(num_episodes)

game.evaluate_agent()
