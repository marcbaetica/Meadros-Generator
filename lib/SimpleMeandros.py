from lib.drawing_utils import draw_borders_as_line, draw_in_direction
from lib.MeanderDrawingBase import MeandrosDrawingBase
from turtle import window_width, window_height, penup, pendown, forward, backward, right, \
    left, position, setpos


BORDER_SPACING_UNITS = 6


class SimpleMeandros(MeandrosDrawingBase):
    def __init__(self, pen_size, stroke_speed, pen_color, background_color, meandros_type):
        self.pen_size = pen_size
        self.stroke_speed = stroke_speed
        self.pen_color = pen_color
        self.set_pen_properties(self.pen_size, self.stroke_speed, self.pen_color)
        self.background_color = background_color
        self.set_background_color(background_color)
        self.meandros_type = meandros_type

    def _draw_borders(self):
        if self.meandros_type == 'line':
            draw_borders_as_line(self.pen_size, BORDER_SPACING_UNITS)

    def _draw_pattern_once(self):
        print(position())
        draw_in_direction(self.pen_size * 1)
        draw_in_direction(self.pen_size * 2, 'left', 90)
        draw_in_direction(self.pen_size * 2, 'right', 90)
        draw_in_direction(self.pen_size * 2, 'right', 90)
        draw_in_direction(self.pen_size * 2, 'left', 90)

    def _draw_pattern_corner(self):
        pass

    def draw(self):
        self._draw_borders()
        # TODO: Setup method.
        penup()
        setpos(position()[0], position()[1] + self.pen_size * 2)
        pendown()
        for _ in range(31):  # TODO: Calculate range!
            self._draw_pattern_once()
