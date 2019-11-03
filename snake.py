import math
import random
import pygame
from cube import *
from gene import *
import math
import tkinter as tk
from tkinter import messagebox

class snake(object):
    body = []
    turns = {}

    vision = {'v1':[], 'v2':[], 'v3':[], 'v4':[], 'v5':[], 'v6':[], 'v7':[], 'v8':[]}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        
        self.dirnx = 0
        self.dirny = 1

        self.g = Gene()

    def makeNewGene(self):
        self.g = Gene()
        
    def getVision(self):
        return self.vision

    def moveLeft(self):
        self.dirnx = -1
        self.dirny = 0
        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def moveRight(self):
        self.dirnx = 1
        self.dirny = 0
        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
    
    def moveup(self):
        self.dirnx = 0
        self.dirny = -1
        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def movedown(self):
        self.dirnx = 0
        self.dirny = 1
        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def detectwall(self):
        rightborder = abs(19-self.head.pos[0])
        leftborder = abs(0-self.head.pos[0])
        upborder = abs(0-self.head.pos[1])
        downborder = abs(19-self.head.pos[1])
        return (upborder, rightborder, downborder, leftborder)
    
    def detectbody(self):
        # walltosnake = self.detectwall()
        [up, ri, do, le] = [0, 0, 0, 0]
        for x in range(len(self.body)):
            rightbody = range((self.body[0].pos[0]+1), 19)
            leftbody = range(0, self.body[0].pos[0])
            upbody = range(0, self.body[0].pos[1])
            downbody = range(self.body[0].pos[1]+1, 19)
            for y in range(len(rightbody)):
                if(rightbody[y] == self.body[x].pos[0]):
                    ri = 1
            for z in range(len(leftbody)):
                if(leftbody[z] == self.body[x].pos[0]):
                    le = 1
            for w in range(len(upbody)):
                if(upbody[w] == self.body[x].pos[1]):
                    up = 1
            for u in range(len(downbody)):
                if(downbody[u] == self.body[x].pos[1]):
                    do = 1    

        return [up, ri, do, le]   

    def seeingAlgo(self, snackPos):

        d1, d2, d3, d4 = [False, False, False, False]
    
        if  not ((self.head.pos[1] - snackPos[1] == 0) or (self.head.pos[0] - snackPos[0]) == 0):
            if((self.head.pos[0] - snackPos[0] <= 0) and  (self.head.pos[1] - snackPos[1] >=0) and (abs((self.head.pos[1] - snackPos[1]) / (self.head.pos[0] - snackPos[0])) == 1)):
                d1 = True
            elif((self.head.pos[0] - snackPos[0] <= 0) and (self.head.pos[1] - snackPos[1] <=0) and ((self.head.pos[1] - snackPos[1]) / (self.head.pos[0] - snackPos[0])) == 1):
                d2 = True
            elif((self.head.pos[0] - snackPos[0] >= 0) and (self.head.pos[1] - snackPos[1] <=0) and (abs((self.head.pos[1] - snackPos[1]) / (self.head.pos[0] - snackPos[0])) == 1)):
                d3 = True
            elif((self.head.pos[0] - snackPos[0] >= 0) and (self.head.pos[1] - snackPos[1] >=0) and ((self.head.pos[1] - snackPos[1]) / (self.head.pos[0] - snackPos[0])) == 1):
                d4 =True

        headtoborder = self.detectwall()   #(self.head.pos[1] - snackPos[1] == 0) and (self.head.pos[1] - snackPos[1] >= 0)
        bodypos = self.detectbody()
        
        self.vision['v1'] = [headtoborder[0], bodypos[0], int(((self.head.pos[0] - snackPos[0] == 0) and (self.head.pos[0] - snackPos[0] >= 0)))]
        self.vision['v2'] = int(d1)
        self.vision['v3'] = [headtoborder[1], bodypos[1], int(((self.head.pos[1] - snackPos[1] == 0) and (self.head.pos[1] - snackPos[1] >= 0)))]
        self.vision['v4'] = int(d2)
        self.vision['v5'] = [headtoborder[2], bodypos[2], int(((self.head.pos[0] - snackPos[0] == 0) and (self.head.pos[0] - snackPos[0] <= 0)))]
        self.vision['v6'] = int(d3)
        self.vision['v7'] = [headtoborder[3], bodypos[3], int(((self.head.pos[0] - snackPos[0] == 0) and (self.head.pos[0] - snackPos[0] >= 0)))]
        self.vision['v8'] = int(d4)
        
    def dead(self):

        
        if ( (self.head.pos[0] == 0 or self.head.pos[0] == 19) or (self.head.pos[1] == 0 or self.head.pos[1] == 19)):
            print('Score: ', len(self.body))
            self.reset((10,10))
            return True
        
        
        for x in range(len(self.body)):
            if self.body[x].pos in list(map(lambda z:z.pos,self.body[x+1:])):
                print('Score: ', len(self.body))
                self.reset((10,10))
                return True

        

        return False
        
        
        

        


    
    def move(self, snackPos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.moveLeft()

                elif keys[pygame.K_RIGHT]:
                    self.moveRight()

                elif keys[pygame.K_UP]:
                    self.moveup()

                elif keys[pygame.K_DOWN]:
                    self.movedown()


        self.seeingAlgo(snackPos)

        

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)
        
        

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
        

    def draw(self, surface):

        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)