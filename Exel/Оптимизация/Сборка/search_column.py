

def search_column(sheet, name: str) -> str:
    """
    Функция возвращает имя столбца, содержащего колонку "name"
    """
    current_cell = sheet['A4']  # Текущая ячейка
    index = 0
    while current_cell.value != name:
        current_cell = sheet[f'{alphabet[index]}4']
        index += 1

    return alphabet[index - 1]


alphabet = [chr(i) for i in range(65, 91)]  # Алфавит в верхнем регистре
