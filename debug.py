# Import modules
import pygame as pg
import random
from pygame.locals import *
from setup import fps_clock, update_screen, quit_game, Screen, Colors
from theme.theme_display import *
from new_mission.horse_shooting import *
from new_mission.mole_in_hole import *
from new_mission.zombie_slap import *

pg.init()

# Initialize variable for Main function
# current_theme = ThemeZero()
open_theme = ThemeZero()
zombie_slap = ZombieSlapTheme()
horse_shooting = HorseShootingTheme()
mole_in_hole = MoleTheme()
game_list = [ZombieSlapTheme(), HorseShootingTheme(), MoleTheme()]

current_theme = open_theme

open_theme.prior_game_loop()

# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)
    current_theme.game_loop()
    
    if current_theme.end_theme == True:
        current_theme = random.choice(game_list)
        current_theme.prior_game_loop()
        current_theme.end_theme = False
        
        # reset the timer 
        current_theme.start = pg.time.get_ticks()
    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game()

    fps_clock()
    update_screen()
