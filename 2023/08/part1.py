def exce_map(directions, maps):
    counter = 0
    key = 'AAA'
    while True:
        for d in directions:
            if d == 'L':
                key = maps[key][0]
            else:
                key = maps[key][1]
            counter += 1
            if key == 'ZZZ':
                return counter

lines = open("input").readlines()
directions = [*lines[0].rstrip()]
maps = {}
for line in lines[2:]:
    key, value = line.split('=')
    maps[key.rstrip()] = [x.strip() for x in filter(None, value.replace('(', '').replace(')', '').split(','))]

print(exce_map(directions, maps))
