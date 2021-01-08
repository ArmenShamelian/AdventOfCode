# 1
ip = 0
manual_input = 1
m = input
while True:
    instr = str(m[ip])
    if instr == '99':
        break
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
    assert(par_a == 0)
    if opcode in [1,2]:
        a = int(m[int(m[ip+1])] if not par_c else m[ip+1])
        b = int(m[int(m[ip+2])] if not par_b else m[ip+2])
        c = int(m[ip+3])
        if opcode == 1:
            m[c] = a+b
        elif opcode == 2:   
            m[c] = a*b
        ip += 4
    elif opcode == 3:
        m[int(m[ip+1])] = manual_input
        ip += 2
    elif opcode == 4:
        a = int(m[int(m[ip+1])] if not par_c else m[ip+1])
        # Final result is answer to 5.1
        print('Output: ', a)
        ip += 2

# 2
input = input.split(',')
ip = 0
manual_input = 5
m = input
while True:
    instr = str(m[ip])
    if instr == '99':
        break
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
    assert(par_a == 0)
    if par_c:
        a = int(m[ip+1])
    else:
        a = int(m[int(m[ip+1])])
    try: 
        if par_b:
            b = int(m[ip+2])
        else:
            b = int(m[int(m[ip+2])])
    except:
        pass
    try:
        c = int(m[ip+3])
    except:
        pass
    if opcode in [1,2]:
        if opcode == 1:
            m[c] = a+b
        elif opcode == 2:     
            m[c] = a*b
        ip += 4
    elif opcode == 3:
        m[int(m[ip+1])] = manual_input
        ip += 2
    elif opcode == 4:
        print('Output value: ', a)
        ip += 2
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
            m[c] = 1
        else:
            m[c] = 0
        ip += 4
    elif opcode == 8:
        print(m[ip+3])
        if a == b:
            m[c] = 1
        else:
            m[c] = 0
        ip += 4

    