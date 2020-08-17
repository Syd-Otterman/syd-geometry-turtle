# Geometry Turtles
from turtle import *

t = Turtle()
t.speed(100)

def circle():
    t.pencolor('yellow')
    for i in range(12):
        t.forward(10)
        t.left(30)

def square():
    t.pencolor('red')
    for i in range(4):
        t.forward(50)
        t.right(90)

def triangle():
    t.pencolor('orange')
    for i in range(3):
        t.forward(50)
        t.right(30)

for i in range (75):
    circle()
    t.right(3)
    square()
    t.right(15)
    triangle()
    t.right(3)

input('hit enter to end program')
