from window import Window
from maze import Maze


def main():

    win = Window(800, 600)

    # Create a 3x3 grid of cells for testing
    print("Drawing a 3x3 Maze...")
    maze = Maze(50, 50, 3, 3, 100, 100, win)

    # Create a larger grid to test further
    print("Drawing a 10x5 Maze...")
    maze_large = Maze(400, 50, 5, 10, 50, 50, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
