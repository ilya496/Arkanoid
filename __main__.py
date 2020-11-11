import pygame as pg, settings
pg.init()
import game
screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
pg.key.set_repeat(50)
while True:
    game.game(screen)