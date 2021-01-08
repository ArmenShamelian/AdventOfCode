import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import pickle

file = open('input_16.txt', 'r')
input = file.read()

def apply_pattern(input, pattern):
    return sum(input * pattern[0:len(input)])

# Input * 10000
input = input * 10000
original_length = len(input)
offset = int(input[:7])

phases = 0
output = ''
while phases < 100:
    input_array = np.array([int(x) for x in input])
    print(phases)
    output = ''
    # First half is always 0s
    start_half = int(len(input)/2)
    output += '0' * start_half
    starting_sum = sum(input_array[start_half:])
    output += str(starting_sum)[-1]
    for i in range(start_half+1, len(input)):
        starting_sum -= input_array[i-1]
        output += str(starting_sum)[-1]
    input = output
    assert len(input) == original_length
    phases += 1

# First 8 digits = answer
print(output[offset:offset+8])
