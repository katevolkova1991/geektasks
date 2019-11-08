n = 834
i = len(str(n))+1
result = 0

while i != 0:
    cifra_1 = n % 10
    if cifra_1 > result:
        result = cifra_1
    n = n // 10
    i -= 1


print(result)