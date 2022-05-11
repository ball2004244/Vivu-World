# Import modules
import pygame as pg
import sys
import shutil
from pygame.locals import *
from setup import fps_clock, update_screen, Screen, Colors
from theme.t0_home import load_background0, ThemeZero
pg.init()

# Initialize variable for Main function
theme_0 = ThemeZero()
# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)
    theme_0.draw(load_background0())


    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree('__pycache__') #delete cache folder
            shutil.rmtree('theme\__pycache__')
            pg.quit()
            sys.exit()

    fps_clock()
    update_screen()
