from hexapawn import*
from blackWhiteOperators import*

#search for all the states for the white player and create hexapawn object and return the states
def whiteState(white, game):
    states = []
    length = len(white)
    for i in range(length):
        right = whiteDiagonalR(game, white[i][0], white[i][1])
        left = whiteDiagonalL(game, white[i][0], white[i][1])
        down = whiteDown(game, white[i][0], white[i][1])

        if(right):
            hexRight = hexapawnInit(right, game.size, game.wb, game.depth)
            hexRight.current = "b"
            states.append(hexRight)
        if(left):
            hexLeft = hexapawnInit(left, game.size, game.wb, game.depth)
            hexLeft.current = "b"
            states.append(hexLeft)
        if(down):
            hexDown = hexapawnInit(down, game.size, game.wb, game.depth)
            hexDown.current = "b"
            states.append(hexDown)
    if(states == []):
        if(game.current == game.wb):
            game.score = int(game.size * (-5))
        else:
            game.score = int(game.size * 5)
    return states

#search for all the states for the black player and create hexapawn object and return the states
def blackState(black, game):
    states = []
    length = len(black)
    for i in range(length):
        right = blackDiagonalR(game, black[i][0], black[i][1])
        left = blackDiagonalL(game, black[i][0], black[i][1])
        up = blackUp(game, black[i][0], black[i][1])

        if(right):
            hexRight = hexapawnInit(right, game.size, game.wb, game.depth)
            hexRight.current = "w"
            states.append(hexRight)
        if(left):
            hexLeft = hexapawnInit(left, game.size, game.wb, game.depth)
            hexLeft.current = "w"
            states.append(hexLeft)
        if(up):
            hexUp = hexapawnInit(up, game.size, game.wb, game.depth)
            hexUp.current = "w"
            states.append(hexUp)
    if(states == []):
        if(game.current == game.wb):
            game.score = int(game.size * (-5))
        else:
            game.score = int(game.size * 5)
    return states

#find all white and black pieces on the board
def whiteBlack(game, toFind):
    board = game.board.copy()
    boardSize = game.size
    white= []
    black= []

    for i in range(boardSize):
        for j in range(boardSize):
            if(board[i][j] == "w"):
                white.append((j,i))
            if(board[i][j] == "b"):
                black.append((j,i))
    if(toFind == "white"):
        return white
    elif(toFind == "black"):
        return black
    else:
        return None
    

def generateMoves(game):
    if(game.current == "w"):
        white = whiteBlack(game, 'white')
        states = whiteState(white, game)
    else:
        black = whiteBlack(game, "black")
        states = blackState(black, game)
    return states
