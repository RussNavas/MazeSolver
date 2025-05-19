from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False

        self._root = Tk()
        self._root.title = "Maze Solver"
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self._root, bg="white", width=self.width,
                             height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running_state = False
        #  self._root.destroy()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y,
                           self.p2.x,
                           self.p2.y,
                           fill=fill_color,
                           width=2)


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


def main():
    win = Window(800, 600)

    # Draw a grid of cells
    cell_size = 100
    num_rows = 4
    num_cols = 5

    for row in range(num_rows):
        for col in range(num_cols):
            x1 = col * cell_size + 50
            x2 = x1 + cell_size
            y1 = row * cell_size + 50
            y2 = y1 + cell_size

            # Create and draw each cell
            cell = Cell(win)

            # Example of modifying walls for some cells
            if row == 1 and col == 2:
                cell.has_left_wall = False
            if row == 2 and col == 3:
                cell.has_bottom_wall = False

            cell.draw(x1, x2, y1, y2)

    win.wait_for_close()


if __name__ == "__main__":
    main()
