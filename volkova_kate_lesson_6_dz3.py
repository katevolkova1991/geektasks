class Worker:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.surname = kwargs.get('surname', None)
        self.position = kwargs.get('position', None)
        self.income = {'wage': kwargs.get('wage', None), 'bonus': kwargs.get('bonus', None)}


class Position(Worker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_full_name(self):
        return(f'{self.name} {self.surname}')

    def get_total_income(self):
        return(int(self.income['wage']) + int(self.income['bonus']))


worker_1 = Position(name = 'Kate', surname = 'Volkova', position = 'teacher',
                    wage = '10', bonus = 5)

print(worker_1.get_full_name())
print(worker_1.get_total_income())
