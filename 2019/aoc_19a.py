import numpy as np

# Globals
intcode_input = []


# Adjusted IntCode computer to take global input array values 1 by 1.
def run_amp(m, ip=0, relative_base=0):
    while True:
        instr = str(m[ip])
        if instr == '99':
            return 0, True, 0, relative_base
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
            # Take 1st input val and remove it from list
            global intcode_input
            current_input = intcode_input.pop(0)
            if par_c == 0:
                m[int(m[ip + 1])] = current_input
            elif par_c == 2:
                m[relative_base + int(m[ip + 1])] = current_input
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


def load_input():
    file = open('input_19.txt', 'r')
    input_ = file.read()
    return input_


def make_input():
    # Make X,Y input 0-49 list.
    all_input = []
    for y in range(50):
        for x in range(50):
            all_input.append(x)
            all_input.append(y)
    return all_input


# Execute
def run():
    global intcode_input
    intcode_input = make_input()
    points_pulled = 0
    screen = ''
    count_x = 0
    while intcode_input:
        # Initialize intcode state
        ip = 0
        relative_base = 0
        stop = False
        found = 0
        input_ = load_input()
        input_ = input_.split(',') + ['0'] * 1000000
        while not stop:
            output, stop, ip, relative_base = run_amp(input_, ip, relative_base)
            if output == 1:
                found = 1
        if found:
            screen += '#'
        else:
            screen += ' '
        count_x += 1
        if count_x == 50:
            count_x = 0
            screen += '\n'
    print(screen)
    return points_pulled


answer = run()
print(answer)

