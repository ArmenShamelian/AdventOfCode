with open("input/08.txt") as f:
    commands = f.read().splitlines()

# 1
acc = 0
pos = 0
executed_before = []
while True:
    if pos in executed_before:
        print(acc)
        break
    executed_before += [pos]
    command = commands[pos].split(' ')[0]
    value = commands[pos].split(' ')[1]
    if command == 'nop':
        pos += 1
    if command == 'acc':
        sign = value[0]
        number = int(value[1:])
        if sign == '-':
            number = number * -1
        acc += number
        pos += 1
    if command == 'jmp':
        sign = value[0]
        number = int(value[1:])
        if sign == '-':
            number = number * -1
        pos += number

# 2
def check_terminate(cs):
    acc = 0
    pos = 0
    executed_before = []
    while True:
        if pos in executed_before:
            return (acc, False)
        elif pos == len(cs):
            return (acc, True)
        executed_before += [pos]
        c = cs[pos].split(' ')[0]
        value = cs[pos].split(' ')[1]
        if c == 'nop':
            pos += 1
        if c == 'acc':
            sign = value[0]
            number = int(value[1:])
            if sign == '-':
                number = number * -1
            acc += number
            pos += 1
        if c == 'jmp':
            sign = value[0]
            number = int(value[1:])
            if sign == '-':
                number = number * -1
            pos += number

change = 0
for change in range(0, len(commands)):
    fixed_commands = commands.copy()
    if 'nop' in commands[change]:
        fixed_commands[change] = 'jmp' + commands[change][3:]
    elif 'jmp' in commands[change]:
        fixed_commands[change] = 'nop' + commands[change][3:]
    else:
        change += 1
        continue
    answer, terminate = check_terminate(fixed_commands)
    if terminate:
        print(answer)
        break
    change += 1