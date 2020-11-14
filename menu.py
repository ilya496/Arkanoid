import pygame as pg, settings

clock = pg.time.Clock()
text = pg.font.match_font('Arial')
f = pg.font.Font(text, 24)
f1 = pg.font.Font(text, 36)
game_mode = 'Easy'

def menu(screen):
    clock.tick(100)
    pg.event.get()
    screen_mode = ''
    # Конутр кнопок
    rmode1 = pg.Rect(430, 387, 200, 50)
    rmode2 = pg.Rect(430, 487, 200, 50)
    rmode3 = pg.Rect(430, 587, 200, 50)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # if i.type == pg.KEYDOWN and i.key == pg.K_SPACE:
        #     screen_mode = 'game'
        if i.type == pg.MOUSEBUTTONDOWN:
            if rmode1.collidepoint(pg.mouse.get_pos()):
                game_mode = 'Easy'
                return game_mode
            elif rmode2.collidepoint(pg.mouse.get_pos()):
                game_mode = 'Medium'
                return game_mode
            elif rmode3.collidepoint(pg.mouse.get_pos()):
                game_mode = "Hard"
                return game_mode

    screen.fill([0, 0, 0])
    fps = f.render('FPS: ' + str(round(clock.get_fps())), True, [255, 255, 255])
    screen.blit(fps, [875, 35])
    start_game = f1.render('Press space to start', True, [255, 255, 255])
    screen.blit(start_game, [380, 250])
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

    pg.display.flip()
    return screen_mode
