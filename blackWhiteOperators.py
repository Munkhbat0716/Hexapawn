
#function to move the white down and check boundaries and return the changed board
def whiteDown(game, x, y):
    board = (game.board).copy()

    #check if you are on white
    if(board[y][x] != "w"):
        return None
    #check if you are out of range
    if((y+1) >= game.size):
        return print("Out of range")
    #check possible down moves on white
    if(board[y+1][x] == "-"):
        #change the current position to a dash and move the white
        dash = list(board[y])
        dash[x] = "-"

        #move white down
        moveChar = list(board[y + 1])
        moveChar[x] = "w"
        
        whiteString = "".join(moveChar)
        dashString = "".join(dash)
        #replace it on the board
        board[y] = dashString
        board[y + 1] = whiteString
    else:
        return None
    return board

#here you move the white piece diagonally to take out a black piece
def whiteDiagonalR(game, x, y):
    board = (game.board).copy()
    # check if current piece is white 
    if (board[y][x] != 'w'):
        return None
    # check if right diagonal is in range
    if((x + 1) >= game.size) or ((y + 1) >= game.size):
        return None
    # check if right diagonal is black
    if(board[y + 1][x + 1] == 'b'):
        dash = list(board[y])
        dash[x] = '-'
        white = list(board[y + 1])
        white[x + 1] = 'w'
        dashString = ''.join(dash)
        whiteString = ''.join(white)
        board[y] = dashString
        board[y + 1] = whiteString
        return board
    else: 
        return None

#Same as diagonal right but just go left
def whiteDiagonalL(game, x, y):
    board = (game.board).copy()
    # check if current piece is white 
    if (board[y][x] != 'w'):
        return None
    # check if left diagonal is in range
    if((x - 1) < 0) or ((y + 1) >= game.size):
        return None
    # check if right diagonal is black
    if(board[y + 1][x - 1] == 'b'):
        dash = list(board[y])
        dash[x] = '-'
        changeToWhite = list(board[y + 1])
        changeToWhite[x - 1] = 'w'
        dashString = ''.join(dash)
        whiteString = ''.join(changeToWhite)
        board[y] = dashString
        board[y + 1] = whiteString
        return board
    else: 
        return None

#have the black piece move up and do the same thing as white but the opposite
def blackUp(game, x, y):
    board = (game.board).copy()
    # check that position is b
    if(board[y][x] != 'b'):
        return None
    # check if out of range
    if ((y - 1) < 0):
        return None
    # check if move possible
    if (board[y - 1][x] == '-'):
        # change current position to '-'
        dash = list(board[y]) 
        dash[x]= '-'
        # 'move' white down
        char = list(board[y - 1])
        char[x] = 'b'
        charString = ''.join(char)
        dashString = ''.join(dash)
        board[y] = dashString
        board[y - 1] = charString
    else:
        return None
    return board

#move the black diagonally to the right
def blackDiagonalR(game, x, y):
    board = (game.board).copy()
    # check if  piece is black
    if (board[y][x] != 'b'):
        return None
    # check if right diagonal is in range
    if ((x + 1) >= game.size) or ((y - 1) < 0):
        return None
    # check if right diagonal is w
    if (board[y - 1][x + 1] == 'w'):
        dash = list(board[y])
        dash[x] = '-'
        changeToWhite = list(board[y - 1])
        changeToWhite[x + 1] = 'b'
        dashString = ''.join(dash)
        whiteString = ''.join(changeToWhite)
        board[y] = dashString
        board[y - 1] = whiteString
        return board
    else:
        return None

#move the black diagonally to the left
def blackDiagonalL(game, x, y):
    board = (game.board).copy()
    # check if  piece is black
    if (board[y][x] != 'b'):
        return None
    # check if right diagonal is in range
    if ((x + 1) >= game.size) or ((y + 1) < 0):
        return None
    # check if right diagonal is w
    if (board[y - 1][x - 1] == 'w'):
        dash = list(board[y])
        dash[x] = '-'
        changeToWhite = list(board[y - 1])
        changeToWhite[x - 1] = 'b'
        dashString = ''.join(dash)
        whiteString = ''.join(changeToWhite)
        board[y] = dashString
        board[y - 1] = whiteString
        return board
    else:
        return None
