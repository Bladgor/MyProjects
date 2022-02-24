# ## Задача 3. Логирование
# Реализуйте декоратор logging, который будет отвечать за логирование функций.
# На экран выводится название функции и её документация.
# Если во время выполнения декорируемой функции возникла ошибка,
# то в файл function_errors.log записываются название функции и название ошибки.
#
# Также постарайтесь сделать так, чтобы бы программа не завершалась после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.
#
# Дополнительно: используя модуль datetime также запишите дату и время возникновения ошибки

import functools
import datetime
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """
    Декоратор. Логирует функции.
    Ошибки записываются в файл function_errors.log
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print(f'\nФункция: {func.__name__}\n'
                  f'Документация: {func.__doc__}\n'
                  f'Результат выполнения: ', end='')
            result = func(*args, **kwargs)
        except (TypeError, ZeroDivisionError) as error:
            with open('function_errors.log', 'a', encoding='utf-8') as f:
                f.write(f'{func.__name__} {type(error)} {error} {datetime.datetime.now()}\n')
                return f'Ошибка! {error}'
        return result
    return wrapped_func


@logging
def division_nums_1() -> int:
    """ Возвращает сумму деления числа 16 на числа от -4 до 4 """
    total = 0
    for x in range(-4, 5, 2):
        total += 16 / x
    return total


@logging
def division_nums_2(number: int) -> int:
    """ Возвращает сумму деления числа 20 на числа от -4 до переданного числа """
    total = 0
    for x in range(-4, number, 2):
        total += 20 / x
    return total


with open('function_errors.log', 'w', encoding='utf-8'):
    pass

print(division_nums_1())
print(division_nums_2('Tom'))
