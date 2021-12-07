from lib.drawing_utils import draw_in_direction
from time import sleep
from turtle import width, window_width, window_height, penup, pendown, forward, backward, right, left, speed, pos, setpos


PEN_WIDTH = 5


"""
PATTERN
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


def draw_horizontal_line_at_position(y):
    pass


def draw_borders(units_between_borders):
    pos()
    backward(window_width()/2)
    print(pos())  # (-384.00,0.00)
    print(int(pos()[0]))
    pendown()
    forward(window_width())
    penup()
    backward(window_width())
    left(90)
    forward(units_between_borders*PEN_WIDTH)
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
        draw_in_direction(1, PEN_WIDTH)
        draw_in_direction(8, PEN_WIDTH, 'left', 90)
        draw_in_direction(8, PEN_WIDTH, 'right', 90)
        draw_in_direction(6, PEN_WIDTH, 'right', 90)
        draw_in_direction(4, PEN_WIDTH, 'right', 90)
        draw_in_direction(2, PEN_WIDTH,  'right', 90)
        draw_in_direction(2, PEN_WIDTH, 'right', 90)
        draw_in_direction(2, PEN_WIDTH, 'left', 90)
        draw_in_direction(4, PEN_WIDTH, 'left', 90)
        draw_in_direction(6, PEN_WIDTH, 'left', 90)
        draw_in_direction(7, PEN_WIDTH, 'left', 90)


set_pen_characteristics(PEN_WIDTH, 20)
print(window_width(), window_height())
# set_window_size(width, height)

draw_borders(12)
draw_pattern()
# sleep(5)
