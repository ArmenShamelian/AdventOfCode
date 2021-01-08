import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = open('input_15.txt', 'r')
_input = file.read()


def run_amp(m, man_input, ip=0, first_input=True, first_loop=False, relative_base=0):
    while True:
        instr = str(m[ip])
        if instr == '99':
            return man_input, True, 0, relative_base
        par_c = 0
        par_b = 0
        par_a = 0
        opcode = int(instr[-1])
        # Check if there are parameter modes
        if len(instr) > 1:
            instr = instr[:-2]
            if len(instr) > 0:
                par_c = int(instr[-1])
                instr = instr[:-1]
                if len(instr) > 0:
                    par_b = int(instr[-1])
                    instr = instr[:-1]
                    if len(instr) > 0:
                        par_a = int(instr[-1])
        assert (par_a in [0, 2])
        if par_c == 1:
            a = int(m[ip + 1])
        elif par_c == 2:
            a = int(m[relative_base + int(m[ip + 1])])
        else:
            a = int(m[int(m[ip + 1])])
        try:
            if par_b == 1:
                b = int(m[ip + 2])
            elif par_b == 2:
                b = int(m[relative_base + int(m[ip + 2])])
            else:
                b = int(m[int(m[ip + 2])])
        except:
            pass
        try:
            if par_a == 0:
                c = int(m[ip + 3])
            elif par_a == 2:
                c = relative_base + int(m[ip + 3])
        except:
            pass
        if opcode in [1, 2]:
            if opcode == 1:
                if par_a == 0:
                    m[c] = a + b
                elif par_a == 2:
                    m[c] = a + b
            elif opcode == 2:
                if par_a == 0:
                    m[c] = a * b
                elif par_a == 2:
                    m[c] = a * b
            ip += 4
        elif opcode == 3:
            if par_c == 0:
                m[int(m[ip + 1])] = man_input
            elif par_c == 2:
                m[relative_base + int(m[ip + 1])] = man_input
            ip += 2
        elif opcode == 4:
            return a, False, ip+2, relative_base
        elif opcode == 5:
            if a != 0:
                ip = b
            else:
                ip += 3
        elif opcode == 6:
            if a == 0:
                ip = b
            else:
                ip += 3
        elif opcode == 7:
            if a < b:
                if par_a == 0:
                    m[c] = 1
                elif par_a == 2:
                    m[c] = 1
            else:
                if par_a == 0:
                    m[c] = 0
                elif par_a == 2:
                    m[c] = 0
            ip += 4
        elif opcode == 8:
            if a == b:
                if par_a == 0:
                    m[c] = 1
                elif par_a == 2:
                    m[c] = 1
            else:
                if par_a == 0:
                    m[c] = 0
                elif par_a == 2:
                    m[c] = 0
            ip += 4
        elif opcode == 9:
            relative_base += a
            ip += 2


def draw_grid(grid, position):
    min_x = 9999
    max_x = -9999
    min_y = 9999
    max_y = -9999
    for x,y in grid:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    screen = ''
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) == position:
                screen += 'D'
            else:
                screen += grid.setdefault((x,y), ' ')
        screen += '\n'
    print(screen)


def get_movement(grid, open, closed, position):
    pass


# Key = (x,y), value=value. . = terrain, # = wall, X = goal.
grid = {}
# Start at 0,0.
position = (0, 0)
# For each index, store: cost, open/closed, type
grid[position] = [0, 0, '.']

directions = {1: (0, -1),
              2: (0,  1),
              3: (-1, 0),
              4: (1,  0)}

# A* open and closed lists
open = []
closed = []

_input = _input.split(',') + ['0'] * 1000000
relative_base = 0
ip = 0
stop = False
steps = 0
while not stop:
    move = get_movement(grid, open, closed, position)
    output, stop, ip, relative_base = run_amp(_input, move, ip, relative_base=relative_base)
    # If sucessful: move in that direction, and update grid with .
    if output == 1:
        new_position = tuple(map(sum, zip(position, directions[move])))
        grid[new_position] = '.'
        position = new_position
        steps += 1
    # If unsucessful: stay in current position, update grid with #.
    elif output == 0:
        blocked_position = tuple(map(sum, zip(position, directions[move])))
        grid[blocked_position] = '#'
    elif output == 2:
        # New position is correct answer, return no of steps
        new_position = tuple(map(sum, zip(position, directions[move])))
        grid[new_position] = 'X'
        steps += 1
        break
    draw_grid(grid, position)
    if stop:
        break

print(grid)