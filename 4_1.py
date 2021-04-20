#Joyce Moon

from tkinter import *
import math

# # ###################################
# # Fancy Wheel
# # ###################################

# def init(data):
#     data["cx"]=data["width"]/2
#     data["cy"]=data["height"]/2
#     data["r"]=200
#     data["n"]=4
#     data["color"]="blue"
#     data["px"]=[]
#     data["py"]=[]
#     data["angle"]=0
#     data["time"]=0
#     data["rotate"]=math.pi/180*10

# #if mouse click inside the circle, change direction or rotation
# def mousePressed(event, data):
#     if (event.x-data["cx"])**2+(event.y-data["cy"])**2<=data["r"]**2:
#         data["rotate"]=-data["rotate"]

# def keyPressed(event, data):
#     #if right or up key is pressed, increase the number or vertices by 1
#     if (event.keysym =="Right") or (event.keysym=="Up"):
#         data["n"]+=1
#     #if left or down key is pressed, decrease the number or vertices by 1
#     if (event.keysym=="Left") or (event.keysym=="Down"):
#         if data["n"]>2:
#             data["n"]-=1
#     #change the color if r,g,b is pressed
#     if (event.keysym=="r"):data["color"]="red"
#     if (event.keysym=="g"):data["color"]="green"
#     if (event.keysym=="b"):data["color"]="blue"

# def timerFired(data):
#     N=data["n"]
#     data["px"]=[]
#     data["py"]=[]
#     #rotate each vertices by data["rotate"]
#     for num in range (N+1):
#         data["angle"]=2*math.pi/N*num+data["time"]
#         data["px"].append(data["cx"]+data["r"]*math.cos(data["angle"]))
#         data["py"].append(data["cy"]-data["r"]*math.sin(data["angle"]))
#     data["time"]+=data["rotate"]


# def redrawAll(canvas, data):
#     # draw in canvas
#     (color,N)=(data["color"],data["n"])
#     #connect each vertices with lines
#     for i in range (N):
#         for j in range (i+1,N):
#             canvas.create_line(data["px"][i],data["py"][i],data["px"][j],
#                 data["py"][j],fill=color) 

# ####################################
# # use the run function as-is
# ####################################

# def run(width=600, height=600):
#     def redrawAllWrapper(canvas, data):
#         canvas.delete(ALL)
#         redrawAll(canvas, data)
#         canvas.update()    

#     def mousePressedWrapper(event, canvas, data):
#         mousePressed(event, data)
#         redrawAllWrapper(canvas, data)

#     def keyPressedWrapper(event, canvas, data):
#         keyPressed(event, data)
#         redrawAllWrapper(canvas, data)

#     def timerFiredWrapper(canvas, data):
#         timerFired(data)
#         redrawAllWrapper(canvas, data)
#         # pause, then call timerFired again
#         canvas.after(data["timerDelay"], timerFiredWrapper, canvas, data)
#     # Set up data and call init
#     data = dict()
#     data["width"] = width
#     data["height"] = height
#     data["timerDelay"] = 100 # milliseconds
#     init(data)
#     # create the root and the canvas
#     root = Tk()
#     canvas = Canvas(root, width=data["width"], height=data["height"])
#     canvas.pack()
#     # set up events
#     root.bind("<Button-1>", lambda event:
#                             mousePressedWrapper(event, canvas, data))
#     root.bind("<Key>", lambda event:
#                             keyPressedWrapper(event, canvas, data))
#     timerFiredWrapper(canvas, data)
#     # and launch the app
#     root.mainloop()  # blocks until window is closed
#     print("bye!")

# run(600, 600)

















# ####################################
# # SquareDrop!
# ####################################

import random

def init(data):
    data["x"]=[]
    data["y"]=[]
    data["size"]=[]
    data["color"]=[]
    data["new"]=True
    data["gameover"]=False
    data["score"]=0


def mousePressed(event, data):
    pass

#randomly select color
def getColors(data):
    color=random.choice(["red","blue","green","yellow"])
    data["color"].append(color)

#randomly select size
def getSize(data):
    size=random.randint(25,75)
    data["size"].append(size)


def keyPressed(event, data):
    c=len(data["x"])-1
    #if right key is pressed, move right
    if (event.keysym =="Right"):
        if not rectanglesOverlap(data):
            if data["x"][c]<data["width"]-data["size"][c]:
                data["x"][c]+=10
    #if left key is pressed, move left
    if (event.keysym=="Left"):
        if not rectanglesOverlap(data):
            if data["x"][c]>0:
                data["x"][c]-=10
    #if down key is pressed, move down
    if (event.keysym=="Down"):
       if data["y"][c]<data["height"] and not rectanglesOverlap(data):
            data["y"][c]+=10
    #if r is pressed, reset
    if (event.keysym=="r"):
        init(data)   

def timerFired(data):
    # only do things when not game over
    if not data["gameover"]:  
        #make new falling block by appending components into lists    
        if data["new"]==True:
            data["x"].append(data["width"]/2)
            data["y"].append(0)
            getColors(data)
            getSize(data)
            data["score"]+=1
            data["new"]=False
        c=len(data["y"])-1
        #if falling block is placed, make new falling block
        if rectanglesOverlap(data) or data["y"][c]>=data["height"]:
            data["new"]=True
        #if the block doen't collide or get out of the canvas, make it fall
        if data["y"][c]<data["height"]and not rectanglesOverlap(data):
            data["y"][c]+=10
        #if the falling block touch the ceiling, game over
        if rectanglesOverlap(data) and data["y"][c]-data["size"][c]<=0:
            data["gameover"]=True


#check if falling block collides with other preexisting blocks
def rectanglesOverlap(data):
    y1,x1=data["y"][len(data["y"])-1],data["x"][len(data["x"])-1]
    w1=data["size"][len(data["size"])-1]
    for i in range (len(data["x"])-1):
        #ygap is just for better visual
        ygap=7
        y2,x2,w2=data["y"][i]-ygap,data["x"][i],data["size"][i]
        #check the falling box's horizontal location in terms of other boxes
        if(x2<=x1<=x2+w2)or(x2<=x1+w1<=x2+w2)or(x1<=x2<x2+w2<=x1+w1):
            #check the falling box's vertical location in terms of other boxes
            # up y point
            (u1,u2)=(y1-w1,y2-w2)
            if(u2<=y1<=y2)or(u2<=u1<=y2)or(u1<=u2<=y2<=y1)or(u2<=u1<=y1<=y2):
                    return True
    return False


def redrawAll(canvas, data):
    # draw in canvas
    for i in range (len(data["x"])):
        size,color=data["size"][i],data["color"][i]
        x1,y1=data["x"][i],data["y"][i]
        x2,y2=x1+size,y1-size
        canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    #print the score and game over if game over
    if data["gameover"]:
        cx,cy=data["width"]/2,data["height"]/2
        canvas.create_text(cx,cy,text="Game Over")
        canvas.create_text(cx,cy+20,text=data["score"])
####################################
# use the run function as-is
####################################

def run(width=400, height=600):
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
        canvas.after(data["timerDelay"], timerFiredWrapper, canvas, data)
    # Set up data and call init
    data = dict()
    data["width"] = width
    data["height"] = height
    data["timerDelay"] = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data["width"], height=data["height"])
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

run(400, 600)

########################################################################
#######################Test Functions###################################
########################################################################


# def testRectangleOverlap():
#     data={}
#     data["x"]=[10,50]
#     data["y"]=[550,40]
#     data["size"]=[30,35]
#     assert(not rectanglesOverlap(data))
#     data["x"].append(40)
#     data["y"].append(70)
#     data["size"].append(40)
#     assert(rectanglesOverlap(data))    
#     print("Passed!!!")


