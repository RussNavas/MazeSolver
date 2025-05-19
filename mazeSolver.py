from window import Window
from cell import Cell


def main():

    win = Window(800, 600)

    # Create some cells
    cell1 = Cell(win)
    cell1.draw(50, 150, 50, 150)

    cell2 = Cell(win)
    cell2.draw(200, 300, 50, 150)

    cell3 = Cell(win)
    cell3.draw(50, 150, 200, 300)

    cell4 = Cell(win)
    cell4.draw(200, 300, 200, 300)

    # Draw moves between cells
    cell1.draw_move(cell2)  # Red line to the right
    cell1.draw_move(cell3)  # Red line downward

    # Draw a backtrack move
    cell2.draw_move(cell4, undo=True)  # Gray line downward

    win.wait_for_close()


if __name__ == "__main__":
    main()
