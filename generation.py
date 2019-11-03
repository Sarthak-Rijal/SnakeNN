import pandas as pd

from snake import * 
from gene import *

import random

class Generation(object):

    def __init__(self, population):

        self.population = population
        #self.screen = screen

        self.generation = 0
        self.init()

   
    def init(self, genes=None):
        self.train_snakes = []
        
        
        for i in range(self.population):
            color = (255,0,0)
            startingPos = (10,10)
            self.train_snakes.append((snake(color, startingPos)))
      
        #self.init()
    def fitnessFunction(self, steps, apples):
        return steps + (2**(apples) + apples^(2) * 500) - (apples**1 * (0.25*steps)**1.3)


    def save_parameters(self, filename):
        pass

    def on_update(self):
        pass
    # this method returns a new generation of those who had the best fitness of the dead paddles
    # it choses the highest two fitness scores and crossbreeds these two
    def selection(self):
        pass

