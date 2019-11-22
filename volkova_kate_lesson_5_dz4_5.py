numbers = {
    "One": 'один',
    "Two": 'два',
    "Three": 'три',
    "Four": 'четыре',
    'Five': 'пять',
    'Six': 'шесть'
}

with open('dz_4.txt', 'r') as text:
    for line in text:
        content = line.split()
        number = numbers.get(content[0])
        print(f'{number} {content[1]} {content[2]}')