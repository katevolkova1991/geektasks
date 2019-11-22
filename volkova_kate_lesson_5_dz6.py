with open('dz_6.txt', 'a') as text:
    text.write('6 7 8 2 3 1 4')

with open('dz_6.txt', 'r') as text:
    for line in text:
        content = line.split()
    for i, el in enumerate(content):
        content[i] = int(el)
    print(sum(content))