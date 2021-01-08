with open("input/25.txt") as f:
    lines = f.read().splitlines()

subject = 7
value = 1
loop = 0
key1 = int(lines[0])
key2 = int(lines[1])
loop1 = 0
loop2 = 0
done = False
while not done:
    loop += 1
    value *= subject
    value %= 20201227
    if value in [key1, key2]:
        if value == key1:
            loop1 = loop
        if value == key2:
            loop2 = loop
        if (loop1>0) or (loop2>0):
            done = True

if loop1 > 0:
    subject = key2
    loopsize = loop1
elif loop2 > 0:
    subject = key1
    loopsize = loop2

value = 1
for i in range(0, loopsize):
    loop += 1
    value *= subject
    value %= 20201227
print(value)