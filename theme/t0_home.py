import pygame as pg
from pygame.locals import *
from setup import Screen

pg.init()
def load_background0():  
    return pg.image.load(r'theme\background\t0.jpg')
    
class ThemeZero():
    def __init__(self):
        pass

    def draw(self, background):
        Screen.blit(background, (0, 0))
        pass

    def update(self):
        pass
    pass
    