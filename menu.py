import pygame as pg

clock = pg.time.Clock()
text = pg.font.match_font('Arial')
f = pg.font.Font(text, 24)
f1 = pg.font.Font(text, 36)
game_mode = 'easy'


def menu(screen):
    clock.tick(100)

    # Контур кнопок
    rmode1 = pg.Rect(430, 387, 200, 50)
    rmode2 = pg.Rect(430, 487, 200, 50)
    rmode3 = pg.Rect(430, 587, 200, 50)

    # Проверка на события
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if rmode1.collidepoint(pg.mouse.get_pos()):
                game_mode = 'easy'
                return game_mode
            elif rmode2.collidepoint(pg.mouse.get_pos()):
                game_mode = 'medium'
                return game_mode
            elif rmode3.collidepoint(pg.mouse.get_pos()):
                game_mode = "hard"
                return game_mode

    # Цвет фона меню
    screen.fill([0, 0, 0])

    # FPS
    fps = f.render('FPS: ' + str(round(clock.get_fps())), True, [255, 255, 255])
    screen.blit(fps, [875, 35])

    # Отрисовка кнопок
    pg.draw.rect(screen, [255, 0, 0], rmode1, 1)
    pg.draw.rect(screen, [255, 0, 0], rmode2, 1)
    pg.draw.rect(screen, [255, 0, 0], rmode3, 1)
    mode1 = f.render('Easy mode', True, [255, 255, 255])
    mode2 = f.render('Medium mode', True, [255, 255, 255])
    mode3 = f.render('Hard mode', True, [255, 255, 255])
    screen.blit(mode1, [470, 400])
    screen.blit(mode2, [450, 500])
    screen.blit(mode3, [470, 600])

    # Обновление дисплея
    pg.display.flip()
