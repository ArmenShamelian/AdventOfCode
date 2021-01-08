with open("input/02.txt") as f:
    i = f.readlines()

# 1
valid = 0
for line in i:
    _min = int(line.split("-")[0])
    _max = int(line.split("-")[1].split(" ")[0])
    l = line.split(":")[0][-1]
    pw = line.split(" ")[-1]
    
    occurrences = sum([1 if x == l else 0 for x in pw])
    if (occurrences >= _min) and (occurrences <= _max):
        valid += 1
print(valid)

# 2
valid = 0
for line in i:
    i1 = int(line.split("-")[0])
    i2 = int(line.split("-")[1].split(" ")[0])
    l = line.split(":")[0][-1]
    pw = line.split(" ")[-1]
    if ((pw[i1-1] == l) and not (pw[i2-1] == l)) or ((pw[i2-1] == l) and not (pw[i1-1] == l)):
        valid += 1
print(valid)