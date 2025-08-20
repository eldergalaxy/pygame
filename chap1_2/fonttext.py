import pygame, sys
from pygame.locals import *


pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption(("hello world"))

WHITE = (255,255,255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

font_path = pygame.font.match_font('forte')
fontObj = pygame.font.Font(font_path, 32)
textSurfaceObj= fontObj.render('hello world', False, RED, None)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

#create a sound obj
soundObj = pygame.mixer.Sound('Sounds\sunflower.mp3')

while True: #main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                soundObj.play()
    pygame.display.update()