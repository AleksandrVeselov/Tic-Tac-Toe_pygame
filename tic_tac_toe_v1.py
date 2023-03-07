import pygame
import sys
import utils


pygame.init()  # Инициализация модуля pygame

SIZE_BLOCK = 100  # размер одного блока
MARGIN = 15  # отступ
WIDTH = HEIGHT = SIZE_BLOCK * 3 + MARGIN * 4

# цвета для блоков
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)

game_filed = [[0] * 3 for _ in range(3)]  # массив с цифрами

size_window = (WIDTH, HEIGHT)  # размеры игрового окна
screen = pygame.display.set_mode(size_window)  # создание объекта экран с нужными размерами
pygame.display.set_caption('Крестики-нолики версия_1')  # заголовок окна
winner = None

while True:
    # обработка событий клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
            x_mouse, y_mouse = pygame.mouse.get_pos()  # Получение координат клика мышки
            col = x_mouse // (SIZE_BLOCK + MARGIN)
            row = y_mouse // (SIZE_BLOCK + MARGIN)

            # Проверка свободна ли клетка. Если да, записать на игровое поле 1
            if utils.is_space_free(game_filed, (row, col)):
                game_filed[row][col] = 1

                # Проверка на выигрыш игрока
                if utils.is_winner(game_filed, 1):
                    # print(*game_filed, sep='\n')
                    game_over = True
                    winner = 'x'

                # Проверка на ничью
                elif utils.is_board_full(game_filed):
                    game_over = True
                    winner = 'Ничья'

                if not winner:
                    # Передача хода компьютеру
                    comp_move = utils.computer_move(game_filed)  # Просчет хода компьютера
                    utils.make_move(game_filed, 2, comp_move)  # Запись хода на игровое поле

                    # Проверка на выигрыш компьютера
                    if utils.is_winner(game_filed, 2):
                        # print(*game_filed, sep='\n')
                        game_over = True
                        winner = 'O'

                    # проверка на ничью
                    elif utils.is_board_full(game_filed):
                        game_over = True
                        winner = 'Ничья'

        # По клавише пробел перезапуск игры
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            winner = None
            game_filed = [[0] * 3 for _ in range(3)]  # массив с цифрами
            screen.fill(BLACK)

    if not winner:
        # отрисовка игрового поля
        for row in range(3):
            for col in range(3):
                if game_filed[row][col] == 1:
                    color = RED
                elif game_filed[row][col] == 2:
                    color = GREEN
                else:
                    color = WHITE
                x = col * SIZE_BLOCK + (col + 1) * MARGIN  # координата х для блока
                y = row * SIZE_BLOCK + (row + 1) * MARGIN  # координата у для блока
                pygame.draw.rect(screen, color, (x, y, SIZE_BLOCK, SIZE_BLOCK))  # отрисовка прямоугольника

                # Если цвет ячейки игрового поля красный, рисуется крестик
                if color == RED:
                    pygame.draw.line(screen, BLACK, (x + 20, y + 20), (x + SIZE_BLOCK - 20, y + SIZE_BLOCK - 20), 10)
                    pygame.draw.line(screen, BLACK, (x + SIZE_BLOCK - 20, y + 20), (x + 20, y + SIZE_BLOCK - 20), 10)

                # Если цвет ячейки игрового поля зеленый, рисуется нолик
                elif color == GREEN:
                    pygame.draw.circle(screen, BLACK, (x + SIZE_BLOCK // 2, y + SIZE_BLOCK // 2), SIZE_BLOCK // 2 - 10, 7)

    # Если игра закончена отображение текста
    if winner:
        screen.fill(BLACK)

        # Шрифты для вывода на экран
        font = pygame.font.SysFont(name='stxingkai', size=80)
        font1 = pygame.font.SysFont(name='stxingkai', size=25)

        # Тексты для вывода на экран
        text1 = font.render(winner, True, WHITE)
        text2 = font.render('победил', True, WHITE)
        text3 = font1.render('Нажмите "Пробел" для перезапуска', True, WHITE)

        text_rect_1 = text1.get_rect()
        text_rect_2 = text2.get_rect()
        text_rect_3 = text3.get_rect()

        # Координаты отрисовки текста
        text1_x = screen.get_width() / 2 - text_rect_1.width / 2
        text1_y = screen.get_height() / 2 - text_rect_1.height / 2 - 70
        text2_x = screen.get_width() / 2 - text_rect_2.width / 2
        text2_y = screen.get_width() / 2 - text_rect_2.width / 2 + 90
        text3_x = screen.get_width() / 2 - text_rect_3.width / 2
        text3_y = screen.get_width() / 2 - text_rect_3.width / 2 + 200

        screen.blit(text1, [text1_x, text1_y])
        screen.blit(text2, [text2_x, text2_y])
        screen.blit(text3, [text3_x, text3_y])

    pygame.display.update()  # обновление экрана и отображение на нем игрового поля



