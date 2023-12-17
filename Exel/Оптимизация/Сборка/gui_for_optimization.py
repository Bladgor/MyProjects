import PySimpleGUI as sg
from check_value import check_value
from optimization_1 import main

sg.theme('DarkGreen5')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Введите максимальное кол-во бутылок в ячейке:'), sg.InputText()],
          [sg.Text('Введите максимальное кол-во бутылок после объединения:'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Optimization', layout, icon='plugins24.ico')
# Event Loop to process "events" and get the "values" of the inputs

in_cell = None
total = None

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):  # if user closes window or clicks cancel
        break
    if check_value(values[0]):
        in_cell = int(values[0])
    else:
        sg.popup_error('В первой строке введено неверное значение.', title='Ошибка')
        continue
    if check_value(values[1]):
        total = int(values[1])
    else:
        sg.popup_error('Во второй строке введено неверное значение.', title='Ошибка')
        continue
    print('You entered: ', values[0], values[1])
    break

main(in_cell, total)
sg.popup_ok('Программа завершена. Данные сохранены в файл "Оптимизация.xlsx')

window.close()
