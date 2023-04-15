from TicTacToe_engine import makeMove, checkWinners, getOpponent, validateMove, render
from TicTacToeAI import minMaxAITurnPlay, minMaxAI
import copy

board = [['X', 'X', None],
         ['O', None, None],
         [None, 'O', None]]

b1 =     [['X', 'X', 'O'],
         ['O', None, None],
         [None, 'O', None]]

b2 =     [['X', 'X', 'O'],
          ['O', 'X', None],
          [None, 'O', None]]

print(minMaxAI(b2, 'O'))
