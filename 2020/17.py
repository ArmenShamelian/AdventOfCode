with open("input/17.txt") as f:
    lines = f.read().splitlines()

# 1
# Parse input
grid = {}
z = 0
y = 0
for line in lines:
    x = 0
    for c in line:
        if c == '#':
            grid[(x, y, z)] = 1
        else:
            grid[(x, y, z)] = 0
        x += 1
    y += 1

def add_neighbors(grid):
    min_x = 999
    max_x = -999
    min_y = 999
    max_y = -999
    min_z = 999
    max_z = -999
    for i in grid:
        x = i[0]
        y = i[1]
        z = i[2]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        if z < min_z:
            min_z = z
        if z > max_z:
            max_z = z
    # Add all adjacent cubes as inactive
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                if (x, y, z) not in grid:
                    grid[(x, y, z)] = 0
    return grid

def get_active_neighbors(cube, grid):
    n = 0
    x = cube[0]
    y = cube[1]
    z = cube[2]
    for _x in [x-1, x, x+1]:
        for _y in [y-1, y, y+1]:
            for _z in [z-1, z, z+1]:
                if ((_x, _y, _z) in grid) and (grid[(_x, _y, _z)] == 1):
                    if (_x, _y, _z) != (x, y, z):
                        n += 1
    return n
    
for cycle in range(0, 6):
    next_grid = {}
    grid = add_neighbors(grid)
    for cube in grid:
        no_active_neighbors = get_active_neighbors(cube, grid)
        if grid[cube] == 1:
            if no_active_neighbors in [2,3]:
                next_grid[cube] = 1
            else:
                next_grid[cube] = 0
        if grid[cube] == 0:
            if no_active_neighbors == 3:
                next_grid[cube] = 1
            else:
                next_grid[cube] = 0
    grid = next_grid.copy()

answer = 0
for cube in grid:
    if grid[cube] == 1:
        answer += 1
print(answer)

# 2
# Parse input
grid = {}
w = 0
z = 0
y = 0
for line in lines:
    x = 0
    for c in line:
        if c == '#':
            grid[(x, y, z, w)] = 1
        else:
            grid[(x, y, z, w)] = 0
        x += 1
    y += 1

def add_neighbors(grid):
    min_x = 999
    max_x = -999
    min_y = 999
    max_y = -999
    min_z = 999
    max_z = -999
    min_w = 999
    max_w = -999
    for i in grid:
        x = i[0]
        y = i[1]
        z = i[2]
        w = i[3]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        if z < min_z:
            min_z = z
        if z > max_z:
            max_z = z
        if w < min_w:
            min_w = w
        if w > max_w:
            max_w = w
    # Add all adjacent cubes as inactive
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                for w in range(min_w-1, max_w+2):
                    if (x, y, z, w) not in grid:
                        grid[(x, y, z, w)] = 0
    return grid

def get_active_neighbors(cube, grid):
    n = 0
    x = cube[0]
    y = cube[1]
    z = cube[2]
    w = cube[3]
    for _x in [x-1, x, x+1]:
        for _y in [y-1, y, y+1]:
            for _z in [z-1, z, z+1]:
                for _w in [w-1, w, w+1]:
                    if ((_x, _y, _z, _w) in grid) and (grid[(_x, _y, _z, _w)] == 1):
                        if (_x, _y, _z, _w) != (x, y, z, w):
                            n += 1
    return n
    
for cycle in range(0, 6):
    next_grid = {}
    grid = add_neighbors(grid)
    for cube in grid:
        no_active_neighbors = get_active_neighbors(cube, grid)
        if grid[cube] == 1:
            if no_active_neighbors in [2,3]:
                next_grid[cube] = 1
            else:
                next_grid[cube] = 0
        if grid[cube] == 0:
            if no_active_neighbors == 3:
                next_grid[cube] = 1
            else:
                next_grid[cube] = 0
    grid = next_grid.copy()

answer = 0
for cube in grid:
    if grid[cube] == 1:
        answer += 1
print(answer)