class Cells:
    def __init__(self, amount):
        self._amount = amount
        #self._amount = kwargs.get('amount', None)

    def __add__(self, other):
        return Cells(self._amount + other._amount)

    def __sub__(self, other):
        a = self._amount - other._amount
        if a >= 0:
            return Cells(a)
        else: return f'sub is less than 0'

    def __mul__(self, other):
        return Cells(self._amount * other._amount)

    def __truediv__(self, other):
        return Cells(self._amount / other._amount)

    def make_order(self, cells_in_row):
        c = "*" * cells_in_row
        return (f'{c}\n')


cell_1 = Cells(12)
cell_2 = Cells(10)

cell_3 = cell_1 + cell_2
print(cell_3._amount)

cell_3 = cell_1 - cell_2
print(cell_3._amount)

cell_3 = cell_1 * cell_2
print(cell_3._amount)

cell_3 = cell_1 / cell_2
print(cell_3._amount)

print(cell_1.make_order(5))