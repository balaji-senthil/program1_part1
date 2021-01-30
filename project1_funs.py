'''
    Programming Assignment 1 - Part1
    Submitted by Balaji Senthilkumar
'''
#The funtion to load the board (.txt to 2Dlist/array)
def loadBoard(board):
    inputFile = open(board, 'r')
    myBoard = []
    for row in inputFile:
        myBoard.append(row.split())
    return myBoard


#THE FUNCTION TO PRINT 'myBoard'
def printBoard(myBoard): 
    for row in myBoard:
        print (" ".join(map(str,row)))
    # print('****'+myBoard[2][3])
   
    
def possibleMoves(currentPosition,myBoard):
    #So here I have used a graph based approach, for figuring out the solution,
    #  using x_co_ordinates and y_co_oridinates as the positional arguments.
    
    x_co_ordinate,y_co_ordinate = currentPosition #spreading operation 
    
    possibleMovesArray=[]
    
    limit=len(myBoard) # ensuring that the program does not cause an outOfBounds or any negative array positioning
    
    if(x_co_ordinate+1<limit and y_co_ordinate<limit): #left to right
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate))
    
    if(x_co_ordinate<limit and y_co_ordinate+1<limit): #Top-Bottom
        possibleMovesArray.append((x_co_ordinate,y_co_ordinate+1))
    
    if(x_co_ordinate+1<limit and y_co_ordinate+1<limit): #diagonal 1
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate+1))
    
    if(x_co_ordinate+1<limit and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)): #diagonal 2
        possibleMovesArray.append((x_co_ordinate+1,y_co_ordinate-1))
    
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)): #diagonal 3
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate-1))
    
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and (y_co_ordinate+1<limit)): #diagonal 4
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate+1))
    
    if(((x_co_ordinate-1<limit)and x_co_ordinate-1>=0) and y_co_ordinate<limit): #right to left
        possibleMovesArray.append((x_co_ordinate-1,y_co_ordinate))
    
    if(x_co_ordinate<limit and ((y_co_ordinate-1<limit)and y_co_ordinate-1>=0)): #Bottom Up
        possibleMovesArray.append((x_co_ordinate,y_co_ordinate-1))
    print(set(possibleMovesArray))
    return(possibleMovesArray)
    


def legalMoves(possibleMovesArg,pathArg):
    legalMovesArray=[]          #creating a list to store the legal moving positions(co_ordinates)
    for pos in possibleMovesArg:    
        if pos not in legalMovesArray:  #checking for non-repetion of positions, to comply the rules of the game
            legalMovesArray.append(pos) 
    return legalMovesArray
   

def examineState(myBoard,currentPosition,path,myDict):
    wordList = []
    for i in path:
        x_co_ordinate, y_co_ordinate = i    #spreading x_co_ordinate and y_co_ordinate out of the path 
        wordList.append(myBoard[x_co_ordinate][y_co_ordinate])
    x_co_ordinate, y_co_ordinate = currentPosition 
    wordList.append(myBoard[x_co_ordinate][y_co_ordinate])
    finalList = ''.join([str(i) for i in wordList])
    # print(finalList)
    if finalList.lower() in myDict: #Checking whether the word is in the given dicionary
        outputTuple=(finalList.lower(),'Yes')
        print(outputTuple)
    else:
        outputTuple=(finalList.lower(),'No')
        print(outputTuple)
