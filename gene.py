import random
import numpy as np

"""
fitness = # num of times it bounces
gitA fitness function which takes a chromosome as input and returns a higher value for better solutions (much more likely to reproduce)
A population which is just a set of many chromosomes
A crossover operation which determines how parents combine to produce offspring
A mutation operation which determines how random deviations manifest themselves
"""

#state = ( delta_y_ball/delta_x_ball                 range: (-1 to 1)
#           (y_ball-y_paddle)/height                 range: (-1 to 1)
#                   y_paddle/height                  range (0 to 1)    
#             x_ball/width                           range (0 to 1))


#states
#output = # -1 0 1 scalar which way to go

#linear model 
# tanh(A*inputs) = output
# (1x4) * (4x1) = (1x1)
# A = (a1 a2 a3 a4) lets create a linear constraint where a has a possible value between (-1 to 1)


#create chromosome with 64 bits of information
class Gene(object):

    n = 64
    def __init__(self):
        self.alleles = []
        for i in range(Gene.n):
            self.alleles.append(random.randint(0,1))

   
    # default chance of mutation is 1%
    def mutate(self, chance=0.01):
        changed = []
        for i in range(Gene.n):
            if ((1/(random.randint(1, 100)) == chance)):
                changed.append(i)
                if (self.alleles[i] == 0):
                    self.alleles[i] = 1
                else:
                    self.alleles[i] = 0 
        print(changed)

        

    #corsses over this and the other allales
    def crossover(self, other, chance = 0.5):
        changed = []
        for i in range(Gene.n):

            if (random.randint(1,100)) / 100 >= .5:
                changed.append(i)

                temp = self.alleles[i]
                self.alleles[i] = other.alleles[i]
                other.alleles[i] = temp
            else:
                changed.append(0)


        
    
