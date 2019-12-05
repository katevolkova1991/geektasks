class Data:

    def __init__(self, dmy):
        self.dmy = dmy.split('-')


    @classmethod
    def dmy_turn_to_number(cls, day_month_year):
        my_list = day_month_year.split('-')
        for el in my_list:
            el = int(el)
        return my_list

    @staticmethod
    def check_date(dmy):
        dmy = dmy.split('-')
        check = []
        if int(dmy[0]) in range(1, 32):
            check.append('День введен верно')
        else:
            check.append('День введен неверно')

        if int(dmy[1]) in range(1, 13):
            check.append('Месяц введен верно')
        else:
            check.append('Месяц введен неверно')

        if int(dmy[2]) in range(1, 2020):
            check.append('Год введен верно')
        else:
            check.append('Год введен неверно')

        return(check)



a = Data('12-12-2012')

print(Data.dmy_turn_to_number('13-12-2013'))
print(a.dmy)
print(a.check_date('12-12-2012'))
