# Один проект состоит из огромного количества разнообразных функций,
# часть из которых используется в других проектах в качестве плагинов,
# то есть они как бы «подключаются» и создают дополнительный функционал.
#
# Реализуйте специальный декоратор,
# который будет «регистрировать» нужные функции как плагины и заносить их в соответствующий словарь.

import functools
from typing import Callable


PLUGINS = dict()


def register(func: Callable) -> Callable:
    """ Декоратор. Регистрирует функцию как плагин. """
    PLUGINS[func.__name__] = func
    return func


@register
def ingredients(func: Callable) -> Callable:
    """ Декоратор. Выводит начинку сэндвич. """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('#помидоры#')
        print('--ветчина--')
        print('~салат~')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@register
def bread(func: Callable) -> Callable:
    """ Декоратор. Оборачивает начинку в булки. """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('</----------\>')
        result = func(*args, **kwargs)
        print('<\______/>')
        return result
    return wrapped_func


@register
@bread
@ingredients
def sandwich():
    """ Выводит сэндвич. """
    pass


print(PLUGINS)
sandwich()
print(sandwich.__name__)
print(sandwich.__doc__)
