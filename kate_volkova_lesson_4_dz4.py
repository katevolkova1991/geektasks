my_list = [10, 20, 13, 14, 15, 20, 10, 35, 13]
my_set = set(my_list)
new_list = []

for el in my_list:
    if el in my_set:
        new_list.append(el)
        my_set.remove(el)

result = [my_list[i] for i in range(0, len(my_list)) if my_list[i] not in my_list[:i]]


print(result)