# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию.
# Не забывайте про документацию и аннотации типов.
#
# Пример декорируемой функции:
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))
#
# Основной код:
# greeting('Tom')
#
# Результат:
# Привет, Tom!
# Привет, Tom!

from typing import Callable


def do_twice(func: Callable) -> Callable:
    """Декоратор, дважды вызывающий функцию"""

    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapped_func


@do_twice
def greeting(name: str) -> None:
    """Выводит сообщение-приветствие с именем"""

    print('Привет, {name}!'.format(name=name))


greeting('Tom')
