class Seed():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, self.start, self.stop)


class SeedMap():
    def __init__(self, dest, src, len):
        self.dest = dest
        self.src = src
        self.len = len
        self.src_range = range(src, src + len)
        self.conv = dest - src

    def __repr__(self):
        return "{0}({1}, {2}, {3})".format(self.__class__.__name__, self.dest, self.src, self.len)

    def convert(self, seed : Seed):
        src_seed = None
        dest_seed = None
        if seed.start in self.src_range and seed.stop in self.src_range: # Convert all
            dest_seed = Seed(seed.start + self.conv, seed.stop + self.conv)
        elif seed.start in self.src_range: # Divide into 2
            length = (self.src + self.len) - seed.start
            src_seed = Seed(seed.start + length, seed.stop)
            dest_seed = Seed(seed.start + self.conv, seed.start + length + self.conv)
        elif seed.stop in self.src_range: # Divide into 2
            length = seed.stop - self.src
            src_seed = Seed(seed.start, seed.stop - length)
            dest_seed = Seed(self.dest, self.dest + length)
        else:
            src_seed = seed
        return (src_seed, dest_seed)


lines = open("input").readlines()
seeds = [int(x) for x in lines[0].split(':')[1].lstrip().rstrip().split(' ')]
seeds = [Seed(x, x+y) for x, y in zip(seeds[0::2], seeds[1::2])]

# Parse field
fields = list()
field_index = -1
for line in lines[2:]:
    line = line.rstrip()
    if 'map:' in line:
        field_index += 1
        fields.append(list())
    elif len(line) > 0:
        fields[field_index].append(SeedMap(*[int(x) for x in line.split(' ')]))

# Apply all maps
current_seeds = seeds
rest_seeds = current_seeds
for field in fields:
    next_seeds = list()
    for map in field:
        rest_seeds = list()
        for seed in current_seeds:
            src_seed, dest_seed = map.convert(seed)
            # print("{0} + {1} => {2} & {3}".format(seed, map, src_seed, dest_seed))
            if src_seed is not None:
                rest_seeds.append(src_seed)
            if dest_seed is not None:
                next_seeds.append(dest_seed)
        current_seeds = rest_seeds
    current_seeds += next_seeds

seed_min = None
for seed in current_seeds:
    if seed_min is None:
        seed_min = seed
    elif seed.start < seed_min.start:
        seed_min = seed
# print(current_seeds)
print(seed_min.start)