# Задача 1. Работа с файлом
# Реализуйте класс File — контекстный менеджер для работы с файлами.
# Он должен принимать на вход имя файла и режим чтения/записи и открывать сам файл.
# В начале работы менеджер возвращает файловый объект, а в конце — закрывает файл.
#
# Пример основного кода:
# with File(‘example.txt’, ‘w’) as file:
#     file.write(‘Всем привет!’)

class File:
    def __init__(self, file: str, mode: str = None):
        self.mode = mode
        if self.mode == 'r' or self.mode is None:
            self.file = open(file, encoding='utf-8')
        elif self.mode == 'w':
            self.file = open(file, 'w', encoding='utf-8')

    def write(self, text):
        if self.mode == 'w':
            self.file.write(text)
        else:
            print('Файл не открыт в режиме записи.')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('example.txt') as f:
    f.write('Всем привет!')
