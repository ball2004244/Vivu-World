import pygame as pg
from pygame.locals import *
import sys 
import shutil 
from random import randint
sys.path.append('../Vivu-World')
from setup import *

pg.init()

# Init
game_speed = 6
pipe_img = pg.image.load(r'old_mission\flappybird\pipe.png').convert_alpha()
pipe_img = pg.transform.scale(pipe_img, (78 * 24 // 35, 560 * 24 // 35))

background_img = pg.image.load(r'old_mission\flappybird\background.png').convert_alpha()
background_img = pg.transform.scale(background_img, (ScreenWidth, ScreenHeight))

ground_img = pg.image.load(r'old_mission\flappybird\ground.png').convert_alpha()
ground_img = pg.transform.scale(ground_img, (ScreenWidth + 50, ScreenHeight // 5))
class FlappyBirdTheme():
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
        self.ground_speed = game_speed
        pass

    def draw(self):
        Screen.blit(self.ground, self.ground_rect)
        pass

    def update(self):
        self.ground_rect = self.ground.get_rect(
            bottomleft=(self.ground_x, ScreenHeight))
        self.ground_x -= self.ground_speed

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
        self.rect.x -= game_speed
        if self.rect.right < 0:
            self.kill()
        pass


class ScoreBoard():
    def __init__(self):
        self.value = 0
        self.pass_pipe = False
        pass

    def draw(self):
        self.text_surf = pg.font.Font.render(
            FontType.FONT1, str(self.value), True, Colors.WHITE)
        self.text_rect = self.text_surf.get_rect(
            center=(ScreenWidth // 2, ScreenHeight // 14))
        Screen.blit(self.text_surf, self.text_rect)
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
                score.value = 0
        pass

    def reset(self):
        pipe_group.empty()
        bird.rect.x = 100
        bird.rect.y = int(ScreenHeight / 2) - 100
        pass


# Initialize
last_pipe = pg.time.get_ticks()
pipe_frequency = 1500  # miliseconds

flappy_theme = FlappyBirdTheme()
ground = Ground()
score = ScoreBoard()
restart = Restart()

bird = Bird(100, int(ScreenHeight / 2) - 100)
bird_group = pg.sprite.Group()
bird_group.add(bird)

pipe_group = pg.sprite.Group()
top_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), 1, 0)
bottom_pipe = Pipe(ScreenWidth, int(ScreenHeight / 2), -1, 0)
pipe_group.add(top_pipe)
pipe_group.add(bottom_pipe)

'''
TESTING HERE
'''
if __name__ == '__main__':
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
            gap_position = randint(-50, 125)
            top_pipe = Pipe(ScreenWidth, int(
                ScreenHeight / 2), 1, gap_position)
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
