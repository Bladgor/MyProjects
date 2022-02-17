# Дан любой итерируемый объект, например список из N чисел.
# Реализуйте функцию, которая эмулирует работу цикла for с помощью цикла while
# и проходит во всем элементам итерируемого объекта.
# Не забудьте про исключение «конца итерации».

num_list = [10, 20, 30]


def my_for(my_list):
    my_iter = my_list.__iter__()
    while True:
        try:
            print(my_iter.__next__() * 2)
        except StopIteration:
            break


my_for(num_list)
