a = int(input('Введите результат в километрах в первый день: '))
b = int(input('Введите общий результат в километрах: '))

result = 0

while a < b:
        a = a + a / 10
        result += 1

print (result)

