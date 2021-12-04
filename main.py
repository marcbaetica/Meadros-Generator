
from turtle import width, window_width, window_height, penup, pendown, forward, backward, right, left, speed
from time import sleep


PEN_WIDTH = 5



"""
8 up
8 right
6 down
4 left
2 up
2 right
2 up
4 left
6 down
8 right
"""


def set_pen_characteristics(pen_size, stroke_speed):
    width(pen_size)
    speed(stroke_speed)


def set_window_size(width, height):
    pass


def draw_borders():
    penup()
    backward(window_width()/2)
    pendown()
    forward(window_width())
    penup()
    backward(window_width())
    left(90)
    forward(12*PEN_WIDTH)
    right(90)
    pendown()
    forward(window_width())


def draw_pattern():
    penup()
    backward(window_width())
    right(90)
    forward(10*PEN_WIDTH)
    left(90)
    pendown()
    for _ in range(window_width()//(PEN_WIDTH*10)+1):  # TODO: round up
        forward(1*PEN_WIDTH)
        left(90)
        forward(8*PEN_WIDTH)
        right(90)
        forward(8*PEN_WIDTH)
        right(90)
        forward(6*PEN_WIDTH)
        right(90)
        forward(4*PEN_WIDTH)
        right(90)
        forward(2*PEN_WIDTH)
        right(90)
        forward(2*PEN_WIDTH)
        left(90)
        forward(2*PEN_WIDTH)
        left(90)
        forward(4*PEN_WIDTH)
        left(90)
        forward(6*PEN_WIDTH)
        left(90)
        forward(7*PEN_WIDTH)


set_pen_characteristics(PEN_WIDTH, 100)
print(window_width(), window_height())
# set_window_size(width, height)

sleep(3)
draw_borders()
draw_pattern()
sleep(5)