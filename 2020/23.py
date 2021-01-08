with open("input/23.txt") as f:
    lines = f.read().splitlines()

# 1
cups = [int(x) for x in lines[0]]
max_cup = max(cups)

def pick_destination_cup(cups, i):
    goal = i-1
    if goal == 0:
        goal = max_cup
    if goal in cups:
        return goal
    else:
        return pick_destination_cup(cups, goal)

for i in range(0, 100):
    current_cup = cups[0]
    picked_cups = cups[1:4]
    remaining_cups = [cups[0]] + cups[4:]
    destination_cup = pick_destination_cup(cups[4:], current_cup)
    destination_index = remaining_cups.index(destination_cup)
    cups = remaining_cups[0:destination_index+1] + picked_cups + remaining_cups[destination_index+1:]
    cups = cups[1:] + [cups[0]]
print(cups)

# 2
raw_cups = [int(x) for x in lines[0]] + list(range(len(lines[0])+1, 1000001))
cups = {}
for i, cup in enumerate(raw_cups):
    cups[cup] = raw_cups[(i+1) % len(raw_cups)]
max_cup = max(cups)

def pick_destination_cup(cups, i, skip):
    goal = i-1
    if goal == 0:
        goal = len(raw_cups)
    if goal in skip:
        return pick_destination_cup(cups, goal, skip)
    return goal

current_cup = raw_cups[0]
for i in range(0,10000000):
    skip = [cups[current_cup], cups[cups[current_cup]], cups[cups[cups[current_cup]]]]
    destination_cup = pick_destination_cup(cups, current_cup, skip)
    next_dest = cups[destination_cup]
    next_curr = cups[cups[cups[cups[current_cup]]]]
    cups[destination_cup] = cups[current_cup]
    cups[cups[cups[cups[current_cup]]]] = next_dest
    cups[current_cup] = next_curr
    current_cup = cups[current_cup]
print(cups[1]*cups[cups[1]])