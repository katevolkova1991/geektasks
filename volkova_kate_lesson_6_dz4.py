class Car:
    def __init__(self, **kwargs):
        self._speed = kwargs.get('speed', None)
        self._color = kwargs.get('color', None)
        self._name = kwargs.get('name', None)
        self.__is_police = kwargs.get('is_police', None)

    def go_forward(self):
        return f'the car goes forward'

    def stop_moving(self):
        return f'the car stopped'

    def turning(self, direction):
        if direction == 'right':
            return f'the car turns to the right'
        elif direction == 'left':
            return f'the car turns to the left'
        else:
            return f'direction is not recognized'

    def show_speed(self):
        return self._speed


class TownCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_speed(self):
        if self._speed > 60:
            return f'Your speed is above the limit'
        else:
            return self._speed


class SportCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WorkCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_speed(self):
        if self._speed > 40:
            return f'Your speed is above the limit'
        else:
            return self._speed


class PoliceCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


town_car_1 = TownCar(speed = 60, color = 'red', name = 'NK12058', is_police = False)
sport_car_1 = SportCar(speed = 90, color = 'blue', name = 'AR21068', is_police = False)
work_car_1 = WorkCar(speed = 60, color = 'white', name = 'FH34086', is_police = False)
police_car_1 = PoliceCar(speed = 120, color = 'black', name = 'NK1000', is_police = True)

work_car_1.__is_police = True
print(work_car_1.__is_police)

town_car_1._color = 'yellow'
print(town_car_1._color)

print(town_car_1.go_forward())
print(sport_car_1.stop_moving())
print(work_car_1.turning('left'))
print(police_car_1.turning('right'))

print(town_car_1.show_speed())
print(work_car_1.show_speed())
print(sport_car_1.show_speed())
print(police_car_1.show_speed())