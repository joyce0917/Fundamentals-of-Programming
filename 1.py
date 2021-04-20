import random
def doPigStrategyAnalysis():
    player1WinTimes=0
    player2WinTimes=0
    for i in range (10000):
        Winner=playGame()
        if Winner=="player 1":
            player1WinTimes+=1
        else:
            player2WinTimes+=1
    
    return player1WinTimes


def playGame():
    pointPlayer1=0
    pointPlayer2=0
    while pointPlayer1 <100 and pointPlayer2 <100: 
        r1 = turns(1) #computes the score for player 1 in the function turns()
        pointPlayer1 += r1
        # print(pointPlayer1,pointPlayer2)
        r2 = turns(2)
        pointPlayer2 += r2
        # print(pointPlayer1,pointPlayer2)
        
    if pointPlayer1>=100:
        return ("player 1")
    if pointPlayer2>=100:
        return ("player 2")
    

def turns(player):
    point=0
    continueRollDice=1
    while continueRollDice==1: #repeatedly throw dice in their respective turns
        r=roll_die()
        # print(player,"die",r)
        if player == 1:
            if r==1:
                point=0
                continueRollDice=2
                break
            else:
                point+=r
                continueRollDice=1
                if point>=20:
                    continueRollDice=2
                    break
        if player==2: 
            if r==1:
                point=0
                continueRollDice=2
                break
            else:
                point+=r
                action=random.randint(0,1) 
                # print(action,"action")
                if action == 0:
                    continueRollDice=2
                    # break
                else:
                    continueRollDice=1
    return point


def roll_die():
    r= random.randint (1,6)
    return r

doPigStrategyAnalysis()