import sys
import shutil
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *
from new_mission.general import *
pg.init()

mole_img = pg.image.load(r'new_mission\mole_in_hole\mole.png').convert_alpha()
mole_img = pg.transform.scale(mole_img, (190, 190))

hole_img = pg.image.load(r'new_mission\mole_in_hole\hole.png').convert_alpha()
hole_img = pg.transform.scale(hole_img, (180, 180))

hammer_img = pg.image.load(r'new_mission\mole_in_hole\hammer.png').convert_alpha()
hammer_img = pg.transform.scale(hammer_img, (170, 170))

# background = pg.image.load(r'')
# background = pg.transform.scale(background, (ScreenWidth, ScreenHeight))

class MoleTheme(Minigame):
    def __init__(self):
        Minigame.__init__(self)
        pass 

    def prior_game_loop(self):
        self.mole_die = True
        self.mole_alive_time = 0
        self.mole_group = pg.sprite.Group()
        self.hammer_group = pg.sprite.Group()
        self.hole_group = pg.sprite.Group()

        self.hammer = Hammer()
        self.hammer_group.add(self.hammer)

        # Screen Resolution: 1024 x 768
        self.hole_pos = [(150, 170), (900, 300), (200, 500), (800, 600), (550, 350), (470, 672)]
        for i in range(len(self.hole_pos)):
            hole_x, hole_y = self.hole_pos[i][0], self.hole_pos[i][1]
            hole = Hole(hole_x, hole_y)
            self.hole_pos.append((hole_x, hole_y))
            self.hole_group.add(hole)

        self.mole = Mole(self.hole_pos[0][0], self.hole_pos[0][1])
        self.mole_group.add(self.mole)

        Minigame.prior_game_loop(self)
        pass

    def game_loop(self):
        # draw
        Screen.fill(Colors.WHITE)
        self.hole_group.draw(Screen)
        self.hammer.draw()
        self.mole.draw()
        scoreboard.draw()

        if self.game_over == False:
            # create mole 
            if self.mole_die == True:
                self.lucky_number = randint(0, len(self.hole_pos) - 1)
                self.mole = Mole(self.hole_pos[self.lucky_number][0], self.hole_pos[self.lucky_number][1])
                self.mole_group.add(self.mole)
                self.mole_alive_time = pg.time.get_ticks()
                self.mole_die = False

            if self.mole_die == False:
                if (pg.time.get_ticks() - self.mole_alive_time) // 1000 > 0.2:
                    self.mole_die = True
                    self.mole.kill()

                # hit mole when click
                if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    if pg.sprite.groupcollide(self.hammer_group, self.mole_group, False, True):
                        scoreboard.add_score()
                        self.mole_die = True
                        self.mole.kill()

                if pg.mouse.get_pressed()[0] == 0:
                    self.clicked = False
                
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
        Screen.blit(self.background, self.background_rect)
        pass


class Mole(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.image = mole_img
        self.rect = self.image.get_rect(center=(self.x, self.y))
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

class Hammer(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = hammer_img
        self.rect = self.image.get_rect()
        self.x, self.y = pg.mouse.get_pos()
        pass

    def draw(self):
        self.x, self.y = pg.mouse.get_pos()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        pass    

class Hole(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = hole_img
        self.x, self.y = x, y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        pass

    def draw(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        pass    

'''
TESTING HERE
'''
if __name__ == '__main__':
    mole_theme = MoleTheme()
    mole_theme.prior_game_loop()

    while True:
        if mole_theme.end_theme == True:
            pg.quit()
            sys.exit()
        mole_theme.game_loop()

        # check event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutil.rmtree(r'__pycache__')  # delete cache folder
                pg.quit()
                sys.exit()
                
        fps_clock()
        update_screen()
