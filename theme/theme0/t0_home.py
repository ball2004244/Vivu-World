'''This is a starting screen'''
import pygame as pg
from pygame.locals import *
from setup import Screen, Colors, FontType, ScreenWidth, ScreenHeight

pg.init()


def load_image(url):
    return pg.image.load(url)


class ThemeZero():
    def __init__(self):
        button_row_x = 690
        button_row_y = 90
        button_step = 110
        button_width = 180
        button_height = button_width // 3
        self.start_button = Button('NEW GAME', button_row_x, button_row_y +
                                   button_step, button_width, button_height, self.new_game)
        self.continue_button = Button('CONTINUE', button_row_x, button_row_y +
                                      2 * button_step, button_width, button_height, self.cont_game)
        self.setting_button = Button('SETTING', button_row_x, button_row_y +
                                     3 * button_step, button_width, button_height, self.setting)
        self.exit_button = Button('EXIT', button_row_x, button_row_y +
                                  4 * button_step, button_width, button_height, self.exit_game)
        pass

    def draw(self):
        Screen.blit(load_image(r'theme\theme0\t0.jpg'), (0, 0))
        title_pic = load_image(r'theme\theme0\vivuworld.png')
        Screen.blit(pg.transform.rotate(title_pic, -90), (20, 40))

        self.start_button.draw()
        self.continue_button.draw()
        self.setting_button.draw()
        self.exit_button.draw()
        pass

    def update(self):
        pass

    def check_click(self):
        self.start_button.check_click()
        pass

    def new_game(self):
        # theme1.draw()
        # under construction
        pass

    def cont_game(self):
        # load save files from notepad
        pass

    def setting(self):
        pass

    def exit_game(self):
        pass
    pass


class Button():
    def __init__(self, text, x, y, width, height, function):
        self.top_size = (x, y, width, height)
        self.bot_size = (x + 5, y + 5, width, height)

        self.text_surf = pg.font.Font.render(
            FontType.FONT3, text, True, Colors.WHITE)
        self.text_rect = self.text_surf.get_rect(
            center=(x + width // 2, y + height // 2))

        self.pressed = False
        self.function = function()  # What can a button do after click
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
            self.pressed = True
            print('Click')
        else:
            self.pressed = False

        if self.pressed:
            # self.function()
            pass
        pass
    pass
