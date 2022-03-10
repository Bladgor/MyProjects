# Задача 2. Замедление кода 2.
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор,
# который перед выполнением декорируемой функции ждёт несколько секунд.
# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
# По умолчанию декоратор ждёт одну секунду.
# Помимо этого сделайте так, чтобы декоратор можно было использовать как с аргументами, так и без них.

import functools
import time
from typing import Callable, Optional


def timer_sleep(_func: Optional[Callable] = None, *, sleep_sec: int = 1):
    def timer(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            time.sleep(sleep_sec)
            result = func(args, kwargs)
            return result
        return wrapped_func
    if _func is None:
        return timer
    return timer_sleep(_func)


@timer_sleep
def my_print():
    print('Hello, World!')


my_print()
