import pygame as pg, game_view, game_model, game_controller

clock = pg.time.Clock()


def restart(game_mode):
    # Перезапуск всей игры
    game_model.restart_all(game_mode)


def game(screen):
    global score, speedy, speedx
    clock.tick(100)
    pause_mode = game_controller.process_events()

    # Проверка на паузу
    if pause_mode:
        game_view.pause(screen)
        return ''
    else:
        game_model.step()
        game_view.draw(screen, round(clock.get_fps()))
        if game_model.game_finish():
            return 'menu'
