# Game engine fuctions
def newBoard():   
    return([[None, None, None],
            [None, None, None],
            [None, None, None]])


def render(board):   
    print(' | 0 | 1 | 2 |')
    print(' -------------')
    for i in range(0,3):
        print(f'{i}|', end = '')

        for j in range(0,3):
            if((board[i][j]) == None):
                print(f'   ', end = '|')        
            else:
                print(f' {board[i][j]} ', end = '|')

        print("")
        
    print(' -------------\n')


def getWinLines():
    return [[(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)]]


def getMove():
    while True:
        move_opt = input('Insert the move coordinates: ')

        if int(move_opt) not in range(0,9):
            print('Invalid move, try again!')
        else:
            break

    match int(move_opt):
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


def makeMove(board, move_coord, player):
    updated_board = board
    updated_board[move_coord[0]][move_coord[1]] = player

    return updated_board


def validateMove(board, move_coord):
    if board[move_coord[0]][move_coord[1]] != None:
        return False
    else:
        return True

                                                                  
def checkWinners(board):
    win_lines = getWinLines()

    count = 0
    for line in win_lines:
        aux = [None, None, None]
        for i in range(0,3):
            candidate_line = line[i]
            aux[i] = board[candidate_line[0]][candidate_line[1]]
        
        win_lines[count] = aux
        count = count + 1
    
    for line in win_lines:
        if len(set(line)) == 1 and line[0] != None:
            return line[0]
    
    return False


def getOpponent(turn_player):
    match turn_player:
        case 'X':
            return 'O'
        case 'O':
            return 'X'

# Human turn functions
def humanTurnPlay(board, turn_player):    
    while True:
        move_coord = getMove()

        if validateMove(board, move_coord):
            break
        else:
            print('Position already taken, try again!')
    
    updated_board = makeMove(board, move_coord, turn_player)
    
    return updated_board