# Задача 1. Транспорт 2
# Используя код задачи про автомобили, лодки и амфибии,
# дополните абстрактный класс геттерами и сеттерами для соответствующих атрибутов.
# Используйте встроенные декораторы. Вот входные данные той задачи:
#
# У нас есть парк транспорта.
# У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
#
# В парке транспорта стоят:
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def __init__(self, color: str, speed: int = 0) -> None:
        self._color = color
        self._speed = speed

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        if isinstance(color, str):
            self._color = color
        else:
            print('Недопустимое значение цвета.')

    @property
    def move(self) -> str:
        if self._speed != 0:
            return f'Транспорт движется со скоростью: {self._speed}'

    @move.setter
    def move(self, speed: int) -> None:
        self._speed = speed
        print(f'Транспорт установил скорость: {self._speed}')

    @classmethod
    def give_a_signal(cls) -> None:
        print('Громкий гудок!')


class Car(Transport):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.movement_surface = 'land'


class Boat(Transport):
    def __init__(self, color: str) -> None:
        super().__init__(color)
        self.movement_surface = 'water'


class Music:
    def __init__(self):
        self.music = False

    def play_music(self) -> None:
        self.music = True
        print('Музыка включена')


class Amphibian(Transport, Music):
    def __init__(self, color: str, speed: int = 0):
        super().__init__(color, speed)
        self.movement_surface = 'land and water'


amphibian = Amphibian('white')
print(amphibian.movement_surface)
print(amphibian.__class__.__mro__)
amphibian.play_music()
print(amphibian.music)

print(amphibian.color)
print(amphibian.move)
amphibian.move = 10
print(amphibian.move)

