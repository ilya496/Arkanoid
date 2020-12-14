import pygame as pg, settings

pg.init()
import game, menu

# Создание окна
screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
screen_mode = 'menu'

while True:

    # Проверка на игру
    if screen_mode == 'game':
        g = game.game(screen)
        if g == 'menu':
            screen_mode = 'menu'

    # Проверка на меню
    if screen_mode == 'menu':
        m = menu.menu(screen)
        if m == 'easy' or m == 'medium' or m == 'hard':
            game.restart(m)
            screen_mode = 'game'
