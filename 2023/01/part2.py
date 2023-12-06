LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REPLACE = '                          '

def spelled2number(line):
    line = line.replace('one', 'o1e')
    line = line.replace('two', 't2o')
    line = line.replace('three', 't3e')
    line = line.replace('four', 'f4r')
    line = line.replace('five', 'f5e')
    line = line.replace('six', 's6x')
    line = line.replace('seven', 's7n')
    line = line.replace('eight', 'e8t')
    line = line.replace('nine', 'n9e')
    return line

lines = open('input').readlines()
translation = str.maketrans(LETTERS, REPLACE)
cal = 0
for l in lines:
    l = spelled2number(l)
    nb_str = l.translate(translation).replace(' ', '').rstrip()
    cal += int(nb_str[0] + nb_str[-1])

print(cal)