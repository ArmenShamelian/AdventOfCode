with open("input/11.txt") as f:
    lines = f.read().splitlines()

# 1
# Parse input
max_x = len(lines[0])
max_y = len(lines)
map = {}
for y in range(0, max_y):
    for x in range(0, max_x):
        map[x, y] = lines[y][x]

def get_new_state(x, y, map):
    c = map[x, y]
    if c == '.':
        return '.'
    # Get surrounding tiles
    surrounding_tiles = []
    for _x in range(x-1, x+2):
        for _y in range(y-1, y+2):
            if (_x,_y) in map.keys():
                surrounding_tiles += [(_x, _y)]
    # Count how many of them are occupied
    no_occupied = 0
    for t in surrounding_tiles:
        _c = map[t]
        if _c == '#':
            no_occupied += 1
    if (c == 'L') and (no_occupied == 0):
        return '#'
    if (c == '#') and (no_occupied > 4):
        return 'L'
    return c
        
next_map = map.copy()
while True:
    for y in range(0, max_y):
        for x in range(0, max_x):
            next_map[x, y] = get_new_state(x, y, map)
    if map == next_map:
        break
    else:
        map = next_map.copy()

no_occupied = 0
for x, y in next_map:
    if next_map[x, y] == '#':
        no_occupied += 1
print(no_occupied)

# 2
# Parse input
max_x = len(lines[0])
max_y = len(lines)
map = {}
for y in range(0, max_y):
    for x in range(0, max_x):
        map[x, y] = lines[y][x]

# Set visible tiles
visible_seats= {}
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
for y in range(0, max_y):
    for x in range(0, max_x):
        if map[x, y] == '.':
            continue
        this_seats = []
        for d in directions:
            new_pos = (x, y)
            while True:
                new_pos = (new_pos[0]+d[0], new_pos[1]+d[1]) 
                if new_pos in map.keys():
                    if map[new_pos] != '.':
                        this_seats += [new_pos]
                        break
                else:
                    break
        visible_seats[x, y] = this_seats

def get_new_state(x, y, map):
    c = map[x, y]
    if c == '.':
        return '.'
    # Count how many visible tiles are occupied
    no_occupied = 0
    for t in visible_seats[x, y]:
        _c = map[t]
        if _c == '#':
            no_occupied += 1
    if (c == 'L') and (no_occupied == 0):
        return '#'
    if (c == '#') and (no_occupied >= 5):
        return 'L'
    return c
        
next_map = map.copy()
while True:
    for y in range(0, max_y):
        for x in range(0, max_x):
            next_map[x, y] = get_new_state(x, y, map)
    if map == next_map:
        break
    else:
        map = next_map.copy()

no_occupied = 0
for y in range(0, max_y):
    for x in range(0, max_x):
        if next_map[x, y] == '#':
            no_occupied += 1
print(no_occupied)