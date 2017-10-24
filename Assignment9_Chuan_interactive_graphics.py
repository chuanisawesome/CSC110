#Assignment_9
#interactive graphics program
#finds the intersection(s) of a circle and horizontal line.

from graphics import *
from math import *

def main():

    # Creates the graphic window 
    win = GraphWin("Mouse Click", 720, 720)
    win.setCoords(-10,-10,10,10)
    message = Text(Point(0,0), "Click anywhere to set the circle's radius")
    message.draw(win)
    p = win.getMouse()
    message.undraw()
    pX = p.getX()
    pY = p.getY()
    
    # Draws the circle on the radius that is given
    radius = (sqrt((pX-0)**2+(pY-0)**2))
    cir = Circle(Point(0,0), radius)
    cir.draw(win)

    # Draws the interface
    Text(Point(-1,4), "Enter the intercept: ").draw(win)
    input = Entry(Point(1,4), 6)
    input.setText("0.0")
    input.draw(win)
    button = Text(Point(0,3.0),"Find the intersect")
    button.draw(win)
    Rectangle(Point(-2,2.5), Point(2,3.5)).draw(win)


    # wait for the user to click
    win.getMouse()

    # Draws the horizontal line on the y-intercept
    Yinter = eval(input.getText())
    lin = Line(Point(-10,Yinter), Point(10,Yinter))
    lin.draw(win)

    # Calculates the x value
    x1 = -sqrt(radius**2-Yinter**2)
    x2 = sqrt(radius**2+Yinter**2)

    # Creates intersection points
    if x1 or x2 >= 1:
        point1 = Point(x1,Yinter)
        point1.draw(win)
        point1.setFill('red')
        point2 = Point(x2,Yinter)
        point2.draw(win)
        point2.setFill('red')

    # Prints value on screen
    message = Text(Point(0,-7),"The x values are +/-" + " " + str(x1) + "\nand" + " " + str(x2))
    message.setSize(13)
    message.draw(win)
    
    # Prints "click to exit"
    ex = Text(Point(0,0),"Click to exit")
    ex.setSize(12)
    ex.draw(win)

    # waits for a mouse to click then close
    win.getMouse()
    win.close()
 
main()
    
