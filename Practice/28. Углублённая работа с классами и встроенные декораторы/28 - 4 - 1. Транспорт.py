# Задача 1. Транспорт
# У нас есть парк транспорта.
# У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:
#
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы.
# Класс «Транспорт» должен быть абстрактным и содержать абстрактные методы.
#
# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки.
# «Замешайте» этот класс в «Амфибию»

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def __init__(self, color, speed=0):
        self.__color = color
        self.__speed = speed

    def move(self, speed):
        self.__speed = speed
        print(f'Транспорт двигается со скоростью {self.__speed}')

    def give_a_signal(self):
        print('Громкий гудок!')


class Land:
    def __init__(self):
        self.movement_surface = 'land'


class Water:
    def __init__(self):
        self.movement_surface = 'water'


class Car(Transport, Land):
    def __init__(self, color):
        super().__init__(color)


class Boat(Transport, Water):
    def __init__(self, color):
        super().__init__(color)


class Amphibian(Transport, Water, Land):
    def __init__(self, color):
        super().__init__(color)


amphibian = Amphibian('white')
print(amphibian.movement_surface)
