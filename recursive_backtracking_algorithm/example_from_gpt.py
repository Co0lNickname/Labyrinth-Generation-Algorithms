import numpy as np
import random


def generate_maze_recursive_backtracking(width, height):
    maze = np.zeros((width, height), dtype=np.uint8)

    def carve(x, y):
        maze[x, y] = 1
        directions = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(directions)
        for nx, ny in directions:
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[nx, ny] == 0:
                maze[x + (nx - x) // 2, y + (ny - y) // 2] = 1
                carve(nx, ny)
    carve(random.randrange(1, width, 2), random.randrange(1, height, 2))
    return maze
