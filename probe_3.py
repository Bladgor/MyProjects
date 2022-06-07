
product_list = []

pos_num = int(input("Введите количество позиций: "))
str_num = 1

while pos_num > 0:
    product_list.append((str_num, {
        "название": input(f"Введите название товара №{str_num}: "),
        "цена": int(input(f"Введите цену товара №{str_num}: ")),
        "количество": int(input(f"Введите количество товара №{str_num}: ")),
        "ед": input(f"Введите единицу измерения товара №{str_num}: ")
    }))
    pos_num -= 1
    str_num +=1

print(product_list)
