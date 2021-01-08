with open("input/09.txt") as f:
    inputs = f.read().splitlines()

# 1
def check_valid_sum(i, p):
    valid_numbers = []
    for number in p:
        valid_numbers += [i - int(number)]
    for number in p:
        if int(number) in valid_numbers:
            return True
    return False

preamble = 25
for ix in range(0,len(inputs)):
    # Skip preamble
    if ix < preamble:
        continue
    i = int(inputs[ix])
    valid = check_valid_sum(i, inputs[ix-preamble:ix])
    if not valid:
        print(i)
        break

# 2
inputs = [int(x) for x in inputs]
# Use answer of # 1 
ans = 36845998
start = 0
end = 0
while True:
    total = sum(inputs[start:end])
    if total == ans:
        print(min(inputs[start:end]) + max(inputs[start:end]))
        break
    if total < ans:
        end += 1
    elif total > ans:
        start += 1