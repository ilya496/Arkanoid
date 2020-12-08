import pygame as pg, game_view, game_model, game_controller

clock = pg.time.Clock()


def restart(game_mode):
    #TODO все строки этой функции обращаются к модели. Ей явно место в game_model.
    # Только модель знает, как правильно перезапустить игру.
    game_model.restart_blocks(game_mode)
    game_model.restart_player_settings()
    game_model.restart_position()
    game_model.restart_speed_and_angle(game_mode)

def game(screen):
    global score, speedy, speedx
    clock.tick(100)
    pause_mode = game_controller.process_events()

    if pause_mode:
        game_view.pause(screen)
        return ''
    else:
        game_model.step()
        game_view.draw(screen, round(clock.get_fps()))
        if game_model.game_finish():
            return 'menu'
