with open("input/12.txt") as f:
    lines = f.read().splitlines()

# 1
start = (0, 0)
pos = start
dir = 'E'
dirs = {'N': (0, -1), 'W':(-1, 0), 'E':(1, 0), 'S':(0, 1)}
rotation = 'NESW'
for line in lines:
    c = line[0]
    n = int(line[1:])
    if c in 'NWES':
        pos = (pos[0]+n*dirs[c][0], pos[1]+n*dirs[c][1])
    if c == "F":
        pos = (pos[0]+n*dirs[dir][0], pos[1]+n*dirs[dir][1])
    if c in 'LR':
        degrees = int(n / 90)
        if c == "L":
            dir = rotation[(rotation.index(dir)-degrees)%4]
        if c == 'R':
            dir = rotation[(rotation.index(dir)+degrees)%4]
print(abs(pos[0])+abs(pos[1]))

# 2
start = (0, 0)
start_wp = (10, -1)
pos = start
wp = start_wp
dirs = {'N': (0, -1), 'W':(-1, 0), 'E':(1, 0), 'S':(0, 1)}
for line in lines:
    c = line[0]
    n = int(line[1:])
    if c in 'NWES':
        wp = (wp[0]+n*dirs[c][0], wp[1]+n*dirs[c][1])
    if c == "F":
        pos = (pos[0]+n*wp[0], pos[1]+n*wp[1])
    if c in 'LR':
        degrees = n
        if (degrees == 90) and c == 'L':
            degrees = 270
        elif (degrees == 270) and c == 'L':
            degrees = 90
        if degrees == 270:
            wp = (wp[1], -wp[0])
        elif degrees == 180:
            wp = (-wp[0], -wp[1])
        elif degrees == 90:
            wp = (-wp[1], wp[0])
print(abs(pos[0])+abs(pos[1]))