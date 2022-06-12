import pygame as pg
import sys
import shutil
from setup import Screen, Colors, Screen, fps_clock, update_screen, ScreenWidth, ScreenHeight, FontType
from mission.breakout import *


# init
brick = Brick(100, 100, 200, 200)
while True:
    # draw
    Screen.fill(Colors.WHITE)
    # update 
    brick.draw()
    # check event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            pg.quit()
            sys.exit()

    fps_clock()
    update_screen()