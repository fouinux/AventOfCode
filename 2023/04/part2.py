lines = open('input').readlines()
scratchcards = [1] * len(lines)
counter = 0

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
            points += 1

    for i in range(counter+1, counter+1+points):
        scratchcards[i] += scratchcards[counter]

    counter += 1

print(sum(scratchcards))
