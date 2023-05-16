import PySimpleGUI as sg
import requests
import json
import re
from config import url, timeout, font_size


def data_from_req(data_req):
    pattern = '&quot;'
    repl = '"'
    data_list = []
    list_row_colors = []
    for i, elem in enumerate(data_req['passes']):
        if elem['personalData'] == 1:
            # sub_list = [elem['id'], elem['visitor'], re.sub(pattern, repl, elem['company']),
            #             elem['passport'], 'Необходимо согласие']
            list_row_colors.append((i, 'yellow'))
        sub_list = [elem['id'], elem['visitor'], re.sub(pattern, repl, elem['company']),
                    elem['passport']]
        data_list.append(sub_list)

    return data_list, list_row_colors


def main():
    request = requests.get(url)
    data = json.loads(request.text)
    print(data)

    sg.theme('Dark Green')

    data_table, row_colors = data_from_req(data)

    headings = ['  id  ', 'Посетители', 'Компания', 'Удостоверение личности']
    size = font_size
    size_row = round(font_size * 2.5)

    layout = [[sg.Table(values=data_table, headings=headings, max_col_width=50,
                        row_colors=row_colors,
                        font=('Calibri', size),
                        # selected_row_colors='blue',
                        background_color='light blue',
                        auto_size_columns=True,
                        justification='centre',
                        num_rows=15,
                        key='-TABLE-',
                        row_height=size_row,
                        sbar_arrow_width=True,
                        expand_x=True,
                        expand_y=True,
                        tooltip='Пропускная система')],
              ]

    window = sg.Window('Пропускная система', layout, resizable=True, no_titlebar=True, location=(0, 0),
                       keep_on_top=True, icon='plugins24.ico').Finalize()
    window.Maximize()

    while True:
        pre_data = data
        event, values = window.read(timeout=timeout)
        request = requests.get(url)
        data = json.loads(request.text)
        if data != pre_data:
            data_table = data_from_req(data)
            window['-TABLE-'].update(values=data_table)
        if event == sg.WIN_CLOSED:
            break
        elif event == sg.TIMEOUT_KEY:
            window.refresh()

    window.close()


if __name__ == '__main__':
    main()
