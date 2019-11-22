with open('dz_3.txt', 'r') as text:
    summary = 0
    i = 0
    for line in text:
        content = line.split()
        if int(content[1]) < 20000:
            print(line)
        summary += int(content[1])
        i += 1
    print(summary / i)