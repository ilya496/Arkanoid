import pygame as pg, game_model


def process_events():
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

        if i.type == pg.MOUSEMOTION:
            game_model.set_platform(i.pos[0])
