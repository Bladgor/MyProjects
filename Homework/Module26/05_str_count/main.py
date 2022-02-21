# ## Задача 5. Количество строк
# Реализуйте функцию-генератор,
# которая берёт все питоновские файлы в директории и вычисляет общее количество строк кода,
# игнорируя пустые строки и строчки комментариев.
import os
from typing import Generator


def search_py(folder: str) -> Generator:  # TODO здесь тот же вопрос, что и в первой задачи:
    total_string = 0                      #  что в данном случае пишется в аннотации?
    for element in os.listdir(folder):
        path = os.path.join(folder, element)
        if os.path.isdir(path):
            for i_elem in search_py(path):
                total_string += i_elem
        else:
            if element.endswith('.py'):
                with open(path, encoding='utf-8') as f:
                    for elem in f:
                        if not elem.startswith('#') and not elem.startswith('\n'):
                            total_string += 1
    yield total_string


my_path = os.path.abspath(os.path.join('..', '..', 'Module26'))
total = 0
for my_elem in search_py(my_path):
    total += my_elem
print('Общее количество строк кода во всех файлах:', total)
