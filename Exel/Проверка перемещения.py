# import openpyxl
from openpyxl import load_workbook

# Load in the workbook
wb = load_workbook('file_1.xlsx')
ws = wb['Лист1']  # В каком листе проверяем
my_dict = dict()  # Словарь со всеми значениями
dict_error = dict()  # Словарь, в который будут добавляться ячейки, из которых товар был перемещён на несколько других

current_cell = (ws['A1']).value
index = 1
while current_cell is not None:
    if current_cell in my_dict:
        if (ws[f'B{index}']).value not in my_dict[current_cell]:
            my_dict[current_cell].append((ws[f'B{index}']).value)
    else:
        my_dict[current_cell] = [(ws[f'B{index}']).value]
    index += 1
    current_cell = (ws[f'A{index}']).value

wb.save('file.xlsx')

for elem in my_dict:
    if len(my_dict[elem]) > 1:
        dict_error[elem] = my_dict[elem]

print(dict_error)
