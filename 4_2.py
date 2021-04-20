# Joyce Moon seojinm
# events-example0.py

# referenced
# https://www.cs.cmu.edu/~112/notes/notes-animations-examples.html#modeDemo

from tkinter import *
import copy
import math


####################################
# init
####################################

def init(data):
    # load data.xyz as appropriate
    data.mode="splash"
    data.n=len(data.initialBoard)
    data.size=60
    data.margin=(data.width-data.size*data.n)/2
    data.selection=(-1,-1)
    data.board=copy.deepcopy(data.initialBoard)
    data.prevselection=[]
    data.undoList=[]
    data.time=0
    data.legal=True
    data.complete=False




####################################
# mode dispatcher
####################################


def mousePressed(event, data):
    # use event.x and event.y
    if data.mode=="help":
        helpMousePressed(event, data)
    elif data.mode=="sudoku":
        sudokuMousePressed(event, data)
    elif data.mode=="splash":
        splashMousePressed(event, data)

def keyPressed(event, data):
    # use event.char and event.keysym
    if data.mode=="help":
        helpKeyPressed(event, data)
    elif data.mode=="sudoku":
        sudokuKeyPressed(event, data)
    elif data.mode=="splash":
        splashKeyPressed(event, data)


def timerFired(data):
    if data.mode=="help":
        helpTimerFired(data)
    elif data.mode=="sudoku":
        sudokuTimerFired(data)
    elif data.mode=="splash":
        splashTimerFired(data)

def redrawAll(canvas, data):
    # draw in canvas
    if data.mode=="help":
        helpRedrawAll(canvas, data)
    elif data.mode=="sudoku":
        sudokuRedrawAll1(canvas, data)
        sudokuRedrawAll2(canvas, data)
    elif data.mode=="splash":
        splashRedrawAll(canvas, data)




####################################
# splash mode
####################################

# change mode when start game button or help button is pressed
def splashMousePressed(event, data):
    # use event.x and event.y
    if (data.width/2-data.size<event.x<data.width/2+data.size and 
        data.height/2-data.size*1.25<event.y<data.height/2-data.size*0.25):
        data.mode="sudoku"
    if (data.width/2-data.size<event.x<data.width/2+data.size and 
        data.height/2+data.size*1.25>event.y>data.height/2+data.size*0.25):
        data.mode="help"

def splashKeyPressed(event, data):
    # use event.char and event.keysym
    pass

def splashTimerFired(data):
    pass

def splashRedrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(data.width/2-data.size,data.height/2-data.size*1.25,
            data.width/2+data.size,data.height/2-data.size*0.25,fill="white",
            outline="DeepPink3")
    canvas.create_rectangle(data.width/2-data.size,data.height/2+data.size*1.25,
            data.width/2+data.size,data.height/2+data.size*0.25,fill="white",
            outline="DeepPink3")
    canvas.create_text(data.width/2,data.height/2+data.size*0.75,text="HELP")
    canvas.create_text(data.width/2,data.height/2-data.size*0.75,
            text="PLAY GAME")

####################################
# help mode
####################################

#go back to game if go back button is pressed
def helpMousePressed(event, data):
    # use event.x and event.y
    if (data.width-data.size*3.5<event.x<data.width-data.size*1.5 and 
        data.height-data.size*1.5>event.y>data.height-data.size*2.5):
        data.mode="sudoku"
    
#go back to game if any key is pressed
def helpKeyPressed(event, data):
    # use event.char and event.keysym
    data.mode="sudoku"

def helpTimerFired(data):
    pass


def helpRedrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(data.size,data.size,data.width-data.size,
            data.height-data.size,fill="white",outline="pink")
    canvas.create_text(data.width/2,data.height/2-data.size,
            text=" click in the box and enter\nnumber to fill in the sudoku"
            ,fill="DeepPink3")
    canvas.create_text(data.width/2,data.height/2-data.size/4,
            text="press u to undo",font=("Arial",17),fill="DeepPink3")
    canvas.create_text(data.width/2,data.height/2+data.size/4,
            text="press r to redo",font=("Arial",17),fill="DeepPink3")
    canvas.create_text(data.width/2,data.height/2+data.size,
            text="press any key to go back",fill="DeepPink3")
    canvas.create_rectangle(data.width-data.size*3.5,data.height-data.size*1.5,
            data.width-data.size*1.5,data.height-data.size*2.5,
            outline="DeepPink3")
    canvas.create_text(data.width-data.size*2.5,data.height-data.size*2,
            text="back to game")


####################################
# sudoku mode
####################################

#check if the point is in the board
def pointInGrid(x,y,data):
    return((data.margin<=x<=data.width-data.margin)
        and (data.margin<=y<=data.height-data.margin))

#return row and col of the point
def getCell(x,y,data):
    if (not pointInGrid(x,y,data)):
        return(-1,-1)
    row=int((y-data.margin)//data.size)
    col=int((x-data.margin)//data.size)
    return (row,col)

#retrun the boundary points of the box of the row and col
def getCellBounds(row,col,data):
    x0=data.margin+col*data.size
    x1=data.margin+(col+1)*data.size
    y0=data.margin+row*data.size
    y1=data.margin+(row+1)*data.size
    return (x0,y0,x1,y1)

#check if sudoku board is complete
def sudokuComplete(data):
    for rows in data.board:
        for num in rows:
            if num==0:
                return False
    return True

#select a box or unselect a box
def sudokuMousePressed(event, data):
    # use event.x and event.y
    (row,col)=getCell(event.x,event.y,data)
    #only allow to select box that are not original numbers
    if data.initialBoard[row][col]==0:
        if (data.selection==(row,col)):
            data.selection=(-1,-1)
        else:
            data.selection=(row,col)


def sudokuKeyPressed(event, data):
    # use event.char and event.keysym
    #undo
    if event.keysym=="u":
        if len(data.prevselection)>0:
            (row,col)=data.prevselection.pop()
            data.undoList.append((data.board[row][col],row,col))
            data.board[row][col]=0
    #redo
    elif event.keysym=="r":
        if len(data.undoList)>0:
            (num,row,col)=data.undoList.pop()
            data.prevselection.append((row,col))
            data.board[row][col]=num
    #help
    elif event.keysym=="h" or event.keysym=="question":
        data.mode="help"

    #enter number to fill in the sudoku, only numbers between 1~n
    #if the box is selected, which means only the part not part of the original
    #numbers
    elif data.selection!=(-1,-1):
        if event.keysym.isdigit() and 1<=int(event.keysym)<=data.n:
            data.board[data.selection[0]][data.selection[1]]=int(event.keysym)
            data.prevselection.append((data.selection[0],data.selection[1]))
            data.undoList=[]

    data.legal=isLegalSudoku(data.board)
    data.complete=sudokuComplete(data)

#count timer
def sudokuTimerFired(data):
    if not data.complete:
        data.time+=1

#sudoku redraw all of main board itself
def sudokuRedrawAll1(canvas, data):
    # draw in canvas
    for row in range (data.n):
        for col in range (data.n):
            (x0,y0,x1,y1)=getCellBounds(row,col,data)
            fill="lavender" if (data.selection==(row,col)) else "lemon chiffon"
            canvas.create_rectangle(x0,y0,x1,y1,fill=fill,outline="pink")
            # original numbers in board is bigger,bold, and black
            # newly entered numbers are smaller, and grey
            if data.board[row][col]!=0:
                font=("Helvetica",12) if data.initialBoard[row][col]==0 else (
                    ("Helvetica",15,"bold"))
                color="grey50" if data.initialBoard[row][col]==0 else "black"
                canvas.create_text((x0+x1)/2,(y0+y1)/2,font=font,fill=color,
                    text=data.board[row][col])
    # make the blocks visibly clear
    for i in range (0,data.n+1):
        if i%math.sqrt(data.n)==0:
            canvas.create_line(data.margin,data.margin+data.size*i,
                data.height-data.margin,data.margin+data.size*i,
                fill="DeepPink3")
            canvas.create_line(data.margin+data.size*i,data.margin,
                data.margin+data.size*i,data.width-data.margin,fill="DeepPink3")

#sudoku redrawall of extra decorative parts
def sudokuRedrawAll2(canvas, data):
    canvas.create_text(data.width-data.size,data.margin/2,fill="DeepPink3",
        text="timer:%d "%(data.time))
    canvas.create_text(data.size*1.5,data.margin/2,text="press h or ? for help",
        fill="DeepPink3")
    # if board not legal, print "INCORRECT"
    if not data.legal:
        canvas.create_text(data.width/2,data.height/2,text="INCORRECT",
            fill="Red",font=("Arial",40))
    # if board is complete, print "COMPLETE"
    if data.complete:
        canvas.create_text(data.width/2,data.height/2,text="COMPLETE",
            fill="RoyalBlue1",font=("Arial",40))




####################################
# valid Sudoku
####################################

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



####################################
# use the run function as-is
####################################
def playSudoku(initialBoard):
    run(initialBoard)


def run(initialBoard,width=600, height=600):
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
    data.initialBoard=initialBoard
    data.width = width
    data.height = height
    data.timerDelay = 1000 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height, bg="pink")
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





