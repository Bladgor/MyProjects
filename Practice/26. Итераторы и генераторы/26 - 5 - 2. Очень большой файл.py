# Вам на обработку пришёл огромнейший файл с данными.
# Настолько огромный, что при его открытии компьютер просто зависает,
# так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).
#
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки.
# Напишите программу, которая подсчитает общую сумму чисел в файле.
# Для считывания файла реализуйте специальный генератор.

def my_gen():
    with open('numbers.txt', encoding='utf-8') as f:
        for elem in f:
            yield int(elem)


total = 0

for number in my_gen():
    total += number

print(total)
