from abc import ABC, abstractmethod
from turtle import width, window_width, window_height, penup, pendown, forward, backward, right, left, speed, pos, setpos


class MeanderDrawingBase(ABC):
    @staticmethod
    def set_pen_properties(pen_size, stroke_speed, pen_color):
        width(pen_size)
        speed(stroke_speed)
        # TODO: Pen color.

    @staticmethod
    def set_background_color(background_color):
        pass
        # TODO: Background color.

    @abstractmethod
    def draw_borders(self, borders_type, spacing_pixels):
        pass

    @abstractmethod
    def draw_pattern_once(self, direction, starting_position):
        pass

    @abstractmethod
    def draw_pattern_corner(self):
        pass
