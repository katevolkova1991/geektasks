from functools import reduce

my_list = [el for el in range(100, 1001) if not el % 2]
print(my_list)

def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, my_list))