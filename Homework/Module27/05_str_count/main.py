# ## Задача 5. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
#
# Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем)

import functools
from typing import Callable, Any


class Counter:
    count = dict()


def counter(func: Callable) -> Callable:
    """ Декоратор, подсчитывающий количество вызовов каждой функции с помощью класса. """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        if func.__name__ in Counter.count:
            Counter.count[func.__name__] += 1
        else:
            Counter.count[func.__name__] = 1
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@counter
def squares_sum() -> int:
    """ Возвращает сумму квадратов всех чисел от единицы до миллиона включительно. """
    total = 0
    for x in range(1, 1 * 10 ** 6 + 1):
        total += x ** 2
    return total


@counter
def cubes_sum(number: int) -> int:
    """ Возвращает сумму кубов всех чисел от единицы до переданного числа включительно. """
    total = 0
    for x in range(1, number + 1):
        total += x ** 3
    return total


print(squares_sum())
print(cubes_sum(10))
print(cubes_sum(10))
print(cubes_sum(10))
print(Counter.count)
