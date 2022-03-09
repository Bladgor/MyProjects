# печатать числа от 0 до 1000, которые делятся на 3, не делятся на 5, сумма цифр < 10
for elem in range(1001):
    if elem % 3 == 0 and elem % 5 != 0:
        total_num = 0
        current_num = elem
        while elem != 0:
            total_num += elem % 10
            elem //= 10
        if total_num < 10:
            print(current_num)

