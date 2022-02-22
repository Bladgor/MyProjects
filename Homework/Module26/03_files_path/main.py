# ## Задача 3. Пути файлов
# Реализуйте функцию gen_files_path, которая проходит по всем каталогам указанной директории
# (по умолчанию - корневой диск), находит указанный пользователем каталог и генерирует пути всех файлов,
# которые встретились по пути.

import os


def gen_files_path(path: str = os.path.abspath(os.sep), file_search: str = None) -> str:
    print(path)
    for dirs, folder, files in os.walk(path):
        print('\nВыбранный каталог: ', dirs)
        print('Вложенные папки: ', folder)
        if len(files) > 0:
            print('Файлы в папке: ', files)
            for file in files:
                yield f'Полный путь к файлу: {os.path.join(str(dirs), file)}'
                if file == file_search:
                    print('\nНаш файл найден!!!')
                    return


my_path = os.path.abspath(os.path.join('..', '..', 'Module26'))
my_file = 'my_file.txt'

for elem in gen_files_path(path=my_path, file_search=my_file):
    print(elem)
