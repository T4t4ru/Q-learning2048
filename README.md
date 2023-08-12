# Q-Learning using TPU to solve the 2048 game

This project demonstrates the application of the Q-Learning algorithm to solve the 2048 game. Q-Learning is a reinforcement learning method that allows an agent to learn how to make optimal decisions in an unknown environment. In this case, we use TPU (Tensor Processing Unit) to speed up learning and improve performance.

## How it works

1. **Initialization of the Q-table**: We create a 16x4 Q-table to store the estimates of actions in each state of the game board.

2. **Action Selection**: To select an action, the agent can either explore new actions with some probability, or select the action with the highest Q score from the Q-table.

3. **Training using TPU**: We use TPU to speed up the learning process. The `train_q_learning` function calculates the target value of Q and applies gradient descent to update the Q-table.

4. **Gameplay**: We train the agent over several episodes, in each of which the agent interacts with the game, choosing actions and updating the Q-table based on the rewards received.

5. **The process of playing with a trained Q-table**: After training, we can use the trained Q-table to play 2048. The agent will choose the actions with the highest Q score to achieve the best result.

## Dependencies

To run this project, the following dependencies must be present:

- NumPy
- TensorFlow

## How to use

1. Upload the code to your development environment.

2. Make sure you have access to the TPU. Note: This step may require configuration in your environment.

3. Run the code to train the agent. This may take some time depending on the number of episodes.

4. After completing the training, the code uses a trained Q-table to play 2048 and outputs the minimum number of moves required to win.

## Conclusion

This project shows how the Q-Learning algorithm can be applied using TPU to solve the 2048 game. The project can be expanded and improved, for example, by adjusting hyperparameters or using more complex action selection strategies.
