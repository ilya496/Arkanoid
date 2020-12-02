import pygame as pg, game_model

text = pg.font.match_font('Arial')
f = pg.font.Font(text, 24)


def draw(screen, fps):
    screen.fill([0, 0, 0])

    for j in game_model.blocks:
        k = f.render(str(j['hp']), True, [255, 255, 255])
        pg.draw.rect(screen, [201, 0, 17], j['rect'], 0)
        screen.blit(k, j['rect'].center)

    # Рисуем шарик
    pg.draw.circle(screen, [255, 221, 0], game_model.circle.center, game_model.circle_radius)
    pg.draw.rect(screen, [0,0,255], game_model.circle, 1)
    pg.draw.rect(screen, [0, 195, 4], game_model.platform)
    f1 = f.render('SCORE: ' + str(game_model.score), True, [255, 255, 255])
    fps = f.render('FPS: ' + str(fps), True, [255, 255, 255])
    screen.blit(f1, [25, 25])
    screen.blit(fps, [875, 35])
    pg.display.flip()


def pause(screen):
    screen.fill([0, 0, 0])
    pause = f.render('Game is paused. Press escape to resume', True, [255, 255, 255])
    screen.blit(pause, [300, 450])
    pg.display.flip()
