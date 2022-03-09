# Задача 1. Повторение кода
# В одной из практик вы уже писали декоратор do_twice,
# который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.

from typing import Callable
import functools


def repeat_count(_func: Callable = None, *, count: int = 2):
    def repeat(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):

            while wrapped_func.count != 0:
                func(*args, **kwargs)
                wrapped_func.count -= 1

        wrapped_func.count = count
        return wrapped_func
    if _func is None:
        return repeat
    return repeat(_func)


@repeat_count
def my_print():
    print('Hello, World!')


my_print()
