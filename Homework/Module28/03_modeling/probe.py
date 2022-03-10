from typing import Union


class Figure:
    def __init__(self, **kwargs):
        self._side = kwargs.get('side')
        self._height = kwargs.get('height')
        self._base = kwargs.get('base')
        if self._height:
            self.hip = ((self._base / 2) ** 2 + self._height ** 2) ** 0.5

    def figure_perimeter(self):
        raise NotImplemented('Не надо тебе этого, Барин')

    def figure_square(self):
        raise NotImplemented('Не надо тебе этого, Барин')

    @property
    def side(self) -> Union[int, float]:
        return self._side

    @side.setter
    def side(self, side: int) -> None:
        if side > 0:
            self._side = side
        else:
            raise ValueError('Недопустимая длина стороны')

    @property
    def height(self) -> Union[int, float]:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        if height > 0:
            self._base = height
        else:
            raise ValueError('Недопустимое значение высоты')

    @property
    def base(self) -> Union[int, float]:
        return self._base

    @base.setter
    def base(self, base: int) -> None:
        if base > 0:
            self._base = base
        else:
            raise ValueError('Недопустимое значение основания')


class Square(Figure):
    def figure_perimeter(self):
        return 4 * self._side

    def figure_square(self):
        return self._side ** 2


class Triangle(Figure):
    def figure_perimeter(self):
        return self._base + self.hip * 2

    def figure_square(self):
        return (self._base * self._height) / 2


class Mixin:
    def faces_square(self):
        total = 0
        for elem in self.side_list:
            total += elem.figure_square()
        return total


class Pyramid(Square, Triangle, Mixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.side_list = [Square(), Triangle(), Triangle(), Triangle(), Triangle()]


class Cube(Square, Mixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.side_list = [Square(), Square(), Square(), Square(), Square(), Square()]


cube = Cube(side=2)
print(cube.faces_square())
print(cube.side)

# pyramid = Pyramid(base=2, height=2)
# print(pyramid.side_list[0].base)
