
from turtle import width, window_width, window_height, penup, pendown, forward, backward, right, left, speed
from time import sleep


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


def draw_in_direction(units_count, direction='left', angle=0):
    if direction == 'left':
        left(angle)
    elif direction == 'right':
        right(angle)
    else:
        raise ValueError(f'Direction can be either left or right. Received value: {direction}')
    forward(units_count * PEN_WIDTH)


def draw_horizontal_line_at_position(y):
    pass


def draw_borders(units_between_borders):
    penup()
    backward(window_width()/2)
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
        draw_in_direction(1)
        draw_in_direction(8, 'left', 90)
        draw_in_direction(8, 'right', 90)
        draw_in_direction(6, 'right', 90)
        draw_in_direction(4, 'right', 90)
        draw_in_direction(2, 'right', 90)
        draw_in_direction(2, 'right', 90)
        draw_in_direction(2, 'left', 90)
        draw_in_direction(4, 'left', 90)
        draw_in_direction(6, 'left', 90)
        draw_in_direction(7, 'left', 90)


set_pen_characteristics(PEN_WIDTH, 20)
print(window_width(), window_height())
# set_window_size(width, height)

draw_borders(12)
draw_pattern()
# sleep(5)