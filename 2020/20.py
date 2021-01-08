with open("input/20.txt") as f:
    lines = f.read().splitlines()

# 1
# Parse
tiles = {}
for i, line in enumerate(lines):
    if 'Tile ' in line:
        tile_id = int(line.split(' ')[1][:-1])
        rows = []
        for n in range(i+1, i+11):
            rows += [lines[n]]
        tiles[tile_id] = rows

# Borders dict
borders = {}
for tile_id in tiles:
    tile = tiles[tile_id]
    top = tile[0]
    bottom = tile[9]
    left = ''.join([t[0] for t in tile])
    right = ''.join([t[9] for t in tile])
    for b in [top, bottom, left, right]:
        if b in borders:
            borders[b] += [tile_id]
        else:
            borders[b] = [tile_id]
        flipped = b[::-1]
        if flipped in borders:
            borders[flipped] += [tile_id]
        else:
            borders[flipped] = [tile_id]

# Check which tiles have 2 borders with no match (4 including flipped ones)
no_match = {}
for border in borders:
    ids = borders[border]
    if len(ids) == 1:
        if ids[0] in no_match:
            no_match[ids[0]] += 1
        else:
            no_match[ids[0]] = 1

# Print answer
total = 1
corners = []
for id in no_match:
    if no_match[id] == 4:
        corners += [id]
        total *= id
print(total)

# 2
import re
def rotate(tile, direction):
    if direction == 'right':
        new = list(zip(*tile[::-1]))
    elif direction == 'left':
        new = list(reversed(list(zip(*tile))))
    new = [''.join(line) for line in new]
    return new

def flip(tile):
    flipped = []
    for line in tile:
        flipped += [line[::-1]]
    return flipped

def get_orientations(tile):
    s = []
    s += [tile]
    s += [rotate(tile, 'left')]
    s += [rotate(tile, 'right')]
    s += [rotate(rotate(tile, 'left'), 'left')]
    flipped = flip(tile)
    s += [flipped]
    s += [rotate(flipped, 'left')]
    s += [rotate(flipped, 'right')]
    s += [rotate(rotate(flipped, 'left'), 'left')]
    return s

def get_borders(tile):
    top = tile[0]
    bottom = tile[9]
    left = ''.join([t[0] for t in tile])
    right = ''.join([t[9] for t in tile])
    return [top, bottom, left, right]

# Re-use corners from Part 1
# Start building up the grid at a random corner for 12 by 12 grid. Rotate left first so it's the top left corner.
tiles = {}
for i, line in enumerate(lines):
    if 'Tile ' in line:
        tile_id = int(line.split(' ')[1][:-1])
        rows = []
        for n in range(i+1, i+11):
            rows += [lines[n]]
        tiles[tile_id] = rows

grid = {}
grid[0, 0] = rotate(tiles[corners[0]], 'left')
del tiles[corners[0]]
for y in range(1, 12):
    # Find tile that matches bottom of previous tile
    bottom_to_match = grid[0, y-1][9]
    found = False
    found_id = False
    for id in tiles:
        if found:
            break
        tile = tiles[id]
        orientations = get_orientations(tile)
        for orientation in orientations:
            borders = get_borders(orientation)
            if borders[0] == bottom_to_match:
                grid[0, y] = orientation
                found = True
                found_id = id
                break
    del tiles[found_id]
        
# Fill in the rows too
for y in range(0, 12):
    for x in range(1, 12):
        # Find tile that matches right border of previous tile
        right_to_match = ''.join([t[9] for t in grid[x-1, y]])
        found = False
        found_id = 0
        for id in tiles:
            if found:
                break
            tile = tiles[id]
            orientations = get_orientations(tile)
            for orientation in orientations:
                borders = get_borders(orientation)
                if borders[2] == right_to_match:
                    grid[x, y] = orientation
                    found = True
                    found_id = id
                    break
        del tiles[found_id]

# Strip borders
stripped = {}
for c in grid:
    tile = grid[c]
    stripped_tile = [row[1:9] for row in tile[1:9]]
    stripped[c] = stripped_tile

# Remove the gaps
grid = []
for y in range(0, 12):
    for i in range(0, 8):
        row = ''
        for x in range(0, 12):
            row += stripped[x, y][i]
        grid += [row]    
        
def find_monsters(grid):
    found = 0
    for y in range(0,96-3):
        for x in range(0,96-20):
            m1 = (re.match(r"..................#.", grid[y][x:x+20]) != None)
            m2 = (re.match(r"#....##....##....###", grid[y+1][x:x+20]) != None)
            m3 = (re.match(r".#..#..#..#..#..#...", grid[y+2][x:x+20]) != None)
            if m1 and m2 and m3:
                found += 1
    return found
        
total_filled = 0
for line in grid:
    for c in line:
        if c == '#':
            total_filled += 1
for orientation in get_orientations(grid):
    monsters = find_monsters(orientation)
    tiles_left = total_filled - 15 * monsters
    if monsters > 0:
        print(tiles_left)