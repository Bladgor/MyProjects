# Задача 2. Директории
# Реализуйте функцию in_dir,
# которая принимает в качестве аргумента путь и временно меняет текущую рабочую директорию на новую.
# Функция должна быть контекст-менеджером.
# Также реализуйте обработку ошибок (например, если такого пути не существует).
# Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться в изначальную рабочую директорию.

import os
from contextlib import contextmanager


@contextmanager
def in_dir(path):
    current_path = os.getcwd()
    print('Попытка перехода в папку:', path)
    try:
        yield os.chdir(path)
    except BaseException as ex:
        print('Ошибка:', ex)
    finally:
        os.chdir(current_path)
    print('Вернулись в прежнюю директорию.')
    print(os.getcwd())


my_path = os.path.abspath(os.path.join('..', '..', 'Homework'))

with in_dir(my_path):
    print(os.getcwd())
    print('Список папок:', os.listdir(os.getcwd()))
