import pygame

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480), FULLSCREEN)
# get the size of the fullscreen display
x, y = screen.get_size()
print(x, y)