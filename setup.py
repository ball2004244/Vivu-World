import pygame as pg
import sys
import shutil
from pygame.locals import *
pg.init()


class Colors():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    BROWN = (100, 70, 36)
    SKYBLUE = (154, 203, 255)
    BURNT_SIENNA = (233, 116, 81)
    BRICK = (203, 65, 84)
    REDDISH_BROWN = (89, 0, 0)
    LIGHT_YELLOW = (255, 255, 200)
    SEA_FOAM_GREEN = (57.6, 91.4, 74.5)
    GOLD = (248, 222, 126)
    BRIGHT_BLUE = (25, 116, 210)
    BABY_BLUE = (137, 207, 240)
    AZURE = (0, 127, 255)
    ORANGE = (255, 165, 0)
    BURNT_ORANGE = (204, 85, 0)
    TAUPE = (72, 60, 50)
    LIGHT_ORANGE = (255, 127, 80)
    SAND = (237, 201, 175)
    ORCHE = (204, 119, 34)
    MIDNIGHT_BLUE = (25, 25, 112)
    DARK_YELLOW = (234, 206, 9)
    BLUISH_PURPLE = (113, 69, 240)
    PURPLE = (128, 0, 128)
    AQUAMARINE = (0, 255, 191)
    LIGHT_BROWN = (124, 96, 62)
    PLUM = (221, 160, 221)
    GRASS_GREEN = (0, 154, 23)
    CYAN = (0, 255, 255)
    BRICK_RED = (203, 65, 84)
    BLUE_GREY = (104, 118, 129)
    GOLDEN_ROD = (218, 165, 32)
    CERULEAN = (0, 123, 167)
    MUSTARD = (225, 173, 1)
    TEAL = (0, 128, 128)


class FontType():
    FONT1 = pg.font.SysFont('Garamond', 120)
    FONT2 = pg.font.SysFont('Garamond', 50)
    FONT3 = pg.font.SysFont('Garamond', 30)
    FONT4 = pg.font.SysFont('Garamond', 20)


# Screen
ScreenWidth = 1024
ScreenHeight = 768
Screen = pg.display.set_mode((ScreenWidth, ScreenHeight))
pg.display.set_caption('VIVU: World')


def fps_clock():
    FPS = 120
    clock = pg.time.Clock()
    clock.tick(FPS)


def update_screen():
    pg.display.update()

def quit_game():
    shutil.rmtree(r'__pycache__')  # delete cache folders
    shutil.rmtree(r'theme\__pycache__')
    shutil.rmtree(r'character\__pycache__')
    shutil.rmtree(r'new_mission\__pycache__')
    pg.quit()
    sys.exit()