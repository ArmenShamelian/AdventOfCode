import numpy as np

max_x = 0
max_y = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def load_input():
    file = open('input_24.txt', 'r')
    input_ = file.read()
    return input_


def parse_input(input_):
    split = input_.split('\n')
    global max_x
    global max_y
    max_x = len(split[0])
    max_y = len(split)
    level = 0
    grid = {}
    for y, row in enumerate(split):
        for x, cell in enumerate(row):
            grid[(x, y, level)] = cell
    return grid


def get_layout(grid):
    # Encode layout as indexes of bugs
    bugs = []
    global max_x
    for x, y, level in grid.keys():
        if grid[(x, y, level)] == '#':
            index = x + y * max_x
            bugs.append((index, level))
    return tuple(bugs)


def count_neighboring_bugs(grid, cell):
    global directions
    bugs = 0
    for d in directions:
        neighbor = (cell[0] + d[0], cell[1] + d[1])
        if neighbor in grid.keys():
            if grid[neighbor] == '#':
                bugs += 1
        else:
    return bugs


def update_layout(grid):
    new_grid = grid.copy()
    for x, y, level in grid.keys():
        cell = grid[(x, y, level)]
        nb_neighboring_bugs = count_neighboring_bugs(grid, (x, y, level))
        if (cell == '#') and (nb_neighboring_bugs != 1):
            new_grid[(x, y, level)] = '.'
        elif (cell == '.') and (nb_neighboring_bugs in [1, 2]):
            new_grid[(x, y, level)] = '#'
    del grid
    return new_grid


# Execute
def run():
    input_ = load_input()
    grid = parse_input(input_)
    layouts = {}
    initial_layout = get_layout(grid)
    layouts[initial_layout] = 1
    i = 0
    new_layout = None
    while i < 200:
        print(i)
        i += 1
        grid = update_layout(grid)
        new_layout = get_layout(grid)
    no_of_bugs = len(new_layout)
    return no_of_bugs


answer = run()
print(f"Answer: {answer}")

