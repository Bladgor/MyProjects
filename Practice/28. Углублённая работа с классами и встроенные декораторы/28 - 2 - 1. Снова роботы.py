# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов.
# И в этот раз не абы каких, а летающих: разведывательного дрона и военного робота.
#
# Разведывательный дрон просто летает в поиске противника.
# При команде operate он выводит сообщение «Веду разведку с воздуха» и передвигается немного вперёд.
#
# У летающего военного робота есть оружие,
# и при команде operate он выводит сообщение о защите военного объекта с воздуха с помощью этого оружия.
#
# Напишите программу, которая реализует все необходимые классы роботов.
# Сущности «Робот» и «Может летать» должны быть вынесены в отдельные классы.
# Обычный робот имеет модель и может вывести сообщение «Я — Робот».
# Объект, который умеет летать, дополнительно имеет атрибуты «Высота» и «Скорость»,
# а также может взлетать, летать и приземляться.

from abc import ABC, abstractmethod
from math import sin, cos, radians


class Robot(ABC):
    @abstractmethod
    def __init__(self, model: str) -> None:
        self.model = model
        self.total_distance = 0

    def __str__(self) -> str:
        return 'Я - Робот'


class CanFly(ABC):
    @abstractmethod
    def __init__(self, model: str) -> None:
        super().__init__(model)
        self.height = 0
        self.speed = 0

    def fly_up(self) -> None:
        if self.height == 0:
            self.height += 10
            print(f'Взлетел.\n'
                  f'Текущая высота: {self.height}')
        else:
            print('Робот уже в воздухе.')

    def fly(self, speed: int) -> None:
        if self.height != 0:
            self.speed += speed
            print(f'Увеличил скорость на {speed}\n'
                  f'Текущая скорость: {self.speed}')
        else:
            print('Робот ещё не взлетел.')

    def gain_height(self, height: int) -> None:
        if self.height != 0:
            self.height += height
            print(f'Робот увеличил высоту на {height}\n'
                  f'Текущая высота: {self.height}')

    def land(self) -> None:
        if self.height != 0:
            self.height = 0
            self.speed = 0
            print('Робот приземлился.')
        else:
            print('Робот и так на земле.')


class ReconnaissanceDrone(CanFly, Robot):
    def __init__(self, model: str) -> None:
        super().__init__(model)
        self.x = 0
        self.y = 0
        self.a = 0

    def operate(self) -> None:
        if self.height != 0:
            print('Веду разведку с воздуха')
            time = int(input('Сколько часов вести разведку? '))
            if self.speed != 0:
                self.move(time)
            else:
                print('Разведка проводится со стационарной точки')

    def move(self, time: int = 1) -> None:
        distance = self.speed * time
        self.total_distance += distance
        self.x = self.x + distance * cos(radians(self.a))
        self.y = self.y + distance * sin(radians(self.a))
        print(f'Продвинулся на {distance} км')

    def turning(self, a: int) -> None:
        self.a += a
        print(f'Новое направление: {self.a}')


class MilitaryRobot(CanFly, Robot):
    def __init__(self, model: str, gun: str) -> None:
        super().__init__(model)
        self.gun = gun

    def operate(self) -> None:
        print(f'Защищаю объект с помощью оружия: {self.gun}')


scout = ReconnaissanceDrone('R_Zond-1')
guardian = MilitaryRobot('R_Warior-1', 'Plazmer')
print(scout)
print(scout.height)
scout.fly_up()
scout.fly(50)
scout.operate()
print(scout.__class__.__mro__)
guardian.operate()
print(scout.model)
