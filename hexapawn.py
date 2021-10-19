#ECS170 Munkhbat Munkhtulga
#Hexapawn

#This program takes in input board, size, players, search depth and score
#I believe the score is the positive or negative number that returns when
#the program is finished running through the MiniMax algorithm

from movement import*
from blackWhiteOperators import*

#class to use for miniMax algorithm and this creates a tree with parent and children
class miniMax(object):
    def __init__(self, game):
        self.game = game
        self.level = None
        self.parent = None
        self.children = []
        
        
    #adding a leaf node to the miniMax tree
    def addNode(self, node):
        self.children.append(node)
        node.parent = self

    #setting to figure the min or the max
    def minOrMax(self):
        if(self.parent):
            if(self.parent.level == "MAX"):
                self.level = "MIN"
            else:
                self.level = "MAX"
        else:
            self.level = "MAX"

#creating a class that sets the player wb (white or black), size of the board
#depth of the miniMax, and the score that you output.
class hexapawnInit(object):
    def __init__(self, board, size, wb, depth):
        self.board = board
        self.size = size
        self.wb = wb
        self.depth = depth
        self.score = self. staticEvaluation()
        self.current = wb
        self.depthLevel = 0
        
    def printGame(self):
        print("Color: " , self.current)
        for i in range(self.size):
            print(self.board[i])
        print("Score: ", self.score)

    #this sets the score for white and blacl
    #if its positive then white wins and if its negative then black wins
    def staticEvaluation(self):
        wLose = False
        bLose = False
        firstRow = list(self.board[0])
        lastRow = list(self.board[self.size - 1])

        for i in range(self.size):
            if firstRow[i] == "b":
                wLose = True #means that black reached the other side and won
            if lastRow[i] == "w":
                bLose = True #white is on the other side and won

        #calculate the score, loop thru the board and count how many pieces
        #there are and add 1 point
        black = 0
        white = 0
        blackClear = 0
        whiteClear = 0
        
        for i in range(self.size):
            for j in range(self.size):
                if(self.board[i][j] == "b"):
                    black = black + 1
                    clear = True
                    for k in range(0, i):
                        if(self.board[k][j] != "-"):
                            clear = False
                    if(clear == True):
                        blackClear = blackClear + 1
                if(self.board[i][j] == "w"):
                    white = white + 1
                    clear = True
                    for k in range(i + 1, self.size):
                        if(self.board[k][j] != "-"):
                            clear = False
                    if(clear):
                            whiteClear = whiteClear + 1

        #set the score after calculating above
        if(self.wb == "w"):
            if(wLose):
                self.score = int(self.size * (-5))
            elif(bLose):
                self.score = int(self.size * 5)
            else:
                self.score = int(whiteClear - blackClear) + int(white - black)
        else:
            if(bLose):
                self.score = int(self.size * (-5))
            elif(wLose):
                self.score = int(self.size * 5)
            else:
                self.score = int(whiteClear - blackClear) + int(white - black)
        return self.score

   
#Calling the hexapawn program to run the algorithm
def hexapawn(board, size, wb, depth): 
    startGame = hexapawnInit(board, size, wb, depth)
    head = miniMax(startGame)
    head.minOrMax()
    hNode = createTree(head)
    bestChoice = minMaxSearch(hNode, depth)

    if(bestChoice):
        return bestChoice.game.board
    else:
        return(startGame.board)

#function to create a tree with all possible children
def createTree(head):
    if(head.game.depth > 0):
        level = generateMoves(head.game)
        length = len(level)
        for i in range(length):
            nextRow = miniMax(level[i])
            head.addNode(nextRow)
            nextRow.minOrMax()
            nextRow.game.depth = head.game.depth - 1
            nextRow.game.depthLevel = head.game.depthLevel + 1
        length2 = len(head.children)
        for j in range(length2):
            createTree(head.children[j])
    else:
        return None
    return head
            

#MiniMax algorithm uses the tree created above and recursively calls itself until the last row
def minMaxSearch(head, lookAhead):
    #check if the head is not 0 then call minMax
    if(head.game.depthLevel < lookAhead - 1):
        if(head.children != []):
            for i in range(len(head.children)):
                if(head.children[i].game.score == int(head.children[i].game.size) * (-5)):
                    break
                if(head.children[i].game.score == int(head.children[i].game.size) * (5)):
                    break
                minMaxSearch(head.children[i], lookAhead)
        else: #return nothing if there are no possible states
            return 
    if(head.level == "MAX"):
        maxScore = head.game.size * (-5)
        maxGame = head.children[0]
        for i in range(len(head.children)):
            if(head.children[i].game.score > maxScore):
                maxGame = head.children[i]
                maxScore = head.children[i].game.score
        head.game.score = maxGame.game.score
        #clearing the children list after finished searching
        head.children.clear()
        return maxGame
    elif(head.level == "MIN"):
        minScore = head.game.size*(5)
        minGame = head.children[0]
        for i in range(len(head.children)):
            if(head.children[i].game.score < minScore):
                minGame = head.children[i]
                minScore = head.children[i].game.score
        head.game.score = minGame.game.score
        #clearing the children list after finished searching
        head.children.clear() 
        return minGame
