
import pygame as pg
import sys
import shutil
from setup import Screen, Colors, Screen, fps_clock, update_screen, ScreenWidth, ScreenHeight, FontType

pg.init()

class MainChar():
    def __init__(self):
        self.image = pg.image.load(r'character\maincharacter.png')
        self.image = pg.transform.scale(self.image, (300, 445))

        self.rect = self.image.get_rect(bottomleft = (50, ScreenHeight - 307))
        pass 

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass
    def update(self):
        pass
    pass

class Theme():
    def __init__(self):
        self.image = pg.image.load(r'theme\testtheme.jpg')
        self.image = pg.transform.scale(self.image, (ScreenWidth, ScreenHeight))

        self.rect = self.image.get_rect(topleft = (0, 0))
        pass
    def draw(self):
        Screen.blit(self.image, self.rect)
        pass 
    pass
class TextBox():
    def __init__(self):
        self.image = pg.image.load(r'character\textbox.png')
        self.image = pg.transform.scale(self.image, (1024, 307))

        self.rect = self.image.get_rect(bottomleft = (0, ScreenHeight))
        pass 
    def draw(self):
        Screen.blit(self.image, self.rect)
        pass 
    def update():
        pass 
    pass

# init variables for game loop
player = MainChar()
textbox = TextBox()
background = Theme()
while True:
    # draw
    Screen.fill(Colors.WHITE)
    background.draw()
    player.draw()
    textbox.draw()
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
