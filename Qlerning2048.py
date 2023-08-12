import numpy as np
import random
import tensorflow as tf
import os

q_table = np.zeros((16, 4))  


initial_board = initialize_board()

learning_rate = 0.1
discount_factor = 0.9
exploration_prob = 0.2


resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='grpc://' + os.environ['COLAB_TPU_ADDR'])
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
strategy = tf.distribute.experimental.TPUStrategy(resolver)


def choose_action(state):
    if random.random() < exploration_prob:
        return random.randint(0, 3) 
    return np.argmax(q_table[state])  

@tf.function
def train_q_learning(state, action, new_state, reward):
    with tf.device('/TPU:0'):
        q_target = reward + discount_factor * tf.reduce_max(q_table[new_state])
        with tf.GradientTape() as tape:
            q_predicted = q_table[state][action]
            loss = tf.square(q_target - q_predicted)
        gradients = tape.gradient(loss, [q_table])
        q_table[state][action].assign_sub(learning_rate * gradients[0][state][action])


for episode in range(1000000):  
    state = get_state_representation(initial_board)  
    done = False
    
    while not done:
        action = choose_action(state)
        new_board = perform_action(copy.deepcopy(state), action)  #
        new_state = get_state_representation(new_board) 
        
        reward = calculate_reward(new_board)  
        
        # Обучение Q-learning с использованием TPU
        train_q_learning(state, action, new_state, reward)
        
        state = new_state
        done = check_game_over(new_board)
        

state = get_state_representation(initial_board)
num_moves = 0

while not check_game_over(state):
    action = np.argmax(q_table[state])
    new_board = perform_action(copy.deepcopy(state), action)
    state = get_state_representation(new_board)
    num_moves += 1

print(f"Min to Win: {num_moves}")
