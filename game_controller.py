import pygame as pg, game_model

# Ставим изначальный режим паузы
pause_mode = False


def process_events():
    global pause_mode

    # Перебор элементов в событиях игры
    for i in pg.event.get():

        # Проверка на закрытие окна
        if i.type == pg.QUIT:
            exit()

        # Проверка на перемещение мышки
        if i.type == pg.MOUSEMOTION:
            game_model.set_platform(i.pos[0])

        # Проверка на нажатие мышки
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                game_model.fire()

        # Проверка на нажатие ESCAPE
        if i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
            pause_mode = not pause_mode

    return pause_mode
