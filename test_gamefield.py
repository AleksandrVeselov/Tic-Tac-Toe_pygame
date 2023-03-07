import random

import pygame
import sys


def comp_move(field: list) -> None:
    """
    Функция для хода компьютера
    :param field: игровое поле: массив чисел 0, 1, 2
    :return: ничего не возвращает, записывает в случайную пустую клетку на игровом поле значение 2
    """
    res = 1
    while res != 0:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        res = field[row][column]
    field[row][column] = 2


pygame.init()

size = (510, 510)  # Размер игрового окна
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TicTacToe game')
width = height = 40  # Размеры прямоугольника
red = (255, 0, 0)  # Цвет прямоугольника
white = (255, 255, 255)
green = (0, 128, 0)
margin = 10  # Отступ прямоугольника
mas = [[0] * 10 for i in range(10)]

# Цикл обработки событий
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x={x_mouse} y={y_mouse}')
            column = x_mouse // (margin + width)
            row = y_mouse // (margin + height)
            mas[row][column] = 1
            comp_move(mas)
            print(*mas, sep='\n')


    # Отрисовка игрового поля
    for row in range(10):
        for col in range(10):
            if mas[row][col] == 1:
                color = red
            elif mas[row][col] == 2:
                color = green
            else:
                color = white
            x = col * width + (col + 1) * margin  # Координата х
            y = row * height + (row + 1) * margin  # Координата у
            pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.display.update()  # Обновление экрана



