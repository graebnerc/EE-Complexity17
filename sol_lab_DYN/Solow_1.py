# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:14:06 2017

@author: Miriam Fischer, Ron Yaroslav Grodko and Kenneth Donkor-Hyiaman
"""

import numpy as np
import matplotlib.pyplot as plt


alpha = 0.5 # MPK
l = 0.001 # Labour Growth Rate
d = 0.15 # deprecates Rate
K0 = 1000 # Capital Stock
L0 = 400 # Labour Stock
Y0 = pow(K0, alpha)*pow(L0, 1-alpha)


timesteps = 10 #Amount of periods

K =[K0]
L = [L0]
Y = [Y0]

for t in range(1, timesteps):
    print("Time",t)
    Kchange = 0.3*Y[t-1] - d*K[t-1]
    Lchange = l
    Knew = K[t-1] + Kchange
    Lnew = L[t-1] + Lchange*L[t-1]
    print("the amount of capital", K[t-1])
    K.append(Knew)
    L.append(Lnew)
    Ynew = pow(K[t],alpha)*pow(L[t],(1-alpha))
    print("Kchange:", Kchange,"Lchange: ", Lchange)
    print("Knew: ", Knew,"Lnew: ", Lnew)
    Y.append(Ynew)
    print("K is: ", K[t])
    print("L is: ", L[t])
    print("Y is: ", Y[t])


plt.figure()
plt.title("Solow Model")
plt.xlabel("Time")
plt.ylabel("Y, K, L")
plt.plot(range(timesteps),L,label="Labor", color = 'b')
plt.plot(range(timesteps),K,label="Capital", color = 'g')
plt.plot(range(timesteps),Y,label="Income", color = 'r')
plt.legend(loc='center left', bbox_to_anchor = (1,0.5))
plt.show()