lines = open("input").readlines()
array = []
for line in lines:
    line = line.strip()
    array.append([*line])

# Transpose
array_t = list(map(list, zip(*array)))
for i in range(len(array_t)):
    line = ''.join(array_t[i])
    while True:
        line_r = line.replace('.O', 'O.')
        if line == line_r:
            break
        line = line_r
    print(line)
    array_t[i] = [*line]

array = list(map(list, zip(*array_t)))

result = 0
for i in range(len(array)):
    result += (len(array) - i) * array[i].count('O')

print(result)