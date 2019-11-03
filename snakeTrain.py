import math
import random
import pygame
from snake import *
from generation import *
from cube import *
import math
import tkinter as tk
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
        

def redrawWindow(surface, snake, snack):
    global rows, width
    surface.fill((0,0,0))
    snake.draw(surface)
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



def main():
    global width, rows, s, snack

    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    

    gen = Generation(2)
    
    trainingSnakes = gen.train_snakes

    food = {}

    for i in range(gen.population):
        food[i] = cube(randomSnack(rows, trainingSnakes[i]), color=(0,255,0))

    print(food[0])
    
    flag = True
    clock = pygame.time.Clock()
    
    while flag:
        #pygame.time.delay(500)
        clock.tick(10)

        trainingSnakes[0].move(food[0].pos)

        if trainingSnakes[0].body[0].pos == food[0].pos:
            trainingSnakes[0].addCube()
            food[0] = cube(randomSnack(rows, trainingSnakes[0]), color=(0,255,0))

        print(trainingSnakes[0].dead()) #check for death
        redrawWindow(win, trainingSnakes[0], food[0])

main()