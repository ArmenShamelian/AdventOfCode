with open("input/21.txt") as f:
    lines = f.read().splitlines()

# 1
# Parse
ingredients = {}
for line in lines:
    _ingredients = line.split('(contains ')[0].split(' ')
    _allergens = line.split('(contains ')[1].split(')')[0].split(', ')
    for i in _ingredients:
        if i != '':
            if i in ingredients:
                ingredients[i] = list(set(ingredients[i] + _allergens))
            else:
                ingredients[i] = _allergens

no_allergens = []
# Eliminate allergens
for i in ingredients:
    eliminated_allergens = []
    allergens = ingredients[i]
    for line in lines:
        for a in allergens:
            if (i not in line) and (a in line):
                eliminated_allergens += [a]
    left_allergens = [x for x in allergens if x not in eliminated_allergens]
    ingredients[i] = left_allergens
    if len(left_allergens) == 0:
        no_allergens += [i]

total = 0
for line in lines:
    _ingredients = line.split('(contains ')[0].split(' ')
    for i in _ingredients:
        if i != '':
            if i in no_allergens:
                total += 1    

print(total)

# 2
# Eliminate duplicates, run this until no more multi allergen ingredients left
for n in range(0, 10):
    for i in ingredients:
        if len(ingredients[i]) > 1:
            # Check which allergens are already in different ingredients and remove them
            for a in ingredients[i]:
                for ii in ingredients:
                    if ii != i:
                        if len(ingredients[ii]) == 1:
                            if a in ingredients[ii]:
                                ingredients[i] = [x for x in ingredients[i] if x != a]
allergens = []
for i in ingredients:
    if len(ingredients[i]) > 0:
        allergens += [(i, ingredients[i][0])]
allergens.sort(key=lambda x: x[1])
print(','.join([x[0] for x in allergens]))