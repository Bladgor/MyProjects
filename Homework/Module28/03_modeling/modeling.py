from typing import Union, Any


class Figure:

    def __init__(self, **kwargs) -> None:
        self._height = kwargs.get('height')
        self._base = kwargs.get('base')

    @property
    def height(self) -> Any:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    @property
    def base(self) -> Any:
        return self._base

    @base.setter
    def base(self, base: int) -> None:
        self._base = base

    def figure_perimeter(self):
        raise NotImplemented('Не надо тебе этого, Барин')

    def figure_square(self):
        raise NotImplemented('Не надо тебе этого, Барин')


class Square(Figure):

    def figure_perimeter(self) -> Union[int, float]:
        return self._base * 4

    def figure_square(self) -> Union[int, float]:
        return self._base ** 2


class Triangle(Figure):

    def figure_perimeter(self) -> Union[int, float]:
        return ((self._height ** 2 + (self._base / 2) ** 2) ** 0.5) * 2 + self._base

    def figure_square(self) -> Union[int, float]:
        return (self._height * self._base) / 2


class Mixin:

    def faces_square(self) -> Union[int, float]:
        total = 0
        for elem in self.blanks:
            total += elem.figure_square()
        return total


class Cube(Square, Mixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blanks = [Square(base=self.base), Square(base=self.base), Square(base=self.base),
                       Square(base=self.base), Square(base=self.base), Square(base=self.base)]


class Pyramid(Triangle, Square, Mixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blanks = [Triangle(height=self.height, base=self.base), Triangle(height=self.height, base=self.base),
                       Triangle(height=self.height, base=self.base), Triangle(height=self.height, base=self.base),
                       Square(base=self.base)]


cube = Cube(base=2)
print(cube.faces_square())
print(cube.figure_square())
print(cube.height)
print()
pyramid = Pyramid(height=2, base=2)
print(pyramid.faces_square())
print(pyramid.figure_square())
