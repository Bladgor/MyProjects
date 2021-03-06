# Примечание: начиная с этого домашнего задания во всех задачах используйте аннотации типов
# (как минимум для функций, методов и их аргументов)
#
# ## Задача 1. Квадраты чисел
# Пользователь вводит число N. Напишите программу,
# которая генерирует последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 **2 и так далее).
# Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.

from collections.abc import Iterable


class GenSquare:
    def __init__(self, num: int) -> None:
        self.count = 0
        self.num = num

    def __iter__(self):  # TODO здесь, как понял, возвращается объект итератора,
        self.count = 0   #  но вот что написать в данном случае в аннотаци не совсем понял
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count <= self.num:
            return self.count ** 2
        else:
            raise StopIteration


def gen_square(num: int):  # TODO Здесь дома на python 3.9 работает с -> Iterable[int], а на работе с 3.8 нет
    for number in range(1, num + 1):
        yield number ** 2


my_gen_1 = GenSquare(5)
for elem in my_gen_1:
    print(elem, end=' ')

print()
my_gen_2 = gen_square(5)
for elem in my_gen_2:
    print(elem, end=' ')

print()
my_gen_3 = (num ** 2 for num in range(1, 6))
for elem in my_gen_3:
    print(elem, end=' ')
