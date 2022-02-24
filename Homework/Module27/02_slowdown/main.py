# ## Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно как бы “замедлить”.
# Типичный пример - функция, которая постоянно проверяет, изменились ли данные на веб странице или её код.
#
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

import functools
import time
from typing import Callable, Any


def sleep(func: Callable) -> Callable:
    """ Декоратор. Запрашивает, через какое время выполнить функцию. """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        time_sleep = int(input('Укажите, через сколько секунд выполнить функцию: '))
        time.sleep(time_sleep)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@sleep
def cubes_sum(number: int) -> int:
    """Возвращает сумму кубов всех чисел от единицы до переданного числа включительно."""
    total = 0
    for x in range(1, number + 1):
        total += x ** 3
    return total


print(f'Сумма кубов: {cubes_sum(100)}')
