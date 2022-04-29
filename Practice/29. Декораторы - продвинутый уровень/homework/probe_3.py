# ## Задача 3. Логирование в формате
# Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов)
# и в который можно передавать формат вывода даты и времени логирования.
#
# #### Пример кода, передаётся формат “Месяц День Год - Часы Минуты Секунды:
# ````python
# @log_methods("b d Y - H:M:S")
# class A:
#     def test_sum_1(self) -> int:
#         print('test sum 1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
#
# @log_methods("b d Y - H:M:S")
# class B(A):
#     def test_sum_1(self):
#         super().test_sum_1()
#         print("Наследник test sum 1")
#
#     def test_sum_2(self):
#         print("test sum 2")
#         number = 200
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
#
# my_obj = B()
# my_obj.test_sum_1()
# my_obj.test_sum_2()
# ````
# #### Результат:
# ````
# - Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# - Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_1
# - Завершение 'A.test_sum_1', время работы = 0.187s
# Тут метод test_sum_1 у наследника
# - Завершение 'B.test_sum_1', время работы = 0.187s
# - Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_2 у наследника
# - Завершение 'B.test_sum_2', время работы = 0.370s
# ````

import functools
import time
from datetime import datetime
from typing import Callable


def timer(_func=None, *, format_output: str = 'd m Y - H:M:S', class_name: str = None):
    def timer_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # format_output = 'b d Y - H:M:S'
            format_list = format_output.split(' - ')
            arg_date_1 = format_list[0].split()[0]
            arg_date_2 = format_list[0].split()[1]
            arg_date_3 = format_list[0].split()[2]
            date_text = f'%{arg_date_1} %{arg_date_2} %{arg_date_3}'
            arg_time_1 = format_list[1].split(':')[0]
            arg_time_2 = format_list[1].split(':')[1]
            arg_time_3 = format_list[1].split(':')[2]
            time_text = f'%{arg_time_1}:%{arg_time_2}:%{arg_time_3}'
            running_date = datetime.now().strftime(date_text)
            running_time = datetime.now().strftime(time_text)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'Дата запуска функции {class_name}.{func.__name__}:', running_date)
            print('Время запуска функции:', running_time)
            print(f'Время работы функции: {round(end - start, 3)}s')
            return result
        return wrapper
    if _func is None:
        return timer_decorator
    return timer_decorator(_func)


def log_methods(format_output="d d Y - H:M:S"):

    def wrapper(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_method = timer(cur_method, format_output=format_output, class_name=cls.__name__)
                setattr(cls, i_method, decorated_method)
        return cls
    return wrapper


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(cls):
        print("Наследник test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
