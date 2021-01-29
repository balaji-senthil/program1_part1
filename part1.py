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
    r=int(currentPosition[0])
    c=int(currentPosition[1])
    x=r
    y=c
    possibleMovesArray=[]
    #print(myBoard[r][c]) - checking unpacking of the set to the myBoard
    # print(len(myBoard))
    while(1):
        if(x+1<len(myBoard), y+1<len(myBoard)):
            possibleMovesArray.append((x+1,y+1))
        break
    print(possibleMovesArray)



    

    

#testing output
myBoard=loadBoard('board.txt')
printBoard(myBoard)
pos=(0,0)#get user input
possibleMoves(pos,myBoard)

