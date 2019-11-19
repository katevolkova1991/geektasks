import random


my_list = [random.randint(1, 20) for el in range(10)]
print(my_list)

result = []
for key, el in enumerate(my_list):
    if key == 0:
        result.append(el)
    else:
        if my_list[key-1] < my_list[key]:
            result.append(el)
print(result)