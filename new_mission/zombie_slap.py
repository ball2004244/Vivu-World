import sys
import shutil
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *
from new_mission.general import *
pg.init()

background = pg.image.load(r'new_mission\zombie_slap\background.png').convert_alpha()
background = pg.transform.scale(background, (ScreenWidth, ScreenHeight))

zom_img = pg.image.load(r'new_mission\zombie_slap\zombie.png').convert_alpha()
zom_img = pg.transform.scale(zom_img, (80, 80))

zom2_img = pg.image.load(r'new_mission\zombie_slap\zombie_2.png').convert_alpha()
zom2_img = pg.transform.scale(zom2_img, (80, 80))

swatter_img = pg.image.load(r'new_mission\zombie_slap\swatter.png').convert_alpha()
swatter_img = pg.transform.scale(swatter_img, (100, 100))

class ZombieSlapTheme(Minigame):
    def __init__(self):
        Minigame.__init__(self)
        self.background = Background()
        self.swatter_group = pg.sprite.Group()
        self.zom_group = pg.sprite.Group()
        pass

    def prior_game_loop(self): 
        # set cursor to invisible
        # pg.mouse.set_visible(False)

        # create 30 - 35 zombies
        for i in range(randint(30, 35)):
            zom_x, zom_y = randint(50, ScreenWidth - 50), randint(50, ScreenHeight - 50)
            zom = Zombie(zom_x, zom_y)
            self.zom_group.add(zom)
        self.swatter = Swatter()
        self.swatter_group.add(self.swatter)

        Minigame.prior_game_loop(self)
        pass

    def game_loop(self):
        Screen.fill(Colors.WHITE)
        self.background.draw()
        scoreboard.draw()
        for zom in self.zom_group.sprites():
            zom.draw()
            zom.random_movement()

        self.swatter.draw()

        # update
        if self.game_over == True:
            print(f'Your score is: {scoreboard.score}')
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
                        if zom.movement == True:
                            scoreboard.add_score()
                            zom.change_state()

                self.clicked = True

            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False    

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

# Initialize

'''
TESTING HERE
'''

if __name__ == '__main__':
    zombie_slap = ZombieSlapTheme()
    zombie_slap.prior_game_loop()
    while True:
        zombie_slap.game_loop()
        if zombie_slap.end_theme == True:
            pg.quit()
            sys.exit()

        # check event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutil.rmtree(r'__pycache__')  # delete cache folder
                pg.quit()
                sys.exit()

        fps_clock()
        update_screen()
