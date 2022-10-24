import sys 
import shutil 
import pygame as pg
from pygame.locals import *
from random import randint

sys.path.append('../Vivu-World')
from setup import *
from new_mission.general import *
pg.init()

# Init
pipe_img = pg.image.load(r'old_mission\flappybird\pipe.png').convert_alpha()
pipe_img = pg.transform.scale(pipe_img, (78 * 24 // 35, 560 * 24 // 35))

background_img = pg.image.load(r'old_mission\flappybird\background.png').convert_alpha()
background_img = pg.transform.scale(background_img, (ScreenWidth, ScreenHeight))

ground_img = pg.image.load(r'old_mission\flappybird\ground.png').convert_alpha()
ground_img = pg.transform.scale(ground_img, (ScreenWidth + 50, ScreenHeight // 5))
class FlappyBirdTheme(Minigame):
    def __init__(self):
        Minigame.__init__(self)
        pass

    def prior_game_loop(self):
        # Initialize
        self.pipe_frequency = 1500  # miliseconds
        self.pass_pipe = False
        self.background = Background()
        self.ground = Ground()

        self.bird = Bird(100, int(ScreenHeight / 2) - 100)
        self.bird_group = pg.sprite.Group()
        self.bird_group.add(self.bird)

        self.pipe_group = pg.sprite.Group()
        self.top_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), 1, 0)
        bottom_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), -1, 0)
        self.pipe_group.add(self.top_pipe)
        self.pipe_group.add(bottom_pipe)

        self.last_pipe = pg.time.get_ticks()
        
        Minigame.prior_game_loop(self)
        pass

    def game_loop(self):
        # draw
        Screen.fill(Colors.WHITE)
        self.background.draw()
        self.bird_group.draw(Screen)
        self.pipe_group.draw(Screen)
        self.ground.draw()
        scoreboard.draw()

        # update
        self.ground.update()
        self.pipe_group.update()
        self.bird_group.update()

        self.ground.ground_x -= self.game_speed
        for pipe in self.pipe_group:
            pipe.rect.x -= self.game_speed
        # draw pipes
        current_time = pg.time.get_ticks()
        if current_time - self.last_pipe > self.pipe_frequency:
            gap_position = randint(-50, 125)
            self.top_pipe = Pipe(ScreenWidth, int(
                ScreenHeight / 2), 1, gap_position)
            bottom_pipe = Pipe(ScreenWidth, int(
                ScreenHeight / 2), -1, gap_position)
            self.pipe_group.add(self.top_pipe)
            self.pipe_group.add(bottom_pipe)
            self.last_pipe = current_time

        # check if game is over
        current = (pg.time.get_ticks() - self.start) // 1000
        if pg.sprite.groupcollide(self.pipe_group, self.bird_group, False, False) or self.bird.flying == False or self.time_limit - current <= 0:
            # restart.game_over = True
            self.game_over = True

        if self.game_over == True:
            print(f'Your score is: {scoreboard.score}')
            self.end_theme = True

            # restart.reset()

        # check score
        if len(self.pipe_group) > 0:
            if self.pass_pipe == False \
                    and self.bird_group.sprites()[0].rect.right < self.pipe_group.sprites()[0].rect.right:
                self.pass_pipe = True

            if self.pass_pipe == True:
                if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.right:
                    scoreboard.add_score()
                    self.pass_pipe = False

        pass

class Background():
    def __init__(self):
        self.background = background_img
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        pass

    def draw(self):
        # draw background
        Screen.blit(self.background, self.background_rect)
        pass

class Ground():
    def __init__(self):
        self.ground = ground_img
        self.ground_rect = self.ground.get_rect(bottomleft=(0, ScreenHeight))

        self.ground_x = 0
        pass

    def draw(self):
        Screen.blit(self.ground, self.ground_rect)
        pass

    def update(self):
        self.ground_rect = self.ground.get_rect(
            bottomleft=(self.ground_x, ScreenHeight))

        # if ground img out of screen -> pull it back to screen
        if abs(self.ground_x) > 30:
            self.ground_x = 0
        pass


class Bird(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.images = []
        self.index = 0
        self.counter = 0  # number of iterations of update function
        self.cooldown = 3  # number of iterations to change status
        # showing 3 kinds of birds
        for index in range(1, 4):
            image = pg.image.load(
                r'old_mission\flappybird\bird' + str(index) + '.png')
            self.images.append(image)

        # rescale bird to some resolution
        self.image = self.images[self.index]
        self.image = pg.transform.scale(
            self.image, (int(50 * 1.2), int(35 * 1.2)))
        self.rect = self.image.get_rect(center=(x, y))

        self.velocity = 0.5
        self.clicked = False
        self.flying = True
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        '''Wings Animation'''
        self.image = self.images[self.index]
        self.counter += 1

        if self.counter > self.cooldown:
            self.counter = 0
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        '''Rotate Mechanism'''
        self.image = pg.transform.rotate(
            self.images[self.index], self.velocity * -3)

        '''Gravity'''
        if self.flying == False:
            self.flying = True
        self.velocity += 0.5
        if self.rect.bottom < 768 - 150:
            self.rect.y += int(self.velocity)
        else:
            self.flying = False

        if self.velocity > 8:  # highest velocity
            self.velocity = 8
        pass

        '''Jump Mechanism'''
        # print(self.clicked)
        if pg.mouse.get_pressed()[0] == 1 and self.clicked == False and self.rect.top > 30:
            self.clicked = True
            self.velocity = -10
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
    pass


class Pipe(pg.sprite.Sprite):
    def __init__(self, x, y, position, gap_position):
        pg.sprite.Sprite.__init__(self)
        self.image = pipe_img
        self.rect = self.image.get_rect()

        self.gap = 150  # the space between up pipe and down pipe
        # position = 1 is top, = -1 is bottom
        if position == 1:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect.bottomleft = (
                x, y - 100 - int(self.gap / 2) - gap_position)

        if position == -1:
            self.rect.topleft = (
                x, y - 100 + int(self.gap / 2) - gap_position)
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

    def update(self):
        
        if self.rect.right < 0:
            self.kill()
        pass


class Restart():
    def __init__(self):
        self.game_over = False
        self.restart_button = pg.image.load(r'old_mission\flappybird\restart.png')
        self.restart_rect = self.restart_button.get_rect(
            center=(ScreenWidth // 2, ScreenHeight // 2))
        pass

    def draw(self):
        if self.game_over == True:
            Screen.blit(self.restart_button, self.restart_rect)
        pass

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        if self.restart_rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.game_over:
                self.game_over = False
                scoreboard.score = 0
        pass

    def reset(self):
        # pipe_group.empty()
        # bird.rect.x = 100
        # bird.rect.y = int(ScreenHeight / 2) - 100
        pass

'''
TESTING HERE
'''

if __name__ == '__main__':
    flappy_theme = FlappyBirdTheme()
    flappy_theme.prior_game_loop()
    while True:
        if flappy_theme.end_theme == True:
            pg.quit()
            sys.exit()
        flappy_theme.game_loop()
        # check event

        for event in pg.event.get():
            if event.type == pg.QUIT:
                shutil.rmtree(r'__pycache__')  # delete cache folder
                pg.quit()
                sys.exit()
                
        fps_clock()
        update_screen()
