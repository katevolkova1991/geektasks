def my_func (number1, number2, number3):
    n = [number1, number2, number3]
    n.sort()
    n.reverse()
    return n[0] + n[1]

def sum_numbers_with_args (*args):
    n = sorted(args)
    n.reverse()
    return sum(n[:2])

print(my_func(1, 3, 2))
print(sum_numbers_with_args(1, 3, 2, 5, 6))