# Import modules
import pygame as pg
import sys
import shutil
from pygame.locals import *
from setup import fps_clock, update_screen, Screen, Colors
from theme.theme0.t0_home import ThemeZero
pg.init()

# Initialize variable for Main function
theme0 = ThemeZero()
# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)
    theme0.draw()

    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            shutil.rmtree(r'theme\theme0\__pycache__')
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            theme0.check_click()

    fps_clock()
    update_screen()
