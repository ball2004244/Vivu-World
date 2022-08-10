from setup import Screen, Colors, FontType, ScreenWidth, ScreenHeight
import pygame as pg
from pygame.locals import *
pg.init()


class MainChar():
    def __init__(self):
        self.image = pg.image.load(r'character\main_character.jpg')
        self.image = pg.transform.scale(self.image, (300, 445))

        self.rect = self.image.get_rect(bottomleft=(50, ScreenHeight - 300))

        # attribute
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
    def __init__(self, name, text):
        self.image = pg.image.load(r'character\text_box.jpg')
        self.image = pg.transform.scale(self.image, (1024, 300))

        self.rect = self.image.get_rect(bottomleft=(0, ScreenHeight))

        self.text = text
        self.text_surf = pg.font.Font.render(
            FontType.FONT3, self.text, True, Colors.BLACK)
        self.text_rect = self.text_surf.get_rect(
            center=(ScreenWidth // 2, ScreenHeight - 100))

        self.name = name 
        self.name_surf = pg.font.Font.render(
            FontType.FONT3, self.name, True, Colors.BLACK)
        self.name_rect = self.text_surf.get_rect(
            center=(340, ScreenHeight - 255))        
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        Screen.blit(self.text_surf, self.text_rect)
        Screen.blit(self.name_surf, self.name_rect)
        pass

    def update():
        pass
    pass
