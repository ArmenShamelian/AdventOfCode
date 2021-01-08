import numpy as np


def load_input():
    file = open('input_22.txt', 'r')
    input_ = file.read()
    return input_


def initialize_deck(size=10007):
    deck = [x for x in range(size)]
    return deck


def cut(deck, n):
    cut_1 = deck[:n]
    cut_2 = deck[n:]
    deck = cut_2 + cut_1
    return deck


def deal_with_increment(deck, n):
    res = {}
    i = 0
    for index, card in enumerate(deck):
        res[i] = deck[index]
        i += n
        i = i % len(deck)
    deck = [res[i] for i in range(len(deck))]
    return deck


def apply_shuffle(shuffle, deck):
    if shuffle == 'deal into new stack':
        deck.reverse()
    elif shuffle[:3] == 'cut':
        n = int(shuffle.split(' ')[-1])
        deck = cut(deck, n)
    elif 'deal with increment' in shuffle:
        n = int(shuffle.split(' ')[-1])
        deck = deal_with_increment(deck, n)
    return deck


def shuffle_deck(deck, input_):
    for line in input_:
        deck = apply_shuffle(line, deck)
    return deck

# Execute
def run():
    input_ = load_input()
    input_ = input_.split('\n')
    deck = initialize_deck()
    deck = shuffle_deck(deck, input_)
    return deck.index(2019)


answer = run()
print(answer)

