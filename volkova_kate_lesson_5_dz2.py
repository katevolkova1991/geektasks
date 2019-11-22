with open('dz_2.txt', 'r') as text:
    counting_strings = 0
    amount_of_words = {}
    for line in text:
        content = line.split()
        counting_strings += 1
        amount_of_words[counting_strings] = len(content)

print(amount_of_words)
print(counting_strings)
