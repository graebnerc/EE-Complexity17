#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:04:02 2017

@author: graebnerc

This script creates the graph for the exercise in the lab.
"""
import matplotlib.pyplot as plt
import networkx as nx

#%%
ex_graph = expl_graph = nx.barabasi_albert_graph(5000, 15, seed=123)
nx.write_gml(ex_graph, "output/exercise_graph.gml")

#%%
plt.clf()
fig, ax = plt.subplots(figsize=(7, 7))

nx.draw_networkx(ex_graph,
                 pos=nx.spring_layout(ex_graph),
                 node_color='#3F5D7D',
                 node_size=10, 
                 edge_color=range(10, 
                                  10+ex_graph.number_of_edges()),
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
ax.set_title("A ridiculogram")
fig.tight_layout()
plt.savefig("output/exercise_graph.pdf")