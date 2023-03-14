import sys
import pygame as pg
from pygame.locals import *
sys.path.append('../Vivu-World')
from setup import *
from database.database import import_data, export_data

pg.init()

class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.highest_score = 0
        self.round = 1
        pass

    def draw(self) -> None:
        self.text_surf = pg.font.Font.render(
            FontType.FONT1, str(self.score), True, Colors.RED)
        self.text_rect = self.text_surf.get_rect(
            center=(ScreenWidth // 2, ScreenHeight // 14))
        Screen.blit(self.text_surf, self.text_rect)
        pass
    
    def add_score(self) -> None:
        self.score += 1
        pass

    def update(self) -> None:
        # update highest score
        if self.score > self.highest_score:
            self.highest_score = self.score
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

class System():
    def __init__(self):
        self.choice_list = []
        self.user_choice = None 

    def process_data(self) -> None:
        self.ingame_data = import_data('database.json')

        '''GENERAL DATA'''
        scoreboard.highest_score = self.ingame_data['highest-score']

        '''SPECIFIC DATA'''
        # slot 1 
        slot1_data = self.ingame_data['slot1']

        if slot1_data['status'] == 'SAVED':
            scoreboard.score = slot1_data['score']
            scoreboard.round = slot1_data['current-round']
        else:
            print('Cannot Load Slot 1')
            raise ValueError 

        print(self.ingame_data)
        pass 

    def save_game(self) -> None:
        self.ingame_data = {
            'highest-score': scoreboard.highest_score,
            'slot1': {
                'score': scoreboard.score,
                'current-round': scoreboard.round,
                'status': 'SAVED',
            },
            'slot2': {
                'score': None,
                'current-round': None,
                'status': 'EMPTY',
            },
            'slot3': {
                'score': None,
                'current-round': None,
                'status': 'EMPTY',
            },
        }
        # run this function to save data
        export_data(self.ingame_data, 'database.json')
        pass 

    def reset_data(self) -> None:
        self.choice_list = []
        self.user_choice = None
        
        self.ingame_data = {
            'highest-score': scoreboard.highest_score,
            'slot1': {
                'score': None,
                'current-round': None,
                'status': 'EMPTY',
            },
            'slot2': {
                'score': None,
                'current-round': None,
                'status': 'EMPTY',
            },
            'slot3': {
                'score': None,
                'current-round': None,
                'status': 'EMPTY',
            },
        }
        pass 
system = System()
scoreboard = ScoreBoard()

if __name__ == '__main__':
    pass