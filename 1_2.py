# 15-112, Summer 1, Homework 1.2
######################################
# Full name: Joyce Moon
# Andrew ID: seojinm
# Section: B
######################################

######### IMPORTANT NOTE #############
# You are not allowed to import any modules, or use loops, strings, lists, or recursion.


# Given an integer n, return the ones-digit of n,
# i.e. the first digit of n from the right.
def onesDigit(n):
    return abs(n)%10


# Given an integer n, return the tens-digit of n,
# i.e. the 2nd digit of n from the right.
def tensDigit(n):
    return (abs(n)//10)%10


# Given an integer n and k, return the (k+1)'th digit of n from the right.
# So k = 0 refers to the ones-digit, k = 1 refers to the tens-digit, etc.
# You can assume k is non-negative.
def kthDigit(n, k):
    return (abs(n)//10**k)%10


# Given integers n, k and d, replace the kthDigit of n with d.
# You can assume k is non-negative, and d is an integer between 0 and 9.
def setKthDigit(n, k, d):
    if n<0:
        return n-(d-kthDigit(n,k))*(10**k)
    return n+(d-kthDigit(n,k))*(10**k)


# Given as input four int or float values representing the (x,y)   
# coordinates of two points, return the distance between those points.
def distance(x1, y1, x2, y2):
    return ((abs(x2-x1)**2)+(abs(y2-y1)**2))**0.5


# Given an integer n, round it to the nearest integer.
# You are not allowed to use the built-in round function.
def myRound(n):
    if n%1==0:
        return n
    elif (n>0 and (abs(n)%1<0.5)) or (n<0 and (abs(n)%1>0.5)):
        return (n//1)
    elif (n>0 and (abs(n)%1>=0.5)) or (n<0 and (abs(n)%1<=0.5)):
        return (n//1)+1


# Given an integer n, round it down to the nearest integer.
# You are not allowed to use anything from the math module.
def floor(n):
    return n//1


# Given an integer n, round it to the nearest odd integer.
# In case of a tie, round down.
def nearestOdd(n):
    if n%2==0:
        return n-1
    else:
        return 2*(n//2)+1


# See here for the description of the function: 
# https://www.cs.cmu.edu/~112/notes/hw1.html
def nearestBusStop(street):
    if street%8<=4:
        return 8*(street//8)
    else:
        return 8*(street//8+1)



# If you have written the functions correctly, you should not get any errors
# when you run this file, i.e., you should pass all the tests.

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

import math

def almostEqual(d1, d2, epsilon=10**-7):
    return abs(d1 - d2) < epsilon
    
def testOnesDigit():
    print("Testing onesDigit()...", end="")
    assert(onesDigit(0) == 0)
    assert(onesDigit(789) == 9)
    assert(onesDigit(7) == 7)
    assert(onesDigit(-1234) == 4)
    assert(onesDigit(-3) == 3)
    print("Passed.")

def testTensDigit():
    print("Testing tensDigit()...", end="")
    assert(tensDigit(0) == 0)
    assert(tensDigit(1) == 0)
    assert(tensDigit(10) == 1)
    assert(tensDigit(21) == 2)
    assert(tensDigit(-1234) == 3)
    assert(tensDigit(-3) == 0)
    assert(tensDigit(-10) == 1)
    print("Passed.")

def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert(kthDigit(0,0) == 0)
    assert(kthDigit(789, 0) == 9)
    assert(kthDigit(789, 1) == 8)
    assert(kthDigit(789, 2) == 7)
    assert(kthDigit(789, 3) == 0)
    assert(kthDigit(-1234, 3) == 1)
    assert(kthDigit(-3, 1) == 0)
    print("Passed.")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    print("Passed.")

def testDistance():
    print("Testing distance()...", end="")
    assert(distance(0, 0, 0, 0) == 0)
    assert(distance(0, 0, 100, 0) == 100)
    assert(almostEqual(distance(1.1, 2.2, 3.3, -4.4), 6.957010852370434))
    print("Passed.")
    
def testMyRound():
    print("Testing myRound()...", end="")
    assert(myRound(0) == 0)
    assert(myRound(1) == 1)
    assert(myRound(-1) == -1)
    assert(myRound(1.1) == 1)
    assert(myRound(1.5) == 2)
    assert(myRound(1.9) == 2)
    assert(myRound(-1.1) == -1)
    assert(myRound(-1.5) == -1)
    assert(myRound(-1.9) == -2)
    assert(myRound(0.1) == 0)
    assert(myRound(0.5) == 1)
    assert(myRound(0.9) == 1)
    assert(myRound(-0.1) == 0)
    assert(myRound(-0.5) == 0)
    assert(myRound(-0.9) == -1)
    print("Passed.")

def testFloor():
    print("Testing floor()...", end="")
    assert(floor(0) == math.floor(0))
    assert(floor(1) == math.floor(1))
    assert(floor(-1) == math.floor(-1))
    assert(floor(1.1) == math.floor(1.1))
    assert(floor(1.5) == math.floor(1.5))
    assert(floor(1.9) == math.floor(1.9))
    assert(floor(-1.1) == math.floor(-1.1))
    assert(floor(-1.5) == math.floor(-1.5))
    assert(floor(-1.9) == math.floor(-1.9))
    assert(floor(0.1) == math.floor(0.1))
    assert(floor(0.5) == math.floor(0.5))
    assert(floor(0.9) == math.floor(0.9))
    assert(floor(-0.1) == math.floor(-0.1))
    assert(floor(-0.5) == math.floor(-0.5))
    assert(floor(-0.9) == math.floor(-0.9))
    print("Passed.")

def testNearestOdd():
    print("Testing nearestOdd()...", end="")
    assert(nearestOdd(0) == -1)
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print("Passed.")

def testNearestBusStop():
    print("Testing nearestBusStop()...", end="")
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print("Passed.")


def testAll():
    testOnesDigit()
    testTensDigit()
    testKthDigit()
    testSetKthDigit()
    testDistance()
    testMyRound()
    testFloor()
    testNearestOdd()
    testNearestBusStop()


testAll()
