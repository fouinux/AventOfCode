lines = open("input").readlines()
seeds = [int(x) for x in lines[0].split(':')[1].lstrip().rstrip().split(' ')]

# Parse maps
maps = list()
map_index = -1
for line in lines[2:]:
    line = line.rstrip()
    if 'map:' in line:
        map_index += 1
        maps.append(list())
    elif len(line) > 0:
        maps[map_index].append([int(x) for x in line.split(' ')])

# Apply maps
new_seeds = list()
for seed in seeds:
    for map in maps:
        found = False
        for rng in map:
            if seed in range(rng[1], rng[1]+rng[2]):
                seed = seed + (rng[0] - rng[1])
                found = True
                break
        if found:
            continue
    new_seeds.append(seed)

print(min(new_seeds))