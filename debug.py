
import pygame as pg
import sys
import shutil
import random
from setup import Screen, Colors, Screen, fps_clock, update_screen, ScreenWidth, ScreenHeight, FontType
from mission.flappybird import *
pg.init()


# init variables for game loop
last_pipe = pg.time.get_ticks()
pipe_frequency = 1500  # miliseconds
flappy_theme = FlappyBirdTheme()
ground = Ground()

bird = Bird(100, int(ScreenHeight / 2) - 100)
bird_group = pg.sprite.Group()
bird_group.add(bird)

pipe_group = pg.sprite.Group()
top_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), 1, 0)
bottom_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), -1, 0)
pipe_group.add(top_pipe)
pipe_group.add(bottom_pipe)

game_over = False
flying = True

while True:
    # draw
    Screen.fill(Colors.WHITE)
    flappy_theme.draw()
    bird_group.draw(Screen)
    pipe_group.draw(Screen)

    ground.draw()

    # update
    ground.update()
    pipe_group.update()
    bird_group.update()

    current_time = pg.time.get_ticks()
    # draw pipes
    if current_time - last_pipe > pipe_frequency:
        gap_position = random.randint(-50, 125)
        top_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), 1, gap_position)
        bottom_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), -1, gap_position)
        pipe_group.add(top_pipe)
        pipe_group.add(bottom_pipe)
        last_pipe = current_time

    # check colide
    if pg.sprite.groupcollide(pipe_group, bird_group, False, False) or bird.flying == False:
         game_over = True

    if game_over:
        pg.quit()
        sys.exit()

    # check event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            pg.quit()
            sys.exit()

    fps_clock()
    update_screen()
