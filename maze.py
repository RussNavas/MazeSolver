import time
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        """Initialize and draw the cells in a 2D grid."""
        # Create the grid of cells
        self._cells = [
            [Cell(self.win) for _ in range(self.num_cols)]
            for _ in range(self.num_rows)
        ]

        # Iterate over rows first, then columns
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)

    def _draw_cell(self, row, col):
        """Draw a single cell at (row, col)."""
        # Calculate the cell coordinates
        x1 = self._x1 + col * self.cell_size_x
        y1 = self._y1 + row * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        # Draw the cell
        self._cells[row][col].draw(x1, x2, y1, y2)

        # Animate the drawing
        self.animate()

    def animate(self):
        """Refresh the window and sleep briefly to animate drawing."""
        self.win.redraw()
        time.sleep(0.05)
