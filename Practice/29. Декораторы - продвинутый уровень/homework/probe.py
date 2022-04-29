
import functools
import time
from datetime import datetime


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        format_output = 'b d Y - H:M:S'
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
        print('Дата запуска функции:', running_date)
        print('Время запуска функции:', running_time)
        print(f'Время работы функции: {round(end - start, 3)}s')
        return result
    return wrapper


@timer
def sqr_num(max_num):
    total = 0
    for elem in range(max_num):
        total += elem ** 2
    return total


my_list = sqr_num(10 ** 6)
