import pandas as pd
from gene import *
import random

class Generation(object):

    def __init__(self, initial_population):
        self.generationNumber = 1

        self.population = []

        self.P = initial_population
        #self.screen = screen
        self.generation = 0
    
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

def main():
    one = Generation(10)



main()
   


