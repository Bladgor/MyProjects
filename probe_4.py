# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

print('Введите местоположение коня:')
xHorse = float(input())
yHorse = float(input())
while xHorse < 0 or xHorse > 0.8 or yHorse < 0 or yHorse > 0.8:
    print('Клетки с такой координатой не существует. \nВведите местоположение коня:')
    xHorse = float(input())
    yHorse = float(input())

print('Введите местоположение точки на доске:')
xPoint = float(input())
yPoint = float(input())
while xPoint < 0 or xPoint > 0.8 or yPoint < 0 or yPoint > 0.8:
    print('Клетки с такой координатой не существует. \nВведите местоположение точки на доске:')
    xPoint = float(input())
    yPoint = float(input())

xHorse = int(xHorse * 10)
yHorse = int(yHorse * 10)
xPoint = int(xPoint * 10)
yPoint = int(yPoint * 10)

print('Конь в клетке (' + str(xHorse) + ', ' + str(yHorse) +
      '). Точка в клетке (' + str(xPoint) + ', ' + str(yPoint) + ').')

xDifference = abs(xHorse - xPoint)
yDifference = abs(yHorse - yPoint)

if xDifference - yDifference == 1 or xDifference - yDifference == -1:
    print('Да, конь может ходить в эту клетку.')
else:
    print('Нет, конь не может ходить в эту клетку.')
