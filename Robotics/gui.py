'''
Created on Oct 7, 2015

@author: Jonathan Yu
'''

import threading
import time
import turtle

#sets up window
wn = turtle.Screen()
wn.bgcolor("light blue")
#sets up turtle
raphael = turtle.Turtle()
raphael.speed(0)
raphael.shape("turtle")
raphael.shapesize(2, 2, 2)
#initializes acceleration and velocity vectors
accel = [0, 0]
vel = [0, 0]

def simulate():
    #simulates motion of turtle in 1 second intervals
    threading.Timer(1.0, simulate).start()
    global vel
    dest = (raphael.position()[0] + vel[0] + 0.5 * accel[0], raphael.position()[1] + vel[1] + 0.5 * accel[1])
    raphael.setheading(raphael.towards(dest))
    raphael.goto(dest)
    #updates velocity based off of acceleration
    for k in range(len(vel)):
        vel[k] += accel[k]

if __name__ == '__main__':
    global accel
    simulate()
    accel = [5, 7]
    time.sleep(3)
    accel = [3, -4]
    time.sleep(3)
    accel = [8, 0]
    time.sleep(3)
    accel = [-10, -10]
    wn.exitonclick()
