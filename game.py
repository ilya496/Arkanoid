import pygame as pg, settings, game_view, game_model, game_controller

clock = pg.time.Clock()




# def start_position(rect, circle):
#     pressed = pg.mouse.get_pressed()
#     if pressed[2]:
#         click = 3
#     else:
#         circle.centerx = rect.centerx
#         circle.bottom = rect.top
#         click = 0
#     return click

def restart(game_mode):
    game_model.restart(game_mode)

def game(screen):
    global score, speedy, speedx
    clock.tick(100)
    game_controller.process_events()
    game_model.step()


    # Управление окном
    if game_model.game_finish():
        return 'menu'

    game_view.draw(screen,round(clock.get_fps()))
