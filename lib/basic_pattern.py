# Note: In each method pen always pointing in the right direction with pen down.


import turtle
from time import sleep


def setup():
    turtle.speed(20)
    turtle.pen()
    turtle.width(10)


def upper_line(pixels_up):
    turtle.penup()
    turtle.backward(350)
    turtle.left(90)
    turtle.forward(pixels_up)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(700)


def lower_line(pixels_down):
    turtle.penup()
    turtle.right(90)
    turtle.forward(pixels_down)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(700)
    turtle.right(180)


def draw_pattern():
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.pendown()
    for _ in range(12):
        turtle.left(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)


setup()
# turtle.right(90)
upper_line(100)
lower_line(80)
draw_pattern()
sleep(5)
