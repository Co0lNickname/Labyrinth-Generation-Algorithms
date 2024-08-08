from example_from_gpt import generate_maze_prims


MAZE_SIZE = [255, 255]  # in millimeters
CELL_SIZE = [5, 5]  # in millimeters

MAZE_WIDTH, MAZE_HEIGHT = MAZE_SIZE
CELL_WIDTH, CELL_HEIGHT = CELL_SIZE

MAZE_CELL_DIM_SIZE = [
    MAZE_WIDTH // CELL_WIDTH,
    MAZE_HEIGHT // CELL_HEIGHT
]  # in cells

MAZE_CELL_DIM_WIDTH, MAZE_CELL_DIM_HEIGHT = MAZE_CELL_DIM_SIZE

maze = generate_maze_prims(MAZE_CELL_DIM_WIDTH, MAZE_CELL_DIM_HEIGHT)

for row in maze:
    for col in row:
        print(col, end=' ')
    print()
