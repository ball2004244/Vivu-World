import random
import shutil 
import pygame as pg
import sys
from pygame.locals import *
sys.path.append('../Vivu-World')
from setup import *
pg.init()


class BreakOutTheme():
    def __init__(self):
        self.game_over = False
        self.win = False
        self.score = 0
        self.death_count = 0
        self.difficulty = 0  # 3 difficulty: [0, 1, 2] <=> Easy Med Hard
        pass

    def update(self):
        if self.game_over == True:
            #retart + reset
            self.death_count += 1
            self.reset()
            self.game_over = False
            pass

        if self.win == True:
            # reward + reset
            self.reset()
            self.difficulty += 1
            self.win == False
            self.score += 5000
            pass
        '''
        Difficulty:
            EASY level: slope = 1/3
            MEDIUM level: slope = 3/2
            HARD level: slope = 2 
        '''
        if self.difficulty == 0:
            ball.slope = 1/3
        elif self.difficulty == 1:
            ball.slope = 3/2
        elif self.difficulty == 2:
            ball.slope = 2
        else:
            ball.slope = 2

    def reset(self):
        # Reset ball
        ball.x = ScreenWidth // 2
        ball.y = ScreenHeight - 100
        ball.speed_x, ball.speed_y = 0, 0

        # Reset paddle
        paddle.x = ScreenWidth // 2
        # Redraw bricks
        brick.wall_init()
        pass


class Brick():
    def __init__(self):
        self.image1 = pg.image.load(r'old_mission\breakout\box_1.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image1 = pg.transform.scale(
            self.image1, (72, 40))

        self.image2 = pg.image.load(r'old_mission\breakout\box_2.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image2 = pg.transform.scale(
            self.image2, (72, 40))

        self.image3 = pg.image.load(r'old_mission\breakout\box_3.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image3 = pg.transform.scale(
            self.image3, (72, 40))
        
        self.wall_init()
        pass

    def wall_init(self):
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


class Paddle():
    def __init__(self):
        self.image = pg.image.load(r'old_mission\breakout\paddle.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (240, 18))
        self.x = ScreenWidth // 2
        self.speed = 23
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
        self.image = pg.image.load(r'old_mission\breakout\ball.png')
        # scale image to desire size, original scale: (1920, 1080)
        self.image = pg.transform.scale(
            self.image, (48, 48))
        self.x = ScreenWidth // 2
        self.y = ScreenHeight - 100
        self.speed_x = 0
        self.speed_y = 0
        self.slope = 1/3

        # restart text
        self.text_surf = pg.font.Font.render(
            FontType.FONT2, 'PRESS SPACE TO START', True, Colors.BLACK)
        self.text_rect = self.text_surf.get_rect(
            center=(ScreenWidth // 2, ScreenHeight * 5 // 8))
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        Screen.blit(self.image, self.rect)
        Screen.blit(self.text_surf, self.text_rect)
        pass

    def update(self):
        # start game when click SPACE
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_SPACE] and (self.speed_x, self.speed_y) == (0, 0):
            self.speed_x = 11
            self.speed_y = -self.speed_x * self.slope

        # check collide with side walls
        if self.rect.left < 0 or self.rect.right > ScreenWidth:
            self.speed_x *= -1

        # check collide with ceiling
        if self.rect.top < 0:
            self.speed_y *= -1

        # check collide with floor
        if self.rect.bottom > ScreenHeight:
            # self.speed_y *= -1  # This is for fun, must delete afterward
            breakout.game_over = True
        self.x += self.speed_x
        self.y += self.speed_y

        # check collide with paddle
        collide_threshold = 15  # limitation
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

        # check break all bricks
        if len(brick.brick_arr) == 0:
            breakout.win = True
    pass


# Initialize
breakout = BreakOutTheme()
paddle = Paddle()
ball = Ball()
brick = Brick()

'''
TESTING HERE
'''
if __name__ == '__main__':
    while True:
        # draw
        Screen.fill(Colors.WHITE)
        brick.draw()
        paddle.draw()
        ball.draw()
        
        # update 
        paddle.update()
        ball.update()
        breakout.update()

        # check event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutil.rmtree(r'__pycache__')  # delete cache folder
                shutil.rmtree(r'old_mission/__pycache__')
                pg.quit()
                sys.exit()

        fps_clock()
        update_screen()