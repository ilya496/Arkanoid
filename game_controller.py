import pygame as pg, game_model

pause_mode = False


def process_events():
    global pause_mode
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

        if i.type == pg.MOUSEMOTION:
            game_model.set_platform(i.pos[0])

        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                game_model.fire()

        if i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
            pause_mode = not pause_mode
    return pause_mode



