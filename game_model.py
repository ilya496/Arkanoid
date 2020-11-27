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
        #speedx, speedy = angle(0, 10, 90)
        for i in range(settings.SCREENX // 50):
            b = {
                'hp': 1,
                'rect': pg.Rect(i * 50, 100, 49, 50)
            }
            blocks.append(b)


    if game_mode == 'Medium':
        # speedx, speedy = angle(2, 13, 90)
        for j in range(2):
            for i in range(int(settings.SCREENX / 50)):
                b = {
                    'hp': 3,
                    'rect': pg.Rect(i * 50, 100 + j * 51, 49, 50)
                }
                blocks.append(b)

    if game_mode == 'Hard':
        # speedx, speedy = angle(4, 15, 90)
        for j in range(3):
            for i in range(int(settings.SCREENX / 50)):
                b = {
                    'hp': 3,
                    'rect': pg.Rect(i * 50, 100 + j * 51, 49, 50)
                }
                blocks.append(b)


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


def get_rects_from_blocks(blocks):
    l = []
    for i in blocks:
        l.append(i['rect'])
    return l


def hit_block(blocks, index):
    global score

    blocks[index]['hp'] -= 1
    if blocks[index]['hp'] <= 0:
        score += 1
        blocks.pop(index)


def step(mouse_clicked):
    global speedy, speedx, score

    if mouse_clicked == 2:
        speedx, speedy = angle(0, 10, 90)

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
    blocks_rects = get_rects_from_blocks(blocks)
    t1 = circle.collidelist(blocks_rects)
    if t1 != -1:
        if circle.centery < blocks_rects[t1].top:
            circle.bottom = blocks_rects[t1].top
            speedy = -speedy
            hit_block(blocks, t1)

        elif circle.centery > blocks_rects[t1].bottom:
            circle.top = blocks_rects[t1].bottom
            speedy = -speedy
            hit_block(blocks, t1)

        elif circle.centerx < blocks_rects[t1].left:
            circle.right = blocks_rects[t1].left
            speedx = -speedx
            hit_block(blocks, t1)

        elif circle.centerx > blocks_rects[t1].right:
            circle.left = blocks_rects[t1].right
            speedx = -speedx
            hit_block(blocks, t1)
