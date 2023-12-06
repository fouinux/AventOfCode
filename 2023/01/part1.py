LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REPLACE = '                          '

lines = open('input').readlines()
translation = str.maketrans(LETTERS, REPLACE)
result = 0
for l in lines:
    nb_str = l.translate(translation).replace(' ', '').rstrip()
    result += int(nb_str[0]) * 10 + int(nb_str[-1])

print(result)
