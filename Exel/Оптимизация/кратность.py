my_string = 'НАП.СПИРТНОЙ ДЖИМ БИМ ХАНИ 32.5% 24X0.2Л'

print(my_string.find('X'))
search_x = my_string.find('X')

quant = int(my_string[(search_x - 2):search_x])
print(quant)
print(type(quant))

index = search_x
while my_string[index] != ' ':
    index -= 1

print(my_string[index + 1: search_x])
print(len(my_string[index + 1: search_x]))
