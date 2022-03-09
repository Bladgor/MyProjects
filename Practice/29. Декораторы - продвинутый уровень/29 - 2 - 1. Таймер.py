# Задача 1. Таймер
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера:
# функция должна работать с оператором with и замерять время работы вложенного кода
import os
import time
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def timer() -> Iterator:
    print('Начало работы функции')
    start = time.time()
    try:
        yield
    except Exception as ex:
        print(f'Ошибка: {ex}')
    finally:
        print('Функция выполнялась:', time.time() - start)


with timer():
    x_list = [x ** 3 for x in range(5000000)]
    x_list /= 0

print(os.listdir(os.getcwd()))
