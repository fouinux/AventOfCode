lines = open("input").readlines()

dir_convert = ['R', 'D', 'L', 'U']

coords = []
perimeter = 0
x, y = 0, 0
for l in lines:
    color = l.strip().split(' ')[2]
    num = int(color[2:7], 16)
    dir = dir_convert[int(color[7])]
    match dir:
        case 'R':
            x += num
        case 'L':
            x -= num
        case 'U':
            y += num
        case 'D':
            y -= num
        case _:
            print(f"Unknown direction : {l}")

    # Save coordinates
    coords.append({'x': x, 'y': y})
    perimeter += num

area = 0
for i in range(len(coords)):
    area += (coords[i-1]['x'] * coords[i]['y']) - (coords[i]['x'] * coords[i-1]['y'])

print((abs(area) + perimeter) / 2 + 1)
