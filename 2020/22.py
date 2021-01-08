with open("input/22.txt") as f:
    lines = f.read().splitlines()

# 1
p1 = []
p2 = []
player = 1
for line in lines:
    if 'Player 1' in line:
        player = 1
        continue
    elif 'Player 2' in line:
        player = 2
        continue
    elif line == '':
        continue
    else:
        card = int(line)
        if player == 1:
            p1 += [card]
        elif player == 2:
            p2 += [card]
done = False
winner = 0
while not done:
    card_1 = p1[0]
    card_2 = p2[0]
    if card_1>card_2:
        p1 = p1[1:] + [card_1, card_2]
        p2 = p2[1:]
    elif card_2 > card_1:
        p2 = p2[1:] + [card_2, card_1]
        p1 = p1[1:]
    if len(p1) == 0:
        done = True
        winner = p2
    elif len(p2) == 0:
        done = True
        winner = p1
        
score = 0
multiplier = 1
for card in winner[::-1]:
    score += multiplier*card
    multiplier += 1
print(score)     


# 2
p1 = []
p2 = []
player = 1
for line in lines:
    if 'Player 1' in line:
        player = 1
        continue
    elif 'Player 2' in line:
        player = 2
        continue
    elif line == '':
        continue
    else:
        card = int(line)
        if player == 1:
            p1 += [card]
        elif player == 2:
            p2 += [card]

def play_game(p1, p2):
    done = False
    winner = 0
    previous_states = []
    while not done:
        state = ','.join([str(x) for x in (p1 + [";"] + p2)])
        if state in previous_states:
            # Player 1 wins
            done = True
            return 1
        previous_states += [state]

        # Start round
        card_1 = p1[0]
        card_2 = p2[0]
        p1 = p1[1:]
        p2 = p2[1:]
        if (len(p1) >= card_1) and (len(p2) >= card_2):
            winner_round = play_game(p1.copy()[:card_1], p2.copy()[:card_2])
        else:
            if card_1>card_2:
                winner_round = 1
            elif card_2 > card_1:
                winner_round = 2
        if winner_round == 1:
            p1 += [card_1, card_2]
        elif winner_round == 2:
            p2 += [card_2, card_1]
        # Check if we are done
        if len(p1) == 0:
            return 2
        elif len(p2) == 0:
            return 1
            
done = False
winner = 0
previous_states = []
while not done:
    state = ','.join([str(x) for x in (p1 + [";"] + p2)])
    if state in previous_states:
        # Player 1 wins
        done = True
        winner = p1
        break
    previous_states += [state]

    # Start round
    card_1 = p1[0]
    card_2 = p2[0]
    p1 = p1[1:]
    p2 = p2[1:]
    if (len(p1) >= card_1) and (len(p2) >= card_2):
        winner_round = play_game(p1.copy()[:card_1], p2.copy()[:card_2])
    else:
        if card_1>card_2:
            winner_round = 1
        elif card_2 > card_1:
            winner_round = 2
    if winner_round == 1:
        p1 += [card_1, card_2]
    elif winner_round == 2:
        p2 += [card_2, card_1]
    # Check if we are done
    if len(p1) == 0:
        done = True
        winner = p2
    elif len(p2) == 0:
        done = True
        winner = p1

score = 0
multiplier = 1
for card in winner[::-1]:
    score += multiplier*card
    multiplier += 1
print(score)            