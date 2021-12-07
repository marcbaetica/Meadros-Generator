from lib import MeanderDrawingBase
from turtle import window_width, window_height, penup, pendown, forward, backward, right, \
    left, pos, setpos


class SimpleMeander(MeanderDrawingBase):
    def __init__(self, pen_size, stroke_speed, pen_color, background_color):
        self.pen_size = pen_size
        self.stroke_speed = stroke_speed
        self.pen_color = pen_color
        self.background_color = background_color
        self.set_pen_properties(self.pen_size, self.stroke_speed, self.pen_color)
        self.set_background_color(background_color)

    def draw_borders(self, borders_type, spacing_pixels):
        pass

    def draw_pattern_once(self, direction, starting_position):
        pass

    def draw_pattern_corner(self):
        pass
