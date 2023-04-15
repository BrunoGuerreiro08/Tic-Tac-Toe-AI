import sys
from TicTacToeAI import randomAITurnPlay, winBlockMovesAITurnPlay, winMoveAITurnPlay, minMaxAITurnPlay
from TicTacToe_engine import *

def main():
    board = newBoard()
    player = ['X', 'O']
    turn_count = 0
    game_end = False

    args = sys.argv[1:]

    if len(args) == 0:
        player1 = 'minMaxAI'
        player2 = 'minMaxAI'
        play_game = True
    elif args[0] == '-help':
        # Show help text 
        pass
    elif args[0] == '-players' and len(args) == 3:
        player1 = args[1]
        player2 = args[2]
        play_game = True

    
    if play_game:
        while game_end == False:

            render(board)
            turn_player = player[turn_count % 2]

            if(turn_count % 2 == 0):
                board = eval(player1 + 'TurnPlay'+'(board, turn_player)')
            else:
                board = eval(player2 + 'TurnPlay'+'(board, turn_player)')

            turn_count += 1

            if checkWinners(board) != False:
                render(board)
                print(f'Congratulations {turn_player}, you won!')
                break
            elif turn_count == 9:
                render(board)
                print("It's a draw!")
                break

if __name__ == '__main__':
    main()