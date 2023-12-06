lines = open('input').readlines()
score = 0

for l in lines:
    line = l.split(':')[1].lstrip().rstrip() # Remove header

    cards, winners = line.split('|')

    cards = cards.rstrip().split(' ')
    while '' in cards:
        cards.remove('')

    winners = winners.lstrip().split(' ')
    while '' in winners:
        winners.remove('')

    points = 0
    for card in cards:
        if card in winners:
            if points == 0:
                points = 1
            else:
                points *= 2

    score += points

print(score)
