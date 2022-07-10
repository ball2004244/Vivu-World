# Import modules
import pygame as pg
from pygame.locals import *
from setup import fps_clock, update_screen, quit_game, Screen, Colors
from theme.theme_display import *
from character.main_character import MainChar
from mission.breakout import *
pg.init()

# Initialize variable for Main function
theme0 = ThemeZero()
theme1 = ThemeOne()
theme_list = [theme0, theme1]
theme_num = 0 #index of current theme
player = MainChar()

# Main function
while True:
    current_theme = theme_list[theme_num]
    # draw
    Screen.fill(Colors.WHITE)
    current_theme.draw()

    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game()

        if event.type == pg.MOUSEBUTTONUP:
            if theme_num == 0 and theme0.start_button.check_click():
                theme_num = theme0.new_game(theme_num)

            theme0.update()



        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and theme_num != 0:
                print('SPACE Pressed')
                theme_num += 1
                print('The current theme is ', theme_num)
    fps_clock()
    update_screen()
