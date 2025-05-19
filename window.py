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
