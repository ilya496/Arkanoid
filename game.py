import pygame as pg, game_view, game_model, game_controller

clock = pg.time.Clock()

def restart(game_mode):
    game_model.restart(game_mode)


def game(screen):
    global score, speedy, speedx
    clock.tick(100)
    j = game_controller.process_events()

    if j:
        game_view.pause(screen)
        return ''
    else:
        game_model.step()
        game_view.draw(screen, round(clock.get_fps()))
        if game_model.game_finish():
            return 'menu'
