#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:14:41 2017

@author: graebnerc

This file contains the code for the figure illutrating the different 
graphs resulting from the ER model of the ER model and a plot for the Poisson 
distribution.
"""

#%% Imports
import networkx as nx
from math import factorial, e
import matplotlib.pyplot as plt
import numpy as np
import string

#%% Producing some instances of the ER model

nb_vertices = 15
ER_p = 0.2
nb_graphs = 4
graphs_per_row = 2
rows = int(nb_graphs/graphs_per_row)
graphs = {}
graph_names = []
labs = ["(" + a + ")" for a in string.ascii_lowercase[:nb_graphs]]
labs = np.asarray(labs).reshape(rows, graphs_per_row)

fig, axes = plt.subplots(rows, graphs_per_row, figsize=(7, 4.7))

for i in range(nb_graphs):
    print(i)
    g_name = "g_" + str(i)
    graphs[g_name] = nx.fast_gnp_random_graph(nb_vertices, ER_p)
    graph_names.append(g_name)

graph_names = np.asarray(graph_names).reshape(rows, graphs_per_row)

for col in range(graphs_per_row):
    for row in range(rows):
        nx.draw_networkx(graphs[graph_names[row, col]],
                         pos=nx.spring_layout(graphs[graph_names[row, col]]),
                         node_color='#3F5D7D',
                         node_size=50, 
                         edge_color=range(10, 
                                          10+graphs[graph_names[row, col]].number_of_edges()),
                         width=1.5,
                         edge_vmin=5.0, 
                         edge_cmap=plt.cm.Blues, 
                         with_labels=False,
                         ax=axes[row, col])
        axes[row, col].set_facecolor('white')
        axes[row, col].tick_params(
                axis='both',         # changes apply to both axis
                which='both',      # both major and minor ticks are affected
                bottom='off',      # ticks along the bottom edge are off
                top='off',         # ticks along the top edge are off
                left='off',
                labelbottom='off', # labels along the bottom edge are off
                labelleft='off') 
        axes[row, col].set_xlabel(labs[row, col])
fig.tight_layout()
plt.savefig("output/ER_graphs_expls.pdf")

#%% Illustrate the Poisson distribution (i.e. degree distribution of ER graphs)
slmbda = [1, 4, 6, 10, 15] # lambda is c, the mean degree
k = np.arange(0, 21, 1)

lmbda = [1, 4, 6, 10, 15] # lambda is c, the mean degree
k = np.arange(0, 21, 1)


exp_prob1 = []
exp_prob4 = []
exp_prob6 = []
exp_prob10 = []
exp_prob15 = []

for i in range(len(k)):
    c = 1
    exp_prob1.append(e**(-1*c)*c**k[i] / factorial(k[i]))
    c = 4
    exp_prob4.append(e**(-1*c)*c**k[i] / factorial(k[i]))
    c = 6
    exp_prob6.append(e**(-1*c)*c**k[i] / factorial(k[i]))
    c = 10
    exp_prob10.append(e**(-1*c)*c**k[i] / factorial(k[i]))
    c = 15
    exp_prob15.append(e**(-1*c)*c**k[i] / factorial(k[i]))

results = [exp_prob1, exp_prob4, exp_prob6, exp_prob10, exp_prob15]

plt.clf()
plt.rc('text', usetex=False)
plt.rc('font', family='serif')
fig, ax = plt.subplots(figsize=(7, 4.7))
for i in range(len(results)):
    ax.plot(k, results[i], marker='.',label='c=%s' % (str(lmbda[i])) )
ax.set_title('Degree distribution of the ER Modell')
ax.set_xlabel(r'k')
ax.set_ylabel(r'$\mathbb{P}(\delta(v_i)=k)$')
ax.legend(loc='upper right')
plt.savefig("output/ER_degree-dist.pdf")

#%% Comparison of actual degree distribution and analytical baseline
plt.clf()
fig, axes = plt.subplots(figsize=(7, 4.7))
graph_names = list(graph_names.reshape(1,4))[0]
for g in range(len(graph_names)):
    deg_dist = graphs[graph_names[g]].degree()#.values()
    plt.scatter(list(deg_dist.keys()), list(deg_dist.values()))

    ax.plot(k, results[i],marker='.',label='c=%s' % (str(lmbda[i])) )
ax.set_title('Degree distribution of ER Graphs - low n')
ax.set_xlabel(r'k')
ax.set_ylabel(r'$\mathbb{P}(\delta(v_i)=k)$')
#ax.legend(loc='upper right')
plt.savefig("output/ER_degree-dist-comp.pdf")    