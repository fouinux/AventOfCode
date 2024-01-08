def exec_round(array):
     # Transpose
    array = list(map(list, zip(*array)))

    # North
    for i in range(len(array)):
        line = ''.join(array[i])
        while True:
            line_r = line.replace('.O', 'O.')
            if line == line_r:
                break
            line = line_r
        array[i] = [*line]

    # Transpose
    array = list(map(list, zip(*array)))

    # West
    for i in range(len(array)):
        line = ''.join(array[i])
        while True:
            line_r = line.replace('.O', 'O.')
            if line == line_r:
                break
            line = line_r
        array[i] = [*line]

    # Transpose
    array = list(map(list, zip(*array)))

    # South
    for i in range(len(array)):
        line = ''.join(array[i])
        while True:
            line_r = line.replace('O.', '.O')
            if line == line_r:
                break
            line = line_r
        array[i] = [*line]

    # Transpose
    array = list(map(list, zip(*array)))

    # East
    for i in range(len(array)):
        line = ''.join(array[i])
        while True:
            line_r = line.replace('O.', '.O')
            if line == line_r:
                break
            line = line_r
        array[i] = [*line]

    return array

def load(array):
    result = 0
    for i in range(len(array)):
        result += (len(array) - i) * array[i].count('O')
    return result

def my_hash(array):
    s = ''
    for l in array:
        s += ''.join(l)
    return hash(s)

RANGE_MAX = 1000000000

lines = open("input").readlines()
array = []
for line in lines:
    line = line.strip()
    array.append([*line])

cache = {}
h = my_hash(array)
l = load(array)
for i in range(RANGE_MAX):
    if h not in cache.keys():
        array = exec_round(array)
        h_next = my_hash(array)
        # Store in cache
        cache[h] = (l, h_next, i)
        l = load(array)
        h = h_next
    else:
        # Found in cache
        l, h, index = cache[h]
        loop_size = i - index
        loop_nb = int((RANGE_MAX - i) / loop_size)
        # Unroll the last round of cache loop
        for j in range(i+loop_nb*loop_size, RANGE_MAX):
            l, h, index = cache[h]
        print(l)
        exit(0)

print(l)
