import random
import pygame as pg 
from pygame.locals import *
from math import tan
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
    def __init__(self):
        self.image = pg.image.load(r'mission\breakout\paddle.png')
        #scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (240, 18))
        self.x = ScreenWidth // 2
        self.speed = 10
        pass

    def draw(self):
        self.rect = self.image.get_rect(midbottom=(self.x, ScreenHeight - 50))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        # moving left, right
        key_pressed = pg.key.get_pressed()
        if (key_pressed[pg.K_a] or key_pressed[pg.K_LEFT]) and self.x  - 240 / 2 > 0: 
            self.x -= self.speed

        if (key_pressed[pg.K_d] or key_pressed[pg.K_RIGHT]) and self.x + 240 / 2 < ScreenWidth: 
            self.x += self.speed
        pass

class Ball():
    def __init__(self):
        '''
        x = input x
        y = input y
        rad = 24
        '''
        self.image = pg.image.load(r'mission\breakout\ball.png')
        #scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (48, 48))
        self.x = ScreenWidth // 2
        self.y = ScreenHeight - 100
        self.speed = 2
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        '''
        Movement equation
        y = ax + b
        a: angle 
        b: distance to project vector
        x: position x
        y: position b
        '''
        self.x += self.speed
        self.y -= self.speed
        print(str(self.x) + ',' + str(self.y))
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

paddle = Paddle()
ball = Ball()