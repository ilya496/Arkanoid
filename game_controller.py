import pygame as pg, game_model

pause_mode = False
mouse_clicked = 0

def pause():
    global pause_mode

    for i in pg.event.get():
        if i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
            pause_mode = not pause_mode
    return pause_mode


def process_events():
    global mouse_clicked
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

        if i.type == pg.MOUSEMOTION:
            game_model.set_platform(i.pos[0])
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                mouse_clicked += 1
            return mouse_clicked


