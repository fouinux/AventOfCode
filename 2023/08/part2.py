import math

def exce_map(directions, maps):
    counter = 0
    keys = []
    for key in maps.keys():
        if key[2] == 'A':
            keys.append(key)

    results = []

    while True:
        for d in directions:
            if d == 'L':
                for i in range(len(keys)):
                    keys[i] = maps[keys[i]][0]
            else:
                for i in range(len(keys)):
                    keys[i] = maps[keys[i]][1]

            counter += 1
            for key in keys:
                if key[2] == 'Z':
                    results.append(counter)
                    keys.remove(key)
            if len(keys) == 0:
                return math.lcm(*results)

lines = open("input").readlines()
directions = [*lines[0].rstrip()]
maps = {}
for line in lines[2:]:
    key, value = line.split('=')
    maps[key.rstrip()] = [x.strip() for x in filter(None, value.replace('(', '').replace(')', '').split(','))]

print(exce_map(directions, maps))
