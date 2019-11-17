#how to check the numbers
x = input("Введите действительное положительное число")
if x.isdigit():
    x = int(x)

y = input("Введите целое отрицательное число")
if y.isdigit():
    y = int(y)

def my_func(x, y):
    return abs (1 / (x * y))


print(my_func(2, -2))