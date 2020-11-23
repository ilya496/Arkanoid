import pygame as pg, settings, math

score = 0
circle = pg.Rect(settings.SCREENX / 2, settings.SCREENY / 2, 40, 40)
platform = pg.Rect(0, 700, 300, 50)
blocks = []

speedx = 0
speedy = 0


def restart(game_mode):
    global speedx, speedy, score

    circle.centerx = settings.SCREENX / 2
    circle.centery = settings.SCREENY / 2
    blocks.clear()
    score = 0
    platform.centerx = 600
    platform.centery = 700

    if game_mode == 'Easy':
        speedx, speedy = angle(0, 10, 90)
        for i in range(settings.SCREENX // 50):
            blocks.append(pg.Rect(i * 50, 100, 49, 50))

    if game_mode == 'Medium':
        speedx = 11
        speedy = 11
        for j in range(2):
            for i in range(int(settings.SCREENX / 50)):
                blocks.append(pg.Rect(i * 50, 100 + j * 51, 49, 50))

    if game_mode == 'Hard':
        speedx = 14
        speedy = 14
        for j in range(3):
            for i in range(int(settings.SCREENX / 50)):
                blocks.append(pg.Rect(i * 50, 100 + j * 51, 49, 50))


def set_platform(x_position):
    platform.centerx = x_position


def game_finish():
    if len(blocks) == 0:
        return True
    elif circle.bottom >= settings.SCREENY:
        return True
    return False


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


def step():
    global speedy, speedx, score

    circle.right += speedx

    if circle.right >= settings.SCREENX:
        circle.right = settings.SCREENX
        speedx = -speedx
    elif circle.left <= 0:
        circle.left = 0
        speedx = -speedx

    t = circle.colliderect(platform)

    if t == 1:
        if circle.centerx < platform.left:
            circle.right = platform.left
            speedx = -speedx
            t = circle.colliderect(platform)

        elif circle.centerx > platform.right:
            circle.left = platform.right
            speedx = -speedx

    circle.top += speedy
    t = circle.colliderect(platform)

    if circle.top <= 0:
        circle.top = 0
        speedy = -speedy
    elif circle.bottom >= settings.SCREENY:
        circle.bottom = settings.SCREENY
        speedy = -speedy

    t = circle.colliderect(platform)

    if t == 1:
        if circle.centery < platform.top:
            circle.bottom = platform.top
            sx, sy = angle(speedx, speedy, ballhit(platform.width, abs(platform.centerx - circle.centerx)))
            speedy = -sy
            if platform.centerx - circle.centerx < 0:
                speedx = sx
            else:
                speedx = -sx

        elif circle.centery > platform.bottom:
            circle.top = platform.bottom
            speedy = -speedy

    # Отражении от верхних блоков
    t1 = circle.collidelist(blocks)
    if t1 != -1:
        score += 1
        if circle.centery < blocks[t1].top:
            circle.bottom = blocks[t1].top
            speedy = -speedy
            blocks.pop(t1)
            t1 = circle.collidelist(blocks)

        elif circle.centery > blocks[t1].bottom:
            circle.top = blocks[t1].bottom
            speedy = -speedy
            blocks.pop(t1)
            t1 = circle.collidelist(blocks)

        elif circle.centerx < blocks[t1].left:
            circle.right = blocks[t1].left
            speedx = -speedx
            blocks.pop(t1)
            t1 = circle.collidelist(blocks)

        elif circle.centerx > blocks[t1].right:
            circle.left = blocks[t1].right
            speedx = -speedx
            blocks.pop(t1)
