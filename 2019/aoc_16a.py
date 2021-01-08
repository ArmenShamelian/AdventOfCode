import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = open('input_16.txt', 'r')
input = file.read()


def get_pattern(base_pattern, i):
    pattern = []
    for c in base_pattern:
        pattern += [c] * (i+1)
    return pattern


def apply_pattern(input, pattern):
    output = 0
    for i, v in enumerate(input):
        # Skip the first value once
        if i == 0:
            pattern_index = 1
        else:
            pattern_index = (i+1) % len(pattern)
        value = int(v)
        output += value * pattern[pattern_index]
    return output

# Perform 1 phase
original_length = len(input)
phases = 0
while phases < 100:
    print(phases)
    output = ''
    for i, c in enumerate(input):
        input_value = int(c)
        base_pattern = [0, 1, 0, -1]
        #transform based on i
        pattern = get_pattern(base_pattern, i)
        result = apply_pattern(input, pattern)
        # take ones digit
        result = str(result)[-1]
        output += result
    input = output
    assert len(input) == original_length
    phases += 1

# First 8 digits = answer
print(output[:8])