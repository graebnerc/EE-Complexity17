# This program creates the pictures used in the script
# Author: Claudius Graebner, claudius@claudius-graebner.com

# install.packages("igraph")
# install.packages("network") 
# install.packages("sna")
# install.packages("ndtv")
rm(list=ls())
library(igraph)
library(network)
library(sna)
library(ndtv)
library(xtable)

file_00 <- "example_data/expl_graph_00.txt"
file_01 <- "example_data/expl_graph_01.txt"
file_02 <- "example_data/expl_graph_02.txt"
g_00 <- read_graph(file_00, format = "edgelist")
g_01 <- read_graph(file_01, format = "edgelist")
g_02 <- read_graph(file_02, format = "edgelist")

make_plot <- function(graph_dat, layout_dat, filename){
  l <- layout.norm(layout_dat, ymin=-0.9, ymax=0.9, xmin=-0.9, xmax=0.9)
  return_plot <- plot(graph_dat, 
                      edge.arrow.size=1.2, 
                      edge.curved=.1, 
                      vertex.label=NA,
                      vertex.size=8,
                      vertex.color="#008ae6")
}


# Figure 2: directed vs. undirected graph ----
base_name <- "output/script/dir-undir"
dev.off()
pdf(file=paste(base_name, "_dir.pdf", sep = ""), 10, 10)
pl <- g_02
l <- 1.5*layout.kamada.kawai(pl)
plot_02_undirected <- make_plot(pl, l, paste(base_name, "_dir.pdf", sep = ""))
dev.off()

pdf(file=paste(base_name, "_undir.pdf", sep = ""), 10, 10)
plot_02_undirected <- make_plot(as.undirected(pl), l, paste(base_name, "_undir.pdf", sep = ""))
dev.off()

pdf(file=paste(base_name, "_p00.pdf", sep = ""), 10, 10)
l <- layout.fruchterman.reingold(g_00)
plot_00 <- make_plot(g_00, l, paste(base_name, "_p00.pdf", sep = ""))
dev.off()

pdf(file=paste(base_name, "_p01.pdf", sep = ""), 10, 10)
plot_01 <- make_plot(as.undirected(g_00), l, paste(base_name, "_p00.pdf", sep = ""))
dev.off()

# Figure 3: Adjacency matrix and adjacency list ----
base_name <- "output/script/adj"
file_adj <- "example_data/expl_graph_adj.txt"
g_adj <- read_graph(file_adj, format = "edgelist")
l <- layout.fruchterman.reingold(g_adj)
pdf(file=paste(base_name, "_adj00.pdf", sep = ""))
plot_adj <- make_plot(as.undirected(g_adj), l, paste(base_name, "_adj00.pdf", sep = ""))
dev.off()

adj_m <- as_adjacency_matrix(g_adj)
# inc_m <- as_incidence_matrix(g_adj)
adj_l <- as_adj_list(g_adj)
as.matrix(adj_l)
# as.matrix(inc_m)
print(xtable(as.matrix(adj_m), type = "latex", digits=0), file = "output/script/adj_matrix.tex")
print(xtable(as.matrix(adj_m), type = "latex", digits=0), file = "output/script/inc_matrix.tex")

#-----
expl_graph <- read.graph("output/expl_graph.gml", format=c("gml"))

# Find nice layout:
# l <- layout.kamada.kawai(expl_graph)
# l <- layout.fruchterman.reingold(expl_graph)
# l <- layout.lgl(expl_graph)
# l <- layout.graphopt(expl_graph)
# l <- layout.kamada.kawai(expl_graph)

l <- layout.lgl(expl_graph)
l <- layout.norm(l, ymin=-0.9, ymax=0.9, xmin=-0.9, xmax=0.9)
pdf(file="output/script/example_graph.pdf")

return_plot <- plot(expl_graph, 
                    edge.arrow.size=0.8, 
                    edge.width=0.75,
                    edge.curved=.1, 
                    vertex.label=NA,
                    vertex.size=6,
                    vertex.color="#008ae6",
                    rescale=F,
                    layout=1.15*l)
dev.off()
