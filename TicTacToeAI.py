import copy
import random
from TicTacToe_engine import getWinLines, makeMove, validateMove, checkWinners, getOpponent, render


def convertMoveOpt(move_opt):
    match move_opt:
        case 0:
            return (0,0)
        case 1:
            return((0,1))
        case 2:
            return((0,2))
        case 3:
            return((1,0))
        case 4:
            return((1,1))
        case 5:
            return((1,2))
        case 6:
            return((2,0))
        case 7:
            return((2,1))
        case 8:
            return((2,2))


def findValidMoves(board):
    valid_moves = []

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == None:
                valid_moves.append((i + j) + 2 * i)
    
    return valid_moves


def checkBlockMoves(board, turn_player, valid_moves):
    win_lines = getWinLines()
    block_lines = []

    for line in win_lines:
        aux = line
        for i in range(0,3):
            candidate_line = line[i]
            if board[candidate_line[0]][candidate_line[1]] != None:
                aux[i] = board[candidate_line[0]][candidate_line[1]]               
            else:
                aux[i] = win_lines[candidate_line[0]][candidate_line[1]]
                
        block_lines.append(aux)

    for line in win_lines:
        if list(map(type,line)).count(tuple) == 1 and line.count(turn_player) == 0:
            for i in range(0,3):
                if isinstance(line[i], tuple):
                    x = line[i][slice(0,1)]
                    x = x[0]
                    y = line[i][slice(1,2)]    
                    y = y[0]
                    if valid_moves.count((x + y) + 2 * x) > 0:
                        move_opt = (x + y) + 2 * x
                        return True, move_opt
        
    return False, -1
    
    
def checkWinMoves(board, turn_player, valid_moves):
    win_lines = getWinLines()
    aux_lines = []

    for line in win_lines:
        aux = line
        for i in range(0,3):
            candidate_line = line[i]
            if board[candidate_line[0]][candidate_line[1]] != None:
                aux[i] = board[candidate_line[0]][candidate_line[1]]
            else:
                aux[i] = win_lines[candidate_line[0]][candidate_line[1]]       
        
        aux_lines.append(aux)

    for line in aux_lines:
        if list(map(type,line)).count(tuple) == 1 and line.count(turn_player) == 2:
            for i in range(0,3):
                if isinstance(line[i], tuple):
                    x = line[i][slice(0,1)]
                    x = x[0]
                    y = line[i][slice(1,2)]    
                    y = y[0]
                    if valid_moves.count((x + y) + 2 * x) > 0:
                        move_opt = (x + y) + 2 * x
                        return True, move_opt
        
    return False, -1


def randomAI(board, turn_player):
    valid_moves = findValidMoves(board)

    if len(valid_moves) == 1:
        move_opt = valid_moves[0]
    else:
        move_opt = valid_moves[random.randrange(0, len(valid_moves) - 1)]
    
    return convertMoveOpt(move_opt)


def winMovesAI(board, turn_player):
    valid_moves = findValidMoves(board)

    winner_moves, move_opt = checkWinMoves(board, turn_player, valid_moves)
    if winner_moves:
        #print(f'win move {turn_player} {move_opt}')
        return convertMoveOpt(move_opt)
    else:
        if len(valid_moves) == 1:
            move_opt = valid_moves[0]
        else:
            move_opt = valid_moves[random.randrange(0, len(valid_moves) - 1)]
    #print(f'rnd move {turn_player} {move_opt}')
    return convertMoveOpt(move_opt)


def winBlockMovesAI(board, turn_player): 
    valid_moves = findValidMoves(board)

    found_move, move_opt = checkWinMoves(board, turn_player, valid_moves)
    
    if found_move:
        #print(f'win move {turn_player} {move_opt}')
        return convertMoveOpt(move_opt)
    
    found_move, move_opt = checkBlockMoves(board, turn_player, valid_moves)

    if found_move:
        #print(f'block move {turn_player} {move_opt}')
        return convertMoveOpt(move_opt)
    
    if len(valid_moves) == 1:
        move_opt = valid_moves[0]
    else:
        move_opt = valid_moves[random.randrange(0, len(valid_moves) - 1)]
        #print(f'rnd move {turn_player} {move_opt}')
    return convertMoveOpt(move_opt)


def calculateScore(board, turn_player, wish_to_win):
    winner = checkWinners(board)

    if winner != False:
        if winner == wish_to_win:
            return 10
        else:
            return -10
    elif len(findValidMoves(board)) == 0:
        return 0

    valid_moves = findValidMoves(board)

    scores = []

    for move in valid_moves:
        new_board = copy.deepcopy(board)
        new_board = makeMove(new_board, convertMoveOpt(move), turn_player)
        #print(f'next move by {turn_player} = {move}')
        #render(new_board)
        next_player = getOpponent(turn_player)
        next_player_resp_score = calculateScore(new_board, next_player, wish_to_win)

        scores.append(next_player_resp_score)
    #print(scores)
    if turn_player == wish_to_win:
        return max(scores)
    else:
        return min(scores)


# AI turn functions
def randomAITurnPlay(board, turn_player):
    while True:
        move_coord = randomAI(board, turn_player)

        if validateMove(board, move_coord):
            break
        else:
            print('Position already taken, try again!')
    
    updated_board = makeMove(board, move_coord, turn_player)
    
    return updated_board
    
    
def winMoveAITurnPlay(board, turn_player):
    while True:
        move_coord = winMovesAI(board, turn_player)

        if validateMove(board, move_coord):
            break
        else:
            print('Position already taken, try again!')
    
    updated_board = makeMove(board, move_coord, turn_player)
    
    return updated_board


def winBlockMovesAITurnPlay(board, turn_player):
    while True:
        move_coord = winBlockMovesAI(board, turn_player)

        if validateMove(board, move_coord):
            break
        else:
            print('Position already taken, try again!')
    updated_board = makeMove(board, move_coord, turn_player)
    
    return updated_board


def minMaxAITurnPlay(board, turn_player):
    while True:
        move_coord = minMaxAI(board, turn_player)

        if validateMove(board, move_coord):
            break
        else:
            print('Position already taken, try again!')

    updated_board = makeMove(board, move_coord, turn_player)
    
    return updated_board


def minMaxAI(board, turn_player):
    move_opt = highest_value = None

    for move in findValidMoves(board):
        new_board = copy.deepcopy(board)
        new_board = makeMove(new_board, convertMoveOpt(move), turn_player)
        #print(f'my move = {move}')
        #print('next cenario:')
        #render(new_board)
        opponent_player = getOpponent(turn_player)
        value = calculateScore(new_board, opponent_player, turn_player)

        if highest_value == None or highest_value < value:
            move_opt = move
            highest_value = value
    
    return convertMoveOpt(move_opt)