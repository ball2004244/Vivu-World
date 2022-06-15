import random
import pygame as pg
from pygame.locals import *
from math import tan
from setup import Screen, Colors, ScreenWidth, ScreenHeight
from mission.breakout import *
pg.init()


class BreakOutTheme():
    pass


class Brick():
    def __init__(self):
        self.image1 = pg.image.load(r'mission\breakout\box_1.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image1 = pg.transform.scale(
                self.image1, (64, 36))

        self.image2 = pg.image.load(r'mission\breakout\box_2.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image2 = pg.transform.scale(
                self.image2, (64, 36))
        
        self.image3 = pg.image.load(r'mission\breakout\box_3.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image3 = pg.transform.scale(
                self.image3, (64, 36))

        '''Draw bricks'''
        self.brick_arr = []
        image = self.image1
        for brick_y in range(0, ScreenHeight // 4, 42):
            for brick_x in range(0, ScreenWidth, 74):
                # change bricks' color
                if brick_y < ScreenHeight // (3 * 4):
                    image = self.image1    
                elif brick_y < ScreenHeight * 2 // (3 * 4):
                    image = self.image2
                else:
                    image = self.image3

                rect = image.get_rect(topleft=(brick_x, brick_y))
                self.brick_arr.append((image, rect))
        pass

    def draw(self):
        for (image, rect) in self.brick_arr:
            Screen.blit(image, rect)       
        pass

    def update(self):
        pass


class Paddle():
    def __init__(self):
        self.image = pg.image.load(r'mission\breakout\paddle.png')
        # scale image to desire size, original scale: (1920, 1080)
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
        if (key_pressed[pg.K_a] or key_pressed[pg.K_LEFT]) and self.x - 240 / 2 > 0:
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
        # scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (48, 48))
        self.x = ScreenWidth // 2
        self.y = ScreenHeight - 100
        self.speed_x = 5
        self.speed_y = - self.speed_x
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        # check collide with side walls
        if self.rect.left < 0 or self.rect.right > ScreenWidth:
            self.speed_x *= -1

        # check collide with ceiling
        if self.rect.top < 0:
            self.speed_y *= -1

        # check collide with floor
        if self.rect.bottom > ScreenHeight:
            self.speed_y *= -1  # This is for fun, must delete afterward
            self.game_over = True
        self.x += self.speed_x
        self.y += self.speed_y

        # check collide with paddle
        collide_threshold = 5  # limitation
        if self.rect.colliderect(paddle):
            if abs(self.rect.bottom - paddle.rect.top) < collide_threshold and self.speed_y > 0:
                self.speed_y *= -1

        # check collide with bricks
        for item in brick.brick_arr:
            if self.rect.colliderect(item[1]):
                # check collide above
                if abs(self.rect.bottom - item[1].top) < collide_threshold and self.speed_y > 0:
                    self.speed_y *= -1
                # check collide below
                if abs(self.rect.top - item[1].bottom) < collide_threshold and self.speed_y < 0:
                    self.speed_y *= -1
                # check collide left
                if abs(self.rect.right - item[1].left) < collide_threshold and self.speed_x > 0:
                    self.speed_x *= -1
                # check collide right
                if abs(self.rect.left - item[1].right) < collide_threshold and self.speed_x < 0:
                    self.speed_x *= -1
                brick.brick_arr.remove(item)
                print(len(brick.brick_arr))




    pass


# init
paddle = Paddle()
ball = Ball()
brick = Brick()
