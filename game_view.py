import pygame as pg, game_model

# Создание шрифта
text = pg.font.match_font('Arial')
f = pg.font.Font(text, 24)

def draw(screen, fps):
    # Цвет фона игры
    screen.fill([0, 0, 0])

    # Надпись ХП у верхних блоков и сами блоки
    for j in game_model.blocks:
        j.draw(screen, [255, 0, 0])
        j.draw_hp(screen)

    # Отрисовка шарика
    pg.draw.circle(screen, [255, 221, 0], game_model.circle.center, game_model.circle_radius)
    pg.draw.rect(screen, [0, 0, 255], game_model.circle, 1)

    # Отрисовка платформы
    pg.draw.rect(screen, [0, 195, 4], game_model.platform)

    # Разные надписи и текста
    score_text = f.render('SCORE: ' + str(game_model.score), True, [255, 255, 255])
    fps = f.render('FPS: ' + str(fps), True, [255, 255, 255])
    hp = f.render('HP: ' + str(game_model.player_hp), True, [255, 255, 255])
    screen.blit(hp, [25, 600])
    screen.blit(score_text, [25, 25])
    screen.blit(fps, [875, 25])

    # Обновление дисплея
    pg.display.flip()


def pause(screen):
    # Цвет фона экрана паузы
    screen.fill([0, 0, 0])

    # Отрисовка текста паузы
    pause = f.render('Game is paused. Press escape to resume', True, [255, 255, 255])
    screen.blit(pause, [300, 450])

    # Обновление дисплея
    pg.display.flip()
