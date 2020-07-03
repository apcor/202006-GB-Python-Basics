'''Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        dir_dict = {'left': 'налево', 'right': 'направо'}
        print(f'{self.name} повернула {dir_dict[direction]}')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed} км/ч')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed} км/ч')
        if self.speed > 60:
            print(f'{self.name} превышает лимит в 60 км/ч!')


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed} км/ч')
        if self.speed > 40:
            print(f'{self.name} превышает лимит в 40 км/ч!')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


first = Car(120, 'red', 'Девятка')
first.go()
first.turn("left")
first.turn("right")
first.show_speed()
first.stop()

second = TownCar(120, 'black', 'Развалюха')
second.show_speed()
print(second.is_police)

third = WorkCar(42, 'yellow', 'грузовик')
third.show_speed()
