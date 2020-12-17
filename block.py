import pygame as pg


class Block():

    def __init__(self, left, top, width, height, hp):

        self.hp = hp
        self.rect = pg.Rect(left, top, width, height)
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
            'height': self.rect.height
        }
        return data

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
