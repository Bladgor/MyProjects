# Вы работаете в отделе тестирования,
# и вам поручили с помощью различных функций замерить скорость передачи данных на нескольких десятках сайтов.
# Конечно же, вручную «щёлкать» сайты и замерять время вам было лень,
# поэтому возникла идея написать «автотест», который всё сделает сам.
#
# С помощью понятия функции высшего порядка реализуйте функцию-таймер,
# которая замеряет время работы переданной функции func и выдаёт ответ на экран.
#
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.

from typing import Callable, Any
import time


def timer(func, *args, **kwargs):
    start_time = time.time()
    result_1 = args
    result_2 = kwargs
    print(f'args = {result_1}\nkwargs = {result_2}')
    result = func(*args, **kwargs)
    end_time = time.time()
    run_time = end_time - start_time
    print(f'Функция работала {run_time} секунд(ы).')

    return result


def squares_sum():
    total = 0
    for x in range(1, 11 * 10 ** 4):
        total += x ** 2
    return total


def cubes_sum(number):
    total = 0
    for x in range(number + 1):
        total += x ** 3
    return total


my_result_1 = timer(squares_sum)
print(my_result_1)
print()
my_result_2 = timer(cubes_sum, 9000000)
print(my_result_2)
