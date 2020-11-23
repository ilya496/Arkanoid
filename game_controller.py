import pygame as pg, game_model

a = 0


def process_events():
    a = 0
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

        if i.type == pg.MOUSEMOTION:
            game_model.set_platform(i.pos[0])

        if i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
            a += 1
        if a == 1:
           return 'pause'
        elif a == 2:
            a = 0
            return 'pause_stop'


