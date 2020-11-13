import pygame as pg, settings
pg.init()
import game, menu
screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
screen_mode = 'menu'
pg.key.set_repeat(50)
while True:
    b = pg.event.get()

    if screen_mode == 'game':
        game.game(screen)
    if screen_mode == 'menu':
        menu.menu(screen)
        for i in b:
            if i.type == pg.KEYDOWN and i.key == pg.K_SPACE:
                screen_mode = 'game' 