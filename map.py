import pygame as pg, settings, block

pg.init()

screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
blocks = []
color_of_blocks = []
selected_blocks = []


def create_blocks(list_of_blocks):

    for j in range(int(settings.SCREENY / 50) - 4):
        for i in range(int(settings.SCREENX / 50)):
            list_of_blocks.append(block.Block(i * 50, j * 50, 49, 49, 1))


def check_click(list_of_blocks, selected_blocks):

    for i in pg.event.get():
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                for b in list_of_blocks:
                    if b.rect.collidepoint(i.pos):
                        selected_blocks.append(b)
            elif i.button == 3:
                for b in list_of_blocks:
                    if b.rect.collidepoint(i.pos):
                        if b in selected_blocks:
                            selected_blocks.remove(b)


def draw_blocks(surface, list_of_blocks):
    for i in list_of_blocks:
        if i.rect.collidepoint(pg.mouse.get_pos()):
            color_of_blocks = [255, 255, 0]
        else:
            color_of_blocks = [255, 0, 0]

        if i in selected_blocks:
            color_of_blocks = [255, 255, 0]

        i.draw(surface, color_of_blocks)


# def save_txt(list_of_blocks, selected_blocks):
#     list_of_chars = []
#
#     for i in list_of_blocks:
#         list_of_blocks.remove(i)
#         list_of_chars.append('.')
#
#     for i in selected_blocks:
#         list_of_blocks.remove(i)
#         list_of_chars.append('-')


create_blocks(blocks)

while True:
    check_click(blocks, selected_blocks)
    screen.fill([0, 0, 0])
    draw_blocks(screen, blocks)
    # Обновление дисплея
    pg.display.flip()
