with open("input/06.txt") as f:
    lines = f.read().splitlines()

# 1
# Parse
def read_answer(start, end):
    answer = ''
    for i in range(start, end):
        answer += lines[i]
    return answer

answers = []
start = 0
end = 0
for l in lines:
    if l == '':
        answers += [read_answer(start, end)]
        start = end+1
        end = start
    else:
        end += 1
        if end == len(lines):
            answers += [read_answer(start, end)]

counts = 0
for a in answers:
    counts += len(set(a))
print(counts)

# 2
# Parse differently
def read_answer(start, end):
    this_answers = []
    for i in range(start, end):
        this_answers += [lines[i]]
    # Check which answers are in each sublist
    correct_answers = []
    for c in this_answers[0]:
        c_in_all = True
        for a in this_answers:
            if not (c in a):
                c_in_all = False
        if c_in_all:
            correct_answers += [c]
    return correct_answers

answers = []
start = 0
end = 0
for l in lines:
    if l == '':
        answers += [read_answer(start, end)]
        start = end+1
        end = start
    else:
        end += 1
        if end == len(lines):
            answers += [read_answer(start, end)]
            
counts = 0
for a in answers:
    counts += len(set(a))
print(counts)