import tiletool
import pygame  # Импортируем модуль Pygame

pygame.init()  # Инициализируем инструментарий Pygame
window = pygame.display.set_mode((700, 640))  # Создаем окно шириной 700 и высотой 640
Box = tiletool.TileTool((7, 5), 120, 120, fill=1)
Box.fill_dict((1, 0), ('Cell.png', 'Empty'))

while True:  # Бесконечный цикл, в котором будет "жить" игра
    window.fill((0, 0, 0))
    Box.blit_tiles(window)
    for i in pygame.event.get():  # Перебираем все события, происходящие в окне
        if i.type == pygame.QUIT:  # Если событие совпадаем с "закрытием окна", то есть нажатием на крестик
            pygame.quit()  # Выходим из Pygame
    pygame.display.update()  # Обновляем экран

# Cоздаём первый объект TileTool с шириной в 7 и высотой 5 тайлов
# в координатах x=120 и y=120 с включенной заливкой
# Необязательный параметр fill принимая значение 1, заполняет весь создаваемый прямоугольник плитками,мии
# значение fill=0, оставляет внутреннее пространство пустым

# К созданному объекту Box применяем метод fill_dict, связывая таким образом
# элементы созданной матрицы с графическими файлами тайлов

