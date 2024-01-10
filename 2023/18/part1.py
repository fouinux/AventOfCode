lines = open("input").readlines()

h_min, h_max = 0, 0
w_min, w_max = 0, 0

x, y = 0, 0
for l in lines:
    dir, num, color = l.strip().split(' ')
    match dir:
        case 'R':
            x += int(num)
        case 'L':
            x -= int(num)
        case 'U':
            y -= int(num)
        case 'D':
            y += int(num)
        case _:
            print(f"Unknown direction : {l}")
    h_min = min(h_min, y)
    h_max = max(h_max, y)
    w_min = min(w_min, x)
    w_max = max(w_max, x)

# Map size
height = h_max - h_min + 1
width = w_max - w_min + 1

# Correct x, y start
x = -w_min
y = -h_min

map = [['.'] * width for _ in range(height)]

# Draw map
for l in lines:
    dir, num, color = l.strip().split(' ')
    dx, dy = 0, 0
    match dir:
        case 'R':
            dx = 1
        case 'L':
            dx = -1
        case 'U':
            dy = -1
        case 'D':
            dy = 1
        case _:
            print(f"Unknown direction : {l}")

    for _ in range(int(num)):
        map[y][x] = '#'
        x += dx
        y += dy

# Fill map from the center
fill_list = [{'x': int(width/2), 'y': int(height/2)}]
while len(fill_list) > 0:
    fill_next = []
    for fill in fill_list:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if map[fill['y']+dy][fill['x']+dx] == '.':
                    map[fill['y']+dy][fill['x']+dx] = '#'
                    fill_next.append({'x': fill['x']+dx, 'y': fill['y']+dy})
    fill_list = fill_next

result = 0
for l in map:
    for c in l:
        if c == '#':
            result += 1
        print(c, end='')
    print()
print(result)