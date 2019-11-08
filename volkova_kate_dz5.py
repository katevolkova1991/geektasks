incomes = int(input('Введите значение выручки: '))
outcomes = int(input('Введите значение расходов: '))

if (incomes - outcomes) > 0:
    print(f'Ваша компания работает в плюс: {incomes - outcomes}')
    print(f'Рентабельность выручки: {(incomes - outcomes) / incomes}')
    amount_of_workers = int(input('Число сотрудников: '))
    print(f'Прибыль на одного сотрудника: {(incomes - outcomes) / amount_of_workers}')
else:
    print(f'Ваша компания работает в убыток: {incomes - outcomes}')