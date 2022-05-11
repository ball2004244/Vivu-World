# Import modules
import pygame as pg
import sys
import shutil
from pygame.locals import *
from setup import fps_clock, update_screen, Screen, Colors
pg.init()


# Initialize variable for Main function

# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)
    
    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree('__pycache__') #delete cache folder
            pg.quit()
            sys.exit()

    fps_clock()
    update_screen()
