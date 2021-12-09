from abc import ABC, abstractmethod
from turtle import width, penup, pendown, speed, color, screensize, goto, hideturtle, forward


class MeandrosDrawingBase(ABC):
    @staticmethod
    def set_pen_properties(pen_size, stroke_speed, pen_color):
        width(pen_size)
        speed(stroke_speed)
        color(pen_color)

    @staticmethod
    def _set_background_color(background_color):
        screensize(300, 100, background_color)  # TODO: Fix size enforcement and take resolution as parameters.

    @abstractmethod
    def _draw_borders(self):
        pass

    @abstractmethod
    def _draw_pattern_once(self):
        pass

    @abstractmethod
    def _draw_pattern_corner(self):
        # TODO: Change logic to make this rely on _draw_pattern_once().
        pass

    def draw_meandros(self, width_patterns_count, length_patterns_count, start_position):
        # forward(1)  # For pinpointing center.
        penup()
        print(start_position)
        goto(start_position)
        pendown()
        # right(45)  # TODO: this should be a parameter
        for _ in range(2):
            for _ in range(width_patterns_count):
                self._draw_pattern_once()
            self._draw_pattern_corner()
            for _ in range(length_patterns_count):
                self._draw_pattern_once()
            self._draw_pattern_corner()
        self._draw_borders()
        hideturtle()
