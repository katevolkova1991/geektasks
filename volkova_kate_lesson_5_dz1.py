with open('text.txt', 'a') as text:
    while True:
        user_data = input('введите данные: ')
        if user_data != '':
            text.write(f'{user_data}\n')
        else:
            break

