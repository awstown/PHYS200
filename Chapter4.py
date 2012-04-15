from TurtleWorld import *
from math import pi


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

##print bob
##
##for i in range(4):
##  fd(bob, 100)
##  lt(bob)
##    
##wait_for_user()



def square(t, length=100):
    polygon(t, length, 4)

def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arcLength = 2*pi*r*angle/360
    n = int(arcLength / 3) + 1
    stepLength = arcLength / n
    stepAngle  = float(angle) / n
    polyline(t, n, stepLength, stepAngle)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
    

square(bob)
square(bob, 75)
polygon(bob, 100, 5)
circle(bob, 100)
arc(bob, 50, 270)


wait_for_user()
