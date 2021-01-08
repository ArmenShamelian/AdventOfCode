import numpy as np

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def load_input():
    file = open('input_20.txt', 'r')
    input_ = file.read()
    return input_

def neighbors(grid, position, only_walkable=False):
    global directions
    result = []
    for d in directions:
        neighbor = (position[0]+d[0], position[1]+d[1])
        if neighbor in grid.keys():
            if not only_walkable:
                result.append(neighbor)
            elif grid[neighbor][0] == '.':
                result.append(neighbor)
    # Check for portals
    if len(grid[position]) > 1:
        result.append(grid[position][1])
    return result


def get_portal_name(grid, l1p, l2p, pp):
    # Either read left-right or top-down depending on position of portal name.
    l1 = grid[l1p]
    l2 = grid[l2p]
    if pp[0] > l1p[0] > l2p[0]:
        return l2+l1
    elif pp[0] < l1p[0] < l2p[0]:
        return l1+l2
    elif pp[1] > l1p[1] > l2p[1]:
        return l2 + l1
    elif pp[1] < l1p[1] < l2p[1]:
        return l1 + l2


def parse_input(input_):
    # First, parse only donut shapes, without portals.
    input_ = input_.split('\n')
    grid = {}
    for y, line in enumerate(input_):
        for x, c in enumerate(line):
            if c != ' ':
                grid[(x, y)] = c

    # Find portals and link them to each other
    portals = {}
    portals_done = {}
    start = None
    end = None
    letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    for x, y in grid:
        if grid[x, y] not in letters:
            continue
        n = neighbors(grid, (x, y))
        chars = [grid[(x, y)] for (x, y) in n]
        # If 1 neighbor is a letter and 1 neighbor is a grid point: add portal.
        if any([x in letters for x in chars]) and '.' in chars:
            # Add portal
            letter_1 = grid[x, y]
            letter_2_pos = None
            portal_pos = None
            for neighbor in n:
                if grid[neighbor] in letters:
                    letter_2_pos = neighbor
                if grid[neighbor] == '.':
                    portal_pos = neighbor
            letter_2 = grid[letter_2_pos]
            # Sort portal name
            portal_name = get_portal_name(grid, (x,y), letter_2_pos, portal_pos)
            # Map start and end
            if portal_name == 'AA':
                start = portal_pos
            elif portal_name == 'ZZ':
                end = portal_pos
            # Link it to the other portal, if exists
            if portal_name in portals.keys():
                grid[portal_pos] = ['.', portals[portal_name]]
                grid[portals[portal_name]] = ['.', portal_pos]
            else:
                portals[portal_name] = portal_pos
    del portals
    return grid, start, end


def bfs(grid, start, end):
    visited = {}
    queue = [start]
    visited[start] = 0

    while queue:
        position = queue.pop(0)
        steps = visited[position]
        # Check if done
        if position == end:
            return steps

        for n in neighbors(grid, position, only_walkable=True):
            if n not in visited:
                queue.append(n)
                visited[n] = steps + 1

    return 'Error'


# Execute
def run():
    input_ = load_input()
    grid, start, end = parse_input(input_)
    min_steps = bfs(grid, start, end)
    return min_steps


answer = run()
print(answer)

