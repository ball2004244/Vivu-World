
import pygame as pg
import sys
import shutil
from setup import Screen, Colors, Screen, fps_clock, update_screen, ScreenWidth, ScreenHeight, FontType

pg.init()

class MainChar():
    def __init__(self):
        self.image = pg.image.load(r'character\main_character.png')
        self.image = pg.transform.scale(self.image, (700, 800))

        self.rect = self.image.get_rect(bottomleft = (-100, ScreenHeight + 50))
        pass 

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass
    def update(self):
        pass
    pass

class TextBox():
    def __init__(self):
        pass 
    def draw(self):
        pass 
    def update():
        pass 
    pass

# init variables for game loop
player = MainChar()

while True:
    # draw
    Screen.fill(Colors.WHITE)
    player.draw()
    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            pass

    fps_clock()
    update_screen()
