with open("input/14.txt") as f:
    lines = f.read().splitlines()

# 1
mem = {}
mask = None
bits_to_replace = {}
for line in lines:
    if 'mask' in line:
        mask = line.split(' = ')[1]
        bits_to_replace = {}
        for i, x in enumerate(mask[::-1]):
            if x != 'X':
                bit = i
                bits_to_replace[bit] = x
        continue
    else:
        index = int(line.split('mem[')[1].split('] = ')[0])
        value = int(line.split(' = ')[1])
        value = list(str(bin(value))[2:])
        # prepend zeroes if needed
        if len(value) < len(mask):
            value = ['0'] * (len(mask) - len(value)) + value
        for i in bits_to_replace:
            value[-1-i] = bits_to_replace[i]
        new_value = int(''.join(value).encode('ascii'), 2)
        mem[index] = new_value
answer = 0
for i in mem:
    answer += mem[i]
print(answer)

# 2
mem = {}
mask = None
bits_to_replace = {}
for line in lines:
    if 'mask' in line:
        mask = line.split(' = ')[1]
        bits_to_replace = {}
        for i, x in enumerate(mask[::-1]):
            if x != '0':
                bit = i
                bits_to_replace[bit] = x
        continue
    else:
        index = int(line.split('mem[')[1].split('] = ')[0])
        value = int(line.split(' = ')[1])
        index = list(str(bin(index))[2:])
        # prepend zeroes if needed
        if len(index) < len(mask):
            index = ['0'] * (len(mask) - len(index)) + index
        floating_indices = []
        for i in bits_to_replace:
            index[-1-i] = bits_to_replace[i]
        # Explode floating indices
        addresses = [index]
        for i, x in enumerate(index):
            if x == 'X':
                to_add = []
                for a in addresses:
                    a0 = a.copy()
                    a1 = a.copy()
                    a0[i] = '0'
                    a1[i] = '1'
                    to_add += [a0, a1]
                addresses += to_add
        for a in addresses:
            if not 'X' in a:
                mem[int(''.join(a).encode('ascii'), 2)] = value
answer = 0
for i in mem:
    answer += mem[i]
print(answer)