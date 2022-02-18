# ## Задача 4. Последовательность Хофштадтера
# Реализуйте генерацию последовательности Q Хофштадтера (итератором или генератором).
# Сама последовательность выглядит так:
#
# Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))
#
# В итератор (или генератор) передаётся список из двух чисел.
# Например, QHofstadter([1, 1]) генерирует точную последовательность Хофштадтера.
# Если передать значения [1, 2], то последовательность должна немедленно завершиться.

# Пример для понимания алгоритма:
# например надо подставлять значения Q(1) = 1, Q(2)=1 (по условию).
# Q(3) = Q(3-1)+Q(3-1) = Q(2)+ Q(2) = 2
# Q(4) = (Q(4-Q(3))+Q(4-Q(2)) = Q(4-2)+Q(4-1) = Q(2)+Q(3) = 1+2=3
# Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))

class QHofstadter:
    def __init__(self, my_list):
        self.prev_q = 1
        self.cur_q = self.set_q(my_list[0])
        self.next_q = self.set_q(my_list[1])
        self.count = 0

    def set_q(self, q):
        if q != 1:
            raise StopIteration
        return q

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1

        self.cur_q = (self.count - self.cur_q) + (self.count - self.prev_q)
        if self.cur_q == 1:
            return 1
        return self.cur_q


my_q = QHofstadter([1, 1])
count = 0

for elem in my_q:
    count += 1
    print(elem)
    if count == 5:
        break

