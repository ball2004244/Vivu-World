import pygame as pg
from pygame.locals import *
import sys 
import shutil 
from random import randint
sys.path.append('../Vivu-World')
from setup import *

pg.init()

# Init
game_speed = 6


class ZombieSlapTheme():
    def __init__(self):
        self.background = pg.image.load(r'mission\flappybird\background.png')
        self.background = pg.transform.scale(
            self.background, (ScreenWidth, ScreenHeight))
        self.background_rect = self.background.get_rect(topleft=(0, 0))

        pass

    def draw(self):
        # draw background
        Screen.blit(self.background, self.background_rect)
        pass

class Zombie(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'')
        self.image =  pg.transform.scale(
            self.ground, (ScreenWidth + 50, ScreenHeight // 5))
        self.rect =  self.image(bottomleft=(0, ScreenHeight))
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
