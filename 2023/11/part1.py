class Universe():
    def __init__(self, lines):
        self.space = []
        for line in lines:
            self.space.append([*line.strip()])

    def __repr__(self):
        s = ''
        for l in self.space:
            for c in l:
                s += c
            s += '\n'
        return s

    def expand(self):
        new_space = []
        # Lines of space
        for l in self.space:
            if '#' in l:
                new_space.append(l)
            else:
                new_space.append(l)
                new_space.append(l)

        # Transpose
        new_space = list(map(list, zip(*new_space)))

        self.space = []
        # Columns of space
        for c in new_space:
            if '#' in c:
                self.space.append(c)
            else:
                self.space.append(c)
                self.space.append(c)

        # Transpose
        self.space = list(map(list, zip(*self.space)))

    def get_galaxies(self):
        galaxies_list = []
        for y in range(len(self.space)):
            for x in range(len(self.space[0])):
                if self.space[y][x] == '#':
                    galaxies_list.append((x, y))
        return galaxies_list



lines = open("input").readlines()
universe = Universe(lines)
universe.expand()

galaxies = universe.get_galaxies()
distance = 0
for g1 in galaxies:
    for g2 in galaxies:
        d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        distance += d
print(int(distance/2))