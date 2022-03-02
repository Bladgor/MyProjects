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
        self.file = file
        self.mode = mode

    def write(self, text):
        if self.mode == 'w':
            self.file.write(text)

    def __enter__(self):
        if self.mode == 'r' or self.mode is None:
            self.file = open(self.file, encoding='utf-8')
            return self.file
        elif self.mode == 'w':
            self.file = open(self.file, 'w', encoding='utf-8')
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File('example.txt', 'w') as file:
    file.write('Всем привет!')
