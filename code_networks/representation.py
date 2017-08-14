#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 12:03:28 2017

@author: graebnerc

This file contains the code for an example graph, used to illustrate the 
various ways of how to store graphs (adjacency matrix, edge list, etc.).
"""
#%% Imports
import collections
import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from tabulate import tabulate

#%% Create graph a graph to illustrate different forms of representation
edgelist = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]
nodelist = [0, 1, 2, 3]
repr_graph = nx.Graph(edgelist)
adj_matrix = nx.adjacency_matrix(repr_graph) # returns sparse matrix
inc_matrix = nx.incidence_matrix(repr_graph)
adj_list = nx.generate_adjlist(repr_graph)

#%% # Graph representation
actualgraph = repr_graph
colors = range(10, 10+len(actualgraph.edges()))
pos=nx.spring_layout(actualgraph)
plt.clf()
nx.draw(actualgraph,
        pos,
        node_color='#A0CBE2',
        node_size=300, 
        edge_color=colors,
        width=1.5,
        edge_vmin=5.0, 
        edge_cmap=plt.cm.Blues, 
        with_labels=True)
plt.savefig("output/repr-graph.pdf")

#%%
# Get the output for Latex (just copy paste)
# Print adjecency matrix to Latex
print(tabulate(adj_matrix.toarray(), [1,2,3,4],tablefmt="latex_booktabs", showindex=True))
# Print incidence matrix to Latex
print(tabulate(inc_matrix.toarray(), [1,2,3,4,5],tablefmt="latex_booktabs", showindex=True))
# Print adjecency list to Latex
for l in nx.generate_adjlist(repr_graph, delimiter=" & "):
    print(l)
# Print edge list to Latex
for l in nx.generate_edgelist(repr_graph, data=False):
    print(l)
    
#%% Create a triple and a triad
nodes = (1,2,3)
edges = [(1,2),(2,3)]
triple = nx.Graph()
triple.add_nodes_from(nodes)
triple.add_edges_from(edges)
plt.clf()
nx.draw_shell(triple, node_color='#A0CBE2', node_size=800, with_labels=False)
plt.savefig('output/triple.pdf')
plt.clf()

# Triangles
edges.append((1,3))
triangle = nx.Graph()
triangle.add_nodes_from(nodes)
triangle.add_edges_from(edges)
plt.clf()
nx.draw_shell(triangle, node_color='#A0CBE2', node_size=800, with_labels=False)
plt.savefig('output/triangle.pdf')
plt.clf()

#%% Create an example illustration for the degree distribution

#%% Define a drawing function

def draw_graph_with_dist(edge_list, node_list, graph_title, layout="fruchtermann",
                         size_title=16, size_axis_label=12, name=None):
    """
    Draws a graph together with its degree distribution and saves it.
    
    Parameters
    -----------
    edge_list: list
        List object containing all edges of the graph.
    
    node_list: list
        List object containing all the nodes of the graph.
    
    name: str
        Name of the graph. Used for title and output file.
        
    layout: str (opt, default: fruchtermann)
        Specifies the layout for the graph. There are two options:
        'fruchtermann' calls the Fruchtermann-Reingold layout, a good default 
        option.
        'circular' call the circular layout, a good option for cycle graphs or 
        small-world networks.
    """
    g = nx.Graph()
    g.add_nodes_from(node_list)
    g.add_edges_from(edge_list)
    degree_sequence = sorted([d for n,d in g.degree_iter()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    plt.clf()
    f, ax = plt.subplots(1, 2, figsize=(11.84, 4.15))
    if layout == "fruchtermann":
        pos = nx.fruchterman_reingold_layout(g)
    elif layout == "circular":
        pos = nx.circular_layout(g)
    else:
        print("There are only two layout options: fruchtermann or circular,", 
              "but not {}.".format(layout))
    
    nx.draw_networkx(g, pos, 
                     node_color='#3F5D7D', 
                     node_size=300, 
                     edge_color='k', 
                     with_labels=True, 
                     ax=ax[0])
    if graph_title!="auto":
        graphname = "A " + name + " network"
    else:
        graphname = "An example network"
    ax[0].set_title(graphname, fontsize=size_title, ha='left', loc='left')
    ax[0].set_facecolor('white')
    ax[0].tick_params(
            axis='both',         # changes apply to both axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            left='off',
            labelbottom='off', # labels along the bottom edge are off
            labelleft='off') 

    hist, bins = np.histogram(degree_sequence)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    x_axis_max = max(degree_sequence) + 2
    y_axis_max = math.ceil(1.1 * max(cnt) + 2)
    ax[1].set_title("The corresponding degree distribution", 
      fontsize=size_title, ha='left', loc='left')
    ax[1].bar(deg, cnt, color="#3F5D7D", alpha=1.0, edgecolor = "#3F5D7D")
    ax[1].set_xlim(-0.5, x_axis_max)
    ax[1].set_ylim(0, y_axis_max)
    ax[1].set_yticks(range(0,y_axis_max))
    ax[1].set_xticks([d+0.0 for d in range(0,x_axis_max)])
    ax[1].set_xticklabels([d for d in range(0,x_axis_max)])
    ax[1].set_xlabel("Degree", fontsize=size_axis_label)  
    ax[1].set_ylabel("Frequency", fontsize=size_axis_label)  
    ax[1].spines["top"].set_visible(False)  
    ax[1].spines["right"].set_visible(False)
    figname = "output/" + name + ".pdf"

    plt.savefig(figname, bbox_inches="tight")

#%%
plt.style.use('ggplot')
degreedistgraph = nx.fast_gnp_random_graph(8, 0.3)
actualgraph = degreedistgraph

draw_graph_with_dist(actualgraph.edges(), actualgraph.nodes(), "auto", 
                     layout="fruchtermann", size_title=16, size_axis_label=12,
                     name="expl_degree_distribution")

nx.draw_shell(degreedistgraph, node_color='#A0CBE2', node_size=800, with_labels=True)

plt.savefig('output/degree_expl_nodist.pdf')
plt.clf()

# %% A bigger example graph to illustrate the measures

# expl_graph = nx.barabasi_albert_graph(100, 5)
# nx.write_adjlist(expl_graph, "output/expl_graph_adj_list.txt")
expl_graph = nx.read_adjlist("output/expl_graph_adj_list.txt")
nx.read_adjlist("output/expl_graph_adj_list.txt")
nx.write_gml(expl_graph, "output/expl_graph.gml")
nb_vertices = expl_graph.number_of_nodes()
nb_edges = expl_graph.number_of_edges()
v5_neighbors = expl_graph.neighbors(5)

connection_status_graph = nx.is_connected(expl_graph)
path_1_8 = nx.has_path(expl_graph, 1,8)
distance_1_8 = nx.shortest_path(expl_graph, 1, 8)
diam = nx.diameter(expl_graph)
av_path_len = nx.average_shortest_path_length(expl_graph)
densi = nx.density(expl_graph)
transi = nx.transitivity(expl_graph)
degree_v6 = expl_graph.degree(6)
av_degree = np.mean(list(expl_graph.degree().values()))
clustering_v6 = nx.clustering(expl_graph, 6)
clustering = nx.average_clustering(expl_graph)

#%%
plt.clf()
degree_sequence = sorted([d for n,d in expl_graph.degree_iter()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
    
f, ax = plt.subplots()
hist, bins = np.histogram(degree_sequence)
x_axis_max = max(degree_sequence) + 2
y_axis_max = math.ceil(1.1 * max(cnt) + 2)
ax.set_title("The corresponding degree distribution", 
  fontsize=12, ha='left', loc='left')
ax.bar(deg, cnt, color="#3F5D7D", alpha=1.0, edgecolor = "#3F5D7D")
ax.set_xlim(-0.5, x_axis_max)
ax.set_ylim(0, y_axis_max)
#ax.set_yticks(range(0,y_axis_max))
#ax.set_xticks([d+0.0 for d in range(0,x_axis_max)])
#ax.set_xticklabels([d for d in range(0,x_axis_max)])
ax.set_xlabel("Degree", fontsize=10)  
ax.set_ylabel("Frequency", fontsize=10)  
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False)
figname = "output/" + "example_plot_digdis" + ".pdf"
plt.savefig(figname, bbox_inches="tight")
#%%
draw_graph_with_dist(expl_graph.edges(), actualgraph.nodes(), "auto", 
                     layout="fruchtermann", size_title=16, size_axis_label=12,
                     name="expl_graph_distribution")

