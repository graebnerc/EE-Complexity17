# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:45:37 2017

@author: Susanna Bolz, Patrick Hufschmidt and Daniel Obst
"""

# Zombies in Solow World


# import libraries
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np



#%%

# define function "zombies"


def zombies(duration,survp,survc,dep):
    """
    Solow imagined a peaceful world: 
    people enjoyed working and thereby increased the capital stock.
    But there were enemies outside - zombies were frequently invading.
    They killed the people and destroyed capital.
    How long is mankind going to survive?
    The following function provides the answer to this question, given some parameters
        1) time period you want to explore - integer
        2) survival rate of the population when Zombies invade - between 0 and 1
        3) "survival" rate of the capital - between 0 and 1
        4) how does survival rate depend on capital stock? - between 0 and 1
    """
    if type(duration)!=int:
        return("First argument: please type an integer")
    if not 0<=survp<=1:
        return("Second argument: please type something between 0 and 1")
    if not 0<=survc<=1:
        return("Third argument: please type something between 0 and 1")
    if not 0<=dep<=1:
        return("Fourth argument: please type something between 0 and 1")
    else:
        print("Fine! Now let's see what happens to Solow World!", "\n")
        

        # define variables
        t = 0
        L = [400]
        K = [1000]
        T = [0]
        delta = 0.15
        n = 0.001
        Y = [(K[0]**0.5)*(L[0]**0.5)]
    
        while K[-1] > 0 and len(T)<duration:
            for t in range (1,duration):
                # create random variable between 0 and 1 for Zombie invasion
                random = np.random.random()
                # do Zombies invade?
                if random > 0.995:
                    # if yes, only survp % of the labor and survc% of the capital force survives
                    pl = survp*(1-dep*(1/L[t-1]))
                    pk = survc*(1-dep*(1/K[t-1]))
                    Lnew = L[-1]*pl
                    Knew = pk*((1-delta)*K[-1] + 0.3*((K[-1]**0.5)*(L[-1]**0.5)))
                    print("Holy Shit! Zombie invasion in period", t)
                    print(round(((1 - pl)*100),2), "percent of the population does not survive.")
                    print(round(((1 - pk)*100),2), "percent of the capital is destroyed.", "\n")
                else:
                    # if not, nothing happens
                    Lnew = (1+n)*L[-1]
                    # define K in next period
                    Knew = (1-delta)*K[-1] + 0.3*((K[-1]**0.5)*(L[-1]**0.5))
                # append new K to existing list
                K.append(Knew) # append new L to existing list
                L.append(Lnew)
                Ynew = (K[t]**0.5)*(L[t]**0.5)
                Y.append(Ynew)
                T.append(t)
                    
        # transform lists to arrays
        y = np.asarray(Y)
        c = np.asarray(K)
        persons = np.asarray(L)
        time = np.asarray(T)

        # calculate per capita values
        ypc = y/persons
        cpc = c/persons

        # plot
        plt.figure()
        plt.plot(T,Y, 'b')
        plt.plot(T,K, 'g')
        plt.xlabel("Time")
        outputl = mpatches.Patch(color='b', label='Output')
        capitall = mpatches.Patch(color='g', label='Capital')
        plt.legend(handles=[outputl, capitall])
        plt.figtext(0.12, -0.15, "Survival rate population is " + str(survp) + "\nSurvival rate capital is " + str(survc) + "\nDependency Survival rate on capital stock is " + str(dep))
        plt.show()

        plt.figure()
        plt.plot(time,ypc, 'b')
        plt.plot(time,cpc, 'g')
        plt.xlabel("Time")
        outputl = mpatches.Patch(color='b', label='Output per Capita')
        capitall = mpatches.Patch(color='g', label='Capital per Capita')
        plt.legend(handles=[outputl, capitall])
        plt.figtext(0.12, -0.15, "Survival rate population is " + str(survp) + "\nSurvival rate capital is " + str(survc) + "\nDependency Survival rate on capital stock is " + str(dep))
        plt.show()
        
        
#%%
        

# execute!

zombies(1000,0.75,0.9,1)