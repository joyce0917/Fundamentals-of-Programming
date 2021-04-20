# # oopy-playing-cards-demo.py
# # Demos class attributes, static methods, repr, eq, hash
# # oopyDotsDemo.py
# # starts with betterDotsDemo and adds:
# #   * a dotCounter that counts all the instances of Dot or its subclasses
# #   * a MovingDot subclass of Dot that scrolls horizontally
# #   * a FlashingMovingDot subclass of MovingDot that flashes and moves

# import random
# from tkinter import *

# class Dot(object):
#     dotCount = 0

#     def __init__(self, x, y):
#         Dot.dotCount += 1
#         self.x = x
#         self.y = y
#         self.r = random.randint(20,50)
#         self.fill = random.choice(["pink","orange","yellow","green",
#                                    "cyan","purple"])
#         self.clickCount = 0

#     def containsPoint(self, x, y):
#         d = ((self.x - x)**2 + (self.y - y)**2)**0.5
#         return (d <= self.r)

#     def draw(self, canvas):
#         canvas.create_oval(self.x-self.r, self.y-self.r,
#                            self.x+self.r, self.y+self.r,
#                            fill=self.fill)
#         canvas.create_text(self.x, self.y, text=str(self.clickCount))

#     def onTimerFired(self, data):
#         pass

# class MovingDot(Dot):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.speed = 5 # default initial speed

#     def onTimerFired(self, data):
#         self.x += self.speed
#         if (self.x > data.width):
#             self.x = 0

# class FlashingMovingDot(MovingDot):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.flashCounter = 0
#         self.showFlash = True

#     def onTimerFired(self, data):
#         super().onTimerFired(data)
#         self.flashCounter += 1
#         if (self.flashCounter == 5):
#             self.flashCounter = 0
#             self.showFlash = not self.showFlash

#     def draw(self, canvas):
#         if (self.showFlash):
#             canvas.create_rectangle(self.x-self.r, self.y-self.r,
#                                self.x+self.r, self.y+self.r,
#                                fill="lightGray")
#         super().draw(canvas)

# def init(data):
#     data.dots = [ ]

# def mousePressed(event, data):
#     for dot in reversed(data.dots):
#         if (dot.containsPoint(event.x, event.y)):
#             dot.clickCount += 1
#             return
#     dotType = (len(data.dots) % 3)
#     if (dotType == 0):
#         data.dots.append(Dot(event.x, event.y))
#     elif (dotType == 1):
#         data.dots.append(MovingDot(event.x, event.y))
#     else:
#         data.dots.append(FlashingMovingDot(event.x, event.y))

# def redrawAll(canvas, data):
#     for dot in data.dots:
#         dot.draw(canvas)
#     canvas.create_text(data.width/2, 10, text="%d Dots" % Dot.dotCount)

# def keyPressed(event, data):
#     pass

# def timerFired(data):
#     for dot in data.dots:
#         dot.onTimerFired(data)

# ####################################
# # use the run function as-is
# ####################################

# def run(width=300, height=300):
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
#         canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
#     # Set up data and call init
#     class Struct(object): pass
#     data = Struct()
#     data.width = width
#     data.height = height
#     data.timerDelay = 100 # milliseconds
#     init(data)
#     # create the root and the canvas
#     root = Tk()
#     canvas = Canvas(root, width=data.width, height=data.height)
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

# run(400, 200)
# images-demo.py

from tkinter import *

def init(data):
    data["step"] = 0
    loadPlayingCardImages(data) # always load images in init!

def loadPlayingCardImages(data):
    cards = 55 # cards 1-52, back, joker1, joker2
    data["cardImages"] = [ ]
    for card in range(cards):
        rank = (card%13)+1
        suit = "cdhsx"[card//13]
        filename = "playing-card-gifs/%s%d.gif" % (suit, rank)
        data["cardImages"].append(PhotoImage(file=filename))

def getPlayingCardImage(data, rank, suitName):
    suitName = suitName[0].lower() # only car about first letter
    suitNames = "cdhsx"
    assert(1 <= rank <= 13)
    assert(suitName in suitNames)
    suit = suitNames.index(suitName)
    return data["cardImages"][13*suit + rank - 1]

def getSpecialPlayingCardImage(data, name):
    specialNames = ["back", "joker1", "joker2"]
    return getPlayingCardImage(data, specialNames.index(name)+1, "x")

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    data["step"] += 1

def redrawAll(canvas, data):
    suitNames = ["Clubs", "Diamonds", "Hearts", "Spades", "Xtras"]
    suit = (data["step"]//10) % len(suitNames)
    suitName = suitNames[suit]
    cards = 3 if (suitName == "Xtras") else 13
    margin = 10
    (left, top) = (margin, 40)
    for rank in range(1,cards+1):
        image = getPlayingCardImage(data, rank, suitName)
        if (left + image.width() > data["width"]):
            (left, top) = (margin, top + image.height() + margin)
        canvas.create_image(left, top, anchor=NW, image=image)
        left += image.width() + margin
    canvas.create_text(data["width"]/2, 20, text=suitName, font="Arial 28 bold")
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
        canvas.after(data["timerDelay"], timerFiredWrapper, canvas, data)
    # Set up data and call init
    root = Tk()
    data = dict()
    data["width"] = width
    data["height"] = height
    data["timerDelay"] = 100 # milliseconds
    init(data)
    # create the root and the canvas
    
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

run(600, 600)
