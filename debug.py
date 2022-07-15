import pygame as pg
import sys
import shutil
from setup import *
from character.main_character import MainChar, TextBox
from theme.theme_display import Setting

# init
setting = Setting()
main_char = MainChar()
text_box = TextBox('Tam Ng', 'Hello everybody, my name is T')
while True:
    # draw
    Screen.fill(Colors.WHITE)
    setting.draw()
    main_char.draw()
    text_box.draw()
    # update 
    
    # check event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            shutil.rmtree(r'__pycache__')  # delete cache folder
            pg.quit()
            sys.exit()

        # check mouse click
        if event.type == pg.MOUSEBUTTONUP:
            pass
            
        # check button hit
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pass

    fps_clock()
    update_screen()