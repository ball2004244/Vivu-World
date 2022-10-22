import sys
import shutil
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *

pg.init()

background = pg.image.load(r'new_mission\zombie_slap\background.png').convert_alpha()
background = pg.transform.scale(background, (ScreenWidth, ScreenHeight))

zom_img = pg.image.load(r'new_mission\zombie_slap\zombie.png').convert_alpha()
zom_img = pg.transform.scale(zom_img, (80, 80))

zom2_img = pg.image.load(r'new_mission\zombie_slap\zombie_2.png').convert_alpha()
zom2_img = pg.transform.scale(zom2_img, (80, 80))

swatter_img = pg.image.load(r'new_mission\zombie_slap\swatter.png').convert_alpha()
swatter_img = pg.transform.scale(swatter_img, (100, 100))

class ZombieSlapTheme():
    def __init__(self):
        self.background = Background()
        self.swatter_group = pg.sprite.Group()
        self.zom_group = pg.sprite.Group()
        self.clicked = False
        self.end_theme = False
        pass

    def prior_game_loop(self): 
        # set cursor to invisible
        # pg.mouse.set_visible(False)

        for i in range(randint(30, 35)):
            zom_x, zom_y = randint(50, ScreenWidth - 50), randint(50, ScreenHeight - 50)
            zom = Zombie(zom_x, zom_y)
            self.zom_group.add(zom)
        self.swatter = Swatter()
        self.swatter_group.add(self.swatter)

        self.cliced = False
        self.score_board = ScoreBoard()
        self.game_over = False
        self.time_limit = TimeLimit # 15 seconds time limit
        self.start = pg.time.get_ticks() #start count time
        pass

    def game_loop(self):
        Screen.fill(Colors.WHITE)
        self.background.draw()
        self.score_board.draw()
 
        for zom in self.zom_group.sprites():
            zom.draw()
            zom.random_movement()

        self.swatter.draw()

        # update
        if self.game_over == True:
            print(f'Your score is: {self.score_board.score}')
            self.end_theme = True
        else:
            self.current = (pg.time.get_ticks() - self.start) // 1000 #convert tick to second, 1s = 1000ticks
            if self.time_limit - self.current <= 0:
                print('Time Out!')
                self.game_over = True

            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if pg.sprite.groupcollide(self.zom_group, self.swatter_group, False, False):                    
                    # change zombie from alive to death, and add score to total
                    collide_zom = pg.sprite.spritecollide(self.swatter, self.zom_group, False)
                    for zom in collide_zom:
                        self.score_board.score = zom.add_score(self.score_board.score)
                        zom.change_state()

                self.clicked = True

            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False    

            # check event
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    shutil.rmtree(r'__pycache__')  # delete cache folder
                    pg.quit()
                    sys.exit()

        pass

class Background():
    def __init__(self):
        self.image = background
        self.rect = self.image.get_rect()

        self.game_over = False
        pass

    def draw(self):
        # draw background
        Screen.blit(self.image, self.rect)
        pass

class Zombie(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = zom_img
        self.x, self.y = x, y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.vel_x, self.vel_y = randint(-30, 30), randint(-30, 30)
        self.movement = True
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def add_score(self, score):
        if self.movement == True:
            return score + 1
        return score
    def change_state(self):
        
        # change from alive image to death image
        self.image = zom2_img
        self.movement = False

        pass

    def random_movement(self):
        if self.movement == True:
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
            FontType.FONT1, str(self.score), True, Colors.WHITE)
        self.text_rect = self.text_surf.get_rect(
            center=(ScreenWidth // 2, ScreenHeight // 14))
        Screen.blit(self.text_surf, self.text_rect)
        pass

# Initialize

'''
TESTING HERE
'''
zombie_slap = ZombieSlapTheme()
zombie_slap.prior_game_loop()
if __name__ == '__main__':
    while True:
        zombie_slap.game_loop()

        fps_clock()
        update_screen()
