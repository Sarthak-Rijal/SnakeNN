import math
import random
import pygame
from snake import *
import math


class cube(object):
    rows = 20
    w = 500
    def __init__(self,start, type, direction = (1, 0),color=(255,0,0)):
        self.pos = start
        self.direction = direction
        self.color = color

    #sets which direction the cube is moving
    def setDirection(self, newDirection):
        self.direction = newDirection
    
    #constantly updates the postion of the snake
    def move(self):
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    
    def update(self, surface, eyes = False):

        self.move()

        dis = self.w // self.rows

        i = self.pos[0]
        j = self.pos[1]

        #the +1 and -2 add a cool pop out effect
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-3, dis-3))
        
        if eyes:
            centre = dis//2
            radius = 3

            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)

            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
            
            
            ##want to add a feature where the line turs the color after it  "sees it"
            pygame.draw.line(surface, (0,255,0), (i*dis, j*dis + centre),(0, j*dis + centre ))
            pygame.draw.line(surface, (0,255,0), (i*dis, j*dis + centre),(500, j*dis + centre ))
            
            pygame.draw.line(surface, (0,255,0), (i*dis + centre, j*dis ),(i*dis + centre, 0 ))
            pygame.draw.line(surface, (0,255,0), (i*dis + centre, j*dis ),(i*dis + centre, 500 ))

            pygame.draw.line(surface, (0,255,0), (i*dis + centre, j*dis + centre ),(i*dis + centre + 500, j*dis + centre + 500 ))
            pygame.draw.line(surface, (0,255,0), (i*dis + centre, j*dis + centre ),(i*dis + centre - 500, j*dis + centre - 500 ))
            
            pygame.draw.line(surface, (0,255,0), (i*dis + centre, j*dis + centre ),(i*dis + centre + 500, j*dis + centre - 500 ))
            pygame.draw.line(surface, (0,255,0), (i*dis + centre, j*dis + centre ),(i*dis + centre - 500, j*dis + centre + 500 ))
