from tkinter import *
import math

#take two lists and combine the elements in order
def combine(L1,L2):
    result=[]
    if L1==[] or L2==[]:
        return L2 if L1==[] else L1
    indexL1=0
    indexL2=0
    lengthL1=len(L1)
    lengthL2=len(L2)
    #add to list if smaller and repeat
    while indexL1<lengthL1 and indexL2<lengthL2:
        if L1[indexL1]>L2[indexL2]:
            result.append(L2[indexL2])
            indexL2+=1
        else:
            result.append(L1[indexL1])
            indexL1+=1
    #add leftover part of either L1 or L2
    result=result+L1[indexL1:]+L2[indexL2:]
    return result


#count number of consecutively repeating integer and return the number and count
def lookAndSay(a):
    result=[]
    count=1
    for index in range (len(a)):
        if index!=len(a)-1 and a[index]==a[index+1]:
            count+=1
        else:
            result.append((count,a[index]))
            count=1
    return result

#does opposite of what lookAndSay do
def inverseLookAndSay(a):
    result=[]
    for tuples in a:
        count=tuples[0]
        number=tuples[1]
        for times in range (count):
            result.append(number)
    return result

#assign the puzzle with numerical value that matches with the index
#of the solution.Then check if the math expression is correct.
def solvesCryptarithm(puzzle, solution):
    if puzzle=="" or solution=="":
        return False
    solution=list(solution)
    add=(puzzle.split("=")[0].split("+"))
    result=puzzle.split("=")[1]
    first=changeString(add[0],solution)
    second=changeString(add[1],solution)
    result=changeString(result,solution)
    #if not letter in puzzle in solution, return False
    if first==False or second==False or result==False:
        return False
    return first+second==result

#assign the puzzle with numerical value that matches with the index
#of the solution.
def changeString(puzzle, solution):
    result=0
    for char in puzzle:
        if char in solution:
            result=result*10+solution.index(char)
        else:
            return False
    return result

####################################################################
# ignore_rest: The autograder will ignore all code below here
####################################################################

#fill nxn grid with circles
#red:every 4th diagnal. green:every 3rd row. yellow:every 2nd column. 
#blue:everything else
def drawCirclePattern(n):
    r=20
    root=Tk()
    canvas=Canvas(root,width=r*2*n,height=r*2*n,bg="cyan")
    canvas.pack()
    drawCircle(canvas,r*2*n,r*2*n,n)
    root.mainloop()
    print("Done")

#draw circles with radius of increment of 2/3
def drawCircle(canvas, width, height,n):
    r=20
    newr=r
    while newr>1:
        for i in range(n):
            for j in range(n):
                (center1,center2)=((r*2)*i+r,(r*2)*j+r)
                p1=center1-newr
                p2=center2-newr
                p3=center1+newr
                p4=center2+newr
                #change color
                if (i+j)%4==0:
                    canvas.create_oval(p1,p2,p3,p4,fill="red")
                elif j%3==0:
                    canvas.create_oval(p1,p2,p3,p4,fill="green")
                elif i%2==1:
                    canvas.create_oval(p1,p2,p3,p4,fill="yellow")
                else:
                    canvas.create_oval(p1,p2,p3,p4,fill="blue")
        #change radius
        newr=newr*2/3


#simple version of Turtle Graphics
def runSimpleTortoiseProgram(program,winWidth=500,winHeight=500):
    root=Tk()
    canvas=Canvas(root,width=winWidth,height=winHeight)
    canvas.pack()
    writetext(canvas,program)
    drawtortoise(canvas,winWidth,winHeight,program)
    root.mainloop()
    print("Done")

#make each line of program run on canvas
def drawtortoise(canvas,width,height,program):
    (x,y,angle,color)=(width/2,height/2,0,None)
    for line in program.splitlines():
        #ignore after #
        if ("#" in line): line=line[:line.find("#")]
        if len(line)!=0:
            command=line.split(" ")
            #follow the instructions
            if command[0]=="color": color=command[1]
            elif command[0]=="move":
                d=int(command[1])
                if color!="none":
                    canvas.create_line(x,y,x+d*math.cos(angle),
                        y+d*math.sin(angle),fill=color,width=4)
                x+=d*math.cos(angle)
                y+=d*math.sin(angle)
            elif command[0]=="left": angle-=int(command[1])*(math.pi/180)
            else: angle+=int(command[1])*(math.pi/180)

# write the program on canvas
def writetext(canvas,program):
    xlen=10
    ylen=10
    canvas.create_text(10,10,text=program,font=("Arial",10),
        anchor=NW,fill="gray")


def testCombine():
    print("---testing combine")
    assert(combine(["Alice", "Bob", "Charlie", "Eve"],["Adam", "Chloe"])
        ==["Adam", "Alice", "Bob", "Charlie", "Chloe", "Eve"])
    assert(combine(["A","D","E"],["B","C"])==["A","B","C","D","E"])
    assert(combine(["C","D"],["A"])==["A","C","D"])
    print("Passed!!!")


def testLookAndSay():
    print("---testing lookAndSay")
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) == [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    print("Passed!!!")


def testInverseLookAndSay():
    print("---testing inverseLookAndSay")
    assert(inverseLookAndSay(lookAndSay([])) == [])
    assert(inverseLookAndSay(lookAndSay([1,1,1]))==[1,1,1])
    assert(inverseLookAndSay(lookAndSay([-1,2,7]))==[-1,2,7])
    assert(inverseLookAndSay(lookAndSay([3,3,8,-10,-10,-10]))
        ==[3,3,8,-10,-10,-10])
    print("Passed!!!")


def testSolvesCryptarithm():
    print("---testing solvesCryptarithm")
    assert(solvesCryptarithm("a+a=d","a")==False)
    assert(solvesCryptarithm("","")==False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    print("Passed!!!")


def testChangeString():
    print("---testing changeString")
    assert(changeString("abc",["a","b","c"])==12)
    assert(changeString("cba",["a","b","c"])==210)
    assert(changeString("bca",["a","b","c"])==120)
    print("Passed!!!")

def testAll():
    testCombine()
    testLookAndSay()
    testInverseLookAndSay()
    testChangeString()
    testSolvesCryptarithm()
