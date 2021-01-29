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
    # print('****'+myBoard[2][3])
   
    
def possibleMoves(currentPosition,myBoard):
    x=int(currentPosition[0])
    y=int(currentPosition[1])
    possibleMovesArray=[]
    limit=len(myBoard)
    if(x+1<limit and y<limit):#left to right
        possibleMovesArray.append((x+1,y))
    if(x<limit and y+1<limit):#Top down
        possibleMovesArray.append((x,y+1))
    if(x+1<limit and y+1<limit):#diagonal 1
        possibleMovesArray.append((x+1,y+1))
    if(x+1<limit and ((y-1<limit)and y-1>=0)):#diagonal 2
        possibleMovesArray.append((x+1,y-1))
    if(((x-1<limit)and x-1>=0) and ((y-1<limit)and y-1>=0)):#diagonal 3
        possibleMovesArray.append((x-1,y-1))
    if(((x-1<limit)and x-1>=0) and (y+1<limit)):#diagonal 4
        possibleMovesArray.append((x-1,y+1))
    if(((x-1<limit)and x-1>=0) and y<limit):#right to left
        possibleMovesArray.append((x-1,y))
    if(x<limit and ((y-1<limit)and y-1>=0)):#Bottom Up
        possibleMovesArray.append((x,y-1))
    return possibleMovesArray

    
#testing output of part1
myBoard=loadBoard('board.txt')
printBoard(myBoard)
pos=(2,2)#get user input
print(possibleMoves(pos,myBoard))




