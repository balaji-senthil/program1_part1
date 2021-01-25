# print('Checking file output...')
def loadBoard(board):
    inputFile = open(board, 'r')
    myBoard = []
    for row in inputFile:
        myBoard.append(row.split())
    return myBoard


def printBoard(myBoard):
    for row in myBoard:
        print (" ".join(map(str,row)))


# def possibleMoves(currentPosition,myBoard):
#     for i 

#testing output
myBoard=loadBoard('board.txt')
printBoard(myBoard)
pos=(0,0)

