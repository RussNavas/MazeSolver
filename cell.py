from point import Point
from line import Line


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = -1
        self._x2 = -1
        self._y1 = -1
        self._y2 = -1

        self._win = window

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            pt1 = Point(x1, y1)
            pt2 = Point(x1, y2)
            l1 = Line(pt1, pt2)
            l1.draw(self._win.canvas, "black")

        if self.has_right_wall:
            pt1 = Point(x2, y1)
            pt2 = Point(x2, y2)
            l1 = Line(pt1, pt2)
            l1.draw(self._win.canvas, "black")

        if self.has_top_wall:
            pt1 = Point(x1, y1)
            pt2 = Point(x2, y1)
            l1 = Line(pt1, pt2)
            l1.draw(self._win.canvas, "black")

        if self.has_bottom_wall:
            pt1 = Point(x1, y2)
            pt2 = Point(x2, y2)
            l1 = Line(pt1, pt2)
            l1.draw(self._win.canvas, "black")

    def draw_move(self, to_cell, undo=False):

        color = "gray" if undo else "red"

        # center of source cell
        center_x1 = (self._x1 + self._x2) // 2
        center_y1 = (self._y1 + self._y2) // 2

        # center of target cell
        center_x2 = (to_cell._x1 + to_cell._x2) // 2
        center_y2 = (to_cell._y1 + to_cell._y2) // 2

        # draw the line between centers
        start_pt = Point(center_x1, center_y1)
        end_pt = Point(center_x2, center_y2)
        move_line = Line(start_pt, end_pt)
        move_line.draw(self._win.canvas, color)
