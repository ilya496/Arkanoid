import pygame as pg, settings, math, block, json, os

score = 0
circle_radius = 25
circle = pg.Rect(settings.SCREENX / 2, settings.SCREENY / 2, circle_radius * 2, circle_radius * 2)
platform = pg.Rect(0, 700, 300, 50)
blocks = []

game_mode = 0
speedx = 0
speedy = 0
ball_flight = False
player_hp = 3
level = 1


def cross_with_objectlist(circle, list_of_objects):
    for i in list_of_objects:
        if cross_with_objectes(i, circle):
            return list_of_objects.index(i)
    return -1


def cross_with_objectes(rect1, circle_rect):
    global circle_radius

    cross = rect1.colliderect(circle_rect)

    if not cross:
        return cross

    mask1 = pg.mask.Mask(rect1.size, True)
    img_rect2 = pg.Surface(circle_rect.size, pg.SRCALPHA)
    img_rect2.fill([0, 0, 0, 0])
    pg.draw.circle(img_rect2, [255, 255, 255, 255], [circle_rect.w // 2, circle_rect.h // 2], circle_radius)
    mask2 = pg.mask.from_surface(img_rect2)

    cross2 = mask1.overlap(mask2, [circle_rect.x - rect1.x, circle_rect.y - rect1.y])
    return cross2 is not None


def fire():
    global ball_flight
    ball_flight = True


def restart_position():
    global ball_flight

    ball_flight = False
    platform.centerx = circle.centerx
    platform.centery = 850
    circle.centerx = settings.SCREENX / 2
    circle.centery = settings.SCREENY / 2


def restart_speed_and_angle(gm):
    global speedx, speedy

    if gm == 'easy':
        speedx, speedy = angle(0, 10, 90)
    elif gm == 'medium':
        speedx, speedy = angle(2, 13, 90)
    elif gm == 'hard':
        speedx, speedy = angle(4, 15, 90)


def reading_map(json_file):
    data = []
    file = open(json_file, 'r')
    data.append(json.load(file))
    return data[0]


def restart_blocks(gm):
    global speedx, speedy, game_mode, level

    blocks.clear()

    if gm == 'easy':
        maps_directory = 'easy_mode_maps'
        postfix = 'e'

    elif gm == 'medium':
        maps_directory = 'medium_mode_maps'
        postfix = 'm'

    elif gm == 'hard':
        maps_directory = 'hard_mode_maps'
        postfix = 'h'

    fullname = os.path.join(os.getcwd(), maps_directory)
    names = os.listdir(fullname)
    for name in names:
        fullname_file = os.path.join(fullname, name)
        print(fullname)
        if os.path.isfile(fullname_file):
            filename, file_extension = os.path.splitext(name)
            if file_extension == '.json' and filename == str(level) + postfix:
                list_of_dicts = reading_map(fullname_file)
                break
    else:
        return False

    for i in list_of_dicts:
        b = block.Block(i)
        blocks.append(b)

    return True

def restart_player_settings():
    global player_hp, score, level

    level = 1
    player_hp = 3
    score = 0


def restart_all(gm):
    global game_mode

    game_mode = gm

    restart_player_settings()
    restart_position()
    restart_blocks(game_mode)
    restart_speed_and_angle(game_mode)


def set_platform(x_position):
    platform.centerx = x_position


def game_finish():
    global player_hp, level

    if len(blocks) == 0:
        level += 1
        restart_speed_and_angle(game_mode)
        restart_position()

        if not restart_blocks(game_mode):
            return True

    if circle.bottom >= settings.SCREENY:
        restart_speed_and_angle(game_mode)
        restart_position()
        player_hp -= 1

    if player_hp <= 0:
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
        l.append(i.rect)
    return l


def hit_block(blocks, index):
    global score

    blocks[index].hp -= 1
    if blocks[index].hp <= 0:
        score += 1
        blocks.pop(index)


def step():
    global speedy, speedx, score
    if not ball_flight:
        return
    circle.right += speedx

    if circle.right >= settings.SCREENX:
        circle.right = settings.SCREENX
        speedx = -speedx
    elif circle.left <= 0:
        circle.left = 0
        speedx = -speedx

    t = cross_with_objectes(platform, circle)

    if t:
        if circle.centerx <= platform.left:
            circle.right = platform.left
            speedx = -speedx

        elif circle.centerx >= platform.right:
            circle.left = platform.right
            speedx = -speedx

    circle.top += speedy

    if circle.top <= 0:
        circle.top = 0
        speedy = -speedy
    elif circle.bottom >= settings.SCREENY:
        circle.bottom = settings.SCREENY
        speedy = -speedy

    t = cross_with_objectes(platform, circle)

    if t:
        if circle.centery <= platform.top:
            circle.bottom = platform.top
            sx, sy = angle(speedx, speedy, ballhit(platform.width, abs(platform.centerx - circle.centerx)))
            speedy = -sy
            if platform.centerx - circle.centerx < 0:
                speedx = sx
            else:
                speedx = -sx

        elif circle.centery >= platform.bottom:
            circle.top = platform.bottom
            speedy = -speedy

    # Отражении от верхних блоков
    blocks_rects = get_rects_from_blocks(blocks)
    t1 = cross_with_objectlist(circle, blocks_rects)  # circle.collidelist(blocks_rects)
    if t1 != -1:
        if circle.centery <= blocks_rects[t1].top:
            circle.bottom = blocks_rects[t1].top
            speedy = -speedy
            hit_block(blocks, t1)

        elif circle.centery >= blocks_rects[t1].bottom:
            circle.top = blocks_rects[t1].bottom
            speedy = -speedy
            hit_block(blocks, t1)

        elif circle.centerx <= blocks_rects[t1].left:
            circle.right = blocks_rects[t1].left
            speedx = -speedx
            hit_block(blocks, t1)

        elif circle.centerx >= blocks_rects[t1].right:
            circle.left = blocks_rects[t1].right
            speedx = -speedx
            hit_block(blocks, t1)
