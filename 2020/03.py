with open("input/03.txt") as f:
    grid = f.read().splitlines()

# 1
x = 0
y = 0
dest = len(grid)-1
row_length = len(grid[0])
trees = 0

def istree(x, y):
    pos_x = x % row_length
    char = grid[y][pos_x]
    if char == "#":
        return True
    else:
        return False

while y < dest:
    x += 3
    y += 1
    if istree(x, y):
        trees += 1
print(trees)

# 2
slopes_to_check = [[1,1],[3,1],[5,1],[7,1],[1,2]]
trees_found = [0,0,0,0,0]

for i in range(0, 5):
    x_slope = slopes_to_check[i][0]
    y_slope = slopes_to_check[i][1]
    x = 0
    y = 0
    dest = len(grid)-1
    trees = 0
    while y < dest:
        x += x_slope
        y += y_slope
        if istree(x, y):
            trees += 1
    trees_found[i] = trees
print(trees_found[0]*trees_found[1]*trees_found[2]*trees_found[3]*trees_found[4])