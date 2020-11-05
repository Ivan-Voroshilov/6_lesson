
class Car:
    speed = None
    colour = None
    name = None
    is_police = None

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'GO'

    def stop(self):
        return 'STOP'

    def turn_left(self):
        return 'TURN LEFT'

    def turn_right(self):
        return 'TURN RIGHT'

    def show_speed(self):
        return self.speed


class TownCar(Car):

    speed = 60
    colour = 'Yellow'
    name = 'Toyota'
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            return 'High speed warning!'
        return self.speed


class SportCar(Car):

    speed = 90
    colour = 'White'
    name = 'Ferrari'
    is_police = False


class WorkCar(Car):

    speed = 40
    colour = 'Red'
    name = 'Cat'
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            return 'High speed warning!'
        return self.speed


class PoliceCar(Car):

    speed = 70
    colour = 'Black'
    name = 'Ford'
    is_police = True


car = Car(100, 'Black', 'Tesla', False)
print(car.show_speed())
print(car.go())
print(car.turn_left())

police_car = PoliceCar(PoliceCar.speed, PoliceCar.colour, PoliceCar.name, PoliceCar.is_police)
print(police_car.show_speed())
print(police_car.go())
print(police_car.is_police)

town_car = TownCar(TownCar.speed, 'Yellow', 'Lexus', False)
print(town_car.show_speed())

work_car = WorkCar(42, 'green', WorkCar.name, WorkCar.is_police)
print(work_car.name)
print(work_car.show_speed())
