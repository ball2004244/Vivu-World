
import pygame as pg
import sys
import shutil
from setup import Screen, Colors, Screen, fps_clock, update_screen, ScreenWidth, ScreenHeight, FontType

pg.init()

'''This Button contain 2 layers rectangles, named "top" and "bot"'''


class Button():
    def __init__(self, text, x, y, width, height):
        self.top_size = (x, y, width, height)
        self.bot_size = (x + width // 100, y + y // 30, width, height)

        self.text_surf = pg.font.Font.render(
            FontType.FONT1, text, True, Colors.WHITE)
        self.text_rect = self.text_surf.get_rect(
            center=(x + width // 2, y + height // 2))

        self.pressed = False
        pass

    def draw(self):
        self.bot_rect = pg.draw.rect(
            Screen, Colors.BLACK, self.bot_size)
        self.top_rect = pg.draw.rect(
            Screen, Colors.MIDNIGHT_BLUE, self.top_size)
        Screen.blit(self.text_surf, self.text_rect)
        pass

    def check_click(self):
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = Colors.RED
            self.pressed = True
            print('Click')
        else:
            self.pressed = False

        if self.pressed:
            # do something when hit a button
            pass
        pass
    pass


# init variables for game loop
button1 = Button('Click', 200, 100, 210, 70)

while True:
    # draw
    Screen.fill(Colors.WHITE)
    button1.draw()

    # update
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            button1.check_click()

    fps_clock()
    update_screen()
