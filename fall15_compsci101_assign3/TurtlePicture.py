'''
Created on Sep 15, 2015

@author: Jonathan Yu
'''

import math
import turtle
wn = turtle.Screen()

def circleLine(turtle, center, heading, length, numCircles, numLines):
    #draws a set of lines, which are made up of circles, that are rotated around a point
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    turtle.setheading(heading)
    radius = (length / numCircles) / 2
    for k in range(numLines / 2):
        lineHeading = turtle.heading()
        turtle.penup()
        turtle.forward(length / 2)
        turtle.pendown()
        turtle.left(90)
        for l in range(numCircles):
            turtle.circle(radius, 180)
            turtle.setheading(lineHeading + 90)
        turtle.setheading(lineHeading - 90)
        for l in range(numCircles):
            turtle.circle(radius, 180)
            turtle.setheading(lineHeading - 90)
        turtle.penup()
        turtle.goto(center)
        turtle.pendown()
        turtle.right(360 / numLines)

def circularSpiral(turtle, center, heading, color):
    #draws a circular spiral with a stamped symbol at its center
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    turtle.setheading(heading)
    turtle.color(color)
    for k in range(8):
        #draws the stamped symbol by stamping the turtle in 8 different rotated positions
        turtle.stamp()
        turtle.right(45)
    for k in range(130):
        turtle.circle(k, 10 * 3.14)
   
def diamond(turtle, top, color):
    #draws a diamond with congruent sides (rotated square) with its center at the origin
    turtle.penup()
    turtle.goto(top)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.color(color)
    turtle.begin_fill()
    length = top[1] * math.sqrt(2)
    for k in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()
    
def octagon(turtle, radius, color):
    #draws a regular octagon with its center at the origin
    length = (2 * radius) / (1 + (2 / math.sqrt(2)))
    turtle.penup()
    turtle.goto(-0.5 * length, radius)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(color)
    turtle.begin_fill()
    for k in range(8):
        turtle.forward(length)
        turtle.right(45)
    turtle.end_fill()
                        
def triforce(turtle, bottom, heading, length, color, penSize):
    #draws a triforce with magenta dots as the vertices of the larger triangle
    turtle.penup()
    turtle.goto(bottom)
    turtle.pendown()
    turtle.setheading(heading)
    turtle.color(color)
    turtle.pensize(penSize)
    turtle.forward(length / 2)
    for k in range(2):
        turtle.dot(5,"magenta")
        turtle.left(120)
        turtle.forward(length)
    turtle.left(120)
    turtle.forward(length / 2)
    turtle.left(120)
    turtle.forward(length / 2)
    for k in range(2):
        turtle.right(120)
        turtle.forward(length / 2)
        
def triforceFlower(turtle, center, heading, length, color):
    #draws a flower made up of triforces rotated around a point
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    turtle.setheading(heading)
    turtle.color(color)
    for k in range(20):
        triforce(turtle, turtle.position(), turtle.heading(), length, turtle.color()[0], turtle.pensize())
        turtle.left(120)
        turtle.right(18)

def picture():
    leonardo = turtle.Turtle()
    leonardo.speed(0)
    circleLine(leonardo, leonardo.position(), 0, 7 * 75 * math.sqrt(3) + 30, 10, 8)
    octagon(leonardo, 3 * 75 * math.sqrt(3), "black")
    diamond(leonardo, (0, 75 * math.sqrt(3)), "blue")
    triforceFlower(leonardo, (-75 * math.sqrt(3), 0), 0, 300, "red")
    circularSpiral(leonardo, leonardo.position(), 0, "green")
    triforceFlower(leonardo, (75 * math.sqrt(3), 0), 0, 300, "red")
    circularSpiral(leonardo, leonardo.position(), 0, "green")
    triforceFlower(leonardo, (0,75 * math.sqrt(3)), 0, 300, "red")
    circularSpiral(leonardo, leonardo.position(), 0, "green")
    triforceFlower(leonardo, (0,-75 * math.sqrt(3)), 0, 300, "red")
    circularSpiral(leonardo, leonardo.position(), 0, "green")
    triforce(leonardo, (0, -25 * math.sqrt(3)), 0, 100, "yellow", 5)

if __name__ == '__main__':
    picture()
    wn.exitonclick()