class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def amount(self, width_of_road):
        mass_of_material = 25
        return self._length * self._width * mass_of_material * width_of_road

road_1 = Road(20, 5000)
print(road_1.amount(5))