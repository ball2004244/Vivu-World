import sys
import shutil
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *

pg.init()

zom_img = pg.image.load(r'new_mission\zombie_slap\zombie.png').convert_alpha()
zom_img = pg.transform.scale(zom_img, (50, 50))

swatter_img = pg.image.load(r'new_mission\zombie_slap\swatter.png').convert_alpha()
swatter_img = pg.transform.scale(swatter_img, (60, 60))

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
        self.image = zom_img
        self.x, self.y = x, y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.vel_x, self.vel_y = randint(-30, 30), randint(-30, 30)
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def random_movement(self):
        if self.x > ScreenWidth + 80:
            self.x = -80
            self.vel_x = randint(-30, 30)
        elif self.x < -80:
            self.x = ScreenWidth + 80
            self.vel_x = randint(-30, 30)
        else:
            self.x += self.vel_x

        if self.y > ScreenHeight+ 80:
            self.y = -80
            self.vel_y = randint(-30, 30)
        elif self.y < -80:
            self.y = ScreenHeight + 80 
            self.vel_y = randint(-30, 30)
        else:
            self.y += self.vel_y
        
        pass

class Swatter(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = swatter_img
        self.rect = self.image.get_rect()
        pass

    def draw(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.rect = self.image.get_rect(center=(mouse_x, mouse_y))
        Screen.blit(self.image, self.rect)
        pass

class ScoreBoard():
    def __init__(self):
        self.score = 0
        pass

    def draw(self):
        self.text_surf = pg.font.Font.render(
            FontType.FONT1, str(self.score), True, Colors.BLACK)
        self.text_rect = self.text_surf.get_rect(
            center=(ScreenWidth // 2, ScreenHeight // 14))
        Screen.blit(self.text_surf, self.text_rect)
        pass

# Initialize
swatter_group = pg.sprite.Group()
zom_group = pg.sprite.Group()
for i in range(20):
    zom_x, zom_y = randint(50, ScreenWidth - 50), randint(50, ScreenHeight - 50)
    zom = Zombie(zom_x, zom_y)
    zom_group.add(zom)
swatter = Swatter()
swatter_group.add(swatter)

score_board = ScoreBoard()
game_over = False
time_limit = 15 # 15 seconds time limit
start = pg.time.get_ticks() #start count time
'''
TESTING HERE
'''
if __name__ == '__main__':
    while True:
        # draw
        Screen.fill(Colors.WHITE)
        swatter.draw()
        score_board.draw()

        for zom in zom_group.sprites():
            zom.draw()
            zom.random_movement()

        # update
        if game_over:
            print(f'Your score is: {score_board.score}')
            pg.quit()
            sys.exit()


        current = (pg.time.get_ticks() - start) // 1000 #convert tick to second, 1s = 1000ticks
        if time_limit - current <= 0:
            print('Time Out!')
            game_over = True

        if pg.mouse.get_pressed()[0] == 1 and game_over == False:
            if pg.sprite.groupcollide(zom_group, swatter_group, True, False):
                score_board.score += 1

        # check event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutil.rmtree(r'__pycache__')  # delete cache folder
                pg.quit()
                sys.exit()

        fps_clock()
        update_screen()
