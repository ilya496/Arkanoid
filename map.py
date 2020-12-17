import pygame as pg, settings, block, button, json

pg.init()

screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
blocks = []

save_button = button.Button('Calibri', 'Save', 30, [255, 255, 255], [800, 900], [0, 255, 0], [255, 0, 0])


def create_blocks(list_of_blocks):
    for j in range(int(settings.SCREENY / 50) - 4):
        for i in range(int(settings.SCREENX / 50)):
            list_of_blocks.append(block.Block(i * 50, j * 50, 49, 49, 1))


def get_block_by_point(list_of_blocks, pos):
    for i in list_of_blocks:
        if i.check_point(pos):
            return i
    return None


def process_events():
    event = pg.event.get()
    for j in event:
        if j.type == pg.MOUSEBUTTONDOWN and j.button == 1:
            b = get_block_by_point(blocks, j.pos)
            if save_button.check_point(pg.mouse.get_pos()):
                save_txt(blocks)
            if b is not None:
                b.selected_block = True
        elif j.type == pg.MOUSEBUTTONDOWN and j.button == 3:
            b = get_block_by_point(blocks, j.pos)
            if b is not None:
                b.selected_block = False


def draw_blocks(surface, list_of_blocks):
    for i in list_of_blocks:
        i.draw(surface)


def save_txt(list_of_blocks):
    data = []
    for i in list_of_blocks:
        if i.selected_block:
            block_data = i.serialize()
            data.append(block_data)
    f = open('map.json', 'w')
    json.dump(obj=data, fp=f, indent=0)


create_blocks(blocks)

while True:
    process_events()
    screen.fill([0, 0, 0])
    draw_blocks(screen, blocks)
    save_button.draw(screen)
    # Обновление дисплея
    pg.display.flip()
