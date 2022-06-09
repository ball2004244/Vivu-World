from setup import Screen, Colors, FontType, ScreenWidth, ScreenHeight
import pygame as pg
from pygame.locals import *
pg.init()


class MainChar():
    def __init__(self):
        self.image = pg.image.load(r'character\maincharacter.png')
        self.image = pg.transform.scale(self.image, (300, 445))

        self.rect = self.image.get_rect(bottomleft = (50, ScreenHeight - 307))

        #attribute
        self.hp = 100
        self.mp = 50 
        self.die = False 
        pass 

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass
    def update(self):
        pass
    pass

class TextBox():
    def __init__(self):
        self.image = pg.image.load(r'character\textbox.png')
        self.image = pg.transform.scale(self.image, (1024, 307))

        self.rect = self.image.get_rect(bottomleft = (0, ScreenHeight))
        pass 
    def draw(self):
        Screen.blit(self.image, self.rect)
        pass 
    def update():
        pass 
    pass