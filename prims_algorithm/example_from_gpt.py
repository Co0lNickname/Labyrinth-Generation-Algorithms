import random
import numpy as np


def generate_maze_prims(width, height):
    maze = np.zeros((width, height), dtype=np.uint8)
    walls = []

    def add_walls(x, y):
        if width > x >= 0 == maze[x, y] and 0 <= y < height:
            maze[x, y] = 1
            if x > 0:
                walls.append((x - 1, y))
            if x < width - 1:
                walls.append((x + 1, y))
            if y > 0:
                walls.append((x, y - 1))
            if y < height - 1:
                walls.append((x, y + 1))

    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    add_walls(start_x, start_y)

    while walls:
        x, y = walls.pop(random.randrange(len(walls)))
        add_walls(x, y)

    return maze
