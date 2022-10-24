import sys
import shutil
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *
from new_mission.general import *

pg.init()

horse_img = pg.image.load(r'new_mission\horse_shooting\horse.png').convert_alpha()
horse_img = pg.transform.scale(horse_img, (50, 50))

bullet_img = pg.image.load(r'new_mission\horse_shooting\bullet.png').convert_alpha()
bullet_img = pg.transform.scale(bullet_img, (30, 30))

gun_img = pg.image.load(r'new_mission\horse_shooting\pistol.png').convert_alpha()
gun_img = pg.transform.scale(gun_img, (60, 60))

# background = pg.image.load(r'')
# background = pg.transform.scale(background, (ScreenWidth, ScreenHeight))

class HorseShootingTheme(Minigame):
    def __init__(self):
        Minigame.__init__(self)
        self.shooting = True
        pass

    def prior_game_loop(self):
        self.bullet_group = pg.sprite.Group()
        self.horse_group = pg.sprite.Group()

        for i in range(30):
            horse_x, horse_y = randint(50, ScreenWidth - 50), randint(50, ScreenHeight - 50)
            horse = Horse(horse_x, horse_y)
            self.horse_group.add(horse)

        self.gun = Gun()

        Minigame.prior_game_loop(self)
        pass

    def game_loop(self):
        # draw
        Screen.fill(Colors.WHITE)
        self.gun.draw()
        for bullet in self.bullet_group.sprites():
            bullet.draw()
            bullet.update()

        for horse in self.horse_group.sprites():
            horse.draw()
            horse.update()
        
        if self.game_over == False:
            scoreboard.draw()
            if self.shooting == True:
                # shoot bullets when click
                if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    bullet = Bullet(mouse_x, mouse_y)
                    self.bullet_group.add(bullet)
                    self.gun.bullet_num -= 1
                    self.clicked = True

                # check out of ammo
                if self.gun.bullet_num <= 0:
                    self.shooting = False 
                    self.reload_start = pg.time.get_ticks()
                    print('Reloading')
                    
                if pg.mouse.get_pressed()[0] == 0:
                    self.clicked = False
            else:
                # reload ammo
                if (pg.time.get_ticks() - self.reload_start) // 1000 >= 1:
                    self.shooting = True
                    self.gun.bullet_num = 6
                    print('Finish Reload')

            # check bullet hit horse
            if pg.sprite.groupcollide(self.bullet_group, self.horse_group, True, True):
                scoreboard.add_score()
        else:
            print(f'Your score is: {scoreboard.score}')
            self.end_theme = True

        current = (pg.time.get_ticks() - self.start) // 1000 #convert tick to second, 1s = 1000ticks
        if self.time_limit - current <= 0:
            print('Time Out!')
            self.game_over = True

        pass

class Background():
    def __init__(self):
        self.image = background
        self.rect = self.image.get_rect(topleft=(0, 0))
        pass

    def draw(self):
        # draw background
        Screen.blit(self.image, self.rect)
        pass


class Horse(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.image = horse_img
        self.rect = self.image.get_rect(center=(self.x, self.y))
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        #border check
        if self.x < 0:
            self.x = ScreenWidth + 60
        else:
            self.x -= randint(3, 5)

class Gun():
    def __init__(self):
        self.image = gun_img
        self.rect = self.image.get_rect()
        self.x, self.y = pg.mouse.get_pos()
        self.bullet_num = 6
        pass

    def draw(self):
        self.x, self.y = pg.mouse.get_pos()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        pass    

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        self.x += 5
        if self.x >= ScreenWidth:
            self.kill()
        pass    

# Initialize
horse_shooting = HorseShootingTheme()

'''
TESTING HERE
'''
if __name__ == '__main__':
    horse_shooting.prior_game_loop()
    while True:
        horse_shooting.game_loop()
        if horse_shooting.end_theme == True:
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
