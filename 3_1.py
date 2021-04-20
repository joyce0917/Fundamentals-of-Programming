import math


def isMagicSquare(a):
    # check valid square
    if type(a[0])!=list or len(a)==0 or len(a)!=len(a[0]):return False
    #check integer & repetition
    for row in range (len(a)):
        if len(a[row])!=len(a):return False
        for n in a[row]:
            if a[row].count(n)!=1:return False
        for col in range (len(a)):
            if type(a[row][col])!=int:return False
    #Row sum and Col sum
    (rowSum,col,diagnolSum1,diagnolSum2)=(sum(a[0]),0,0,0)
    while col<len(a):
        colSum=0
        for row in range (len(a)):
            if sum(a[row])!=rowSum:return False
            colSum+=a[row][col]
        col+=1
        if colSum!=rowSum:return False
    #diagnol sum1 
    for row in range (len(a)): diagnolSum1+=a[row][row]
    if diagnolSum1!=rowSum:return False
    #diagnol sum2
    for row in range (len(a)): diagnolSum2+=a[row][len(a)-1-row]
    if diagnolSum2!=rowSum: return False   
    return True



def isKingsTour(board):
    #check valid board
    if validBoard(board)==False:return False
    #find location of 1
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col]==1:
                startpt=(row,col)
    #check if valid move
    (p1,p2)=(startpt,None)
    for i in range (1,len(board)**2+1):
        goal=board[p1[0]][p1[1]]+1
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]==goal:
                    p2=(row,col)
        if p2==None:return False
        if max(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]))!=1 and i!=len(board)**2:
            return False
        p1=p2
    return True

# check if the board is valid
def validBoard(board):
    #2d list
    if len(board)<=1:
        if not board[0]==[1]: return False
    #check repetition and valid numbers
    supposedTotal=0
    for i in range (1,len(board)**2+1):
        supposedTotal+=i
    total=0
    for row in range(len(board)):
        for n in board[row]:
            if board[row].count(n)!=1:return False
        for col in range(len(board)):
            total+=board[row][col]
    if total!=supposedTotal:
        return False
    return True


#check if lists are from 1 to N^2
def areLegalValues(values):
    if math.sqrt(len(values))%1!=0:return False
    N=int(math.sqrt(len(values)))
    if N**2!=len(values) or max(values)>len(values) or min(values)<0: 
        return False
    for i in range(1,N**2+1):
        count=0
        for index in range(len(values)):
            if values[index]==i:
                count+=1
        #check repeating numbers
        if count>1:return False
    return True

#check if row is legal
def isLegalRow(board,row):
    newrow=board[row]
    return areLegalValues(newrow)

#check if column is legal
def isLegalCol(board,col):
    newcol=[]
    for row in range(len(board)):
        newcol.append(board[row][col])
    return areLegalValues(newcol)

#check if block is legal
def isLegalBlock(board, block):
    N=int(math.sqrt(len(board)))
    if block>=len(board):return False
    (startRow,startCol)=(N*(block//N),N*(block%N))
    newblock=[]
    for row in range(startRow,startRow+N):
        for col in range(startCol,startCol+N):
            newblock.append(board[row][col])
    return areLegalValues(newblock)

#check if the whole sudoku is legal
def isLegalSudoku(board):
    for row in range(len(board)):
        if not isLegalRow(board,row):return False
    for col in range(len(board)):
        if not isLegalCol(board,col):return False
    for block in range(len(board)):
        if not isLegalBlock(board,block):return False
    return True

####################################################################
# ignore_rest: The autograder will ignore all code below here
####################################################################

def testMagicSquare():
    print("---Testing testMagicSquare")
    a=[1,2,3,4,5]
    assert(not isMagicSquare(a))
    a=[[2,7,6],[9,5,1],[4,3,8]]
    assert(isMagicSquare(a))
    a=[[3,3,3],[3,3,3],[3,3,3]]
    assert(not isMagicSquare(a))
    print("Passed!!")

def testIsKingsTour():
    print("---Testing testIsKingsTour")
    board = [[3,2,1],[6,4,9],[5,7,8]]
    assert(isKingsTour(board))
    board = [[3,2,1],[6,4,0],[5,7,8]]
    assert(not isKingsTour(board))
    board = [[1,2,3],[7,4,8],[6,5,9]]
    assert(not isKingsTour(board))
    print("Passed!!")

def testIsValidBoard():
    print("---Testing testValidBoard")
    board = [[3,2,1],[6,4,9],[5,7,8]]
    assert(validBoard(board))
    board = [[3,2,1],[6,4,0],[5,7,7]]
    assert(not validBoard(board))
    board = [[1,2,3],[7,4,8],[6,5,0]]
    assert(not validBoard(board))
    print("Passed!!")

def testAreLegalValues():
    print("---Testing areLegalValues")
    L = [1,2,3,4,5,6,7,8]
    assert(not areLegalValues(L))
    L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    assert(areLegalValues(L))
    L = [1,-1,3,4,5,6,7,8,8]
    assert(not areLegalValues(L))
    print("Passed!!")

def testIsLegalRow():
    print("---Testing isLegalRow")
    board = [[1,2,3,4],
             [2,4,4,1],
             [3,4,1,2],
             [4,1]]
    assert(isLegalRow(board, 0))
    assert(not isLegalRow(board, 1))
    assert(isLegalRow(board, 2))
    assert(not isLegalRow(board, 3))
    print("Passed!!")

def testIsLegalCol():
    print("---Testing isLegalCol")
    board = [[1,2,0,4],
            [2,2,0,1],
            [3,4,0,2],
            [4,1,0,3]]
    assert(isLegalCol(board, 0))
    assert(not isLegalCol(board, 1))
    assert(isLegalCol(board, 2))
    assert(isLegalCol(board,3))
    print("Passed!!")

def testIsLegalBlock():
    print("---Testing isLegalBlock")
    board = [[1,3,0,4],
             [2,4,0,1],
             [3,0,2,2],
             [4,0,0,3]]
    assert(isLegalBlock(board,0))
    assert(isLegalBlock(board,2))
    assert(not isLegalBlock(board,3))
    print("Passed!!")

def testIsLegalSudoku():
    print("---Testing isLegalSudoku")
    board = [
    [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]
    assert(isLegalSudoku(board))
    board[7] = [1,2,3,4,5,6,7,8,9]
    assert(not isLegalSudoku(board))
    board[4] = [1,2,3,4,5,6,7,8,9]
    assert(not isLegalSudoku(board))
    print("Passed!!")

def testAll():
    testMagicSquare()
    testIsKingsTour()
    testIsValidBoard()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()
