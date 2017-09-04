# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:27:08 2017

@author: Miriam Fischer, Ron Yaroslav Grodko and Kenneth Donkor-Hyiaman
"""

import numpy as np
import matplotlib.pyplot as plt

class Solow:
    
    def __init__(self):
        self.K = []
        self.L = []
        self.Y = []
        
    def simulation(self, alpha, populationgrowth, deprecate, k0, l0, periods):
    #Main Method
        self.K = []
        self.L = []
        self.Y = []
        self.alpha = alpha
        self.l = populationgrowth
        self.d = deprecate
        self.K.append(k0)
        self.L.append(l0)
        self.timesteps = periods
        self.Y.append(pow(k0, alpha)*pow(l0, 1-alpha))
        self.internsimulation(self.timesteps)
     

    def internsimulation(self, time):
    #This is only a private function. Do not use it directly!
    #I would have declared it as private, but I do not know how to do it in Python
        for t in range(1, time):
            Kchange = 0.3*self.Y[t-1] - self.d*self.K[t-1]
            Knew = self.K[t-1] + Kchange
            Lnew = (1+self.l)*self.L[t-1]
            self.K.append(Knew)
            self.L.append(Lnew)
            Ynew = pow(self.K[t],self.alpha)*pow(self.L[t],(1-self.alpha))
            self.Y.append(Ynew)
    
    def graph(self):
    #Method showing a plot of the Solow function
        plt.figure()
        plt.title("Solow Model")
        plt.xlabel("Time")
        plt.ylabel("Y, K, L")
        plt.plot(range(self.timesteps),self.L,label="Labor", color = 'b')
        plt.plot(range(self.timesteps),self.K,label="Capital", color = 'g')
        plt.plot(range(self.timesteps),self.Y,label="Income", color = 'r')
        plt.legend(loc='center left', bbox_to_anchor = (1,0.5))
        plt.show()



