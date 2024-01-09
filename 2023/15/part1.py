def ac_hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h = (h * 17) % 256
    return h

line = open("input").readlines()[0]

result = 0
for sub in line.strip().split(','):
    result += ac_hash(sub)

print(result)