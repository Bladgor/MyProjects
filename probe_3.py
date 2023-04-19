import PySimpleGUI as sg


sg.theme('Dark Green')

data = [['rocsptjach1111111111111111111111111', 161, 570, 844, 745, 454],
        ['jwsqgvyatn', 380, 524, 697, 124, 911, 911],
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

headings = ['column 1', 'column 10', 'column 2', 'column 3', 'column 4', 'column 5']
size = 20
size_row = round(size * 2.5)
# ------ Window Layout ------
layout = [[sg.Table(values=data, headings=headings,
                    font=('Calibri', size),
                    # max_col_width=35,
                    def_col_width=True,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='centre',
                    num_rows=20,
                    # alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=size_row,
                    expand_x=True,
                    expand_y=True,
                    tooltip='This is a table')],
          [sg.Button('Read')],
          [sg.Text('Read = read which rows are selected')]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout, resizable=True, no_titlebar=True, location=(0, 0),
                   keep_on_top=True).Finalize()
window.Maximize()

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()
