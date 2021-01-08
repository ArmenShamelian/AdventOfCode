with open("input/05.txt") as f:
    passes = f.read().splitlines()

# 1
rows = 128
cols = 8

def get_pass_id(p):
    min_row = 0
    max_row = rows-1
    row_range = rows
    min_col = 0
    max_col = cols-1
    col_range = cols
    for c in p[0:7]:
        if c == "F":
            max_row -= int(row_range*0.5)
        elif c == "B":
            min_row += int(row_range*0.5)
        row_range *= 0.5
    for c in p[7:]:
        if c == "L":
            max_col -= int(col_range*0.5)
        elif c == "R":
            min_col += int(col_range*0.5)
        col_range = int(col_range*0.5)
    return min_row * 8 + min_col
            

highest_id = 0
for p in passes:
    _id = get_pass_id(p)
    if _id > highest_id:
        highest_id = _id
print(highest_id)

# 2
filled_seats = []
for p in passes:
    filled_seats += [get_pass_id(p)]
for i in range(min(filled_seats), max(filled_seats)):
    if (i not in filled_seats) and ((i+1) in filled_seats) and ((i-1) in filled_seats):
        print(i)
        break