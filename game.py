import pygame as pg, settings, math

clock = pg.time.Clock()
r = pg.Rect(settings.SCREENX / 2, settings.SCREENY / 2, 40, 40)
l = []
step = 20
speedx = 0
speedy = 0
p = pg.Rect(0, 700, 300, 50)
score = 0
pg.key.set_repeat(50)
text = pg.font.match_font('Arial')
f = pg.font.Font(text, 24)
speed = 10


def ballhit(width, point):
    percent = point / width * 2
    percent = min(1, percent)
    angle = 90 - percent * 80
    print(angle)
    return angle


def angle(speedx, speedy, angle):
    speed = math.sqrt(speedx ** 2 + speedy ** 2)
    speedx = math.cos(math.radians(angle)) * speed
    speedy = math.sqrt(speed ** 2 - speedx ** 2)
    return round(speedx), round(speedy)


def restart(game_mode):
    global speedx, speedy, score, speed

    r.centerx = settings.SCREENX / 2
    r.centery = settings.SCREENY / 2
    l.clear()
    score = 0
    p.centerx = 600
    p.centery = 700

    if game_mode == 'Easy':
        speedx, speedy = angle(0, 10, 90)
        for i in range(settings.SCREENX // 50):
            l.append(pg.Rect(i * 50, 100, 49, 50))

    if game_mode == 'Medium':
        speedx = 11
        speedy = 11
        for j in range(2):
            for i in range(int(settings.SCREENX / 50)):
                l.append(pg.Rect(i * 50, 100 + j * 51, 49, 50))

    if game_mode == 'Hard':
        speedx = 10
        speedy = 10
        for j in range(5):
            for i in range(int(settings.SCREENX / 50)):
                l.append(pg.Rect(i * 50, 100 + j * 51, 49, 50))

def start_position(rect, circle):
    pressed = pg.mouse.get_pressed()
    if pressed[2]:
        click = 3
    else:
        circle.centerx = rect.centerx
        circle.bottom = rect.top
        click = 0
    return click


def game(screen):
    global score, speedy, speedx
    clock.tick(100)
    b = pg.event.get()

    # Отражении от верхних блоков
    t1 = r.collidelist(l)
    if t1 != -1:
        score += 1
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
        return 'menu'
    if r.bottom >= settings.SCREENY:
        print('You lose!')
        return 'menu'

    # Управление платформой
    a = 0
    for i in b:
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEMOTION:
            p.centerx = i.pos[0]
        if i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE:
            print(1)
            pause = f.render('Game is paused', True, [255, 255, 255])
            screen.blit(pause, [380, 200])
            a += 1
            return 'menu'
        if a == 2:
            a = 0
            return 'game'

    # Движение шарика
    r.right += speedx

    if r.right >= settings.SCREENX:
        r.right = settings.SCREENX
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

    r.top += speedy
    t = r.colliderect(p)

    if r.top <= 0:
        r.top = 0
        speedy = -speedy
    elif r.bottom >= settings.SCREENY:
        r.bottom = settings.SCREENY
        speedy = -speedy

    t = r.colliderect(p)

    if t == 1:
        if r.centery < p.top:
            r.bottom = p.top
            sx, sy = angle(speedx, speedy, ballhit(p.width, abs(p.centerx - r.centerx)))
            speedy = -sy
            if p.centerx - r.centerx < 0:
                speedx = sx
            else:
                speedx = -sx

        elif r.centery > p.bottom:
            r.top = p.bottom
            speedy = -speedy

    # Рисуем кадры
    screen.fill([0, 0, 0])
    for j in l:
        pg.draw.rect(screen, [201, 0, 17], j, 0)
    pg.draw.circle(screen, [255, 221, 0], r.center, 20)
    pg.draw.rect(screen, [0, 195, 4], p)
    f1 = f.render('SCORE: ' + str(score), True, [255, 255, 255])
    fps = f.render('FPS: ' + str(round(clock.get_fps())), True, [255, 255, 255])
    screen.blit(f1, [25, 25])
    screen.blit(fps, [875, 35])
    pg.display.flip()
