# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    @classmethod
    def draw(cls):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @classmethod
    def draw(cls):
        print('Рисует синяя ручка')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @classmethod
    def draw(cls):
        print('Рисует карандаш')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @classmethod
    def draw(cls):
        print('Рисует маркер')


pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()
