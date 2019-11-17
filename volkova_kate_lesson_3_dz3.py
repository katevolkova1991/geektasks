def my_func (number1, number2, number3):
    n = [number1, number2, number3]
    n.sort()
    n.reverse()
    return n[0] + n[1]

def sum_numbers_with_args (*args):
    sum = 0
    for el in args:
        sum = sum+el
    return sum

print(my_func(1, 3, 2))
print(sum_numbers_with_args(1, 3, 2, 5, 6))