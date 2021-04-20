# Joyce Moon (seojinm)
# partner: Isaac Kweon (ikweon)

#referrenced
#https://www.cs.cmu.edu/~112/notes/notes-tetris/
                                    #TetrisForIntroIntermediateProgrammers.html



from tkinter import *
import random
import copy

def init(data):
    # set board dimensions and margin
    data.rows = 15
    data.cols = 10
    data.margin = 20
    
    # make board
    data.emptyColor = "gray94"
    data.board = [([data.emptyColor] * data.cols) for row in range(data.rows)]
    
    #Seven "standard" pieces (tetrominoes)
    iPiece = [[ True,  True,  True,  True]]
    jPiece = [[ True, False, False ],[ True, True,  True]]
    lPiece = [[ False, False, True],[ True,  True,  True]]
    oPiece = [[ True, True],[ True, True]]
    sPiece = [[ False, True, True],[ True,  True, False ]]
    tPiece = [[ False, True, False ],[ True,  True, True]]
    zPiece = [[ True,  True, False ],[ False, True, True]]
    data.tetrisPieces=[iPiece,jPiece,lPiece,oPiece,sPiece,tPiece,zPiece]
    data.tetrisPieceColors=["coral","royalblue1","darkorchid1","violetred1",
        "yellow2","firebrick1","grey60"]    
    
    data.fallingPiece=None
    data.fallingPieceColor=None
    data.fallingPieceRow=0
    data.fallingPieceCol=0
    data.fallingPieceCols=0
    data.gameover=False
    data.score=0
    newFallingPiece(data)


####################################
# helper functions
####################################

# getCellBounds from grid-demo.py
def getCellBounds(row, col, data):
    # aka "modelToView"s
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    x0 = data.margin + gridWidth * col / data.cols
    x1 = data.margin + gridWidth * (col+1) / data.cols
    y0 = data.margin + gridHeight * row / data.rows
    y1 = data.margin + gridHeight * (row+1) / data.rows
    return (x0, y0, x1, y1)


#choose new falling piece and set the location
def newFallingPiece(data):
    index=random.randint(0,6)
    data.fallingPiece=data.tetrisPieces[index]
    data.fallingPieceColor=data.tetrisPieceColors[index]
    data.fallingPieceCols=len(data.fallingPiece[0])
    data.fallingPieceCol=data.cols//2-data.fallingPieceCols//2



#move the falling piece left,down,right
def moveFallingPiece(data,drow,dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    if not fallingPieceIsLegal(data): 
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol
        return False
    return True


#check if the falling piece is legal, not getting out of grid
#and not colliding with other blocks
def fallingPieceIsLegal(data):
    for row in range (len(data.fallingPiece)):
        for col in range (len(data.fallingPiece[0])):
            if data.fallingPiece[row][col]==True:
                if (0>data.fallingPieceCol or 
                    col+data.fallingPieceCol>=data.cols) or ( 
                    row+data.fallingPieceRow>=data.rows):
                    return False
                elif (data.board[data.fallingPieceRow+row]
                               [data.fallingPieceCol+col] != data.emptyColor):
                    return False
    return True


#rotate the falling piece counterclockwise 90 degrees
def rotateFallingPiece(data):
    op,r,c=data.fallingPiece,data.fallingPieceRow,data.fallingPieceCol
    lenr,lenc=len(op),len(op[0])
    data.fallingPiece=[([0] * lenr) for cols in range(lenc)]
    for row in range (lenr):
        for col in range (lenc):
            data.fallingPiece[lenc-1-col][row]=op[row][col]
            data.fallingPieceRow=r+lenr//2-lenc//2
            data.fallingPieceCol=c+lenc//2-lenr//2
    if not fallingPieceIsLegal(data):
        data.fallingPiece=op
        data.fallingPieceRow=r
        data.fallingPieceCol=c


#place the falling piece on the board
def placeFallingPiece(data):
    for row in range (len(data.fallingPiece)):
        for col in range (len(data.fallingPiece[0])):
            r=row+data.fallingPieceRow
            c=col+data.fallingPieceCol
            if data.fallingPiece[row][col]==True:
                data.board[r][c]=data.fallingPieceColor
    data.fallingPieceRow=0


#if a row is full, remove it and increase the score
def removeFullRows(data):
    index=data.rows-1
    board=copy.deepcopy(data.board)
    fullRows=0
    for oldRow in reversed(board):
        if data.emptyColor in oldRow:
            data.board[index]=oldRow
            index-=1
        else:
            fullRows+=1
    for i in range (index):
        data.board[i]=[data.emptyColor]*data.cols
    data.score+=fullRows**2


####################################
# controllers
####################################

def mousePressed(event, data):
    pass


def keyPressed(event, data):
    if data.gameover==False:
        if event.keysym=="Left":
            moveFallingPiece(data,0,-1)
        elif event.keysym=="Right":
            moveFallingPiece(data,0,1)
        elif event.keysym=="Down":
            moveFallingPiece(data,1,0)
        elif event.keysym=="Up":
            rotateFallingPiece(data)
    if event.keysym=="r":
        init(data)

def timerFired(data):
    if not data.gameover:
        if moveFallingPiece(data,1,0)==False:
            placeFallingPiece(data)
            removeFullRows(data)
            newFallingPiece(data)
            if moveFallingPiece(data,1,0)==False:
                data.gameover=True

####################################
# draw functions
####################################

#draw the new falling piece
def drawFallingPiece(canvas,data):
    for row in range (len(data.fallingPiece)):
        for col in range (len(data.fallingPiece[0])):
            r=row+data.fallingPieceRow
            c=col+data.fallingPieceCol
            if data.fallingPiece[row][col]==True:
                drawCell(canvas, data, r, c, data.fallingPieceColor)


def drawGame(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="SeaGreen1",
            outline="SeaGreen1")
    drawBoard(canvas, data)
    drawFallingPiece(canvas,data)
    drawScore(canvas,data)
    if data.gameover:
        canvas.create_text(data.width/2,data.height/2,text="GAMEOVER",
                fill="red")


def drawBoard(canvas, data):
    # draw grid of cells
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col, data.board[row][col])


def drawCell(canvas, data, row, col, color):
    (x0, y0, x1, y1) = getCellBounds(row, col, data)
    m = 1 # cell outline margin
    canvas.create_rectangle(x0, y0, x1, y1, outline="white",fill="white")
    canvas.create_rectangle(x0+m, y0+m, x1-m, y1-m, fill=color, 
        outline="white")


def drawScore(canvas,data):
    canvas.create_text(data.width-data.margin*2,data.margin/2,
            text="score:%d"%data.score)


def redrawAll(canvas, data):
    drawGame(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 500 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

####################################
# playTetris() [calls run()]
####################################

def playTetris():
    rows = 15
    cols = 10
    margin = 20 # margin around grid
    cellSize = 20 # width and height of each cell
    width = 2*margin + cols*cellSize
    height = 2*margin + rows*cellSize
    run(width, height)

playTetris()






# ####################################
# # Fraction
# ####################################
# # MyFractionTester.py
# # Partial test suite of Fraction class
# # For demonstrational purposes only, as this is quite incomplete.
# # Add more test cases yourself!



# def gcd(a,b):
#     while b!=0:
#         (a,b)=(b,a%b)
#     return a

# def lcm(a,b):
#     return (a*b)/gcd(a,b)

# def gcdFraction(self,other):
#     a=gcd(self.numerator,other.numerator)
#     b=lcm(self.denominator,other.denominator)
#     return "%d/%d"%(a,b)

# class Fraction(object):
#     def __init__(self,n,d):
#         self.numerator = n
#         self.denominator = d

#     def __eq__(self,other):
#         if type(self)==type(other):
#             a=self.numerator/self.denominator
#             b=other.numerator/other.denominator
#             if almostEqual(a,b):
#                 return True
#             return False
#         elif type(self) == Fraction and (type(other)==int 
#             or type(other)==float):
#             a=self.numerator/self.denominator
#             if almostEqual(a,other):
#                 return True
#             return False
#         elif type(other)== Fraction and (type(self)==int or type(self)==float):
#             a=other.numerator/other.denominator
#             if almostEqual(self,a):
#                 return True
#             return False
#         return False

#     def __ne__(self,other):
#         if type(self)==type(other):
#             if type(self)==Fraction:
#                 a=self.numerator/self.denominator
#                 b=other.numerator/other.denominator
#                 if almostEqual(a,b):
#                     return False
#             return True
#         elif type(self) == Fraction and (type(other)==int or (
#             type(other)==float)):
#             a=self.numerator/self.denominator
#             if almostEqual(a,other):
#                 return False
#             return True
#         elif type(other)== Fraction and (type(self)==int or type(self)==float):
#             a=other.numerator/other.denominator
#             if almostEqual(self,a):
#                 return False
#             return True
#         return True

#     def __ge__(self,other):
#         a=self.numerator/self.denominator
#         b=other.numerator/other.denominator
#         if almostEqual(a,b):
#             return True
#         elif a>b:
#             return True
#         return False

#     def __gt__(self,other):
#         a=self.numerator/self.denominator
#         b=other.numerator/other.denominator
#         if a>b:
#             return True
#         return False

#     def __lt__(self,other):
#         a=self.numerator/self.denominator
#         b=other.numerator/other.denominator
#         if a<b:
#             return True
#         return False

#     def __le__(self,other):
#         a=self.numerator/self.denominator
#         b=other.numerator/other.denominator
#         if almostEqual(a,b):
#             return True
#         elif a<b:
#             return True
#         return False

#     def __add__(self,other):
#         a=self.numerator/self.denominator
#         b=other.numerator/other.denominator
#         return (a+b)

#     def __mul__(self,other):
#         a=self.numerator/self.denominator
#         b=other.numerator/other.denominator
#         return (a*b)       

#     def __str__(self):
#         a=gcd(self.numerator,self.denominator)
#         n=self.numerator//a
#         d=self.denominator//a
#         if d==1:
#             return str(n)
#         return "%d/%d"%(n,d)



# def almostEqual(d1, d2, epsilon=10**-8):
#     return abs(d1 - d2) < epsilon

# def testFractionClass():
#     print("Testing %s.Fraction class..." % (Fraction.__module__), end=" ")
#     # Testing ==, !=
#     assert(Fraction(2,3) == Fraction(2,3))
#     assert(not(Fraction(2,3) != Fraction(2,3)))
#     assert(Fraction(2,5) != Fraction(2,3))

#     # Test == for unlike types
#     assert(Fraction(5,1) == 5)
#     assert(5 == Fraction(5,1))
#     assert(Fraction(10,2) == 5)
#     assert(Fraction(10,2) == 5.0)
#     assert(Fraction(2,3) != "fred")

#     # Testing gcd in constructor
#     assert(Fraction(2,3) == Fraction(4,6))

#     # Testing >=, >, <=, <
#     assert(Fraction(2,3) > Fraction(1,3))
#     assert(Fraction(1,3) < Fraction(2,3))
#     assert(Fraction(1,3) <= Fraction(2,3))
#     assert(not (Fraction(2,3) <= Fraction(1,3)))

#     # # Testing str
#     assert(str(Fraction(2,3)) == "2/3")
#     assert(str(Fraction(6,3)) == "2")
#     assert(str(Fraction(0,3)) == "0")

#     # # Testing +
#     assert(Fraction(1,3) + Fraction(1,3) == Fraction(2,3))
#     assert(Fraction(1,3) + Fraction(2,1) == Fraction(7,3))
#     assert(Fraction(2,1) + Fraction(2,4) == Fraction(5,2))
    

#     # # Testing *
#     assert(Fraction(1,3) * Fraction(1,3) == Fraction(1,9))

#     print("Passed!")

# # Test builtin Fraction class
# testFractionClass()