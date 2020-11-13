import pygame as pg, settings
clock = pg.time.Clock()
text = pg.font.match_font('Arial')
f = pg.font.Font(text, 24)

def menu(screen):
    clock.tick(100)
    b = pg.event.get()

    screen.fill([0, 0, 0])
    fps = f.render('FPS: ' + str(round(clock.get_fps())), True, [255, 255, 255])
    screen.blit(fps, [875, 35])
    start_game = f.render('Press space to start', True, [255,255,255])
    screen.blit(start_game, [420,485])
    pg.display.flip()