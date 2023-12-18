EXPAND = 1000000

class Universe():
    def __init__(self, lines):
        self.galaxies = []
        y = 0
        for line in lines:
            x = 0
            for char in [*line.strip()]:
                if char == "#":
                    self.galaxies.append({'x': x, 'y': y})
                x += 1
            y += 1

    def __repr__(self):
        return repr(self.galaxies)

    def expand(self):
        width = max(self.galaxies, key=lambda x: x['x'])['x']
        height = max(self.galaxies, key=lambda x: x['y'])['y']

        w = 0
        while w < width:
            if any(g['x'] == w for g in self.galaxies):
                w += 1
            else:
                for g in self.galaxies:
                    if g['x'] > w:
                        g['x'] += (EXPAND-1)
                width += (EXPAND-1)
                w += EXPAND

        h = 0
        while h < height:
            if any(g['y'] == h for g in self.galaxies):
                h += 1
            else:
                for g in self.galaxies:
                    if g['y'] > h:
                        g['y'] += (EXPAND-1)
                height += (EXPAND-1)
                h += EXPAND

lines = open("input").readlines()
universe = Universe(lines)
universe.expand()

distance = 0
for g1 in universe.galaxies:
    for g2 in universe.galaxies:
        d = abs(g1['x'] - g2['x']) + abs(g1['y'] - g2['y'])
        distance += d
print(int(distance/2))