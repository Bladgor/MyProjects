# Задача 2. Фигуры
# При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты.
# Каждая из них имеет координаты XY, длину и ширину.
# Также каждая фигура может менять координаты (двигаться) и менять размер.
#
# Реализуйте такие классы.
# Учтите, что с точки зрения интерфейса прямоугольник и квадрат — это разные фигуры и работают они по-разному.
# В частности, по-разному работает метод изменения размера фигуры, так как у квадрата все стороны равны.

from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, x: int, y: int, length: int, width: int) -> None:
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Resize:
    def resizing(self, length: int, width: int) -> None:
        self.length = length
        self.width = width


class Square(Figure, Resize):
    """ Квадрат. Родительский класс: Figure """

    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__(x, y, size, size)


class Rectangle(Figure, Resize):
    """ Прямоугольник. Родительский класс: Figure """
    pass


rect_1 = Rectangle(x=2, y=4, length=2, width=4)
rect_2 = Rectangle(x=0, y=0, length=5, width=10)
square = Square(x=4, y=4, size=4)

for figure in [rect_1, rect_2, square]:
    new_length = figure.length * 2
    new_width = figure.width * 2
    figure.resizing(new_length, new_width)

print(square.x, square.y, square.length, square.width)
