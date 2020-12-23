import pygame as pg, settings, os, json

pg.init()
import game, menu

# Создание окна
screen = pg.display.set_mode([settings.SCREENX, settings.SCREENY])
screen_mode = 'menu'
dir = os.getcwd()

while True:

    # Проверка на игру
    if screen_mode == 'game':
        g = game.game(screen)
        if g == 'menu':
            screen_mode = 'menu'

    # Проверка на меню
    if screen_mode == 'menu':
        m = menu.menu(screen)
        if m == 'easy' or m == 'medium' or m == 'hard':
            game.restart(m)
            screen_mode = 'game'

    # for dirpath, dirnames, filenames in os.walk("."):
    #     # перебрать каталоги
    #     for dirname in dirnames:
    #         print("Каталог:", os.path.join(dirpath, dirname))
    #     # перебрать файлы
    #     for filename in filenames:
    #         print("Файл:", os.path.join(dirpath, filename))

    # def finder(directory):
    #     names = os.listdir(directory)
    #     for name in names:
    #         fullname = os.path.join(os.getcwd(), name)
    #         if os.path.isfile(name):
    #             # filename, file_extension = os.path.splitext(name)
    #             # data = []
    #             # if file_extension == '.json':
    #                 # openfile = open(name, 'r')
    #                 # data.append(json.load(openfile))
    #                 # openfile.close()
    #             # print(data)
    #
    # if __name__ == '__main__':
    #     finder(dir)


