import pygame, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from utils import crayola64 as cr
from pygame.locals import *


pygame.init()

#set up the display window
DISPLAYSURF = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

#draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, cr.ALMOND, ((146,0), (291, 106), (236,277), (56, 277), (0, 106))) 
pygame.draw.line(DISPLAYSURF, RED, (60,60), (120,60), (4))
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, WHITE, (100,250), 60, 0)
pygame.draw.ellipse(DISPLAYSURF, BLUE, (300, 250, 180, 80), 0)
pygame.draw.rect(DISPLAYSURF, BLUE, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj



#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()