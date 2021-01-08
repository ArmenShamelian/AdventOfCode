# 1
input_1[1] = 12
input_1[2] = 2
output_1 = input_1

def f_opcode(i, a, b):
    if i==1:
        return a+b
    elif i==2:
        return a*b

index = 0
while True:
    opcode = output_1[index]
    if opcode == 99:
        break
    result = f_opcode(opcode, output_1[output_1[index+1]], output_1[output_1[index+2]])
    output_1[output_1[index+3]] = result
    index += 4

print(output_1[0])

# 2
def run_instructions(m, noun, verb):
    m[1] = noun
    m[2] = verb
    # Instruction Pointer
    ip = 0
    while True:
        opcode = m[ip]
        if opcode == 99:
            return m[0]
        result = f_opcode(opcode, m[m[ip+1]], m[m[ip+2]])
        m[m[ip+3]] = result
        ip += 4

reset_memory = input_1

noun = -1
verb - -1
for n in range(0,100):
    for v in range(0,100):
        memory = reset_memory.copy()
        result = run_instructions(memory, n, v)
        if result == 19690720:
            noun = n
            verb = v
            break

print(100 * noun + verb)