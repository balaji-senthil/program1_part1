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
    x_co_ordinate=int(currentPosition[0])
    y_co_ordinate=int(currentPosition[1])
    possibleMovesArray=[]
    limit=len(myBoard)
    if(x_co_ordinate+1<limit and y_co_ordinate<limit):#left to right
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate))
    if(x_co_ordinate<limit and y_co_ordinate+1<limit):#Top-Bottom
        possibleMovesArray.append((x_co_ordinate,y_co_ordinate+1))
    if(x_co_ordinate+1<limit and y_co_ordinate+1<limit):#diagonal 1
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate+1))
    if(x_co_ordinate+1<limit and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)):#diagonal 2
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate-1))
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)):#diagonal 3
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate-1))
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and (y_co_ordinate+1<limit)):#diagonal 4
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate+1))
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and y_co_ordinate<limit):#right to left
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate))
    if(x_co_ordinate<limit and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)):#Bottom Up
        possibleMovesArray.append((x_co_ordinate,y_co_ordinate-1))
    return possibleMovesArray

def legalMoves(posArg,randPos):
    legalMovesArray=[]
    set1=set((possibleMoves(posArg,randPos)))
    set2=set(randPos)
    legalMovesArray.append(set1.difference(set2))
    return legalMovesArray


    
#testing output of part1
myBoard=loadBoard('board.txt')
printBoard(myBoard)
pos=(2,2)#get user input
pm=possibleMoves(pos,myBoard)
print(pm)
# randArg=set({(0,0),(1,1),(2,2),(3,3)})
# legalMoves(pm,randArg)





