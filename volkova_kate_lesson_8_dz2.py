class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

user_data = input('первое число: ')
user_data_1 = input('второе число: ')
try:
    user_data = int(user_data)
    user_data_1 = int(user_data_1)
    if user_data_1 == 0:
        raise MyOwnError("Вы ввели 0. На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число")
except MyOwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {user_data / user_data_1}")