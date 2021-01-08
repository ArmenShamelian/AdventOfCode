with open("input/24.txt") as f:
    lines = f.read().splitlines()

# 1
black_tiles = []
coords = {'e': (1, 0), 'w': (-1, 0), 'ne': (1, -1), 'nw': (0, -1), 'se':(1, 1), 'sw':(0, 1)}
for tile in lines:
    s = tile
    c = (0, 0)
    while s != '':
        if s[0] in ('e', 'w'):
            c = (c[0] + coords[s[0]][0], c[1])
            s = s[1:]
        else:
            c = (c[0] + coords[s[0:2]][0], c[1] + coords[s[0:2]][1])
            if c[1]%2 == 1:
                # If moved to an uneven row: x -1
                c = (c[0]-1, c[1])
            s = s[2:]
    if c in black_tiles:
        black_tiles = [x for x in black_tiles if x != c]
    else:
        black_tiles += [c]
print(len(black_tiles))

# 2
grid = {}

min_x = min([x[0] for x in black_tiles])
max_x = max([x[0] for x in black_tiles])
min_y = min([x[1] for x in black_tiles])
max_y = max([x[1] for x in black_tiles])

for y in range(min_y-2, max_y+3):
    for x in range(min_x-2, max_x+3):
        if (x, y) in black_tiles:
            grid[(x, y)] = 'b'
        else:
            grid[(x, y)] = 'w'

def add_white_neighbors(grid):
    new_grid = grid.copy()
    for tile in grid:
        if grid[tile] == 'b':
            neighbors = []
            for x in range(tile[0]-3, tile[0]+4):
                for y in range(tile[1]-3, tile[1]+4):
                    if not (x, y) in grid:
                        new_grid[(x, y)] = 'w'
    return new_grid
    
def get_neighbors(tile, grid):
    if tile[1]%2==0:
        neighbors = [(-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1), (0, 1)]
    else:
        neighbors = [(-1, 0), (1, 0), (0, -1), (1, -1), (0, 1), (1, 1)]
    result = [tuple(map(sum, zip(n, tile))) for n in neighbors]
    result = [x for x in result if x in grid]
    return result
        

def apply_flips(grid):
    new_grid = grid.copy()
    for tile in grid:
        neighbors = get_neighbors(tile, grid)
        black_neighbors = 0
        for n in neighbors:
            if grid[n] == 'b':
                black_neighbors += 1
        if (grid[tile] == 'b') and ((black_neighbors == 0) or (black_neighbors > 2)):
            new_grid[tile] = 'w'
        elif (grid[tile] == 'w') and (black_neighbors == 2):
            new_grid[tile] = 'b'
    return new_grid
        
for i in range(0,100):
    grid = add_white_neighbors(grid)
    grid = apply_flips(grid)

black_total = 0
for x in grid:
    if grid[x] == 'b':
        black_total += 1
print(black_total)