from graphics import Line, Point

import random

class Cell:
    def __init__(self, win):
        self.l_wall = True
        self.r_wall = True
        self.t_wall = True
        self.b_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.l_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, 'white')
        if self.r_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, 'white')
        if self.t_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, 'white')
        if self.b_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, 'black')
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, 'white')

    def draw_move(self, to_cell, undo=False):
        if undo:
            colour = 'grey'
        else:
            colour = 'red'
        from_x = (self._x1 + self._x2)/2
        from_y = (self._y1 + self._y2)/2
        to_x = (to_cell._x1 + to_cell._x2)/2
        to_y = (to_cell._y1 + to_cell._y2)/2
        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        self._win.draw_line(line, colour)
    
    
            

