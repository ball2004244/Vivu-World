import sys
import shutil
import time
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *

pg.init()

horse_img = pg.image.load(r'new_mission\horse_shooting\horse.png').convert_alpha()
horse_img = pg.transform.scale(horse_img, (50, 50))

bullet_img = pg.image.load(r'new_mission\horse_shooting\bullet.png').convert_alpha()
bullet_img = pg.transform.scale(bullet_img, (30, 30))

gun_img = pg.image.load(r'new_mission\horse_shooting\pistol.png').convert_alpha()
gun_img = pg.transform.scale(gun_img, (60, 60))

class HorseShootingTheme():
    def __init__(self):
        self.background = pg.image.load(r'')
        self.background = pg.transform.scale(self.background, (ScreenWidth, ScreenHeight))
        self.background_rect = self.background.get_rect(topleft=(0, 0))

        self.game_over = False
        pass

    def draw(self):
        # draw background
        Screen.blit(self.background, self.background_rect)
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
bullet_group = pg.sprite.Group()
horse_group = pg.sprite.Group()

for i in range(30):
    horse_x, horse_y = randint(50, ScreenWidth - 50), randint(50, ScreenHeight - 50)
    horse = Horse(horse_x, horse_y)
    horse_group.add(horse)

gun = Gun()
score_board = ScoreBoard()

shooting = True
game_over = False
time_limit = 15 # 3 seconds time limit
start = pg.time.get_ticks() #start count time
clicked = False
'''
TESTING HERE
'''
if __name__ == '__main__':
    while True:
        # draw
        Screen.fill(Colors.WHITE)
        gun.draw()
        for bullet in bullet_group.sprites():
            bullet.draw()
            bullet.update()

        for horse in horse_group.sprites():
            horse.draw()
            horse.update()
        
        if game_over == False:
            score_board.draw()
            if shooting == True:
                # shoot bullets when click
                if pg.mouse.get_pressed()[0] == 1 and clicked == False:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    bullet = Bullet(mouse_x, mouse_y)
                    bullet_group.add(bullet)
                    gun.bullet_num -= 1
                    clicked = True

                # check out of ammo
                if gun.bullet_num <= 0:
                    shooting = False 
                    reload_start = pg.time.get_ticks()
                    print('Reloading')
                    
                if pg.mouse.get_pressed()[0] == 0:
                    clicked = False
            else:
                # reload ammo
                if (pg.time.get_ticks() - reload_start) // 1000 >= 1:
                    shooting = True
                    gun.bullet_num = 6
                    print('Finish Reload')

            # check bullet hit horse
            if pg.sprite.groupcollide(bullet_group, horse_group, True, True):
                score_board.score += 1
        else:
            print(f'Your score is: {score_board.score}')
            pg.quit()
            sys.exit()

        current = (pg.time.get_ticks() - start) // 1000 #convert tick to second, 1s = 1000ticks
        if time_limit - current <= 0:
            print('Time Out!')
            game_over = True

        # check event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutil.rmtree(r'__pycache__')  # delete cache folder
                pg.quit()
                sys.exit()

        fps_clock()
        update_screen()
