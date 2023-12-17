import PySimpleGUI as sg
import random
import string

sg.theme('Dark Green')

data = [['rocsptjach', 161, 570, 844, 745, 454],
        ['jwsqgvyatn', 380, 524, 697, 124, 911],
        ['egeflqdyvd', 813, 138, 834, 292, 625],
        ['vkrguwdoaw', 642, 607, 209, 688, 699],
        ['rygewgrzst', 670, 570, 499, 557, 518],
        ['stsfbznqtn', 419, 540, 638, 78, 325],
        ['szycvyypig', 786, 581, 489, 279, 264],
        ['rixofzlgil', 483, 243, 970, 664, 313],
        ['yzqrqhtwvt', 213, 887, 55, 119, 211],
        ['rurwvjivsy', 75, 110, 795, 484, 977],
        ['dimuvsdwan', 630, 840, 842, 822, 297],
        ['xnmcmlyyjh', 284, 936, 368, 183, 411],
        ['xogepbuatb', 309, 408, 181, 281, 219],
        ['zpiuwvnfcz', 770, 750, 652, 111, 440]]

headings = ['id', 'Посетители', 'Компания', 'Удостоверение личности', 'personal_data']

# ------ Window Layout ------
layout = [[sg.Table(values=data, headings=headings, max_col_width=35,
                    background_color='light blue',
                    auto_size_columns=True,
                    # display_row_numbers=True,
                    justification='right',
                    num_rows=15,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Пропускная система')],
          ]

# ------ Create Window ------
window = sg.Window('The Table Element', layout)

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()
