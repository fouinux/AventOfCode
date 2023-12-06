import sys

class CharArray():
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0].rstrip())
        self.array =  [['.'] * self.width] * self.height
        self.array = list()
        for y in range(self.height):
            self.array.append([*lines[y].rstrip()])

        #print(self.array)

    def get(self, x, y):
        if x not in range(self.width):
            return '.'
        if y not in range(self.height):
            return '.'
        return self.array[y][x]

def main() -> int:
    lines = open('input').readlines()

    array = CharArray(lines)
    gearDict = dict()

    number = ''
    for h in range(array.height):
        for w in range(array.width+1):
            char = array.get(w, h)
            if char in '0123456789':
                number += char
            elif number != '': # End of a number
                # Search for surrounding symbol '*'
                for y in range(h-1, h+2):
                    for x in range(w-len(number)-1, w+1):
                        if array.get(x, y) == '*':
                            if (x, y) not in gearDict.keys():
                                gearDict[(x, y)] = list()
                            gearDict[(x, y)].append(int(number))
                number = ''
    sum = 0
    for gear in gearDict.keys():
        if len(gearDict[gear]) == 2:
            sum += gearDict[gear][0] * gearDict[gear][1]

    print(sum)
    return 0

if __name__ == "__main__":
    sys.exit(main())