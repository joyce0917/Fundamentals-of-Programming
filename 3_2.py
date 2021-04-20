#joyce moon (seojinm) hw 3.2

"""
slow1
- it goes through every elements in b, which is a copy list of a, and 
adds 1 to c everytime. So, the return value (c) is len(A).
- runtime: O(N)

def faster1(a):
    return len(a) #O(1)

-this is O(1), because len(a) is O(1)

#############

slow2
- it goes through nested for loop of len(a) and counts the number 
of times they are the same.This returns True if there is no repetition in a.
- runtime: O(N^2)

def faster2(a):
    return len(a)==len(set(a)) #O(N)

- this is O(N). making a list into a set has to go through
all the elements once.

############

slow3
- it goes through every elements in b and returns the number of elements
not in a.
- runtime: O(N^2)

def faster3(a,b):
    a=set(a) #O(N)
    count=0
    for c in b: #O(N)
        if c not in a: #O(1)
            count+=1
    return count

- this is O(N). because "a=set(a)" and the for loop are in same indentation, 
so they are O(N)+O(N)=O(N)

###########

slow4
- it goes through two lists and return the biggest difference in the 
elements of two lists.
- runtime: O(N^2)

def faster4(a,b):
    maxa=max(a) #O(N)
    maxb=max(b) #O(N)
    mina=min(a) #O(N)
    minb=min(b) #O(N)
    if abs(maxa-minb)>abs(maxb-mina): O(1)
        return abs(maxa-minb)
    return abs(maxb-mina)

- it is O(N). because the biggest big O is O(N) where variables are initialized 
as min and max.

###########

slow5
- it goes through two lists and return the smallest difference in the 
elements of two lists.
- runtime: O(N^2)

import bisect
def faster5(a,b):
    a.sort() #O(N)
    min1=abs(a[0]-b[0])
    for c in b: #O(N)
        index=bisect.bisect(a,c) #O(logN)
        if index==0:
            min2=abs(c-a[index])
        elif index==len(a):
            min2=abs(c-a[index-1])
        else:
            min2=min(abs(c-a[index]), abs(c-a[index-1]))
        if min1>min2:
            min1=min2
    return min1

- it is O(NlogN). since bisect uses binary search it's logN and it's in for loop 
so N*logN=NlogN

"""

import copy
import math

#flip  row and col
def invertDictionary(d):
    newDict={}
    for keys in d:
        values=d[keys]
        if values not in newDict:
            newDict[values]=set()
        newDict[values].add(keys)
    return newDict

# return friends of friends of a person excluding himself and his friends
def friendsOfFriends(d):
    newDict={}
    #add all the friends of his friends
    for people in d:
        if people not in newDict:
            newDict[people]=set()
        for friends in d[people]:
            if friends in d:
                for friends2 in d[friends]:
                    newDict[people].add(friends2)
    #remove his friends
    for people in d:
        for friends in d[people]:
            if friends in newDict[people]:
                newDict[people].remove(friends)
    #remove himself
    for people in newDict:
        if people in newDict[people]:
            newDict[people].remove(people)
    return newDict

#find biggest sum of two elements in the list
def largestSumOfPairs(a):
    if len(a)<2:
        return None
    b=copy.deepcopy(a) # bc original list shouldn't be destroyed
    max1=max(b)
    b.remove(max1)
    max2=max(b)
    return max1+max2


# check if the list contains pythogorean triple
def containsPythagoreanTriple(a):
    d={}
    a=sorted(a)
    #make the list into dictionary.count the number of times key appear in list
    for keys in a:
        d[keys]=d.get(keys,0)+1
    for index1 in range (len(a)-1):
        num1=a[index1]
        if num1>0:
            d[num1]-=1
            for index2 in range (index1+1,len(a)):
                num2=a[index2]
                d[num2]-=1
                num3=math.sqrt(num1**2+num2**2)
                if num3 in d and d[num3]>=1:
                    return True
                d[num2]+=1
    return False



####################################################################
# ignore_rest: The autograder will ignore all code below here
####################################################################

def testFaster1():
    print("---testing faster1...")
    assert(faster1([1])==1)
    assert(faster1([1,2,3,4,5,6,7,8,9])==9)
    assert(faster1([]) == 0)
    print("Passed!")  

def testFaster2():
    print("---testing faster2")
    assert(faster2([1,2,3])== True)
    assert(faster2([0,1,2,0])== False)
    assert(faster2([-1,1,4])==True)
    print("Passed!")   

def testFaster3():
    print("---testing faster3")
    assert(faster3([1,2,3,4,5],[1,2,3,4,5])==0)
    assert(faster3([0,1,2,3],[1,2,3,4])== 1)
    assert(faster3([7],[0])==1)
    print("Passed!")   

def testFaster4():
    print("---testing faster4")
    assert(faster4([1,2,3],[1,2,3]) == 2)
    assert(faster4([1],[2]) == 1)
    assert(faster4([1],[7]) == 6)
    print("Passed!")

def testFaster5():
    print("---testing faster5")
    assert(faster5([1,2,3],[1,2,3]) == 0)
    assert(faster5([1,2],[3,4]) == 1)
    assert(faster5([1,2,3],[3,4,5]) == 0)
    print("Passed!")


def testinvertDictionary():
    print('---testing invertDictionary')
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == {2:set([1]), 
        3:set([2,5]), 4:set([3])})
    assert(invertDictionary({1:1,0:1,500:1})=={1:set([1,0,500])})
    assert(invertDictionary({}) == {})
    print("Passed!")


def testfriendsOfFriends():
    print("---testing friendsOfFriends")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    fof = friendsOfFriends(d)
    assert(fof["fred"] == {"dino"})
    assert(fof["wilma"] == {"barney","bam-bam"})
    assert(friendsOfFriends({'C': set(), 'B': {'C', 'A', 'E', 'D'}, 
        'A': {'B', 'F', 'D'}, 'F': {'D'}, 'E': {'C', 'D'}, 
        'D': {'B', 'F', 'E'}})=={'C': set(), 'B': {'F'}, 'A': {'C', 'E'}, 
    'F': {'B', 'E'}, 'E': {'B', 'F'}, 'D': {'C', 'A'}})
    print("Passed!")


def testLargestSumOfPairs():
    print("---testing largestSumOfPairs")
    assert(largestSumOfPairs([-1234,10,23,4,0,1])==33)
    assert(largestSumOfPairs([1,2,3,4,5])==9)
    assert(largestSumOfPairs([0])==None)
    print("Passed!")


def testPythagoreanTriple():
    print("---Testing pythagorean")
    assert(containsPythagoreanTriple([1,2,3,4,5]))
    assert(containsPythagoreanTriple([12,1,5,13,9]))
    assert(not containsPythagoreanTriple([12,1,-5,13,9]))
    print("Passed!")  

def testAll():
    testfriendsOfFriends()
    testinvertDictionary()
    testPythagoreanTriple()
    testLargestSumOfPairs()
