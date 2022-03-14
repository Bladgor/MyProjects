# Задача 2. Декорацию знаешь?
# На новой работе вы познакомились с middle-разработчиком на Python,
# который согласился научить вас всему, что умеет сам.
# Но перед этим он решил точечно проверить ваши знания.
# Он показал код, где один и тот же декоратор логирования использовался для каждого метода класса отдельно:
#
# Зная, что классы тоже можно декорировать, вы сразу поняли, как можно упростить код.
#
# Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод в нём.
# Логирование реализуйте на своё усмотрение:
#
# -- это может быть, например, вывод названия метода, его аргов, кваргов и документации на экран;
# -- либо вывод всей этой информации в отдельный файл вместе с датой и временем.
import functools
from typing import Callable
from datetime import datetime


def log_in_file(func: Callable) -> Callable:
    """ Декоратор. Записывает информацию о функции или методе в log-файл. """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        date_run = datetime.now()
        name, doc = func.__name__, func.__doc__
        result = func(*args, **kwargs)
        arg = [x for i, x in enumerate(args) if i > 0]
        kwarg = [x for i, x in enumerate(kwargs) if i > 0]
        with open('log.txt', encoding='utf-8') as f:
            if f.readline().startswith('') is False:
                with open('log.txt', 'w', encoding='utf-8') as f:
                    f.write(f'Название: {name} </> Описание: {doc} </> Время создания: {date_run}\n'
                            f'Параметры: {arg, kwarg}\n\n')
        return result
    return wrapper


def logging(decorator: Callable) -> Callable:
    """Декоратор.
    Принимает другой декоратор и
    применяет его ко всем методам класса.
    """

    @functools.wraps(decorator)
    def decorate(cls):
        for i_name_method in dir(cls):
            if i_name_method.startswith('__') is False:
                current_method = getattr(cls, i_name_method)
                decorated_method = decorator(current_method)
                setattr(cls, i_name_method, decorated_method)
        return cls
    return decorate


@logging(log_in_file)
class CubsSquaresSum:

    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        """Складывает все квадраты чисел от 1 до заданного числа."""
        return sum([x ** 2 for x in range(1, self.max_num + 1)])

    def cubs_sum(self, max_num) -> int:
        """Складывает все кубы чисел от 1 до заданного числа."""
        return sum([x ** 3 for x in range(1, self.max_num + 1)])


my_func = CubsSquaresSum(1000)
print(my_func.squares_sum())
print(my_func.cubs_sum(1000))
