
import pygame as pg
import sys
import os
import shutil
import random

# this import all files in parents folder to children folder
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from setup import Screen, Colors, Screen, fps_clock, update_screen, ScreenWidth, ScreenHeight, FontType
from mission.flappybird import *
pg.init()


# init variables for game loop

while True:
    # draw
    Screen.fill(Colors.WHITE)
    flappy_theme.draw()
    bird_group.draw(Screen)
    pipe_group.draw(Screen)
    ground.draw()
    score.draw()
    restart.draw()

    # update 
    restart.update()
    ground.update()
    pipe_group.update()
    bird_group.update()
    # draw pipes
    current_time = pg.time.get_ticks()
    if current_time - last_pipe > pipe_frequency:
        gap_position = random.randint(-50, 125)
        top_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), 1, gap_position)
        bottom_pipe = Pipe(ScreenWidth, int(
            ScreenHeight / 2), -1, gap_position)
        pipe_group.add(top_pipe)
        pipe_group.add(bottom_pipe)
        last_pipe = current_time

    # check if game is over
    if pg.sprite.groupcollide(pipe_group, bird_group, False, False) or bird.flying == False:
        restart.game_over = True
    
    if restart.game_over == True:
        restart.reset()
    # check score
    if len(pipe_group) > 0:
        if score.pass_pipe == False \
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right:
            score.pass_pipe = True

        if score.pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score.value += 1
                score.pass_pipe = False

    # check event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            pg.quit()
            sys.exit()

    fps_clock()
    update_screen()
