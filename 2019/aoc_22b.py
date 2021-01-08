import numpy as np


def load_input():
    file = open('input_22.txt', 'r')
    input_ = file.read()
    return input_


def initialize_deck(size=10007):
    deck = [x for x in range(size)]
    return deck


def cut(decksize, answer, n):
    new_position = (answer + decksize - n) % decksize
    return new_position


def deal_with_increment(decksize, answer, n):
    new_position = (n * answer) % decksize
    return new_position


def apply_shuffle(shuffle, decksize, answer):
    if shuffle == 'deal into new stack':
        # Count indices from the end, subtract 1 because 0-indexed list.
        answer = decksize - answer - 1
    elif shuffle[:3] == 'cut':
        n = int(shuffle.split(' ')[-1])
        answer = cut(decksize, answer, n)
    elif 'deal with increment' in shuffle:
        n = int(shuffle.split(' ')[-1])
        answer = deal_with_increment(decksize, answer, n)
    return answer


def shuffle_deck(decksize, answer, input_):
    for line in input_:
        answer = apply_shuffle(line, decksize, answer)
    return answer


# Execute
def run():
    input_ = load_input()
    input_ = input_.split('\n')
    decksize = 119315717514047


answer = run()
print(answer)

