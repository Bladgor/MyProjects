# TODO Нужно поступить следующим образом
class Figure:

    def __init__(self, ...):

    # TODO Здесь описываем фигуру с ее возможными значениями - side, height, base
    #  Проще всего это сделать здесь, чтобы потом не описывать в наследниках
    #  .
    #  Чтобы явно не прописывать все параметры лучше принимать именованные параметры
    #  def __init__(self, **kwargs)
    #       self.side = kwargs.get('side')

    # TODO Методы подсчета, которы переопределяют наследники
    def figure_perimetr(self):
        raise NotImplemented('Не надо тебе этого, Барин')

    def figure_square(self):
        raise NotImplemented('Не надо тебе этого, Барин'

    # TODO Конечно же сеттеры для всех параметров
    @property
    def side(self):
        return self.side

    @side.setter
    def side(self, side):
        self.side = side


# TODO В наследниках переопределяем методы подсчета
class Square(Figure):

    def figure_perimetr(self):
        ...

    def figure_square(self):
        ...


class Triangle(Figure):
    ...


# TODO В миксине только считаем общую площадь у фигур
class Mixin:

    def faces_square(self):
        ...


# TODO Класс куба наследуется от квадрата и миксина.
#  В нем должен быть конструктор, и внутри у него есть список его 6 заготовок.
#  То есть список из классов кубов - [Square, Square ....]
class Cube(Square, Mixin):
    ...

# TODO Класс пирамиды наследуется от 3 классов - треугольник, квадарт и миксин
#  В нем должен быть конструктор, и внутри у него есть список его 5 заготовок.
#  То есть список из классов треугольников и 1 квадрата - [Square, Triangle ....]
class Pyramid(Triangle, Square, Mixin):
    ...
