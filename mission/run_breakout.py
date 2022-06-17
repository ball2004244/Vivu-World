import pygame as pg
import sys
import os
import shutil

# this import all files in parents folder to children folder
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from setup import *
from mission.breakout import *

while True:
    # draw
    Screen.fill(Colors.WHITE)
    brick.draw()
    paddle.draw()
    ball.draw()
    
    # update 
    paddle.update()
    ball.update()
    breakout.update()

    # check event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            shutil.rmtree(r'mission/__pycache__')
            pg.quit()
            sys.exit()

    fps_clock()
    update_screen()