#Joyce Moon (seojinm) hw 2.2

import random


#return centered triangle
def myTriangle(height):
    result=""
    for j in range (height):
        spaces=height*2-1
        numStar=j*2+1
        result+=(" "*((spaces-numStar)//2)+"*"*(numStar))
        result+=(" "*((spaces-numStar)//2)+"\n")
    return result[:-1]


#return X
def myX(n):
    result=""
    for i in range (-n,n+1):
        m=-n
        for j in range (2*n+1):
            if abs(i)==abs(m):
                result+=("*")
            else:
                result+=(" ")
            m+=1
        result+="\n"
    return result[:-1]


####################################################################
# ignore_rest: The autograder will ignore all code below here
####################################################################


def playPig():
    (player1win,score1,score2,player,currentplayer)=(0,0,0,1,1)
    while score1 < 100 and score2 < 100:
        currentsum = 0
        while player == currentplayer:
            number = random.randint(1,6)
            #if player rolls 1 change player
            if number==1: currentplayer=2 if currentplayer==1 else 1
            else:
                if currentplayer==1:
                    currentsum+=number
                    if currentsum>=20:
                        score1+=currentsum
                        currentplayer=2
                elif currentplayer==2: 
                    currentsum+=number
                    action=random.randint(0,1)
                    if action==1:
                        score2+=currentsum   
                        currentplayer=1
        if score1<100 and score2<100: player=2 if player==1 else 1
    return player

def doPigStrategyAnalysis():
    trials=1000
    success=0
    for trial in range (trials):
        if playPig()==1:
            success+=1
    return success/trials

def testMyTriangle():
    print("---Testing myTriangle")
    assert(myTriangle(0) == '')
    assert(myTriangle(1) == '*')
    assert(myTriangle(2) == ' * \n***')
    assert(myTriangle(3) == '  *  \n *** \n*****')
    print ("Passed!!")

def testMyX():
    print("---Testing myX")
    assert(myX(0) == "*")
    assert(myX(1) == "* *\n * \n* *")
    assert(myX(2) == "*   *\n * * \n  *  \n * * \n*   *")
    assert(myX(3) == "*     *\n *   * \n  * *  \n   *   \n  * *  \n *   * \n*     *")
    print ("Passed!!")

def testAll():
    testMyTriangle()
    testMyX()
