lines = open("input").readlines()
times = [int(x) for x in filter(None, lines[0].split(':')[1].split(' '))]
distances = [int(x) for x in filter(None, lines[1].split(':')[1].split(' '))]
races = [*zip(times, distances)]

result = 1
for race in races:
    wins = 0
    for i in range(race[0]):
        if i * (race[0] - i) > race[1]:
            wins += 1
    result *= wins

print(result)