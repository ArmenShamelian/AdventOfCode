import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = open('input_13.txt', 'r')
input = file.read()

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

# Key = (x,y), value = block type
grid = {}

input = input.split(',') + [0] * 1000000
relative_base=0
ip=0
stop = False
while not stop:
    output_x, stop, ip, relative_base = run_amp(input, 0, ip, relative_base=relative_base)
    if stop:
        break
    output_y, stop, ip, relative_base = run_amp(input, 0, ip, relative_base=relative_base)
    if stop:
        break
    output_tile, stop, ip, relative_base = run_amp(input, 0, ip, relative_base=relative_base)
    coordinate = (output_x, output_y)
    grid[coordinate] = output_tile
    if stop:
        break

print(sum(x == 2 for x in grid.values()))
