# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:14:08 2017

@author: Patrick Hufschmidt, Juerg Inninger, Enrico Schicketanz
"""

import matplotlib.pyplot as plt

#%%
def pop_growth(time):   
    
    if type(time) != int or time < 0:
        return('Error')
    if time == 1:
        pop_rabbit = [400]
        pop_cat = [50]
    else:
        pop_rabbit = [400]
        pop_cat = [50]
        while len(pop_rabbit) < time:
            pop_rabbit.append((pop_rabbit[-1] * 1.05) - (0.0005 * pop_cat[-1] * pop_rabbit[-1]))
            pop_cat.append(pop_cat[-1] * (0.95 + 0.00005 * pop_rabbit[-2])) 
    return(pop_rabbit, pop_cat)

# Not yet implemented: Check, if one population has died out
# at least there have to be 2 rabbits or 2 cats in order to have a 
# chance of real-world reproduction (we assume: 1 male, 1 female ;-)

#%%
# Program to solve the task
time = 2500                 # define the time steps
result = pop_growth(time)   # the function returns a tuple
pop_rabbit = result[0]
pop_cat = result[1]
        
print("Development of the Population of rabbits: ", pop_rabbit)
print("Development of the Pop of cats: ", pop_cat)    

#%%
# Plotting the results
plt.figure()
plt.title("Development of rabbits and cats")
plt.xlabel("time")
plt.ylabel("population")
plt.plot(range(time), pop_cat, label="cats")
plt.plot(range(time), pop_rabbit, label="rabbits")
plt.legend()
plt.savefig("Group3_Solution-Graph.pdf")
plt.show()
