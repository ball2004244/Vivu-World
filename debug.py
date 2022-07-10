import pygame as pg
import sys
import shutil
from setup import *


# init
while True:
    # draw
    Screen.fill(Colors.WHITE)
    # update 
    
    # check event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            pg.quit()
            sys.exit()

        # check mouse click
        if event.type == pg.MOUSEBUTTONUP:
            pass
            
        # check button hit
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pass

    fps_clock()
    update_screen()