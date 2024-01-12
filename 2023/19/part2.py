class ac_range():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def count(self):
        return self.stop - self.start

    def __repr__(self):
        return f"{self.__class__.__name__}({self.start}, {self.stop})"

    def __contains__(self, item):
        if item >= self.start and item <= self.stop:
            return True
        return False

class Soluce():
    def __init__(self, name, **kwargs):
        self.name = name
        self.dict = kwargs

    def copy(self):
        cpy = Soluce(self.name)
        for k, v in self.dict.items():
            cpy.dict[k] = ac_range(v.start, v.stop)
        return cpy

    def result(self):
        result = 1
        for v in self.dict.values():
            result *= v.count()
        return result

    def __repr__(self):
        s = f"{self.__class__.__name__}('{self.name}'"
        for k, v in self.dict.items():
            s += f", '{k}':{v}"
        return s + ")"

lines = open("input").readlines()

workflows = {}
for l in lines:
    l = l.strip()
    if len(l) == 0:
        break

    name, *rules = l[:-1].replace('{', ',').split(',')
    workflows[name] = rules

soluces = [Soluce('in', x=ac_range(0, 4000), m=ac_range(0, 4000), a=ac_range(0, 4000), s=ac_range(0, 4000))]
# print(soluces)

while any(s.name != 'A' for s in soluces):
    nxt_soluces = []
    for s in soluces:
        if s.name != 'A':
            rules = workflows[s.name]
            for r in rules:
                if ':' in r:
                    test, dest = r.split(':')
                    ltr, op, num = test[0], test[1], int(test[2:])
                    if ltr in s.dict.keys() and num in s.dict[ltr]:
                        # Create a copy of soluce
                        s_ok = s.copy()
                        if op == '>':
                            s_ok.dict[ltr].start = num + 1
                            s.dict[ltr].stop = num
                        else:
                            s_ok.dict[ltr].stop = num - 1
                            s.dict[ltr].start = num
                        s_ok.name = dest
                        if s_ok.name != 'R':
                            nxt_soluces.append(s_ok)
                else: # Dest
                    s.name = r
                    if s.name == 'R':
                        soluces.remove(s)
    soluces += nxt_soluces
    print(soluces)

print(soluces)

result = 0
for s in soluces:
    result += s.result()

print(result)