import pygame
import tiletool

pygame.init()
window = pygame.display.set_mode((1000, 740))  # creating the window(создаем окно)

Box = tiletool.TileTool((7, 5), 100, 120, fill=0)  # Создаем платформу
Box.fill_dict((1, 0), ('Cell.png', 'Empty'))  # Связываем графические файл и платформой.
# Файл platform.png должен содержать изображения тайла и лежать в папке с проектом

while True:
    window.fill((0, 0, 0))  # Заливаем окно черным для очистки следа от движущегося объекта
    Box.blit_tiles(window)  # Отображаем платформу на экране
    Box.moving_tile((300, 200), 1, 500, 'HORIZONTAL', window)  # Заставляем платформу двигаться
    # Box.moving_tile((200, 100), 1, 300, 'VERTICAL', window)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
