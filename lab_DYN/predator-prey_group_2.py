# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:07:03 2017

@author: Katharina Keil
"""

import numpy as np

import matplotlib.pyplot as plt

#define variables
R0 = 400 # Initial population of rabbits
C0 = 50 # Initial population of cats

# lists store populations at each point in time
RL = [R0] # initialisation of list for rabbits
CL = [C0] # initialisation of list for cats

# Variables for given interaction values
RG = 0.1    # rabbit growth
RI = -0.0005    # rabbit interaction
CI = 0.1 * 0.0005   # cat interaction
CA = -0.05  # cars

#number of time periods 
N = 1000 

# Set the initial values for the loops
R = R0
C = C0

#loop: creates list with population for each time period
for i in range(N-1):    # add N-1 values since the first value is given 
    R = (1 + RG)*R + RI*R*C + CA*R 
    C = C + CI*R*C + CA*C 
    RL.append(R)
    CL.append(C)

    
x = np.arange(200) / 200
y = x * (1-x)
plt.figure()
plt.title("Predator-Prey Model")
plt.xlabel("Time") 
plt.ylabel("Population")
plt.plot(range(N),RL,label="Rabbits", color = 'b')
plt.plot(range(N),CL,label="Cats", color = 'g')
#plt.legend(bbox_to_anchor=(0.,1.02,1.,0.102),loc=3, ncol = 2, mode = "expand", borderaxespad=0.)   
plt.legend(loc='center left', bbox_to_anchor = (1,0.5))
#plt.legend(bbox_to_anchor=(0.,1.02,1.,0.102),loc='upper center', ncol = 2, mode = "expand", borderaxespad=0.)
