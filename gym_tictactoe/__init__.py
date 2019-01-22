from gym.envs.registration import register


# Env registration
# ==========================

register(
    id='TicTacToe-v0',
    entry_point='gym_tictactoe.envs:TicTacToeEnv',
)
