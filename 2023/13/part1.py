class Pattern():
    def __init__(self, lines):
        self.data = []
        for line in lines:
            self.data.append([*line.strip()])

    def __repr__(self):
        s = ''
        for l in self.data:
            for c in l:
                s += c
            s += '\n'
        return s

    def rows(self):
        return self.data

    def columns(self):
        return list(map(list, zip(*self.data)))

def find_reflection(l):
    for i in range(len(l)-1):
        if (l[i] == l[i+1]):
            found = True
            # Possible reflection
            rg = min(i+1, len(l) - i - 1)
            for j in range(1, rg):
                if l[i-j] != l[i+1+j]:
                    found = False
                    break
            if found:
                return i+1

    return None

lines = open("input").readlines()
patterns = []
group = []
for line in lines:
    line = line.strip()
    if len(line):
        group.append(line)
    else:
        patterns.append(Pattern(group))
        group = []
patterns.append(Pattern(group))

result = 0
for p in patterns:
    # Search vertical reflection
    reflection = find_reflection(p.columns())
    if reflection:
        result += reflection
        continue

    # Search horizontal reflection
    reflection = find_reflection(p.rows())
    if reflection:
        result += reflection * 100

print(result)