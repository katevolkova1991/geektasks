#how to use enter and others
numbers = input('Введите числа через пробел: ').split()

def summary(numbers):
    result = 0
    for el in numbers:
        result = result + int(el)
    return result

print(numbers)
print(summary(numbers))