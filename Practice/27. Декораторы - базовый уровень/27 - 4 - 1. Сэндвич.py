# Задача 1. Сэндвич
# Есть функция, которая выводит начинку сэндвича.
# Сверху и снизу от начинки идут различные ингредиенты вроде салата, помидоров и других.
# Всё это в свою очередь содержится между двух половинок булочки.
# Реализуйте такую функцию и два соответствующих декоратора — ингредиенты и хлеб.
#
# Пример результата работы программы при вызове функции sandwich:
#
# </----------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

from typing import Callable


def ingredients(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        print('#помидоры#')
        print('--ветчина--')
        print('~салат~')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


def bread(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        print('</----------\>')
        result = func(*args, **kwargs)
        print('<\______/>')
        return result
    return wrapped_func


@bread
@ingredients
def sandwich():
    pass


sandwich()
