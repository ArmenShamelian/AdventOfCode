import numpy as np

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
    file = open('input_21.txt', 'r')
    input_ = file.read()
    return input_


def make_script():
    script = ''
    script += 'NOT A J\n'
    script += 'NOT C T\n'
    script += 'OR T J\n'
    script += 'AND D J\n'
    script += 'WALK\n'
    return script


def translate_script(script):
    translated_script = []
    for c in script:
        translated_script.append(ord(c))
    return translated_script


def input_script(script):
    global intcode_input
    for c in script:
        intcode_input.append(c)
    return


# Execute
def run():
    input_ = load_input()
    input_ = input_.split(',') + ['0'] * 1000000

    script = make_script()
    script_ascii = translate_script(script)
    input_script(script_ascii)

    # Initialize intcode state
    ip = 0
    relative_base = 0
    stop = False
    output = 0
    while not stop:
        prev_output = output
        output, stop, ip, relative_base = run_amp(input_, ip, relative_base)
        if stop:
            return prev_output

    print('Error')


answer = run()
print(f"Answer: {answer}")