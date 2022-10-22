import pygame as pg
from setup import *

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

class Setting():
    def __init__(self):
        self.image = pg.image.load(r'theme\test.jpg')
        self.image = pg.transform.scale(
            self.image, (ScreenWidth, ScreenHeight))
        self.rect = self.image.get_rect(topleft=(0, 0))
        pass
    def draw(self):
        Screen.blit(self.image, self.rect)
        pass

class Theme():
    def __init__(self, theme_num):
        self.theme_num = theme_num
        self.image = pg.image.load(r'theme\\' + str(theme_num) + '.jpg')
        self.image = pg.transform.scale(
            self.image, (ScreenWidth, ScreenHeight))
        self.rect = self.image.get_rect(topleft=(0, 0))
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass
    pass


class ThemeZero():
    def __init__(self):
        Theme.__init__(self, 0)
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

        self.end_theme = False
        pass

    def prior_game_loop(self):
        self.clicked = False
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
                pass   
            
            # click settings
            if pg.sprite.groupcollide(self.settings_group, self.cursor_group, False, False):                    
                print('CLICK Settings')
                pass 
            
            # click exit
            if pg.sprite.groupcollide(self.exit_group, self.cursor_group, False, False):                    
                print('CLICK Exit')
                quit_game()
            self.clicked = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False


            pass 
        pass
    