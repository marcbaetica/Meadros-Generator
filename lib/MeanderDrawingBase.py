from abc import ABC, abstractmethod
from turtle import width, window_width, window_height, penup, pendown, forward, backward, right, left, speed, pos, setpos


class MeandrosDrawingBase(ABC):
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
    def _draw_borders(self):
        pass

    @abstractmethod
    def _draw_pattern_once(self):
        pass

    @abstractmethod
    def _draw_pattern_corner(self):
        pass
