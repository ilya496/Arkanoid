import pygame as pg, settings

pg.init()
import game, menu

screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
screen_mode = 'menu'
while True:
    m = menu.menu(screen)
    g = game.game(screen)
    if screen_mode == 'game':
        if g == 'menu':
            screen_mode = 'menu'
    if screen_mode == 'menu':
        if m == 'Easy' or m == 'Medium' or m == 'Hard' or g == 'game':
            game.restart(m)
            screen_mode = 'game'
