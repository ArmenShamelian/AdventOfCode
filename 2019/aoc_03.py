input_1 = [x.split(',') for x in input_lines]

def draw_line(ans, pos_x, pos_y, length, direction, dist):
    dir_x = 0
    dir_y = 0
    if direction == 'R':
        dir_x = 1
    elif direction == 'L':
        dir_x = -1
    elif direction == 'U':
        dir_y = 1
    elif direction == 'D':
        dir_y = -1
    for i in range(0, length):
        pos_x += dir_x
        pos_y += dir_y
        if (pos_x, pos_y) not in ans:
            ans[(pos_x, pos_y)] = dist + i + 1
    return ans, pos_x, pos_y, dist + length

start_x = 0
start_y = 0

def draw_wire(wire):
    ans = {}
    pos_x = 0
    pos_y = 0
    dist = 0
    for line in wire:
        direction = line[0]
        length = int(line[1:])
        ans, pos_x, pos_y, dist = draw_line(ans, pos_x, pos_y, length, direction, dist)
    return ans

wire_1 = draw_wire(input_1[0])
wire_2 = draw_wire(input_1[1])

intersections = []
for (x,y) in wire_1.keys():
    if (x,y) in wire_2.keys():
        intersections += [(x,y)]

def calculate_distance(_from, _to):
    dist_x = np.abs(_from[0] - _to[0])
    dist_y = np.abs(_from[1] - _to[1])
    dist = dist_x + dist_y
    return dist

min_dist = np.inf
best_i = 0
for i in intersections:
    new_dist = calculate_distance(i, [start_x, start_y])
    if new_dist < min_dist and new_dist > 0:
        min_dist = new_dist
        best_i = i

print(min_dist)

# 2
def calculate_length(i):
    dist = wire_1[i] + wire_2[i]
    return dist

min_dist = np.inf
best_i = 0
for i in intersections:
    new_dist = calculate_length(i)
    if new_dist < min_dist and new_dist > 0:
        min_dist = new_dist
        best_i = i

print(min_dist)