from turtle import left, right, forward, window_width, position, setpos, penup, pendown


def draw_borders_as_line(pen_size, border_spacing_units):
    penup()
    setpos((-window_width()/2, position()[1]))
    pendown()
    forward(window_width())
    penup()
    draw_in_direction(border_spacing_units * pen_size, 'left', 90)
    pendown()
    draw_in_direction(window_width(), 'left', 90)
    penup()
    draw_in_direction(border_spacing_units * pen_size, 'left', 90)
    draw_in_direction(0, 'left', 90)
    pendown()
    print()


def draw_in_direction(pixels, direction='left', angle=0):
    if direction == 'left':
        left(angle)
    elif direction == 'right':
        right(angle)
    else:
        raise ValueError(f'Direction can be either left or right. Received value: {direction}')
    forward(pixels)
