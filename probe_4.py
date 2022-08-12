from random import randint
import datetime as dt


def random_num(my_list):
    num = randint(1, 45)
    if num in my_list:
        num = random_num(my_list)
    return num


num_list = []
for _ in range(6):
    num_list.append(random_num(num_list))

print(num_list)
print(dt.datetime.now())
