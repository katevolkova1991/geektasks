class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    my_list = []
    my_flag = 'д'
    while my_flag == 'д':
        user_data = input('введите число ')
        try:
            if user_data.isdigit():
                user_data = int(user_data)
            else:
                raise MyOwnError('Не верный тип данных')
        except MyOwnError as err:
            print(err)
        else:
            my_list.append(user_data)

        my_flag = input('Вы хотите продолжить? д/н: ')
    print(my_list)
