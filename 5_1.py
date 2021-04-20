#joyce moon (seojinm)
import copy

class mySet(object):
    maxBucketSize=10
    def __init__(self,L=[]):
        self.numBuckets=2
        self.hashTable=[[],[]]
        for c in L:
            if c not in (el for sublist in self.hashTable for el in sublist):
                mySet.add(self,c)

    def resize(self):
        L=[]
        for l in self.hashTable:
            if len(l)==self.maxBucketSize:
                self.numBuckets+=1
                self.hashTable=[[] for i in range(self.numBuckets)]
            for s in l:
                L.append(s)
        for c in L:
            if c not in (el for sublist in self.hashTable for el in sublist):
                mySet.add(self,c)        


    def add(self,element):
        if element not in (el for sublist in self.hashTable for el in sublist):
            index=hash(element)%self.numBuckets
            self.hashTable[index].append(element)
        self.resize()

    def remove(self,element):
        for sublist in self.hashTable:
            if element in sublist:
                sublist.remove(element)

    def clear(self):
        self.hashTable=[[] for i in range(self.numBuckets)]

    def __contains__(self,element):
        if element in (el for sublist in self.hashTable for el in sublist):
            return True
        return False

    def __len__(self):
        length=0
        for sublist in self.hashTable:
            length+=len(sublist)
        return length

    def isSubset(self,other):
        for c in other:
            if c not in (el for sublist in self.hashTable for el in sublist):
                return False
        return True

    def isSuperset(self,other):
        for sublist in self.hashTable:
            for c in sublist:
                if c not in other:
                    return False
        return True

    def __eq__(self,other):
        if not isinstance(other,set):
            return False
        return self.isSubset(other) and self.isSuperset(other)

    def __str__(self):
        string=""
        for sublist in self.hashTable:
            for c in sublist:
                string+=str(c)
                string+=","
        string=string[:-1]
        return "{"+string+"}"

    def union(self,other):
        U=mySet()
        U.hashTable=copy.deepcopy(self.hashTable)
        for c in other:
            if c not in (el for sublist in self.hashTable for el in sublist):
                U.add(c)
        return U

    def intersection(self,other):
        I=mySet()
        I.hashTable=copy.deepcopy(self.hashTable)
        for sublist in self.hashTable:
            for c in sublist:
                if c not in other:
                    I.remove(c)
        return I

    def difference(self,other):
        D=mySet()
        D.hashTable=copy.deepcopy(self.hashTable)
        for sublist in self.hashTable:
            for c in sublist:
                if c in other:
                    D.remove(c)
        return D

    def symmetricDifference(self,other):
        D=mySet()
        D.hashTable=copy.deepcopy(self.hashTable)
        for c in other:
            if c not in (el for sublist in self.hashTable for el in sublist):
                D.add(c)
        for sublist in self.hashTable:
            for s in sublist:
                if s in other:
                    D.remove(s)
        return D

    def update(self,other):
        for c in other:
            self.add(c)
        self.resize()

    def intersectionUpdate(self,other):
        before=copy.deepcopy(self.hashTable)
        for sublist in before:
            for c in sublist:
                if c not in other:
                    self.remove(c)

    def differenceUpdate(self,other):
        for sublist in self.hashTable:
            for c in sublist:
                if c in other:
                    self.remove(c)


    def symmetricDifferenceUpdate(self,other):
        before=copy.deepcopy(self.hashTable)
        for c in other:
            if c not in (el for sublist in self.hashTable for el in sublist):
                self.add(c)
        for sublist in before:
            for s in sublist:
                if s in other:
                    self.remove(s)



###############################################
# test cases
###############################################

def testMySet():
    print("---Testing MySet")
    A=mySet([1,2,3])
    #eq
    assert(A=={1,2,3})
    assert(not A=={1,2})
    #add
    A.add(3)
    assert(A=={1,2,3})
    A.add(4)
    assert(A=={1,2,3,4})
    #remove
    A.remove(4)
    assert(A=={1,2,3})
    #subset
    assert(A.isSubset({1,2}))
    assert(not A.isSubset({1,2,3,4}))
    #superset
    assert(not A.isSuperset({1,2}))
    assert(A.isSuperset({1,2,3,4}))
    #union
    B=A.union({3,4})
    assert(B=={1,2,3,4})
    assert(not B=={1,2,3})
    #intersection
    C=A.intersection({3,4})
    assert(C=={3})
    assert(not C=={3,4})
    #difference
    D=A.difference({3,4})
    assert(D=={1,2})
    #symmetric difference
    E=A.symmetricDifference({3,4})
    assert(E=={1,2,4})
    #update
    A.update({3,4})
    assert(A=={1,2,3,4})
    #intersection update
    A.intersectionUpdate({4,5})
    assert(A=={4})
    #difference update
    A.differenceUpdate({5})
    assert(A=={4})
    #symmetric difference update
    A.symmetricDifferenceUpdate({5})
    assert(A=={4,5})
    print("Passed!!")








# ###############################################
# # OOPY Invaders
# ###############################################

# from tkinter import *
# class Monster(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         self.v=4
#         self.height=10
#         self.width=10
#         self.x0=x
#         self.move=30  

#     def motion(self):
#         #change direction
#         if self.x < self.x0 - self.move:
#             self.v *= -1
#         elif self.x > self.x0 + self.move:
#             self.v *= -1  
#         self.x+=self.v      

# class Cyan(Monster):
#     def __init__(self,x,y):
#         super().__init__(x,y)
#         self.r=10

#     #circle
#     def draw(self,canvas):
#         canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,
#             self.y+self.r,fill="cyan")        

# class Magenta(Monster):
#     def __init__(self,x,y):
#         super().__init__(x,y)
#         self.ovalW=15
#         self.ovalH=10

#     #oval
#     def draw(self,canvas):
#         canvas.create_oval(self.x-self.ovalW/2,self.y-self.ovalH/2,
#             self.x+ovalW/2,self.y+ovalH/2,fill="magenta")

# class Yellow(Monster):
#     def __init__(self,x,y):
#         super().__init__(x,y)
#         self.ovalW=20
#         self.ovalH=10

#     #oval
#     def draw(self,canvas):
#         canvas.create_oval(self.x-self.ovalW/2,self.y-self.ovalH/2,
#             self.x+ovalW/2,self.y+ovalH/2,fill="yellow")


# class Player(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         self.v=10
#         self.boxH=10
#         self.boxW=15
#         self.extralife=3

#     def draw(self,canvas):
#         canvas.create_rectangle(self.x,self.y,self.x+self.boxW,
#             self.y+self.boxH,fill="cyan")

# class Bullet(object):
#     def __init__(self,x,y,v):
#         self.x=x
#         self.y=y
#         self.r=1
#         self.v=v
#         self.w=5
#         self.l=5

#     def motion(self):
#         self.y+=self.v

#     def draw(self,canvas):
#         canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill="red")

# class OopyInvaders(object):
#     totalGamesPlayed=0

#     def __init__(self):
#         self.canvasW=500
#         self.canvasH=500
#         self.numMonster=7
#         self.CyanRows=1
#         self.MagentaRows=2
#         self.YellowRows=2
#         self.monsters=[]
#         self.outergapX=25
#         self.outergapY=50
#         self.gapX=(self.canvasW-2*self.outergapX)/self.numMonster
#         self.gapY=(self.canvasH-2*self.outergapY)/(
#             self.CyanRows+self.MagentaRows+self.YellowRows)
#         OopyInvaders.totalGamesPlayed +=1

#         self.monsterList

#     def monsterList(self):
#         # total Monster Rows
#         for i in range (self.CyanRows+self.MagentaRows+self.YellowRows):
#             L=[]
#             for j in range (self.numMonster):
#                 if i<self.CyanRows:
#                     L.append(Cyan(self.outergapX+self.gapX*j,self.outergapY+self.gapY*i))
#                 # if self.CyanRows<=i<self.CyanRows+self.MagentaRows:
#                 #     L.append(Magenta(self.outergapX+self.gapX*j,self.outergapY+self.gapY*i))
#                 # if self.CyanRows+self.MagentaRows<=i<self.CyanRows+self.MagentaRows+self.YellowRows:
#                 #     L.append(Yellow(self.outergapX+self.gapX*j,self.outergapY+self.gapY*i))
#             self.monsters.append(L)
#         print(self.monsters)
#     def mousePressed(self,event,data):
#         pass

#     def keyPressed(self,event,data):
#         pass

#     def timerFired(self,data):
#         pass

#     def redrawAll(self,canvas,data):
#         for monsterL in self.monsters:
#             for monster in monsterL:
#                 monster.draw(canvas)


#     def run(self,width=500,height=500):
#         def redrawAllWrapper(canvas, data):
#             canvas.delete(ALL)
#             self.redrawAll(canvas, data)
#             canvas.update()    

#         def mousePressedWrapper(event, canvas, data):
#             self.mousePressed(event, data)
#             redrawAllWrapper(canvas, data)

#         def keyPressedWrapper(event, canvas, data):
#             self.keyPressed(event, data)
#             redrawAllWrapper(canvas, data)

#         def timerFiredWrapper(canvas, data):
#             self.timerFired(data)
#             redrawAllWrapper(canvas, data)
#             # pause, then call timerFired again
#             canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
#         # Set up data and call init
#         class Struct(object): pass
#         data = Struct()
#         data.width = width
#         data.height = height
#         data.timerDelay = 500 # milliseconds
#         # create the root and the canvas
#         root = Tk()
#         canvas = Canvas(root, width=data.width, height=data.height)
#         canvas.pack()
#         # set up events
#         root.bind("<Button-1>", lambda event:
#                                 mousePressedWrapper(event, canvas, data))
#         root.bind("<Key>", lambda event:
#                                 keyPressedWrapper(event, canvas, data))
#         timerFiredWrapper(canvas, data)
#         # and launch the app
#         root.mainloop()  # blocks until window is closed
#         print("bye!")



# game1 = OopyInvaders()
# game1.run()
# # print(game1.getFinalScore())

# # game2 = OopyInvaders()
# # game2.run()
# # print(game2.getFinalScore())

# # assert(OopyInvaders.totalGamesPlayed == 2)

