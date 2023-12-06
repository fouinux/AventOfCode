lines = open('input').readlines()
pos_count = 0
counter = 1
for l in lines:
    line = l.split(':')[1].lstrip().rstrip()
    pos = True
    for games in line.split(';'):
        for game in games.split(','):
            # print(game.lstrip().rstrip())
            if "blue" in game:
                if int(game.lstrip().split(' ')[0]) > 14:
                    pos = False
                    # print('fail')
            if "red" in game:
                if int(game.lstrip().split(' ')[0]) > 12:
                    pos = False
                    # print('fail')
            if "green" in game:
                if int(game.lstrip().split(' ')[0]) > 13:
                    pos = False
                    # print('fail')
    if pos:
        pos_count += counter
    counter += 1

print(pos_count)
