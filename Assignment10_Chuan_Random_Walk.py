#Random Walk

from random import random
import math

def main():
    # Prints intro 
    printIntro()
    # Call the method getInput
    n=getInput()
    # Call the function walkRandomly
    steps = walkRandomly(n)
    printSummary(steps,n)

def printIntro():
    # Tells user what the program does
    print("This program helps users")
    print("figure out the distance from start")
    print("with n steps taken")

def getInput():
    # User input
    n = eval(input("How many steps you want to walk?"))
    return n

def walkRandomly(n):
    # Distance left or right
    distanceX = 0
    # Distance front or back
    distanceY = 0
    # Simulates random walk
    for i in range(n):
        angle = randomDirection()
        distanceX = distanceX + math.cos(angle)
        distanceY = distanceY + math.sin(angle)
        totalDistance = pow(distanceX,2) + pow(distanceY,2)
        totalDistance = pow(totalDistance, 0.5)
    return totalDistance

def randomDirection():
    # uses random to get a random angle
    randomNo = random()
    angle = randomNo*2*math.pi
    return angle

def printSummary(steps,n):
    # Prints the summary
    print("\nTotal steps taken:{0}".format(n))
    print("Distance from start:{0}".format(steps))

main()
