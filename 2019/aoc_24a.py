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
    grid = {}
    for y, row in enumerate(split):
        for x, cell in enumerate(row):
            grid[(x, y)] = cell
    return grid


def get_layout(grid):
    # Encode layout as indexes of bugs
    bugs = []
    global max_x
    for x, y in grid.keys():
        if grid[(x, y)] == '#':
            index = x + y * max_x
            bugs.append(index)
    return tuple(bugs)


def count_neighboring_bugs(grid, cell):
    global directions
    bugs = 0
    for d in directions:
        neighbor = (cell[0] + d[0], cell[1] + d[1])
        if (neighbor in grid.keys()) and (grid[neighbor] == '#'):
            bugs += 1
    return bugs


def update_layout(grid):
    new_grid = grid.copy()
    for x, y in grid.keys():
        cell = grid[(x, y)]
        nb_neighboring_bugs = count_neighboring_bugs(grid, (x, y))
        if (cell == '#') and (nb_neighboring_bugs != 1):
            new_grid[(x, y)] = '.'
        elif (cell == '.') and (nb_neighboring_bugs in [1, 2]):
            new_grid[(x, y)] = '#'
    del grid
    return new_grid


def compute_rating(layout):
    rating = 0
    for i in range(len(layout)):
        rating += 2**layout[i]
    return rating


def run():
    input_ = load_input()
    grid = parse_input(input_)
    layouts = {}
    initial_layout = get_layout(grid)
    layouts[initial_layout] = 1
    i = 0
    while True:
        print(i)
        i += 1
        grid = update_layout(grid)
        new_layout = get_layout(grid)
        if layouts.setdefault(new_layout, 0):
            rating = compute_rating(new_layout)
            return rating
        else:
            layouts[new_layout] = 1


answer = run()
print(f"Answer: {answer}")

