# ## Задача 2. Рефакторинг
# После различных вопросов про отличия итераторов, генераторов и генераторных выражений,
# на собеседовании вам дали небольшой пример кода и попросили “провести рефакторинг”. Вот сам код.
#
# ````python
# # Нужно найти какие два числа из списков в результате попарного перемножения дадут число 56
# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
#
# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break
# ````
# Проблема кода состоит в некрасивом выходе из циклов (два break и флаг).
# Реализуйте более красивый выход из циклов, используя генератор.
# Сам алгоритм решения (попарное перемножение) и списки трогать нельзя.

from typing import List, Optional


def search(list_1: List[int], list_2: List[int], find: int) -> Optional[str]:
    for x in list_1:
        for y in list_2:
            result = x * y
            yield f'{x} {y} {result}'
            if result == find:
                print('Found!!!')
                return


my_list_1 = [2, 5, 7, 10]
my_list_2 = [3, 8, 4, 9]
to_find = 56

for elem in search(my_list_1, my_list_2, to_find):
    print(elem)
