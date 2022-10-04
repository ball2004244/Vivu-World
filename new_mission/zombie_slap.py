import sys
import shutil
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *

pg.init()

# Init
game_speed = 6

class ZombieSlapTheme():
    def __init__(self):
        self.background = pg.image.load(r'')
        self.background = pg.transform.scale(
            self.background, (ScreenWidth, ScreenHeight))
        self.background_rect = self.background.get_rect(topleft=(0, 0))

        self.game_over = False
        pass

    def draw(self):
        # draw background
        Screen.blit(self.background, self.background_rect)
        pass


class Zombie(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'')
        self.image = pg.transform.scale(
            self.ground, (ScreenWidth + 50, ScreenHeight // 5))
        self.rect = self.image.get_rect(bottomleft=(0, ScreenHeight))

        self.die = False
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

    def check_hit(self):
        # check click
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.die == True:
                self.game_over = False

        pass

class Swatter(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'')
        self.image = pg.transform.scale(
            self.ground, (ScreenWidth + 50, ScreenHeight // 5))
        self.rect = self.image.get_rect(bottomleft=(0, ScreenHeight))

        self.clicked = False
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        pass    

# Initialize

'''
TESTING HERE
'''
if __name__ == '__main__':
    while True:
        # draw
        Screen.fill(Colors.WHITE)
        # update

        # check event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutil.rmtree(r'__pycache__')  # delete cache folder
                pg.quit()
                sys.exit()

        fps_clock()
        update_screen()
