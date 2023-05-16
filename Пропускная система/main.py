import PySimpleGUI as sg
import requests
import json
import re
from typing import List, Dict
from config import url, timeout, font_size


def data_from_req(data_req: Dict) -> (List, List):
    pattern = '&quot;'
    repl = '"'
    data_list = []
    list_row_colors = []
    if 'passes' in data_req:
        for i, elem in enumerate(data_req['passes']):
            if elem['personalData'] == 1:
                list_row_colors.append((i, 'pink'))
            sub_list = [elem['id'], elem['visitor'], re.sub(pattern, repl, elem['company']),
                        elem['passport']]
            data_list.append(sub_list)
    else:
        data_list, list_row_colors = [['', 'Ошибка доступа', '', '']], [(0, 'pink')]

    return data_list, list_row_colors


def main():
    try:
        request = requests.get(url)
    except requests.exceptions.ConnectionError:
        request = ''
    try:
        data = json.loads(request.text)
    except json.decoder.JSONDecodeError:
        data = {'passes': [{'id': '',
                            'visitor': 'Ошибка формата данных',
                            'company': '', 'passport': '', 'personalData': 1}],
                'success': 1}
    except AttributeError:
        data = {'passes': [{'id': '',
                            'visitor': 'Ошибка соединения',
                            'company': '', 'passport': '', 'personalData': 1}],
                'success': 1}

    sg.theme('Light Blue')

    data_table, row_colors = data_from_req(data)

    headings = ['  id  ', 'Посетители', 'Компания', 'Удостоверение личности']
    size = font_size
    size_row = round(font_size * 2.5)

    layout = [[sg.Table(values=data_table, headings=headings, max_col_width=50,
                        row_colors=row_colors,
                        font=('Calibri', size),
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
                       keep_on_top=True).Finalize()
    window.Maximize()

    while True:
        pre_data = data
        event, values = window.read(timeout=timeout)
        try:
            request = requests.get(url)
        except requests.exceptions.ConnectionError:
            request = ''
        try:
            data = json.loads(request.text)
        except json.decoder.JSONDecodeError:
            data = {'passes': [{'id': '',
                                'visitor': 'Ошибка формата данных',
                                'company': '', 'passport': '', 'personalData': 1}],
                    'success': 1}
        except AttributeError:
            data = {'passes': [{'id': '',
                                'visitor': 'Ошибка соединения',
                                'company': '', 'passport': '', 'personalData': 1}],
                    'success': 1}

        sg.theme('Light Blue')
        if data != pre_data:
            data_table, row_colors = data_from_req(data)
            window['-TABLE-'].update(values=data_table, row_colors=row_colors)
        if event == sg.WIN_CLOSED:
            break
        elif event == sg.TIMEOUT_KEY:
            window.refresh()

    window.close()


if __name__ == '__main__':
    main()
