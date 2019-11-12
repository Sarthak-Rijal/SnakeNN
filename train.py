from gene import *
from snake import *
#need neural network model
import numpy as np
import random
import pygame
import math

MAXBOUNCEANGLE = math.pi/4
MAXSPEED = 15

WIDTH = 858
HEIGHT = 525

class Train(object):
    def __init__(self, color, screen,x,y,length,width,player,speed, gene=None):
        self.color = color
        self.snake = snake(((random.randint(0,255)), (random.randint(0,255), (random.randint(0,255)), random.randint(1,19))))
        self.dead = self.snake.dead()
        
        self.fitness = 0
        
      
        self.g = Gene()
        
        #self.F = self.g.numpy_values()
        #self.A, self.B, self.C, self.D = format_weight_array(self.F)

    def move(self, decision):
        #desion base on the output of NN
        snake.moveRight()
        snake.moveRight()
        snake.moveRight()
        snake.moveRight()

    def on_update(self):
        if self.dead:
            print("Died")
            return
        
        #Neural Network part
        #X = prepare_features(self.ball.x_speed, self.ball.y_speed, self.ball.y, self.paddle.y)
        #self.move(nn(self.A, self.B, self.C, self.D, X))


    def getVision(self):
        self.snake.getVision()


    def prepare_features(ball_dx, ball_dy, y_ball, y_paddle):
        pass
        #return self.snake.getVision()
        
