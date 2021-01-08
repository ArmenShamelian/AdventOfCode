import numpy as np

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
portals = {}

def load_input():
    file = open('input_20.txt', 'r')
    input_ = file.read()
    return input_


def neighbors(grid, position, level=0, only_walkable=False, ignore_portals=False):
    global directions
    result = []
    for d in directions:
        neighbor = (position[0]+d[0], position[1]+d[1])
        if neighbor in grid.keys():
            if not only_walkable:
                result.append([neighbor, level])
            elif grid[neighbor][0] == '.':
                result.append([neighbor, level])
    # Check for portals
    if len(grid[position]) > 1 and not ignore_portals:
        side = grid[position][2]
        if side == 'inside':
            result.append([grid[position][1], level+1])
        elif side == 'outside' and level > 0:
            result.append([grid[position][1], level-1])
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


def get_portal_level(grid, l1p, pp, middle):
    # Check if portal is inside or outside based on letter positions.
    l1 = grid[l1p]
    if pp[0] > l1p[0]:
        # on left side of floor
        if pp[0] < middle[0]:
            return 'outside'
        else:
            return 'inside'
    elif pp[0] < l1p[0]:
        # on right side of floor
        if pp[0] > middle[0]:
            return 'outside'
        else:
            return 'inside'
    elif pp[1] > l1p[1]:
        # on top side of floor
        if pp[1] < middle[1]:
            return 'outside'
        else:
            return 'inside'
    elif pp[1] < l1p[1]:
        # on bottom side of floor
        if pp[1] > middle[1]:
            return 'outside'
        else:
            return 'inside'


def parse_input(input_):
    # First, parse only donut shapes, without portals.
    input_ = input_.split('\n')
    grid = {}
    max_x = 0
    max_y = 0
    for y, line in enumerate(input_):
        if y > max_y:
            max_y = y
        for x, c in enumerate(line):
            if x > max_x:
                max_x = x
            if c != ' ':
                grid[(x, y)] = c
    # Find portals and link them to each other
    global portals
    start = None
    end = None
    letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    middle = (int(max_x/2), int(max_y/2))
    for x, y in grid:
        if grid[x, y] not in letters:
            continue
        n = neighbors(grid, (x, y), ignore_portals=True)
        chars = [grid[x[0]] for x in n]
        # If 1 neighbor is a letter and 1 neighbor is a grid point: add portal.
        if any([x in letters for x in chars]) and '.' in chars:
            # Add portal
            letter_2_pos = None
            portal_pos = None
            for neighbor , _ in n:
                if grid[neighbor] in letters:
                    letter_2_pos = neighbor
                if grid[neighbor] == '.':
                    portal_pos = neighbor
            # Get portal name
            portal_name = get_portal_name(grid, (x,y), letter_2_pos, portal_pos)
            # Get portal side (inside/outside: inside increases level, outside decreases level.)
            portal_side = get_portal_level(grid, (x, y), portal_pos, middle)
            # Map start and end
            if portal_name == 'AA':
                start = portal_pos
            elif portal_name == 'ZZ':
                end = portal_pos
            # Link it to the other portal, if exists
            elif portal_name in portals.keys():
                # Get position and side from portals dict
                grid[portal_pos] = ['.', portals[portal_name][0], portal_side]
                grid[portals[portal_name][0]] = ['.', portal_pos, portals[portal_name][1]]
            else:
                portals[portal_name] = [portal_pos, portal_side]
    del portals
    return grid, start, end


def bfs(grid, start, end):
    visited = {}
    queue = [(start, 0)]
    visited[(start, 0)] = 0
    parent = {}

    while queue:
        position, level = queue.pop(0)
        steps = visited[(position, level)]
        # Check if done
        if (position == end) and (level == 0):
            path = []
            while True:
                path.append((position, level))
                if (position, level) in parent.keys():
                    position, level = parent[(position, level)]
                else:
                    break
            return steps

        for n, l in neighbors(grid, position, level, only_walkable=True):
            if (n, l) not in visited:
                queue.append((n, l))
                visited[(n, l)] = steps + 1
                parent[(n,l)] = (position, level)

    return 'Error'


# Execute
def run():
    input_ = load_input()
    grid, start, end = parse_input(input_)
    min_steps = bfs(grid, start, end)
    return min_steps


answer = run()
print(f"Answer: {answer}")

