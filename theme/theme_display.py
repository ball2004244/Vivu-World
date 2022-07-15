import pygame as pg
from setup import *

pg.init()

class Button():
    def __init__(self, text, x, y, width, height):
        self.top_size = (x, y, width, height)
        self.bot_size = (x + 5, y + 5, width, height)
        self.text = text

        self.text_surf = pg.font.Font.render(
            FontType.FONT3, self.text, True, Colors.WHITE)
        self.text_rect = self.text_surf.get_rect(
            center=(x + width // 2, y + height // 2))

        self.pressed = False
        pass

    def draw(self):
        self.bot_rect = pg.draw.rect(
            Screen, Colors.BLACK, self.bot_size)
        self.top_rect = pg.draw.rect(
            Screen, Colors.DARK_YELLOW, self.top_size)
        Screen.blit(self.text_surf, self.text_rect)
        pass

    def check_click(self):
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            print(str(self.text) + ' Clicked')
            return True
        return False
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


class ThemeZero(Theme):
    def __init__(self):
        Theme.__init__(self, 0)
        self.button_row_x = 690
        self.button_row_y = 90
        self.button_step = 110
        self.button_width = 180
        self.button_height = self.button_width // 3

        self.start_button = Button('NEW GAME', self.button_row_x, self.button_row_y +
                                   self.button_step, self.button_width, self.button_height)
        self.continue_button = Button('CONTINUE', self.button_row_x, self.button_row_y +
                                      2 * self.button_step, self.button_width, self.button_height)
        self.setting_button = Button('SETTING', self.button_row_x, self.button_row_y +
                                     3 * self.button_step, self.button_width, self.button_height)
        self.exit_button = Button('EXIT', self.button_row_x, self.button_row_y +
                                  4 * self.button_step, self.button_width, self.button_height)
        pass

    def draw(self):
        Theme.draw(self)
        title_pic = pg.image.load(r'theme\vivuworld.png')
        Screen.blit(pg.transform.rotate(title_pic, -90),
                    (20, 40))  # rotate game title

        self.start_button.draw()
        self.continue_button.draw()
        self.setting_button.draw()
        self.exit_button.draw()
        pass

    def update(self):
        if self.continue_button.check_click():
            saved_theme_num = -5 # the index of save screen

            file_save = open('save.txt', 'r')
            file_save.close()
            #return saved_theme_num
            pass

        if self.setting_button.check_click():
            setting_theme_num = -4 # the index of setting screen
            #return setting_theme_num
            pass

        if self.exit_button.check_click():
            quit_game()
        pass
    def new_game(self, theme_num):
        return theme_num + 1
    
class ThemeOne(Theme):
    def __init__(self):
        Theme.__init__(self, 1)
        pass
    def update(self):
        pass