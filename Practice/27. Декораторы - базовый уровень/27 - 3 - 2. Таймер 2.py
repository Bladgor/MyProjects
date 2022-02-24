# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию,
# которая сделала всю работу за вас, что позволило большую часть времени смотреть видео с котиками в интернете.
# Однако, увидев свой код, вы как программист с опытом поняли, что этот код можно написать намного красивее и удобнее.
#
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
# Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.

from typing import Callable, Any
import time


def timer(func: Callable) -> Callable:
    """
    Декоратор, выводящий время, которое потребовалось
    на выполнение функции.
    """
    def wrapped_func(*args, **kwargs) -> Any:
        start_time = time.time()
        result_1 = args
        result_2 = kwargs
        print(f'args = {result_1}\nkwargs = {result_2}')
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f'Функция работала {run_time} секунд(ы).')

        return result
    return wrapped_func


@timer
def squares_sum() -> int:
    """
    Возвращает сумму квадратов чисел
    от единицы до одного миллиона.

    :return: int
    """
    total = 0
    for x in range(1, 1 * 10 ** 6 + 1):
        total += x ** 2
    return total


@timer
def cubes_sum(number: int) -> int:
    """
    Возвращает сумму кубов чисел
    от единицы до переданного числа включительно.

    :param number: int
    :return: int
    """
    total = 0
    for x in range(1, number + 1):
        total += x ** 3
    return total


my_result_1 = squares_sum()
print(my_result_1)
print()

my_result_2 = cubes_sum(900000)
print(my_result_2)
