with open("input/07.txt") as f:
    lines = f.read().splitlines()

# 1
# Build dict
bags = {}
for line in lines:
    bag = line.split(' bag')[0]
    bags[bag] = []
    contents = line.split('contain ')[1].split(', ')
    for content in contents:
        number = content.split(' ')[0]
        content_bag = " ".join(content.split(' ')[1:]).split(' bag')[0]
        bags[bag] += [(content_bag, number)]
        
# Check how many entries can contain at least 1 Shiny Gold bag directly
n = 0
bags_checked = set([])
bags_to_check = []
for bag in bags:
    if "shiny gold" in str(bags[bag]):
        n += 1
        can_contain += [bag]
        bags_checked.add(bag)

# Now indirectly
while len(can_contain) > 0:
    bag_to_check = can_contain.pop()
    for bag in bags:
        if (bag_to_check in str(bags[bag])):
            if bag not in bags_checked:
                n += 1
            can_contain += [bag]
            bags_checked.add(bag)
print(n)

# 2
# Recursively count contents
def count_contents(bag):
    contents = bags[bag]
    if contents == [('other', 'no')]:
        return 1
    total = 1
    for content in contents:
        total += int(content[1]) * count_contents(content[0])
    return total

print(count_contents("shiny gold") - 1)