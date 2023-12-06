class CharArray():
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0].rstrip())
        self.array =  [['.'] * self.width] * self.height
        self.array = list()
        for y in range(self.height):
            self.array.append([*lines[y].rstrip()])

    def get(self, x, y):
        if x not in range(self.width):
            return '.'
        if y not in range(self.height):
            return '.'
        return self.array[y][x]

lines = open('input').readlines()
sum = 0

array = CharArray(lines)

number = ''
for h in range(array.height):
    for w in range(array.width+1):
        char = array.get(w, h)
        if char in '0123456789':
            number += char
        elif number != '': # End of a number
            # Search for surrounding symbol
            symbol = False
            for y in range(h-1, h+2):
                for x in range(w-len(number)-1, w+1):
                    if array.get(x, y) not in '.0123456789':
                        symbol = True
            if symbol:
                sum += int(number)
            number = ''
print(sum)
