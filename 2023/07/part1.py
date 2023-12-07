def poker_type(hand_str):
    hand = [*hand_str]
    hand_dict = dict()
    for card in hand:
        if card not in hand_dict:
            hand_dict[card] = 1
        else:
            hand_dict[card] += 1

    if 5 in hand_dict.values():
        return 0 # Five of a kind
    if 4 in hand_dict.values():
        return 1 # Four of a kind
    if 3 in hand_dict.values():
        if 2 in hand_dict.values():
            return 2 # Full house
        return 3 # Three of a kind
    pair = list(hand_dict.values()).count(2)
    if pair == 2:
        return 4 # Two pair
    if pair == 1:
        return 5 # One pair
    return 6 # High card

CARD_ORDER = "AKQJT98765432"

def poker_sort(hand):
    order = ''
    for card in hand[0]:
        order += f"{CARD_ORDER.index(card):02}"
    return int(order)

lines = open("input").readlines()
hands = list()
for line in lines:
    hands.append(line.rstrip().split(' '))

# Class hands by type
hands_dict = dict()
for hand in hands:
    ptype = poker_type(hand[0])
    if ptype not in hands_dict.keys():
        hands_dict[ptype] = list()
    hands_dict[ptype].append(hand)
hands_dict = dict(sorted(hands_dict.items()))

# Overall sort hands
sorted_hands = list()
for ptype, hand_list in hands_dict.items():
    sorted_hands += sorted(hand_list, key=poker_sort)
sorted_hands.reverse()

# Result
result = 0
for count in range(len(sorted_hands)):
    result += (count+1) * int(sorted_hands[count][1])
print(result)
