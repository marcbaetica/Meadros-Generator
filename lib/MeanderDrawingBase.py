from abc import ABC, abstractmethod


class MeanderDrawingBase(ABC):
    @abstractmethod
    def set_properties(self, pen_size, stroke_speed, background_color):
        pass

    @abstractmethod
    def draw_borders(self, borders_type, spacing_pixels):
        pass

    @abstractmethod
    def draw_pattern_once(self, direction, starting_position):
        pass

    @abstractmethod
    def draw_pattern_corner(self):
        pass
