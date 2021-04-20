########################################
# Name: Joyce Moon                     #
# Andrew ID: seojinm                   #
# Section: B                           #
########################################



####################
# Question 0       #
# Study the notes! #
####################

'''
Carefully go over the recursion examples seen in class and recitation.
Make sure that you are able to reproduce the solutions by yourself.
This will help you a lot with the homework and the exam!!! 
'''



##################################
# Question 1                     #
# Reasoning about recursive code #
##################################

# Do "Reasoning About (Recursive) Code" from 
# http://www.kosbie.net/cmu/fall-11/15-112/handouts/hw5.html#Reasoning

# Put your answers below in a triple-quoted string.

# def f(n):
#     # assume n is a non-negative integer
#     if (n < 10):
#         return 1
#     else:
#         return 1 + f(n/10)

# """ returns the digit count of the n"""
 
# def f(a):
#    # assume a is a list of strings
#     if (len(a) == 0):
#         return ""
#     else:
#         x = f(a[1:])
#         if (len(x) > len(a[0])):
#             return x
#         else:
#             return a[0]
# """return the first string in the list if the length of the next string is 
# smaller or equal to the length of this string. Or, the last string 
# if the length of strings are increasing throughout the list."""
 

# def f(a):
#     # assume a is a list of integers
#     if (len(a) == 0):
#         return 0
#     elif (len(a) == 1):
#         return (a[0] % 2)
#     else:
#         i = len(a)//2
#         return f(a[:i]) + f(a[i:])
# """returns the number of odd numbers"""
 
# def f(n):
#     # assume n is a non-negative integer
#     if (n == 0):
#         return 1
#     else:
#         return 2*f(n-1)

# """returns 2 to n power"""
 
# def f(n):
#    # assume n is a non-negative integer
#     if (n == 0):
#         return 0
#     else:
#         return f(n-1) + 2*n - 1
# """return n square"""


# Hint: you may want to try this function with a few sample values.
# The answer should quickly become apparent, though you may wish to
# think about why the answer is in fact what it is.
 



############################
# Question 2               #
# No loops, only recursion #
############################

# Complete the functions below. Your solutions must be completely recursive.
# In particular, you will not receive any points if you use a "for" loop
# or a "while" loop.

'''
Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
and interleaves their characters starting with the first character in s1. 
For example, interleave('pto', 'yhn') would return the string "python". 
If one string is longer than the other, concatenate the rest of the 
remaining string onto the end of the new string. 
For example, ('a#', 'cD!f2') would return the string "ac#D!f2".
'''

def interleave(s1, s2):
    if len(s1)==0:
        return s2
    elif len(s2)==0:
        return s1
    else:
        return s1[0]+s2[0]+interleave(s1[1:],s2[1:])


'''
This function takes an integer n as input. It returns a string of the form
"1 1 2 1 2 3 1 2 3 4 1 2 3 4 5 ...... 1 2 3 4 5 6 7 8...n"
For example, if n is 4, it should return "1 1 2 1 2 3 1 2 3 4".
'''

def foo(n):
    if (n == 1): return "1"
    else:
        result=fooHelper(n,1)
        return foo(n-1)+" "+result
def fooHelper(n,s):
    if s==n:
        return str(s)
    else:
        return str(s)+" "+fooHelper(n,s+1)


'''
In class we saw an example of a non-destructive reverse function.
Write the same function, but this time make it destructive.
'''

def reverse(L):
    if (len(L) == 0 or len(L) == 1): return L
    else:
        last=L.pop(-1)
        start=L.pop(0)
        return [last] + reverse(L) + [start]


'''
The function removeDuplicates(s) takes a string s as input. 
If there is any character that repeats itself consecutively, 
it deletes the repeated copies. For example, if the input is "abccdeeef", 
the function returns "abcdef".
'''

def removeDuplicates(s):
    if len(s)==0:
        return ""
    elif len(s)==1:
        return s
    elif s[0]!=s[1]:
        return (s[0]+removeDuplicates(s[1:]))
    elif s[0]==s[1]:
        return (removeDuplicates(s[1:]))

'''
Write the recursive function flatten(L), which takes a list 
which may contain lists (which themselves may contain lists, and so on), 
and returns a single list (which does not contain any other lists) 
which contains each of the non-lists, in order, from the original list. 
This is called flattening the list. For example:
flatten([1,[2]]) returns [1,2]
flatten([1,2,[3,[4,5],6],7]) returns [1,2,3,4,5,6,7]
flatten(['wow', [2,[[]]], [True]]) returns ['wow', 2, True]
flatten([]) returns []
flatten([[]]) returns []
flatten(3) returns 3 (not a list)
'''

def flatten(L):
    if L==[]:
        return L
    if type(L[0])!=list:
        return (L[:1]+flatten(L[1:]))
    else:
        return flatten(L[0]+flatten(L[1:]))
        


'''
Write the function isPerfectNumber that takes a possibly-negative integer n 
and returns True if it is a perfect number and False otherwise, 
where a number is perfect if it is the sum of its positive divisors less than itself. 
We'll assume 0 is perfect.
The next perfect number is 6 because 6 = 1 + 2 + 3. 
The next one is 28 because 28 = 1 + 2 + 4 + 7 + 14. 
The next one is 496, then 8128, ...
'''

import math

#check if n and the sum of its divisors are the same
def isPerfectNumber(n):
    return n==isPNhelper(n)

#recursion of adding up the divisors except itself
def isPNhelper(n,m=1):
    if m==n-1:
        return 0
    if n%m!=0:
        return isPNhelper(n,m+1)
    if n%m==0:
        return m+isPNhelper(n,m+1)    


################
# Question 3   #
# Backtracking #
################

'''
Modify the solve(n, m, constraints) function seen in class
(for the nQueens problem) so that instead of returning a solution,
it returns the total number of solutions.'''

## basic code from website

def nQueens(n):
    queenRow = [-1] * n
    count=[0]
    def isLegal(row, col):
        # a position is legal if it's on the board (which we can assume
        # by way of our algorithm) and no prior queen (in a column < col)
        # attacks this position
        for qcol in range(col):
            qrow = queenRow[qcol]
            if ((qrow == row) or
                (qcol == col) or
                (qrow+qcol == row+col) or
                (qrow-qcol == row-col)):
                return False
        return True
    def solve(col):
        #base case
        if (col == n):
            count[0]+=1
        else:
            # try to place the queen in each row in turn in this col,
            # and then recursively solve the rest of the columns
            for row in range(n):
                if isLegal(row,col):
                    queenRow[col] = row # place the queen and hope it works
                    solution = solve(col+1)
                    if (solution != None):
                        # ta da! it did work
                        return solution
                    queenRow[col] = -1 # pick up the wrongly-placed queen
            # shoot, can't place the queen anywhere
            return None
    solve(0)
    return count[0]




'''
Background: we will say that a board is a square 2d list of integers. 
As with mazes, a solution is a path from the left-top to the right-bottom, 
only here we will only allow moves that are up, down, left and right (no diagonals). 
A solution is an "increasing path" (a coined term) if each value 
on the solution path is strictly larger than the one before it on that path. 
Consider this board:
    board = [[ 1, 3, 2, 4 ],
             [ 0, 4, 0, 3 ],
             [ 5, 6, 8, 9 ],
             [ 0, 7, 8, 9 ]]
This board has exactly one increasing path: 
right to 3, down to 4, down to 6, down to 7, right to 8, right to 9.
With this in mind, write the function increasingPathCount(board) 
that takes such a board and returns the number of increasing paths 
running from the left-top to right-bottom in that board. 
For the example board above, your function would return 1. 
Similarly, consider this board:
    board = [ [3, 5],
              [4, 7] ]
For this board, your function would return 2:
those paths being right,down and also down,right.
Your solution must be recursive (but you can use iteration too).
Also, you cannot simply explore every possible path to solve this problem.
'''


def increasingPathCount(board):
    result=[0]
    def solve(row,col):
        #if arrive at the end point, increase the count 
        #base case 
        if (row,col)==(len(board)-1,len(board)-1):
            result[0]+=1
        else:
            #recursions
            if col!=len(board)-1 and board[row][col+1]>board[row][col]:
                solve(row,col+1)
            if col!=0 and board[row][col-1]>board[row][col]:
                solve(row,col-1)
            if row!=0 and board[row-1][col]>board[row][col]:
                solve(row-1,col)
            if row!=len(board)-1 and board[row+1][col]>board[row][col]:
                solve(row+1,col)
    solve(0,0)
    return result[0]




##############
# Question 4 #
# H-fractal  #
##############

'''
Do Question 6 from here: https://www.cs.cmu.edu/~112/notes/hw9.html
Please follow the directions given in the hint:
"The H that is drawn right in the middle should always have the same size 
(the width and height should be half the window width and height). 
At each level, we draw new H's with half the dimensions of the previous level. 
This is why the window size never has to change 
(since 1 + 1/2 + 1/4 + 1/8 + ... = 2)."
The pictures in mathworld.wolfram.com are misleading!
At each level, the largest H in the middle should have the same size.
'''

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.level=0

#return a list of 4 tuples of end points in the shape H
def getPoints(data,level,point):
    x=point[0]
    y=point[1]
    w=int((data.width*0.5**(level+1))/2)
    h=int((data.height*0.5**(level+1))/2)
    return [(x-w,y-h),(x-w,y+h),(x+w,y-h),(x+w,y+h)]

def mousePressed(event, data):
    # use event.x and event.y
    pass

#increase and decrease the level depending on the key press
def keyPressed(event,data):
    if event.keysym == "Down":
        if data.level > 0:
            data.level -= 1
    elif event.keysym == "Up":
        data.level += 1

def timerFired(data):
    pass

######draw functions#######

def redrawAll(canvas, data):
    redrawAll2(canvas,data,(data.width/2,data.height/2))

#recursion draw
def redrawAll2(canvas, data, point=(-1,-1),level=0, points=[]):
    points=getPoints(data,level,point)
    drawHelper(canvas,data,level,points)
    if level==data.level:
        return
    for point in points:
        redrawAll2(canvas,data,point,level+1,points)

#draw H shape
def drawHelper(canvas,data,level,points):
    for i in range(0,len(points),2):
        canvas.create_line(points[i],points[i+1],fill="blue")
    midPoint=int((points[0][1]+points[1][1])/2)
    canvas.create_line(points[0][0],midPoint,points[2][0],midPoint,fill="red")

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
    data.timerDelay = 100 # milliseconds
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

def Hfractal():
    run(600,600)


####################################
# test cases
####################################

def testInterleave():
    print("testing interleave...")
    assert(interleave('a#', 'cD!f2')=="ac#D!f2")
    assert(interleave('abc', '')=="abc")
    print("passed")

def testFoo():
    print("testing foo...")
    assert(foo(4)=="1 1 2 1 2 3 1 2 3 4")
    assert(foo(3)=="1 1 2 1 2 3")
    print("passed")

def testReverse():
    print("testing reverse...")
    assert(reverse([1,2,3])==[3,2,1])
    assert(reverse([3,2,1])==[1,2,3])
    print("passed")

def testRemoveDuplicates():
    print("testing removeDuplicates...")
    assert(removeDuplicates("111")=="1")
    assert(removeDuplicates("1112")=="12")
    print("passed")

def testFlatten():
    print("testing flatten...")
    assert(flatten([[]])==[])
    assert(flatten([1,2,[3,[4,5],6],7])==[1,2,3,4,5,6,7])
    print("passed")

def testIsPerfectNumber():
    print("testing isPerfectNumber...")
    assert(isPerfectNumber(6))
    assert(not isPerfectNumber(7))
    print("passed")

def testNQueens():
    print("testing nQueens...")
    assert(nQueens(1)==1)
    assert(nQueens(2)==0)
    assert(nQueens(4)==2)
    print("passed")

def testIncreasingPathCount():
    print("testing increasingPathCount...")
    assert(increasingPathCount([ [3, 5],[4, 7] ])==2)
    assert(increasingPathCount([[ 1, 3, 2, 4 ],
             [ 0, 4, 0, 3 ],
             [ 5, 6, 8, 9 ],
             [ 0, 7, 8, 9 ]])==1)
    print("passed")

def testAll():
    testInterleave()
    testFoo()
    testReverse()
    testRemoveDuplicates()
    testFlatten()
    testIsPerfectNumber()
    testNQueens()
    testIncreasingPathCount()

