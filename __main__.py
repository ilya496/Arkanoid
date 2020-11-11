import pygame as pg, os

os.environ['SDL_VIDEODRIVER'] = 'directx'
pg.init()
screenx = 1000
screeny = 1000
SCORE = 0
step = 20
speedx = 8
speedy = 8
p = pg.Rect(500, 700, 300, 50)
r = pg.Rect(screenx/2, screeny/2, 40, 40)
clock = pg.time.Clock()
l = []
text = pg.font.match_font('Arial')
f = pg.font.Font(text, 28)
print('Choose your game mode. Easy, Medium, Hard')
game_mode = 'Easy'#input()
screen = pg.display.set_mode([screenx, screeny])

if game_mode == 'Easy':
    speedx = 6
    speedy = 6
    step = 14
    for i in range(screenx//50):
        l.append(pg.Rect(i * 50, 100, 49, 50))

if game_mode == 'Medium':
    speedx = 11
    speedy = 11
    step = 17
    for i in range(screenx//50):
        l.append(pg.Rect(i * 50, 100, 49, 50))
    for i in range(screenx//50):
        l.append(pg.Rect(i * 50, 151, 49, 50))

if game_mode == 'Hard':
    speedx = 14
    speedy = 14
    step = 20
    for i in range(int(screenx / 50)):
        l.append(pg.Rect(i * 50, 100, 49, 50))
    for i in range(int(screenx / 50)):
        l.append(pg.Rect(i * 50, 151, 49, 50))
pg.key.set_repeat(50)
while True:
    clock.tick(100)
    b = pg.event.get()

    # Отражении от верхних блоков
    t1 = r.collidelist(l)
    if t1 != -1:
        SCORE += 1
        print(SCORE)
        if r.centery < l[t1].top:
            r.bottom = l[t1].top
            speedy = -speedy
            l.pop(t1)
            t1 = r.collidelist(l)

        elif r.centery > l[t1].bottom:
            r.top = l[t1].bottom
            speedy = -speedy
            l.pop(t1)
            t1 = r.collidelist(l)

        elif r.centerx < l[t1].left:
            r.right = l[t1].left
            speedx = -speedx
            l.pop(t1)
            t1 = r.collidelist(l)

        elif r.centerx > l[t1].right:
            r.left = l[t1].right
            speedx = -speedx
            l.pop(t1)

    # Управление окном
    if len(l) == 0:
        print('You win!')
        break
    # if r.bottom >= screeny:
    #     print('You lose!')
    #     break

    # Управление платформой
    t = r.colliderect(p)

    for i in b:
        if i.type == pg.QUIT:
            exit()
        # if i.type == pg.KEYDOWN and i.key == pg.K_RIGHT:
        #     p.right += step
        #     t = r.colliderect(p)
        #     if t == 1:
        #         r.left = p.right
        #
        # if i.type == pg.KEYDOWN and i.key == pg.K_LEFT:
        #     p.left -= step
        #     t = r.colliderect(p)
        #     if t == 1:
        #         r.right = p.left
        #
        # if i.type == pg.KEYDOWN and i.key == pg.K_UP:
        #     p.bottom -= step
        #     t = r.colliderect(p)
        #     if t == 1:
        #         r.bottom = p.top
        if i.type == pg.MOUSEMOTION:
            print(i)
            p.centerx = i.pos[0]

        if i.type == pg.KEYDOWN and i.key == pg.K_DOWN:
            p.top += step
            t = r.colliderect(p)
            if t == 1:
                r.top = p.bottom

    # Движение прямоугльника
    r.right += speedx
    t = r.colliderect(p)

    if r.right >= screenx:
        r.right = screenx
        speedx = -speedx
    elif r.left <= 0:
        r.left = 0
        speedx = -speedx

    t = r.colliderect(p)

    if t == 1:
        if r.centerx < p.left:
            r.right = p.left
            speedx = -speedx
            t = r.colliderect(p)

        elif r.centerx > p.right:
            r.left = p.right
            speedx = -speedx
            t = r.colliderect(p)

    r.top += speedy
    t = r.colliderect(p)

    if r.top <= 0:
        r.top = 0
        speedy = -speedy
    elif r.bottom >= screeny:
        r.bottom = screeny
        speedy = -speedy

    t = r.colliderect(p)

    if t == 1:
        if r.centery < p.top:
            r.bottom = p.top
            speedy = -speedy
            t = r.colliderect(p)

        elif r.centery > p.bottom:
            r.top = p.bottom
            speedy = -speedy
            t = r.colliderect(p)

    # Рисуем кадры
    screen.fill([0, 0, 0])
    for j in l:
        pg.draw.rect(screen, [201, 0, 17], j, 0)
    pg.draw.circle(screen, [255, 221, 0], r.center, 20)
    pg.draw.rect(screen, [0, 195, 4], p)
    f1 = f.render('score: '+str(SCORE), True, [255,255,255])
    fps = f.render('FPS: '+str(clock.get_fps()), True, [255,255,255])
    screen.blit(f1, [100,100])
    screen.blit(fps, [850,100])
    pg.display.flip()