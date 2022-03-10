# ## Задача 1. Работа с файлом 2
# Реализуйте модернизированную версию контекст менеджера File
# - теперь, при попытке открыть несуществующий файл,
# менеджер автоматически создаёт и открывает этот файл в режиме записи.
# На выходе из менеджера подавляются все исключения, связанные с файлами.

import os


class File:

    def __init__(self, file: str, mode: str = None) -> None:
        self.mode = mode
        if self.mode == 'r' or self.mode is None:
            if os.path.isfile(file):
                self.file = open(file, encoding='utf-8')
            else:
                self.file = open(file, 'w', encoding='utf-8')
                self.mode = 'w'
        elif self.mode == 'w':
            self.file = open(file, 'w', encoding='utf-8')

    def write(self, text: str) -> None:
        if self.mode == 'w':
            self.file.write(text)
        else:
            print('Файл открыт не в режиме записи.')

    def __enter__(self) -> 'File':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('example.txt', 'r') as f:
    f.write('Всем привет!!!')

# зачет!
