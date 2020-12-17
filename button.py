import pygame as pg


class Button():

    def __init__(self, font, btn_text, font_size, btn_text_color, position, btn_bg_color, btn_border_color):
        text = pg.font.match_font(font)
        self._btn_bg_color = btn_bg_color
        self._btn_border_color = btn_border_color
        self._f = pg.font.Font(text, font_size)
        self._btn = self._f.render(btn_text, True, btn_text_color)
        self._background = pg.Rect(position[0], position[1], self._btn.get_width() + 20, self._btn.get_height() + 10)
        self._text_rect = self._btn.get_rect()
        self._text_rect.center = self._background.center

    def draw(self, surface):
        pg.draw.rect(surface, self._btn_bg_color, self._background)
        pg.draw.rect(surface, self._btn_border_color, self._background, 1)
        surface.blit(self._btn, self._text_rect)

    def check_point(self, posx_posy):
        return self._background.collidepoint(posx_posy)