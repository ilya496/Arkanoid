import pygame as pg, settings

pg.init()
import game, menu

screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
screen_mode = 'menu'
while True:
    if screen_mode == 'game':
        g = game.game(screen)
        if g == 'menu':
            screen_mode = 'menu'
    if screen_mode == 'menu':
        m = menu.menu(screen)
        if m == 'game' or m == 'Easy' or m == 'Medium' or m == 'Hard':
            game.restart(m)
            screen_mode = 'game'
