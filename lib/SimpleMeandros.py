from lib.drawing_utils import draw_borders, draw_in_direction
from lib.MeanderDrawingBase import MeandrosDrawingBase
from turtle import window_width, window_height, penup, pendown, forward, backward, right, \
    left, position, setpos, hideturtle


PATTERN_WIDTH = 2  # Represents width of the pattern.


class SimpleMeandros(MeandrosDrawingBase):
    def __init__(self, pen_size, stroke_speed, pen_color, background_color, meandros_type):
        self.corners_edge = []
        self.pen_size = pen_size
        self.stroke_speed = stroke_speed
        self.pen_color = pen_color
        self.set_pen_properties(self.pen_size, self.stroke_speed, self.pen_color)
        self.background_color = background_color
        self.set_background_color(background_color)

    def _draw_borders(self):
        print(self.corners_edge)
        draw_borders(self.pen_size, PATTERN_WIDTH, self.corners_edge)

    def _draw_pattern_once(self):
        # draw_in_direction(self.pen_size * 1)
        draw_in_direction(self.pen_size * 2, 'left', 90)
        draw_in_direction(self.pen_size * 2, 'right', 90)
        draw_in_direction(self.pen_size * 2, 'right', 90)
        draw_in_direction(self.pen_size * 2, 'left', 90)

    def _draw_pattern_corner(self):
        draw_in_direction(self.pen_size * 2, 'left', 90)
        draw_in_direction(self.pen_size * 4, 'right', 90)
        self.corners_edge.append(position())
        draw_in_direction(self.pen_size * 2, 'right', 90)
        draw_in_direction(self.pen_size * 2, 'right', 90)
        draw_in_direction(self.pen_size * 2, 'left', 90)

    def draw(self):
        pendown()
        # right(45)  # TODO: this should be a parameter
        for _ in range(2):
            for _ in range(12):  # TODO: Calculate range!
                self._draw_pattern_once()
            self._draw_pattern_corner()
            for _ in range(10):  # TODO: Calculate range!
                self._draw_pattern_once()
            self._draw_pattern_corner()
        self._draw_borders()
        hideturtle()