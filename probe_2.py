import PySimpleGUI as sg
import operator
from functools import reduce

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Итог выражения ='), sg.Text(size=(12, 1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('+'), sg.Button('-'), sg.Button('='), sg.Button('Exit')]]

window = sg.Window('Калькулятор', layout)

base, base_str = [], ''
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Закрыть':
        break
    if event == '+':
        base.append(int(values['-IN-']))
        base_str += f" {values['-IN-']} +"
        # измените элемент "output" на значение элемента "input"
        window['-OUTPUT-'].update(base_str)
    if event == '=' and '+' in base_str:
        if values['-IN-']:
            base.append(int(values['-IN-']))
        window['-OUTPUT-'].update(sum(base))
        base, base_str = [], ''
    if event == '=' and '-' in base_str:
        if values['-IN-']:
            base.append(int(values['-IN-']))
        window['-OUTPUT-'].update(reduce(operator.__sub__, base))
        base, base_str = [], ''
    if event == '-':
        base.append(int(values['-IN-']))
        base_str += f" {values['-IN-']} -"
        window['-OUTPUT-'].update(base_str)

    window['-IN-'].update('')

window.close()
