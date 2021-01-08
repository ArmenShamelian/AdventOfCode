with open("input/01.txt") as f:
    i = f.readlines()
i = [int(x) for x in i]

# 2
r = range(0, len(i))
for x in r:
    for y in r[x+1:]:
        for z in r[y+1:]:
            a = i[x]+i[y]+i[z]
            if a==2020:
                print(i[x]*i[y]*i[z])
                exit()