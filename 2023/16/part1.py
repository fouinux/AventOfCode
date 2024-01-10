class Beam():
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

def solve(mirror, light, beam):
    x = beam.x
    y = beam.y
    dir = beam.dir

    if y not in range(len(mirror)):
        return []
    if x not in range(len(mirror[0])):
        return []

    if light[y][x] == dir: # Already done
        return []

    light[y][x] = dir

    match mirror[y][x]:
        case '.':
            match dir:
                case '>':
                    return [Beam(x+1, y, '>')]
                case '<':
                    return [Beam(x-1, y, '<')]
                case 'v':
                    return [Beam(x, y+1, 'v')]
                case '^':
                    return [Beam(x, y-1, '^')]

        case '/':
            match dir:
                case '>':
                    return [Beam(x, y-1, '^')]
                case '<':
                    return [Beam(x, y+1, 'v')]
                case 'v':
                    return [Beam(x-1, y, '<')]
                case '^':
                    return [Beam(x+1, y, '>')]

        case '\\':
            match dir:
                case '>':
                    return [Beam(x, y+1, 'v')]
                case '<':
                    return [Beam(x, y-1, '^')]
                case 'v':
                    return [Beam(x+1, y, '>')]
                case '^':
                    return [Beam(x-1, y, '<')]

        case '-':
            match dir:
                case '>':
                    return [Beam(x+1, y, '>')]
                case '<':
                    return [Beam(x-1, y, '<')]
                case 'v' | '^':
                    return [Beam(x+1, y, '>'), Beam(x-1, y, '<')]

        case '|':
            match dir:
                case '>' | '<':
                    return [Beam(x, y-1, '^'), Beam(x, y+1, 'v')]
                case 'v':
                    return [Beam(x, y+1, 'v')]
                case '^':
                    return [Beam(x, y-1, '^')]

lines = open("input").readlines()

mirror = []
for line in lines:
    mirror.append([*line.strip()])

light  = [['.'] * len(mirror[0]) for i in range(len(mirror))]

beams = [Beam(0, 0, '>')]
while len(beams) > 0:
    next_beams = []
    for beam in beams:
        next_beams += solve(mirror, light, beam)
    beams = next_beams

result = 0
for line in light:
    for c in line:
        if c != '.':
            result += 1
print(result)
