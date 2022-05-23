# Import modules
import pygame as pg
from pygame.locals import *
from setup import fps_clock, update_screen, quit_game, Screen, Colors
from theme.theme0.t0_home import ThemeZero
from character.main_character import MainChar
pg.init()

# Initialize variable for Main function
theme0 = ThemeZero()
player = MainChar()
# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)
    theme0.draw()

    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game()
        if event.type == pg.MOUSEBUTTONUP:
            theme0.check_click()

    fps_clock()
    update_screen()
