# Joyce Moon (seojinm) section B


import string
import random

# Write the function patternedMessage(message, pattern) 
# that takes two strings, a message and a pattern, and 
# returns a string produced by replacing the non-whitespace 
# characters in the pattern with the non-whitespace 
# characters in the message.


def patternedMessage(message, pattern):
    result=''''''
    i=0
    message=collapseWhiltespace(message)
    #delete newline before and after
    pattern=pattern.strip("\n")
    for c in pattern:
        if c not in string.whitespace:
            result+=message[i]
            i=(i+1)%(len(message))
        else: result+=c
    return result

#delete all whitespaces in the string
def collapseWhiltespace(s):
    result=""
    for c in s:
        if c not in string.whitespace:
            result+=c
        else:
            if result[-1] not in string.whitespace:
                result+=""
    return result


# Background: for this problem, a "gradebook" is a multiline 
# string where each row contains a student's name (one word, 
# all lowercase) followed by one or more comma-separated 
# integer grades. A gradebook always contains at least one student,
# and each row always contains at least one grade. Gradebooks can 
# also contain blank lines and lines starting with the "#" character, 
# which should be ignored.

def bestStudentAndAvg(gradebook):
    bestAvg=None
    bestStu=""
    # if(gradebook[0] in string.whitespace):
    #     gradebook = gradebook[1:]
    # if(len(gradebook) > 1 and gradebook[-1] in string.whitespace):
    #     gradebook = gradebook[:-1]
    for line in gradebook.splitlines():
        i=0
        currentSum=0
        currentStu=""
        if line in string.whitespace:
            continue
        # ignore line if it starts with #
        if not line.startswith("#"):
            for grades in line.split(","):
                if grades.islower():
                    currentStu=grades
                else:
                    i+=1
                    currentSum+=int(grades)
            if (i!=0) and (bestAvg == None or currentSum/i>=bestAvg):
                bestAvg=currentSum/i
                bestStu=currentStu
    return bestStu+":"+str(int(bestAvg))


# def bestStudentAndAvg(gradebook):
#     bestAvg=None
#     bestStu=""
#     if(gradebook[0] in string.whitespace):
#         gradebook = gradebook[1:]
#     if(len(gradebook) > 1 and gradebook[-1] in string.whitespace):
#         gradebook = gradebook[:-1]
#     for line in gradebook.splitlines():
#         i=0
#         currentSum=0
#         currentStu=""
#         # ignore line if it starts with #
#         if not line.startswith("#"):
#             for grades in line.split(","):
#                 if(grades.isalnum()):
#                     if grades.islower():
#                         currentStu = grades
#                     else:
#                         i+=1
#                         currentSum+=int(grades)
#             if (i!=0) and (bestAvg == None or currentSum/i>=bestAvg):
#                 bestAvg=currentSum/i
#                 bestStu=currentStu
#     return bestStu+":"+str(int(bestAvg))


# This is an open-ended exercise, without any test functions, 
# and without an autograder (the CA's will grade it manually). 
# First, read about the dice game of pig here. Then, write the 
# function playPig() that takes no parameters and plays a 
# console-based (that is, no graphics) two-player interactive 
# game of pig. The computer does not actually play a side, but 
# just manages play between two human players. This involves 
# showing the score and whose turn it is, managing the turn 
# sequence by rolling a die, asking the user what their move 
# will be, enacting that choice, switching sides, determining 
# a winner, and displaying suitable messages for all of this. 
# While you may want to do more than this, say using more exotic 
# rules, or using a GUI rather than console input, resist the urge. 
# We will grade you on how closely you abide to this spec. That said, 
# this spec is broad, so you have some leeway on how you design this, 
# both in terms of the user experience as well as how your code is 
# written. Hint: you will almost surely want to use random.randint(1, 6) 
# to randomly roll your die. Look it up to see the details.

def playPig():
    score1=0
    score2=0
    player=1
    currentplayer=1
    while score1<100 and score2<100:
        currentsum=0
        print ("player"+str(currentplayer)+"'s turn")
        while player==currentplayer:
            number=random.randint(1,6)
            print ("player"+str(currentplayer)+" rolled a "+str(number))
            #if player rolls 1 change player without adding anything to the player's total score
            if number==1: 
                currentplayer=2 if currentplayer==1 else 1
            else:
                currentsum+=number
                action=input("Do you want to hold or continue?")
                #if player choose hold, add current sum of score to player's total score.
                if action == "hold":
                    if currentplayer==1:
                        score1+=currentsum 
                    elif currentplayer==2:
                        score2+=currentsum	
                    currentplayer=2 if currentplayer==1 else 1
        print("player1's score = "+str(score1)+"\n"+"player2's score = "+ str(score2))
        if score1<100 and score2<100:
            player=2 if player==1 else 1
    print("player"+str(player)+" won!!!")






####################################################################
# ignore_rest: The autograder will ignore all code below here
####################################################################


def testPatternedMessage():
    print("---Testing patternedMessage")
    assert(patternedMessage('A', '\n*\n') == """A""")
    assert(patternedMessage("Three Diamonds!", """
*     *     *
""") == """T     h     r"""
           )
    assert(patternedMessage("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
""") ==
"""                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G""")
    assert(patternedMessage("Three Diamonds!", """
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
""") == """    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n"""
           )
    print("Passed!!")


def testbestStudentandAvg():
    print("---Testing bestStudentAndAvg")
    assert(bestStudentAndAvg("""wilma,91,93
fred,80,85,90,95,100""") ==  "wilma:92")
    assert(bestStudentAndAvg("""# nope
joyce,91""") ==  "joyce:91")
    assert(bestStudentAndAvg("""# nope
alex,0
#
bay,50,100""" ) == "bay:75")
    print("Passed!!")


def testAll():
	testPatternedMessage()
	testbestStudentandAvg()
