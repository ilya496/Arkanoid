import pygame as pg, json


class Block():

    def __init__(self, left, top=None, width=None, height=None, hp=None):
        if type(left) is dict:
            self.rect = pg.Rect(left['left'], left['top'], left['width'], left['height'])
            self.hp = left['hp']
        else:
            self.rect = pg.Rect(left, top, width, height)
            self.hp = hp

        self.color_list = [255, 0, 0]
        self.selected_block = False

        # Создание шрифта
        text = pg.font.match_font('Arial')
        self._f = pg.font.Font(text, 24)

    def serialize(self):
        data = {
            'left': self.rect.left,
            'top': self.rect.top,
            'width': self.rect.width,
            'height': self.rect.height,
            'hp': self.hp
        }
        return data

    def unserialize(self, json_file):
        data = []
        file = open(json_file, 'r')
        data.append(json.load(file))
        # return data[0]

    def check_point(self, posx_posy):
        return self.rect.collidepoint(posx_posy)

    def draw(self, screen):

        if self.selected_block:
            self.color_list = [255, 255, 0]
        else:
            self.color_list = [255, 0, 0]

        pg.draw.rect(screen, self.color_list, self.rect)
        k = self._f.render(str(self.hp), True, [255, 255, 255])
        screen.blit(k, self.rect.center)
