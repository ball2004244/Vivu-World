
import pygame as pg
import sys
import shutil
from setup import Screen, Colors, Screen, fps_clock, update_screen, ScreenWidth, ScreenHeight, FontType
from mission import *
pg.init()

class FlappyBirdTheme():
    def __init__(self):
        self.background = pg.image.load(r'mission\flappybird\background.png')
        self.background = pg.transform.scale(self.background, (ScreenWidth, ScreenHeight))
        self.background_rect = self.background.get_rect(topleft = (0, 0))
        
        self.ground = pg.image.load(r'mission\flappybird\ground.png')
        self.ground = pg.transform.scale(self.ground, (ScreenWidth, ScreenHeight // 5))
        self.ground_rect = self.ground.get_rect(bottomleft = (0, ScreenHeight))
        pass

    def draw(self, ground_x):
        self.ground_rect = self.ground.get_rect(bottomleft = (ground_x, ScreenHeight))
        Screen.blit(self.background, self.background_rect)
        Screen.blit(self.ground, self.ground_rect)
        pass

    def update(self):
        pass

# init variables for game loop
flappy_theme = FlappyBirdTheme()
ground_x = 0
ground_speed = 5

while True:
    # draw
    Screen.fill(Colors.WHITE)
    flappy_theme.draw(ground_x)
    ground_x -= ground_speed
    print(ground_x)
    if abs(ground_x) > 30:
        ground_x = 0

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
