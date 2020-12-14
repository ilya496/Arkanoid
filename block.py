import pygame as pg


class Block():

    def __init__(self, left, top, width, height, hp):
        self.hp = hp
        self.rect = pg.Rect(left, top, width, height)

        # Создание шрифта
        text = pg.font.match_font('Arial')
        self._f = pg.font.Font(text, 24)

    def draw(self, screen, color_list):
        pg.draw.rect(screen, color_list, self.rect)


    def draw_hp(self, screen):
        k = self._f.render(str(self.hp), True, [255, 255, 255])
        screen.blit(k, self.rect.center)


class SuperBlock():

    def __init__(self, left, top, width, height, hp):
        self.hp = 10
        self.rect = pg.Rect(left, top, width, height)
        # Создание шрифта
        text = pg.font.match_font('Arial')
        self._f = pg.font.Font(text, 24)

    def draw(self, screen, color):
        pg.draw.circle(screen, color, self.rect.center, self.rect.width//2)


    def draw_hp(self, screen):
        k = self._f.render(str(self.hp), True, [255, 255, 255])
        screen.blit(k, self.rect.center)
