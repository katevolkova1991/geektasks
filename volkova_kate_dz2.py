time_in_sec = int(input('Введите время в секундах: '))

print(f'{time_in_sec // (60 * 60)}:{time_in_sec // 60}:{time_in_sec % 60}')