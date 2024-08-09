from example_from_gpt import generate_maze_recursive_backtracking
from converting.converting_files import matrix_to_image


MAZE_SIZE = [255, 255]  # in millimeters
CELL_SIZE = [5, 5]  # in millimeters

MAZE_WIDTH, MAZE_HEIGHT = MAZE_SIZE
CELL_WIDTH, CELL_HEIGHT = CELL_SIZE

MAZE_CELL_DIM_SIZE = [
    MAZE_WIDTH // CELL_WIDTH,
    MAZE_HEIGHT // CELL_HEIGHT
]  # in cells

MAZE_CELL_DIM_WIDTH, MAZE_CELL_DIM_HEIGHT = MAZE_CELL_DIM_SIZE

maze = generate_maze_recursive_backtracking(MAZE_CELL_DIM_WIDTH, MAZE_CELL_DIM_HEIGHT)

for row in maze:
    for col in row:
        print(col, end=' ')
    print()

image = matrix_to_image(maze)
image.show()
