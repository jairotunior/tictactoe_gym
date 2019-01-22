import gym
import gym_tictactoe
import numpy as np


env = gym.make('TicTacToe-v0')

state = env.reset()

print("Initial State")
env.render()


array = np.array([1,2,3,4,5,6,7,8,9,0])

print(array[::-1])
print(array[5:])


done = False

while not done:

    action = np.random.choice(len(env.legal_actions), 1)
    print("Move Player {} - Action: {}".format(env.turn, env.legal_actions[action[0]]))

    next_state, reward, done, _ = env.step(env.legal_actions[action[0]])

    env.render()

    state = next_state

    if done:
        pass

