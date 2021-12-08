from lib.drawing_utils import draw_borders, draw_in_direction
from lib.MeanderDrawingBase import MeandrosDrawingBase
from turtle import window_width, window_height, penup, pendown, forward, backward, right, \
    left, position, setpos, seth, hideturtle, goto


# Used for calculating the start drawing position of the drawing so meandros fits in the center.
PATTERN_WIDTH_UNITS = 4
CORNERS_WIDTH = 8
# Used for calculating the position of the inner border.
PATTERN_HEIGHT = 3


class SimpleMeandros(MeandrosDrawingBase):
    def __init__(self, pen_size, stroke_speed, pen_color, background_color):
        self.corners_edge = []
        self.pen_size = pen_size
        self.stroke_speed = stroke_speed
        self.pen_color = pen_color
        self.set_pen_properties(self.pen_size, self.stroke_speed, self.pen_color)
        self.background_color = background_color
        self._set_background_color(background_color)

    def _calculate_start_drawing_position(self, width_patterns, length_patterns):
        x_start = (width_patterns * PATTERN_WIDTH_UNITS * self.pen_size + CORNERS_WIDTH) / 2
        y_start = (length_patterns * PATTERN_WIDTH_UNITS * self.pen_size + CORNERS_WIDTH) / 2
        # Draw starting position does not begin at corner. This adjusts the offset.
        x_start = x_start - 1 * self.pen_size
        y_start = y_start + 1 * self.pen_size
        return -int(x_start), int(y_start)

    def _draw_borders(self):
        draw_borders(self.pen_size, PATTERN_HEIGHT, self.corners_edge)

    def _draw_pattern_once(self):
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

    def draw(self, width_patterns_count, length_patterns_count):
        start_drawing_position = self._calculate_start_drawing_position(width_patterns_count, length_patterns_count)
        self.draw_meandros(width_patterns_count, length_patterns_count, start_drawing_position)
        # Reset positioning for other meandros to be drawn within the same canvas.
        penup()
        setpos(0, 0)
        seth(0)
        pendown()