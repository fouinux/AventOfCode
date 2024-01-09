def ac_hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h = (h * 17) % 256
    return h

line = open("input").readlines()[0]

boxes = dict()
for sub in line.strip().split(','):
    if '-' in sub:
        label = sub.split('-')[0]
        h = ac_hash(label)
        if h in boxes.keys():
            if any(x[0] == label for x in boxes[h]):
                for box in boxes[h]:
                    if box[0] == label:
                        boxes[h].remove(box)
                        if len(boxes[h]) == 0:
                          boxes.pop(h)
    else: #  =
        label, num = sub.split('=')
        h = ac_hash(label)
        if h not in boxes.keys():
            boxes[h] = list()
        if any(x[0] == label for x in boxes[h]):
            for box in boxes[h]:
                if box[0] == label:
                    box[1] = int(num)
        else:
            boxes[h].append([label, int(num)])

print(boxes)

result = 0
for key in boxes.keys():
    for i in range(len(boxes[key])):
        result += (key+1) * (i+1) * boxes[key][i][1]

print(result)

