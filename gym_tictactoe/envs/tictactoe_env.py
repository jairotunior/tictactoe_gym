import gym
import gym.spaces
import numpy as np
from gym.utils import seeding

class TicTacToeEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self):
        """
        The board game is a numpy array of 3 x 3

        [[0 0 0]
        [0 0 0]
        [0 0 0]]

        Player X is use the number 1 and player O use the number 2

        """
        self.board = np.full((3, 3), 0)
        # Number of the player turn. Always start the player X
        self.turn = 1
        self.action_space = gym.spaces.Discrete(n = self.board.size)
        self.remain_moves = 9

    @property
    def legal_actions(self):
        legal_actions = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 0:
                    legal_actions.append((i,j))

        return legal_actions

    def end_game(self, player):
        # Check diagonals
        diagonal = [[self.board[0,0], self.board[1,1], self.board[2,2]],
                          [self.board[2, 0], self.board[1, 1], self.board[0, 2]]]

        for i in range(2):
            count_diagonal = np.unique(diagonal[i])
            if len(count_diagonal) == 1 and count_diagonal[0] != 0:
                return True

        # Check rows and columns
        for i in range(self.board.shape[0]):
            count_row = np.unique(self.board[i,])
            if len(count_row) == 1 and count_row[0] != 0:
                return True

        transpose = self.board.transpose()
        for i in range(self.board.shape[0]):
            count_col = np.unique(transpose[i,])
            if len(count_col) == 1 and count_col[0] != 0:
                return True

        return False


    def step(self, action):
        done = False
        if self.turn == 1:
            self.board[action] = 1
            done = self.end_game(self.turn)
            self.turn = 2
        elif self.turn == 2:
            self.board[action] = 2
            done = self.end_game(self.turn)
            self.turn = 1

        self.remain_moves -= 1

        if self.remain_moves == 0:
            done = True

        reward = 0
        info = "Info"


        return [self.board, self.turn], reward, done, info

    def render(self, mode='human'):
        print(self.board)

    def reset(self):
        self.board = np.full((3, 3), 0)
        self.turn = 1

        return [self.board, self.turn]

    def close(self):
        pass

    def seed(self, seed=None):
        self.np_random, seed1 = seeding.np_random(seed)
        seed2 = seeding.hash_seed(seed1 + 1) % 2 ** 31
        return [seed1, seed2]