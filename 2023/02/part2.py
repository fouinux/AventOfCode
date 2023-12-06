lines = open('input').readlines()
pos_count = 0
for l in lines:
    line = l.split(':')[1].lstrip().rstrip()
    blue_max = 0
    red_max = 0
    green_max = 0
    for games in line.split(';'):
        for game in games.split(','):
            if "blue" in game:
                blue =  int(game.lstrip().split(' ')[0])
                if blue > blue_max:
                    blue_max = blue
            if "red" in game:
                red =  int(game.lstrip().split(' ')[0])
                if red > red_max:
                    red_max = red
            if "green" in game:
                green =  int(game.lstrip().split(' ')[0])
                if green > green_max:
                    green_max = green
    pos_count += blue_max*red_max*green_max

print(pos_count)
