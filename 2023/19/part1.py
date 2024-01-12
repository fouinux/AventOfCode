lines = open("input").readlines()
workflow_part = True
workflows = {}
ratings = []
for l in lines:
    l = l.strip()
    if len(l) == 0:
        workflow_part = False
        continue

    if workflow_part:
        name, *rules = l[:-1].replace('{', ',').split(',')
        workflows[name] = rules
    else:
        ratings.append(l)

result = 0
x, m, a, s = 0, 0, 0, 0
for rating in ratings:
    for e in rating[1:-1].split(','):
        exec(e)

    name = 'in'
    while True:
        rules = workflows[name]
        for r in rules:
            if ':' in r:
                test, dest = r.split(':')
                if eval(test):
                    name = dest
                    break
            else:
                name = r

        if name == 'A':
            result += x + m + a + s
            break
        elif name == 'R':
            break

print(result)
