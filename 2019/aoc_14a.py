import numpy as np
from math import ceil

file = open("input_14.txt", "r")
input = file.read()
input = input.split('\n')
input = [s.split(' => ') for s in input]

d = {}
waste_pool = {}

# Create Dict
for i, ls in enumerate(input):
    ingr = ls[0]
    ingr = ingr.split(', ')
    ingr = [tuple(s.split(' ')) for s in ingr]
    result = ls[1].split(' ')[1]
    quantity = int(ls[1].split(' ')[0])
    ingr = [tuple([int(t[0]), t[1]]) for t in ingr]
    d[result] = [quantity, ingr]
    waste_pool[result] = 0


def get_ingredients(ingredient, quantity):
    ore_needed = 0
    ingredients_needed = d[ingredient][1]
    for (q, i) in ingredients_needed:
        if i == 'ORE':
            creation_unit = d[ingredient][0]
            ore_per_unit = d[ingredient][1][0][0]
            # Round up from creation unit
            ore_needed_total = ceil(quantity / creation_unit) * ore_per_unit
            # log
            ores_made.setdefault(ingredient, 0)
            ores_made[ingredient] += ore_needed_total
            return ore_needed_total
        else:
            creation_unit = d[i][0]
            creation_amount = d[ingredient][0]
            # Take existing waste into account when calculating new need
            old_waste = waste_pool[i]
            quantity_needed = ceil((quantity*q) / creation_amount) - old_waste
            min_creation = ceil(quantity_needed / creation_unit) * creation_unit
            new_waste = max(0, min_creation - quantity_needed)
            print(f"Need {quantity_needed} of {i} made per {creation_unit}. Have {old_waste} waste. Adding {new_waste-old_waste} waste. Making {min_creation} new {i}")
            waste_pool[i] = new_waste
            ore_needed += get_ingredients(i, min_creation)
    return ore_needed


ores_made = {}
ore_needed = get_ingredients('FUEL', 1)

print(ore_needed)
print(ores_made)