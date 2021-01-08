with open("input/15.txt") as f:
    lines = f.read().splitlines()

# 1
d = {}
line = lines[0].split(',')
for i, x in enumerate(line):
    d[int(x)] = ([i], 1)
i = len(line)
previous = line[-1]
while i < 2020:
    if previous in d:
        if d[previous][1] == 1:
            previous = 0
        else:
            previous = d[previous][0][-1] - d[previous][0][-2]
    else:
        previous = 0
    if previous in d:
        d[previous] = (d[previous][0][-1:] + [i], d[previous][1]+1)
    else:
        d[previous] = ([i], 1)
    i += 1
print(previous)

# 2
d = {}
line = lines[0].split(',')
for i, x in enumerate(line):
    d[int(x)] = ([i], 1)
i = len(line)
previous = line[-1]
while i < 30000000:
    if i % 1000000 == 0:
        print(i)
    if previous in d:
        if d[previous][1] == 1:
            previous = 0
        else:
            previous = d[previous][0][-1] - d[previous][0][-2]
    else:
        previous = 0
    try:
        d[previous] = (d[previous][0][-1:] + [i], 2)
    except:
        d[previous] = ([i], 1)
    i += 1
print(previous)