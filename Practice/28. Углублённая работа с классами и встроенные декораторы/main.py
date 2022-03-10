# ## Задача 3. Моделирование
# В проекте по 3D моделированию используются две фигуры - Куб и Пирамида.
# Для моделирования этих фигур используются соответствующие 2D фигуры, а именно Квадрат и Треугольник.
# Вся поверхность 3D фигуры может храниться в виде списка,
# например для Куба это будет [Square, Square, Square, Square, Square, Square]
#
# ![task_03_pic](models.png)
#
# Квадрат инициализируется длинами сторон, а треугольник - основанием и высотой.
# Каждая из 2D фигур умеет находить свои периметр и площадь,
# а 3D фигуры, в свою очередь, могут находить площадь своей поверхности.
#
# Используя входные данные о фигурах и знания математики, реализуйте соответствующие классы и методы.
#
# Для базовых классов также реализуйте геттеры и сеттеры.

from typing import Union


class Square:
    def __init__(self, side: Union[int, float]):
        self._side = side

    @property
    def side(self) -> Union[int, float]:
        return self._side

    @side.setter
    def side(self, side: int) -> None:
        if side > 0:
            self._side = side
        else:
            raise ValueError('Недопустимая длина стороны')

    def perimeter(self) -> Union[int, float]:
        return 4 * self._side

    def area(self) -> Union[int, float]:
        return self._side ** 2


class Triangle:
    def __init__(self, base: int, height: int) -> None:
        self._base = base
        self._height = height
        self.hip = ((self._base / 2) ** 2 + self._height ** 2) ** 0.5

    @property
    def base(self) -> Union[int, float]:
        return self._base

    @base.setter
    def base(self, base: int) -> None:
        if base > 0:
            self._base = base
        else:
            raise ValueError('Недопустимое значение основания')

    @property
    def height(self) -> Union[int, float]:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        if height > 0:
            self._base = height
        else:
            raise ValueError('Недопустимое значение высоты')

    def perimeter(self) -> Union[int, float]:
        return self._base + self.hip * 2

    def area(self) -> Union[int, float]:
        return (self._base * self._height) / 2


class Cube(Square):
    def __init__(self, side: Union[int, float]) -> None:
        super().__init__(side)

    def area(self) -> Union[int, float]:
        return self.side ** 2 * 6


class Pyramid(Triangle):
    def __init__(self, base: int, height: int) -> None:
        super().__init__(base, height)

    def area(self) -> Union[int, float]:
        return self.base ** 2 + (self._base * self._height) * 2


square = Square(side=2)
print(square.area())

triangle = Triangle(3, 3)
print(triangle.area())

cube = Cube(side=2)
print(cube.area())

pyramid = Pyramid(base=3, height=3)
print(pyramid.area())
