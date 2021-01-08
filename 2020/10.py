with open("input/10.txt") as f:
    inputs = f.read().splitlines()

# 1
inputs = [int(x) for x in inputs]
inputs.sort()

inputs = [0] + inputs
inputs.append(inputs[-1]+3)

prev_joltage = 0
diff_1 = 0
diff_2 = 0
diff_3 = 0
for i in inputs[1:]:
    diff = i - prev_joltage
    if diff == 1:
        diff_1 += 1
    if diff == 2:
        diff_2 += 1
    if diff == 3:
        diff_3 += 1
    prev_joltage = i
print(diff_1*diff_3)

# 2
arrangements = {}

def count_arrangements(i, v):
    # Count possible arrangements from v until end
    next_values = inputs[i+1:]
    no_arrangements = 0
    for next_value in next_values:
        if next_value - v <= 3:
            no_arrangements += arrangements[next_value]
        else:
            break
    return no_arrangements

arrangements = {}
arrangements[inputs[-1]] = 1
for ix in range(len(inputs)-2, -1, -1):
    v = inputs[ix]
    arrangements[v] = count_arrangements(ix, v)
    ix -= 1
print(arrangements[inputs[0]])