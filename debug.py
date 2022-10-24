# Import modules
import pygame as pg
import random
from pygame.locals import *
from setup import fps_clock, update_screen, quit_game, Screen, Colors
from theme.theme_display import *
from new_mission.horse_shooting import HorseShootingTheme
from new_mission.mole_in_hole import MoleTheme
from new_mission.zombie_slap import ZombieSlapTheme
from new_mission.flappybird import FlappyBirdTheme
from new_mission.general import *
from database.database import *
pg.init()

# Initialize variable for Main function
# current_theme = ThemeZero()
open_theme = ThemeZero()
game_list = [ZombieSlapTheme(), HorseShootingTheme(),
             MoleTheme(), FlappyBirdTheme()]

prev_theme = None
current_theme = open_theme

open_theme.prior_game_loop()

# Main function
while True:
    # draw
    Screen.fill(Colors.WHITE)
    current_theme.game_loop()
    scoreboard.draw()
    # when a player win a minigame -> change to next theme
    if current_theme.end_theme == True: 
        while prev_theme == current_theme: # check if 2 consecutive tries return the same theme
            current_theme = random.choice(game_list)

        prev_theme = current_theme
        current_theme.prior_game_loop()
    
    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game()
    fps_clock()
    update_screen()
