# ## Задача 4. Последовательность Хофштадтера
# Реализуйте генерацию последовательности Q Хофштадтера (итератором или генератором).
# Сама последовательность выглядит так:
#
# Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))
#
# В итератор (или генератор) передаётся список из двух чисел.
# Например, QHofstadter([1, 1]) генерирует точную последовательность Хофштадтера.
# Если передать значения [1, 2], то последовательность должна немедленно завершиться.

from typing import List
from collections import Iterable


def q_hofstadter(num_list: List[int]) -> Iterable[int]:
    if num_list[0] != 1 or num_list[1] != 1:
        return
    for num in num_list:
        yield num
    while True:
        n = len(num_list)
        q = num_list[n - num_list[n - 1]] + num_list[n - num_list[n - 2]]
        yield q
        num_list.append(q)


counter = 0

for elem in q_hofstadter([1, 1]):
    counter += 1
    print(elem, end=' ')
    if counter == 30:
        break

#  TODO А тут pycharm выдаёт предупреждение: DeprecationWarning:
#   Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,
#   and in 3.10 it will stop working from collections import Iterable
#   Как же тогда лучше сейчас делать аннотации?
