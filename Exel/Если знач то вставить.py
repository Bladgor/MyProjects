# import openpyxl
from openpyxl import load_workbook

# Load in the workbook
wb = load_workbook('file.xlsx')

# sheet_out = input('Из')

ws_1 = wb['Лист1']
ws_2 = wb['Лист2']
ws_3 = wb['Лист3']

list_1 = []
list_2 = []
list_3 = []

# row_range_1 = ws_1['A1':'A32']
# for elem in row_range_1:
#     current = list(elem)[0].value
#     list_1.append(current)

row_range_3 = ws_3['H2':'H171']
for i, elem in enumerate(row_range_3):
    current = list(elem)[0].value
    if current:
        current = int(current)
    list_3.append(current)
print(list_3)

row_range_2 = ws_2['A2':'A104']
for i, elem in enumerate(row_range_2):
    current = list(elem)[0].value
    if current in list_3:
        ws_2[f'B{i + 2}'] = 'HG'
    else:
        ws_2[f'B{i + 2}'] = ''

wb.save('file.xlsx')
