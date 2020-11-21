import pygame as pg, game_model


text = pg.font.match_font('Arial')
f = pg.font.Font(text, 24)

def draw(screen,fps):
    screen.fill([0, 0, 0])

    for j in game_model.blocks:
        pg.draw.rect(screen, [201, 0, 17], j, 0)

    #Рисуем шарик
    pg.draw.circle(screen, [255, 221, 0], game_model.circle.center, 20)

    pg.draw.rect(screen, [0, 195, 4], game_model.platform)
    f1 = f.render('SCORE: ' + str(game_model.score), True, [255, 255, 255])
    fps = f.render('FPS: ' + str(fps), True, [255, 255, 255])
    pause = f.render('Game is paused', True, [255, 255, 255])
    screen.blit(f1, [25, 25])
    screen.blit(fps, [875, 35])
    screen.blit(pause, [380, 200])
    pg.display.flip()