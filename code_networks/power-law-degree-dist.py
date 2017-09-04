#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:17:02 2017

@author: graebnerc

This file creates a graph with a degree distribution that follows a power law.
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections

#%%
power_law_graph = expl_graph = nx.barabasi_albert_graph(500, 5, seed=123)

#%%
plt.clf()
fig, ax = plt.subplots(figsize=(7, 7))

nx.draw_networkx(power_law_graph,
                 pos=nx.spring_layout(power_law_graph),
                 node_color='#3F5D7D',
                 node_size=10, 
                 edge_color=range(10, 
                                  10+power_law_graph.number_of_edges()),
                 width=0.5,
                 # edge_vmin=5.0, 
                 edge_cmap=plt.cm.Blues, 
                 with_labels=False)
ax.set_facecolor('white')
ax.tick_params(
        axis='both',         # changes apply to both axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        left='off',
        labelbottom='off', # labels along the bottom edge are off
        labelleft='off') 
# ax.set_title("A ")
fig.tight_layout()
plt.savefig("output/power-law-dist-graph.pdf")

#%%
degree_sequence = sorted(nx.degree(power_law_graph).values(), reverse=True)

#%%

degree_sequence=sorted(nx.degree(power_law_graph).values(),reverse=True) # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
#print "Degree sequence", degree_sequence
dmax=max(degree_sequence)

fig, axes = plt.subplots(2, 1, figsize=(7, 7))
hist, bins = np.histogram(degree_sequence)
x_axis_max = max(degree_sequence) + 2
# y_axis_max = math.ceil(1.1 * max(cnt) + 2)
axes[0].set_title("Degree distribution", fontsize=14, ha='center', loc='center')
axes[0].bar(deg, cnt, color="#3F5D7D", alpha=1.0, edgecolor = "#3F5D7D")

axes[0].set_xlim(4, x_axis_max)
# axes[0].set_ylim(0, y_axis_max)

axes[1].loglog(degree_sequence,'b-',marker='.', color="#3F5D7D")
axes[1].set_title("Cumulative degree dist", fontsize=14, ha='center', loc='center')
axes[1].set_ylabel("degree")
axes[1].set_xlabel("rank")
axes[1].set_xlim(1, 10**4)
plt.tight_layout()
plt.savefig("output/power-law-dist-graph-plot.pdf")
