# По аналогии с бесконечным итератором из практики предыдущего урока,
# реализуйте свой счётчик-генератор, который также в цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

def my_generator():
    num = 1
    while True:
        num += 1
        flag = True
        for i_elem in range(2, num):
            if num % i_elem == 0:
                flag = False
        if flag:
            yield num


for elem in my_generator():
    print(elem)
