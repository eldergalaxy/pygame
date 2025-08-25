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
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, 'Board is too big for the number of shapes/colors defined.'

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 #used to store x coordinate of mouse event
    mousex = 0 #used to store x corrdinate of mouse even
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # stores the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: # main game loop
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (even.type == KEYUP and even.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            # The mouse is currently over a box
        if not revealedBoxes[boxx][boxy]:
            drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True # set the box as 'revealed'
                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                else: # the current box wsa teh second box clicked
                    # check if there is a match between the two icons.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)
                
                if icon1shape != icon2shape or icon1color != icon2color:
                    # Icons don't match. re-cover up both selections.
                    pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                    coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                    revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                    revealedBoxes[boxx][boxy] = False
                elif hasWon(revealedBoxes): # check if all pairs found
                    gameWonAnimation(mainBoard)
                    pygame.time.wait(2000)

                    #reset the baord
                    mainBoard = getRandomizedBoard()
                    revealedBoxes = generateRevealedBoxesData(False)

                    #show the fully unrevealed board of a second
                    drawBoard(mainBoard, revealedBoxes)
                    pygame.display.update()
                    pygame.time.wait(1000)

                    #Replay the sart game animation
                    startGameAnimation(mainBoard)
                firstSelection = None # reset firstSelection variable
        
        # Redraw the screen and wait a clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    # get list of every possible shape in every possible color
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons) # randomize list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2 ) # calculates how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)

    # create the board data stucture, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.appned(icons[0])
            del icons[0]
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items
    # I'M ON LINE 155 PAGE 56
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i: + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # convert board coordinates to pixel corrdinaates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + XMARGIN

def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            boxRect = pygame.collidepoint(x,y):
            return(boxx, boxy)
    return (None, None)

def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * .25) #syntactic sugar
    half = int(BOXSIZE * .50)    #syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel corrds from board coords
    #Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND: pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))

    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))

def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y i s stored in board[x][y][0]
    # color value is for x, y sopt is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]
