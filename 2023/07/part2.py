def poker_type(hand_str):
    hand = [*hand_str]
    hand_dict = dict()
    for card in hand:
        if card not in hand_dict:
            hand_dict[card] = 1
        else:
            hand_dict[card] += 1

    # Ignore Joker
    joker = 0
    if "J" in hand_dict.keys():
        joker = hand_dict['J']
        del hand_dict['J']

    if 5 in hand_dict.values():
        return 0 # Five of a kind
    if 4 in hand_dict.values():
        if joker == 1:
            return 0 # Five of a kind
        return 1 # Four of a kind
    if 3 in hand_dict.values():
        if 2 in hand_dict.values():
            return 2 # Full house
        if joker == 2:
            return 0 # Five of a kind
        if joker == 1:
            return 1 # Four of a kind
        return 3 # Three of a kind
    pair = list(hand_dict.values()).count(2)
    if pair == 2:
        if joker == 1:
            return 2 # Full house
        return 4 # Two pair
    if pair == 1:
        if joker == 3:
            return 0 # Five of a kind
        if joker == 2:
            return 1 # Four of a kind
        if joker == 1:
            return 3 # Three of a kind
        return 5 # One pair
    if joker == 5:
        return 0 # Five of a kind
    if joker == 4:
        return 0 # Five of a kind
    if joker == 3:
        return 1 # Four of a kind
    if joker == 2:
        return 3 # Three of a kind
    if joker == 1:
        return 5 # One pair
    return 6 # High card

CARD_ORDER = "AKQT98765432J"

def poker_sort(hand):
    order = ''
    for card in hand[0]:
        order += f"{CARD_ORDER.index(card):02}"
    return int(order)

lines = open("input").readlines()
hands = list()
for line in lines:
    hands.append(line.rstrip().split(' '))
print(hands)

# Class hands by type
hands_dict = dict()
for hand in hands:
    ptype = poker_type(hand[0])
    if ptype not in hands_dict.keys():
        hands_dict[ptype] = list()
    hands_dict[ptype].append(hand)
hands_dict = dict(sorted(hands_dict.items()))
print(hands_dict)

# Overall sort hands
sorted_hands = list()
for ptype, hand_list in hands_dict.items():
    sorted_hands += sorted(hand_list, key=poker_sort)
sorted_hands.reverse()
print(sorted_hands)

# Result
result = 0
for count in range(len(sorted_hands)):
    result += (count+1) * int(sorted_hands[count][1])
print(result)
