class Storage:
    my_list_of_equipment = []
    def __init__(self, storage_spaces):
        self.storage_spaces = storage_spaces

    def free_storage_spaces(self, spaces):
        return self.storage_spaces - spaces


class OfficeEquipment:
    def __init__(self, **kwargs):
        self.color = kwargs.get('color', None)
        self.works = kwargs.get('works', None)


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.duplex_printing = kwargs.get('duplex_printing', None)
        self.type = kwargs.get('type', None)



class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pixels_per_inch = kwargs.get('pixels_per_inch', None)


class Copier(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.duplex_printing = kwargs.get('duplex_printing', None)
        self.speed = kwargs.get('speed', None)


if __name__ == '__main__':
    a = Storage(20)
    printer = Printer(color='yes', works='yes', duplex_printing='yes', type='lazer')
    scanner = Scanner(color='yes', works='no', pixels_per_inch=450)
    copier = Copier(color='yes', works='yes', speed=60)

    print(a)
    for el in printer:
        print(el)