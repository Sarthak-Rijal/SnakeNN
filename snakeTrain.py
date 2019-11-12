import math
import random
import pygame
from snake import *
from cube import *
import math
from tkinter import messagebox



def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
        

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(1,rows-1)
        y = random.randrange(1,rows-1)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)


def calculateFitness(steps, apples, stalled=False):
    if (stalled):
        return (steps/4) + (apples * 100000.0)
    return (steps/2) + (apples * 100000.0)


def main():
    global width, rows, s, snack

    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    
    s = snake((255,0,0), (10,10))
    snack = cube(randomSnack(rows, s), color=(0,255,0))

    flag = True
    clock = pygame.time.Clock()

    dnaFitness = {}

    counter = 0
    

    #metrics 
    apples = 0
    steps = 0

    while flag:
        #pygame.time.delay(500)
        clock.tick(10)
        s.move(snack.pos)

        #---------------------------------------------------
        #update metrics
        steps += 1
        apples = len(s.body)
        alleal = s.g.alleles

        #------------------------------------------------------
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0,255,0))

        
        if (s.dead() or steps-apples == 50):
            if (steps-apples == 50):
                s.reset
            print(dnaFitness)
            if (counter < 10):
                dnaFitness [counter] = (calculateFitness(steps, apples), alleal)
                s.makeNewGene()

            

        redrawWindow(win)

main()