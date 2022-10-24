import sys
import pygame as pg
from pygame.locals import *
sys.path.append('../Vivu-World')
from setup import *
from database.database import import_data
from new_mission.general import *
pg.init()

theme_zero_img = pg.image.load(r'theme\1.jpg').convert_alpha()
theme_zero_img = pg.transform.scale(theme_zero_img, (ScreenWidth, ScreenHeight))

cursor_img = pg.image.load(r'new_mission\zombie_slap\swatter.png').convert_alpha()
cursor_img = pg.transform.scale(cursor_img, (1, 1))

class Button(pg.sprite.Sprite):
    def __init__(self, text, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.top_size = (x, y, width, height)
        self.bot_size = (x + 5, y + 5, width, height)
        self.text = text

        self.text_surf = pg.font.Font.render(
            FontType.FONT3, self.text, True, Colors.WHITE)
        self.text_rect = self.text_surf.get_rect(
            center=(x + width // 2, y + height // 2))
        self.rect = self.text_rect
        pass

    def draw(self):
        self.bot_rect = pg.draw.rect(
            Screen, Colors.BLACK, self.bot_size)
        self.top_rect = pg.draw.rect(
            Screen, Colors.DARK_YELLOW, self.top_size)

        self.rect = self.top_rect
        Screen.blit(self.text_surf, self.text_rect)
        pass

    pass

class Cursor(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = cursor_img
        self.rect = self.image.get_rect()
        pass

    def draw(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.rect = self.image.get_rect(center=(mouse_x, mouse_y))
        Screen.blit(self.image, self.rect)
        pass

class Theme():
    def __init__(self) -> None:
        self.clicked = False
        self.end_theme = False
        self.user_choice = None
        pass
    def prior_game_loop(self) -> None:
        pass

    def game_loop(self) -> None:
        pass
    def draw(self) -> None:
        Screen.blit(self.image, self.rect)
        pass
    pass

class ThemeZero(Theme):
    def __init__(self):
        Theme.__init__(self)
        self.image = pg.image.load(r'theme\0.jpg').convert_alpha()
        self.image = pg.transform.scale(
            self.image, (ScreenWidth, ScreenHeight))
        self.rect = self.image.get_rect(topleft=(0, 0))

        self.button_row_x = 690
        self.button_row_y = 90
        self.button_step = 110
        self.button_width = 180
        self.button_height = self.button_width // 3
        self.image = theme_zero_img
        self.rect = self.image.get_rect()

        self.start_group = pg.sprite.Group()
        self.continue_group = pg.sprite.Group()
        self.settings_group = pg.sprite.Group()
        self.exit_group = pg.sprite.Group()
        self.cursor_group = pg.sprite.Group()
        pass

    def prior_game_loop(self):
        '''CREATE BUTTONS'''
        self.start_button = Button('NEW GAME', self.button_row_x, self.button_row_y +
                                   self.button_step, self.button_width, self.button_height)
        self.continue_button = Button('CONTINUE', self.button_row_x, self.button_row_y +
                                      2 * self.button_step, self.button_width, self.button_height)
        self.settings_button = Button('SETTINGS', self.button_row_x, self.button_row_y +
                                     3 * self.button_step, self.button_width, self.button_height)
        self.exit_button = Button('EXIT', self.button_row_x, self.button_row_y +
                                  4 * self.button_step, self.button_width, self.button_height)
        
        self.start_group.add(self.start_button)
        self.continue_group.add(self.continue_button)
        self.settings_group.add(self.settings_button)
        self.exit_group.add(self.exit_button)

        '''CREATE CURSOR'''
        self.cursor = Cursor()
        self.cursor_group.add(self.cursor)
        pass

    def game_loop(self):
        if not self.end_theme:
            self.draw()
            self.check_click()
        pass
    
    def draw(self):
        title_pic = pg.image.load(r'theme\vivuworld.png')
        Screen.blit(pg.transform.rotate(title_pic, -90),
                    (20, 40))  # rotate game title
        Screen.blit(self.image, self.rect)
    
        self.cursor.draw()
        self.start_button.draw()
        self.continue_button.draw()
        self.settings_button.draw()
        self.exit_button.draw()
        pass

    def check_click(self):
        if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
            # click start button
            if pg.sprite.groupcollide(self.start_group, self.cursor_group, False, False):                    
                print('CLICK New Game')
                self.end_theme = True
                pass

            # click continue 
            if pg.sprite.groupcollide(self.continue_group, self.cursor_group, False, False): 
                print('CLICK Continue')
                self.end_theme = True
                self.user_choice = 1
                pass   
            
            # click settings
            if pg.sprite.groupcollide(self.settings_group, self.cursor_group, False, False):                    
                print('CLICK Settings')
                self.end_theme = True
                self.user_choice = 2
                pass 
            
            # click exit
            if pg.sprite.groupcollide(self.exit_group, self.cursor_group, False, False):                    
                print('CLICK Exit')
                quit_game()
            self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        pass

class Setting(Theme):
    def __init__(self) -> None:
        Theme.__init__(self)
        self.image = pg.image.load(r'theme\test.jpg').convert_alpha()
        self.image = pg.transform.scale(
            self.image, (ScreenWidth, ScreenHeight))
        self.rect = self.image.get_rect(topleft=(0, 0))
        pass

    def prior_game_loop(self) -> None:
        pass 
    
    def game_loop(self) -> None:
        self.draw()
        pass

    def draw(self) -> None:
        Screen.blit(self.image, self.rect)
        pass

class SavingTheme(Theme):
    def __init__(self) -> None:
        Theme.__init__(self)
        self.image = pg.image.load(r'theme\test.jpg').convert_alpha()
        self.image = pg.transform.scale(
            self.image, (ScreenWidth, ScreenHeight))
        self.rect = self.image.get_rect(topleft=(0, 0))

        self.saveslot_group = pg.sprite.Group()
        self.cursor_group = pg.sprite.Group()
        pass

    def prior_game_loop(self) -> None:
        self.saveslot_one = Button('LOAD SAVESLOT 1', ScreenWidth // 2 - 200, ScreenHeight // 2 - 100, 400, 200)
        self.saveslot_group.add(self.saveslot_one)

        self.cursor = Cursor()
        self.cursor_group.add(self.cursor)
        pass

    def game_loop(self) -> None:
        self.draw()
        self.check_click()
        pass

    def draw(self) -> None:
        Screen.blit(self.image, self.rect)
        self.cursor.draw()
        self.saveslot_one.draw()
        pass

    def check_click(self) -> None:
        if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
            # click load game
            if pg.sprite.spritecollideany(self.cursor, self.saveslot_group):                    
                print('CLICK Load Game')
                self.process_data()

                # navigate to previous game stage
                # self.end_theme = True
                pass

            self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        pass
    def process_data(self) -> None:
        ingame_data = import_data('database.json')

        '''GENERAL DATA'''
        highest_score = ingame_data['highest-score']

        '''SPECIFIC DATA'''
        # slot 1 
        slot1_data = ingame_data['slot1']

        if slot1_data['status'] == 'SAVED':
            scoreboard.score = slot1_data['score']
            scoreboard.round = slot1_data['current-round']

        print(ingame_data)
        pass 

    def load_previous_game(self) -> None:
        pass
# class Theme():
#     def __init__(self, theme_num):
#         self.theme_num = theme_num
#         self.image = pg.image.load(r'theme\\' + str(theme_num) + '.jpg')
#         self.image = pg.transform.scale(
#             self.image, (ScreenWidth, ScreenHeight))
#         self.rect = self.image.get_rect(topleft=(0, 0))
#         pass

#     def draw(self):
#         Screen.blit(self.image, self.rect)
#         pass
#     pass


if __name__ == '__main__':
    theme0 = ThemeZero()
    save_theme = SavingTheme()
    theme_list = [ThemeZero(), SavingTheme(), Setting()]
    theme_index = 0

    current_theme = theme_list[theme_index]
    current_theme.prior_game_loop()
    while True:
        Screen.fill(Colors.WHITE)
        current_theme.game_loop()
        
        if current_theme.end_theme == True:
            if current_theme.user_choice != None:
                current_theme = theme_list[current_theme.user_choice]
            current_theme.prior_game_loop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
        fps_clock()
        update_screen()
    pass
    