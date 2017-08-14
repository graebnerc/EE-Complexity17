#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:29:08 2017

@author: graebnerc


This program creates a plot that illustrates the difference between 
degree distributions of the ER (which is Poisson) and the BA model 
(which is Power law).
"""
#%%
import collections
import networkx as nx
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import poisson, zipf, powerlaw


#%%

fig, ax = plt.subplots(1, 1)
lmbda = [4, 10, 20]
rv = poisson(mu)

# range_considered = np.arange(poisson.ppf(0.01, lmbda),
#                             poisson.ppf(0.99, lmbda))
range_considered = np.arange(0, 40)

for l in range(len(lmbda)):
    print(l)
    print(lmbda)
    rv = poisson(lmbda[l])
    ax.plot(range_considered, rv.pmf(range_considered), marker='.', 
            label='c=%s' % (str(lmbda[l])))
ax.legend(loc='best', frameon=False)
plt.show()

#%%
# powerlaw.pdf(x, a) = a * x**(a-1)
# powerlaw.pdf(x, a) = C * x**(-a) p(x) = Cx**-alpha
powerlaw.pdf(0.5, 3)
#powerlaw.pdf(x, a)
inputs = [i / 10 for i in range(11) ]
pw_vals = [1- powerlaw.cdf(x, 2) for x in inputs]
po_vals = [1- poisson.cdf(2,2) for x in inputs]
print(pw_vals)
#%%
fig, ax = plt.subplots(1, 1)
a = 1.66
# mean, var, skew, kurt = powerlaw.stats(a, moments='mvsk')
 
x = np.linspace(powerlaw.ppf(0.01, a),
                powerlaw.ppf(0.99, a), 100)
ax.loglog(inputs, pw_vals,
        'r-', lw=1, alpha=0.6, label='powerlaw pdf')
ax.loglog(inputs, po_vals,
          'b-', lw=1, alpha=0.6, label='poisson pdf')
ax.legend()
plt.show()
#%%
rvs = powerlaw.rvs(1.66, loc=0, scale=1, size=100, random_state=None)
fig, ax = plt.subplots(1, 1)

plt.show()

#%%
rvs = powerlaw.rvs(1.66, loc=0, scale=1, size=1000, random_state=None)
rvs
fig, ax = plt.subplots(1, 1)
plt.hist(rvs)
plt.show()
#%%
zipf_base = [2, 4]      # The first parameter for the power law
zipf_expo = [2, 4]      # the second parameter for the power law
lmbda = [4, 10]         # The parameter for the Poisson distribution

for i in range(len(zipf_base)):
    rv_poisson = poisson(lmbda[i])
    rv_zipf = zipf(zipf_base[i], zipf_expo[i])

#%%
# range_considered = np.arange(poisson.ppf(0.01, lmbda),
#                             poisson.ppf(0.99, lmbda))
fig, ax = plt.subplots(1, 1)
range_considered = np.arange(0, 20)

for i in range(len(zipf_base)):
    rv_poisson = poisson(lmbda[i])
    rv_zipf = zipf(zipf_base[i], zipf_expo[i])
    #ax.plot(range_considered, rv_zipf.pmf(base_e[l], range_considered), marker='.', 
    #        label='Zipf with={} and {}'.format(zipf_base[i], zipf_expo[i]))
    ax.plot(range_considered, rv_poisson.pmf(range_considered), marker='.', 
            label='Poisson with%s' % (str(lmbda[l])))
    ax.legend("bottom right")
    
plt.show()


#%% The BA graph
power_law_graph = nx.barabasi_albert_graph(500, 5, seed=123)
degree_sequence = sorted(nx.degree(power_law_graph).values(),reverse=True)
degree_freq = collections.Counter(degree_sequence) 
max_degree = max(degree_freq.values())
dmax=max(degree_sequence)

#%% The ER graph
nx.fast_gnp_random_graph(nb_vertices, ER_p)

#%%
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
hist, bins = np.histogram(degree_sequence)
x_axis_max = max(degree_sequence) + 2
y_axis_max = math.ceil(1.1 * max_degree + 2)

axes[0, 0].set_title("BA model: degree distribution", fontsize=14, ha='center', loc='center')
# axes[0, 0].bar(deg, cnt, color="#3F5D7D", alpha=1.0, edgecolor = "#3F5D7D")
axes[0, 0].set_xlim(4, x_axis_max)
axes[0, 0].set_ylim(0, y_axis_max)

axes[1, 0].loglog(degree_sequence,'b-',marker='.', color="#3F5D7D")
axes[1, 0].set_title("BA model: cumul degree distribution", fontsize=14, ha='center', loc='center')
axes[1, 0].set_ylabel("degree")
axes[1, 0].set_xlabel("rank")
axes[1, 0].set_xlim(1, 10**4)
plt.tight_layout()
plt.savefig("output/Poisson-vs-Powerlaw.pdf")


