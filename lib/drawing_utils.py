from turtle import left, right, forward


def draw_in_direction(units_count, pen_width, direction='left', angle=0):
    if direction == 'left':
        left(angle)
    elif direction == 'right':
        right(angle)
    else:
        raise ValueError(f'Direction can be either left or right. Received value: {direction}')
    forward(units_count * pen_width)
