# Напишите программу, которая принимает имя файла и выводит его расширение.
# Если расширение у файла определить невозможно, выбросите исключение.

file_name = '.filetxtru'
elem = ''
index = 0

try:
    if '.' in file_name:
        while elem != '.':
            index -= 1
            elem = file_name[index]
        if len(file_name) != len(file_name[index::]):
            print('Расширение файла:', file_name[index::])
        else:
            raise ValueError
    else:
        raise ValueError
except ValueError:
    print(f'Ошибка ValueError. Файл не имеет расширения.')


