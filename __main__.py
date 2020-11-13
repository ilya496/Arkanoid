import pygame as pg, settings
pg.init()
import game, menu
screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
screen_mode = 'menu'
pg.key.set_repeat(50) #OPTIMIZE В чем смысл этой строчки здесь?
while True:
    b = pg.event.get() #OPTIMIZE это здесь не нужно

    if screen_mode == 'game':
        game.game(screen)
    if screen_mode == 'menu':
        menu.menu(screen)
        # OPTIMIZE эта логика должна быть модуле меню.
        #  Только меню знает, что для того, чтобы начать игру, нужно нажать пробел.
        #  Чтобы модуль main об этом тоже узнал, нужно возвращать значение из menu().
        #  Для этого использую return
        for i in b:
            if i.type == pg.KEYDOWN and i.key == pg.K_SPACE:
                screen_mode = 'game'