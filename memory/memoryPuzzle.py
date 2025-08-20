# Memory Puzzle
# By Al Sweigart

import random, pygame, sys
import utils.crayola64 as cr
from pygame.locals import *

FPS = 30 #frames per second, the general speed of the game
WINDOWWIDTH = 640 # size of the window's width in pixels
WINDOWHEIGHT = 480 # size of the window's height in pixels
REVEALSPEED = 8 #speed boxes sligding reveals and covers
BOXSIZE = 40 # size of box height and width in pixels
GAPSIZE = 10 # size of game between boxes in pixels
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number or rows of icons

assert(BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

BGCOLOR = cr.NAVYBLUE
LIGHTBGCOLOR = cr.GRAY
BOXCOLOR = cr.WHITE
HIGHLIGHTCOLOR = cr.BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (cr.RED, cr.GREEN, cr.BLUE, cr.YELLOW, cr. ORANGE, cr.PURPLE, cr.CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

