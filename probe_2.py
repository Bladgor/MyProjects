# Реализуйте класс-итератор Primes,
# который принимает максимальное число N и выдаёт все простые числа от 1 до N.
#
# Основной код:
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

class Primes:
    def __init__(self, limit):
        self.count = 0
        self.limit = limit
        self.list_num = []

    def __iter__(self):
        if self.limit >= 2:
            self.list_num.append(2)
        for i_elem in range(2, self.limit + 1):
            flag = True
            for num in range(2, i_elem):
                if i_elem % num == 0:
                    flag = False
                    break
            if flag:
                self.list_num.append(i_elem)
        return self

    def __next__(self):
        self.count += 1
        if self.count == len(self.list_num):
            raise StopIteration
        for i in self.list_num[self.count:]:
            return i


nums = Primes(50)

for elem in nums:
    print(elem, end=' ')
print()
for elem in nums:
    print(elem, end=' ')
