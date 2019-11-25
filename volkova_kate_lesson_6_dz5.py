class Stationery:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)

    def draw(self):
        print('Drawing started')


class Pen(Stationery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self):
        print('Drawing started by Pen')


class Pencil(Stationery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self):
        print('Drawing started by Pencil')


class Handle(Stationery):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self):
        print('Drawing started by Handle')


pen_1 = Pen(title = 'Pen')
pencil_1 = Pencil(title = 'Pencil')
handle_1 = Handle(title = 'Handle')

print(pen_1.draw())
print(pencil_1.draw())
print(handle_1.draw())