import sys
import shutil
import pygame as pg
from pygame.locals import *
from random import randint
sys.path.append('../Vivu-World')
from setup import *

pg.init()

mole_img = pg.image.load(r'new_mission\mole_in_hole\mole.png').convert_alpha()
mole_img = pg.transform.scale(mole_img, (190, 190))

hole_img = pg.image.load(r'new_mission\mole_in_hole\hole.png').convert_alpha()
hole_img = pg.transform.scale(hole_img, (180, 180))

hammer_img = pg.image.load(r'new_mission\mole_in_hole\hammer.png').convert_alpha()
hammer_img = pg.transform.scale(hammer_img, (170, 170))

class MoleTheme():
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
mole_die = True
mole_alive_time = 0
mole_group = pg.sprite.Group()
hammer_group = pg.sprite.Group()
hole_group = pg.sprite.Group()

hammer = Hammer()
hammer_group.add(hammer)


# Screen Resolution: 1024 x 768
hole_pos = [(150, 170), (900, 300), (200, 500), (800, 600), (550, 350), (470, 672)]
for i in range(len(hole_pos)):
    hole_x, hole_y = hole_pos[i][0], hole_pos[i][1]
    hole = Hole(hole_x, hole_y)
    hole_pos.append((hole_x, hole_y))
    hole_group.add(hole)

score_board = ScoreBoard()

game_over = False
clicked = False
time_limit = 15 # 15 seconds time limit
start = pg.time.get_ticks() #start count time
'''
TESTING HERE
'''
if __name__ == '__main__':
    while True:
        # draw
        Screen.fill(Colors.WHITE)
        hole_group.draw(Screen)
        hammer.draw()
        score_board.draw()
        if game_over == False:
            # create mole 
            if mole_die == True:
                lucky_number = randint(0, len(hole_pos) - 1)
                mole = Mole(hole_pos[lucky_number][0], hole_pos[lucky_number][1])
                mole_group.add(mole)
                mole_alive_time = pg.time.get_ticks()
                mole_die = False

            if mole_die == False:
                mole.draw()
                if (pg.time.get_ticks() - mole_alive_time) // 1000 > 0.5:
                    mole_die = True
                    mole.kill()
                    continue

                # hit mole when click
                if pg.mouse.get_pressed()[0] == 1 and clicked == False:
                    clicked = True
                    if pg.sprite.groupcollide(hammer_group, mole_group, False, True):
                        score_board.score += 1  
                        mole_die = True
                        mole.kill()

                if pg.mouse.get_pressed()[0] == 0:
                    clicked = False
                


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
