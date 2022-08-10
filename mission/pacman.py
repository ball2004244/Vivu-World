import pygame as pg
from pygame.locals import *
from setup import Screen, ScreenWidth, ScreenHeight, FontType, Colors

pg.init()

# Init
class Pacman():
    def __init__(self):
        self.image = pg.image.load(r'mission\pacman\pacman.png')
        self.image = pg.transform.scale(
            self.image, (72, 40))

        self.rect = self.image.get_rect()
        pass

    def draw(self):
        Screen.blit(self.image, self.rect)
        pass 
    
    def update(self):
        pass

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
  
        self.image = pg.Surface([width, height])
        self.image.fill(Colors.RED)
  
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

def RoomOne(all_sprites_list):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list = pg.sprite.RenderPlain()
     
    # This is a list of walls. Each is in the form [x, y, width, height]
    walls = [ [0,0,6,600],
              [0,0,600,6],
              [0,600,606,6],
              [600,0,6,606],
              [300,0,6,66],
              [60,60,186,6],
              [360,60,186,6],
              [60,120,66,6],
              [60,120,6,126],
              [180,120,246,6],
              [300,120,6,66],
              [480,120,66,6],
              [540,120,6,126],
              [120,180,126,6],
              [120,180,6,126],
              [360,180,126,6],
              [480,180,6,126],
              [180,240,6,126],
              [180,360,246,6],
              [420,240,6,126],
              [240,240,42,6],
              [324,240,42,6],
              [240,240,6,66],
              [240,300,126,6],
              [360,240,6,66],
              [0,300,66,6],
              [540,300,66,6],
              [60,360,66,6],
              [60,360,6,186],
              [480,360,66,6],
              [540,360,6,186],
              [120,420,366,6],
              [120,420,6,66],
              [480,420,6,66],
              [180,480,246,6],
              [300,480,6,66],
              [120,540,126,6],
              [360,540,126,6]
            ]
     
    # Loop through the list. Create the wall, add it to the list
    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3], Colors.BLUE)
        wall_list.add(wall)
        all_sprites_list.add(wall)
         
    # return our new list
    return wall_list

main_char = Pacman()