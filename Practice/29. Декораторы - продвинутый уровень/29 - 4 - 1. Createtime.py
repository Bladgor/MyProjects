# Задача 1. Createtime
# Реализуйте декоратор класса, который выдаёт дату и время создания,
# а также список всех методов объекта класса каждый раз, когда объект класса создаётся в основном коде.

import functools
import time
from datetime import datetime
from typing import Callable


def create_time(cls):
    """ Декоратор класса. Выводит время создания инстанса класса по Гринвичу."""

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print('Время создания инстанса класса по Гринвичу:', datetime.utcnow())
        print(f'Список всех методов класса:\n{dir(cls)}\n')
        return instance
    return wrapper


def timer(func: Callable) -> Callable:
    """ Декоратор. Выводит время работы функции или метода."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Время работы функции или метода', end - start)
        return result
    return wrapper


def for_all_method(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и
    применяет его ко всем методам класса.
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                current_method = getattr(cls, i_method_name)
                decorated_method = decorator(current_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@create_time
@for_all_method(timer)
class CubsSquaresSum:

    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        return sum([x ** 2 for x in range(self.max_num + 1)])

    def cubs_sum(self) -> int:
        return sum([x ** 3 for x in range(self.max_num + 1)])


func_1 = CubsSquaresSum(10000)
time.sleep(1)
func_2 = CubsSquaresSum(20000)
print()
print(func_1.squares_sum())
print(func_2.cubs_sum())
