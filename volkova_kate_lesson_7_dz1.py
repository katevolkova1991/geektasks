class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
       return str(self.param)


class Matrix:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))

    def __str__(self):
        for el in self.my_list:
                return f'{el} '

   # def __add__(self, other):
    #    return Matrix()

    def __getitem__(self, index):
        return self.my_list[index]


my_obj = Matrix([31, 22], [37, 43], [51, 86])

for el in my_obj:
    print(el)




