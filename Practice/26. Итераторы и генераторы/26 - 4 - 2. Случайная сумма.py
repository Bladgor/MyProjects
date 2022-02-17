# Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента
# (первый элемент — просто случайное вещественное число от 0 до 1).
# Алексею нельзя хранить в памяти весь этот список, а со значениями работать как-то надо.
#
# Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
# Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.
#
# Пример работы программы:
#
# Кол-во элементов: 5
# Элементы итератора:
# 0.74
# 1.13
# 1.95
# 2.2
# 2.55
#
# Новое кол-во элементов: 6
# Элементы итератора:
# 0.79
# 1.58
# 2.55
# 2.81
# 3.06
# 3.34

from random import random


class RandomSum:
    def __init__(self, limit_num):
        self.prev_num = round(random(), 2)
        self.count = 0
        self.limit_num = limit_num

    def __iter__(self):
        self.prev_num = round(random(), 2)
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.limit_num:
            self.cur_num = round(self.prev_num + random(), 2)
            self.prev_num = self.cur_num
        else:
            raise StopIteration
        return self.cur_num


quantity = int(input('Кол-во элементов: '))
my_elem = RandomSum(quantity)
for elem in my_elem:
    print(elem)

quantity = int(input('\nНовое кол-во элементов: '))
my_elem = RandomSum(quantity)
for elem in my_elem:
    print(elem)
print('\nЗапускаем ещё раз цикл по тому же итератору:')
for elem in my_elem:
    print(elem)
