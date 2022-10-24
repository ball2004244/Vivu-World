import sys
import pygame as pg
from pygame.locals import *
sys.path.append('../Vivu-World')
from setup import *

pg.init()

class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.current_round = 0
        pass

    def draw(self):
        self.text_surf = pg.font.Font.render(
            FontType.FONT1, str(self.score), True, Colors.RED)
        self.text_rect = self.text_surf.get_rect(
            center=(ScreenWidth // 2, ScreenHeight // 14))
        Screen.blit(self.text_surf, self.text_rect)
        pass
    
    def add_score(self):
        self.score += 1
        pass

class Minigame():
    def __init__(self) -> None:
        self.reset()
        self.game_speed = 5
        self.time_limit = 5
        pass

    def mechanism(self) -> None:
            if self.game_over == True:
                self.end_theme = True

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    shutil.rmtree(r'__pycache__')  # delete cache folder
                    pg.quit()
                    sys.exit()
            pass 
    
    def reset(self) -> None:
        self.game_over = False
        self.end_theme = False
        self.clicked = False
        pass

    def prior_game_loop(self) -> None:
        self.reset()
        self.start = pg.time.get_ticks()
        pass

scoreboard = ScoreBoard()