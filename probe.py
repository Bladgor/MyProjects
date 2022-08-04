from openpyxl import load_workbook
import time

wb = load_workbook('file.xlsx')
print('Начало!')
in_put = input('Привет: ')
sheet_out = input('Из какого листа берём значения: ')
sheet_out_column = input('Из какой колонки: ').upper()
sheet_chek = input('С каким листом будем сравнивать: ')
sheet_chek_column = input('С какой колонкой: ').upper()
value = input('Какое значение подставить: ')

ws_2 = wb[sheet_chek]
ws_3 = wb[sheet_out]

list_2 = []
list_3 = []

current_elem = (ws_3['A2']).value
index = 2
while current_elem is not None:
    elem = (ws_3[f'{sheet_out_column}{index}']).value
    if elem:
        elem = int(elem)
        list_3.append(elem)
    index += 1
    current_elem = (ws_3[f'A{index}']).value

current_elem = (ws_2['A1']).value
index = 1
while current_elem is not None:
    elem = (ws_2[f'{sheet_chek_column}{index}']).value
    if elem:
        try:
            elem = int(elem)
            if elem in list_3:
                ws_2[f'B{index}'] = value
        except ValueError:
            pass
    index += 1
    current_elem = (ws_2[f'A{index}']).value

wb.save('file.xlsx')
print('Всё!')
time.sleep(5)
