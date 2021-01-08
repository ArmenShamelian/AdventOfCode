with open("input/18.txt") as f:
    lines = f.read().splitlines()

# 1
import re
total = 0

class op(int):
    def __init__(self, v) :
        self.value = v

    def __add__(self, v) :
        return op(int(self.value) + int(v.value))

    def __sub__(self, v) :
        return op(int(self.value) * int(v.value))

for line in lines:
    line = line.replace('*', '-')
    line = re.sub(r'(\d+)', r'op(\1)', line)
    answer = eval(line)
    total += answer
print(total)

# 2
import re
total = 0

class op(int):
    def __init__(self, v) :
        self.value = v

    def __mul__(self, v) :
        return op(int(self.value) + int(v.value))

    def __sub__(self, v) :
        return op(int(self.value) * int(v.value))

for line in lines:
    line = line.replace('*', '-')
    line = line.replace('+', '*')
    line = re.sub(r'(\d+)', r'op(\1)', line)
    answer = eval(line)
    total += answer
print(total)