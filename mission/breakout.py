import pygame as pg 
from pygame.locals import *
from setup import Screen, Colors, ScreenWidth, ScreenHeight 
from mission.breakout import *
pg.init()

class BreakOutTheme():
    pass

class Brick(pg.sprite.Sprite):
    def __init__(self, x, y, num):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'mission\breakout\box_' + str(num) + '.png')
        #scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (64, 36))
        self.rect = self.image.get_rect(topleft=(x, y))
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        pass

class Paddle():
    def __init__(self, x, y):
        self.image = pg.image.load(r'mission\breakout\paddle.png')
        #scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (240, 18))
        self.rect = self.image.get_rect(midbottom=(x, y))
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        pass

class Ball():
    def __init__(self, x, y):
        self.image = pg.image.load(r'mission\breakout\ball.png')
        #scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (48, 48))
        self.rect = self.image.get_rect(midbottom=(x, y))
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        pass
    pass

# init
brick_group = pg.sprite.Group()
brick_type = 1 # there are 3 brick types (1, 2, 3)
for brick_y in range(0, ScreenHeight // 4, 42):
    for brick_x in range(0, ScreenWidth, 74):
        brick = Brick(brick_x, brick_y, brick_type)
        brick_group.add(brick)
    # change bricks' color sequentially
    brick_type += 1
    if brick_type > 3:
        brick_type = 1 

paddle = Paddle(ScreenWidth // 2, ScreenHeight - 50)
ball = Ball(ScreenWidth // 2, ScreenHeight - 100)