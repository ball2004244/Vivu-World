# Import modules
import pygame as pg
from pygame.locals import *
from setup import fps_clock, update_screen, quit_game, Screen, Colors
from theme.theme_display import *
from character.main_character import MainChar
pg.init()

# Initialize variable for Main function
theme_num = 0 #the current theme (ex: theme_0)
theme0 = ThemeZero()
player = MainChar()

# Main function
while True:
    current_theme = Theme(theme_num)
    # draw
    Screen.fill(Colors.WHITE)
    current_theme.draw()
    if theme_num == 0:
        theme0.draw()

    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game()

        if event.type == pg.MOUSEBUTTONUP:
            if theme_num == 0: #this is the starting theme
                if theme0.start_button.check_click():
                    theme_num = theme0.new_game(theme_num)
                if theme0.continue_button.check_click():
                    theme0.cont_game()
                if theme0.setting_button.check_click():
                    theme0.setting()
                if theme0.exit_button.check_click():
                    theme0.exit_game()     


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and theme_num != 0:
                print('SPACE Pressed')
                theme_num += 1
                print('The current theme is ', theme_num)
    fps_clock()
    update_screen()
