import PySimpleGUI as sg
import requests
import json
import re
from typing import List, Dict
from config import url, timeout, font_size, length_col_1, length_col_2, length_col_3


def shift(text: str, my_length: int) -> str:
    if len(text) > my_length:
        my_list = list(reversed(list(text)))
        index = len(my_list) - my_length
        for i, elem in enumerate(my_list[index:]):
            if elem == ' ':
                my_list[i + index] = '\n'
                break
        text = ''.join(list(reversed(my_list)))
    return text


def data_from_req(data_req: Dict, length_: int) -> (List, List):
    pattern = '&quot;'
    repl = '"'
    data_list = []
    list_row_colors = []
    if 'passes' in data_req:
        for i, elem in enumerate(data_req['passes']):
            if elem['personalData'] == 1:
                list_row_colors.append((i, 'pink'))
            else:
                list_row_colors.append((i, 'light blue'))
            sub_list = [shift(elem['visitor'], length_), shift(re.sub(pattern, repl, elem['company']), length_),
                        elem['passport']]
            data_list.append(sub_list)
    else:
        data_list, list_row_colors = [['Ошибка доступа', '', '']], [(0, 'pink')]

    return data_list, list_row_colors


def main():
    length = (length_col_1 + length_col_2) / 2
    try:
        request = requests.get(url)
    except requests.exceptions.ConnectionError:
        request = ''
    try:
        data = json.loads(request.text)
    except json.decoder.JSONDecodeError:
        data = {'passes': [{'visitor': 'Ошибка формата данных',
                            'company': '', 'passport': '', 'personalData': 1}],
                'success': 1}
    except AttributeError:
        data = {'passes': [{'visitor': 'Ошибка соединения',
                            'company': '', 'passport': '', 'personalData': 1}],
                'success': 1}

    sg.theme('Light Blue')

    data_table, row_colors = data_from_req(data, length)

    headings = ['      Посетители      ', '       Компания       ', ' Удостоверение ']
    size = font_size
    size_row = round(font_size * 3)

    layout = [[sg.Table(values=data_table, headings=headings,
                        max_col_width=max(length_col_1, length_col_2),
                        row_colors=row_colors,
                        font=('Calibri', size),
                        background_color='light blue',
                        auto_size_columns=False,
                        justification='centre',
                        col_widths=[length_col_1, length_col_2, length_col_3],
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
            data = {'passes': [{'visitor': 'Ошибка формата данных',
                                'company': '', 'passport': '', 'personalData': 1}],
                    'success': 1}
        except AttributeError:
            data = {'passes': [{'visitor': 'Ошибка соединения',
                                'company': '', 'passport': '', 'personalData': 1}],
                    'success': 1}

        sg.theme('Light Blue')
        if data != pre_data:
            data_table, row_colors = data_from_req(data, length)
            window['-TABLE-'].update(values=data_table, row_colors=row_colors)
        if event == sg.WIN_CLOSED:
            break
        elif event == sg.TIMEOUT_KEY:
            window.refresh()

    window.close()


if __name__ == '__main__':
    main()
