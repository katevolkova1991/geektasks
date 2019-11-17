#how to delete all the gaps
# how to union the strings right
def int_func(text):
    text = text.lower()
    first_letter = text[0]
    first_letter = first_letter.upper()
    first_letter = first_letter + text[1:]
    return first_letter

text = input('Введите строку: ').split()
result = ''
for el in text:
    result = result + ' ' + int_func(el)

print(result)
