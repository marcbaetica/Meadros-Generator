from turtle import left, right, forward, seth, setpos, penup, pendown


def draw_outer_border(corners, increment_size):
    upper_left_corner = corners[3]
    lower_right_corner = corners[1]

    buffer = 2 * increment_size

    outer_border_length = abs(upper_left_corner[0]-buffer) + abs(lower_right_corner[0]+buffer)
    outer_border_width = abs(upper_left_corner[1]+buffer) + abs(lower_right_corner[1]-buffer)

    penup()
    setpos(upper_left_corner[0]-buffer, upper_left_corner[1]+buffer)
    pendown()
    seth(0)  # Point East.
    draw_in_direction(outer_border_length)
    draw_in_direction(outer_border_width, 'right', 90)
    draw_in_direction(outer_border_length, 'right', 90)
    draw_in_direction(outer_border_width, 'right', 90)


def draw_inner_border(corners, increment_size, pattern_width):
    upper_left_corner = corners[3]
    lower_right_corner = corners[1]

    # Pattern width moves us to the edge, +1 is for the empty space.
    buffer = increment_size * (pattern_width + 1)

    print(upper_left_corner, lower_right_corner)
    inner_border_length = abs(upper_left_corner[0]+buffer) + abs(lower_right_corner[0]-buffer)
    inner_border_width = upper_left_corner[1]-buffer + abs(lower_right_corner[1]+buffer)

    penup()
    setpos(upper_left_corner[0]+buffer, upper_left_corner[1]-buffer)
    pendown()
    seth(0)  # Point East.
    draw_in_direction(inner_border_length)
    draw_in_direction(inner_border_width, 'right', 90)
    draw_in_direction(inner_border_length, 'right', 90)
    draw_in_direction(inner_border_width, 'right', 90)


def draw_borders(pen_size, pattern_width, corners):
    increment_size = pen_size

    draw_outer_border(corners, increment_size)
    draw_inner_border(corners, increment_size, pattern_width)


def draw_in_direction(pixels, direction='left', angle=0):
    if direction == 'left':
        left(angle)
    elif direction == 'right':
        right(angle)
    else:
        raise ValueError(f'Direction can be either left or right. Received value: {direction}')
    forward(pixels)
