with open('file.txt', encoding='utf-8') as f,\
       open('new_file.txt', 'w', encoding='utf-8') as new_f:
    for i in f:
        string = i[10:14]
        new_f.write(f'{string}\n')
