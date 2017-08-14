# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:10:18 2017

@author: Susanna Bolz, Patrick Hufschmidt, Daniel Obst

"""

#Problem Day3

import matplotlib.pyplot as plt

L = [400]
K = [1000]
T = [0]
delta = 0.15
n = 0.001
Y = [K[0]**(1/2) * L[0]**(1/2)]

#for loop calcalutes output, kapital and labour for the period t. Thereby the values are saved in lists. 
for t in range(1,101):
    print("Period",t)
    #calculation of kapital
    Knew = (1-delta)*K[t-1] + 0.3*((K[t-1]**0.5)*(L[t-1]**0.5))
    K.append(Knew)
    #calculation of labour
    Lnew = L[t-1]*(1+n)
    L.append(Lnew)
    #calculation of output
    Ynew = K[t]**0.5*L[t]**0.5
    Y.append(Ynew)
    #creation of list for time periods for plotting
    T.append(t)
    print("Kapital", Knew, "\nLabour", Lnew, "\nProduction", Ynew) 
    
plt.figure()
plt.title ("Solow Model")
plt.xlabel("t")
plt.ylabel ("Y")
plt.plot (T, Y)
plt.plot (T,K)
plt.savefig("Solution Problem Day 3.pdf")
plt.show()


    
    