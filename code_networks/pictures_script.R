# install.packages("igraph")
# install.packages("network") 
# install.packages("sna")
# install.packages("ndtv")
rm(list=ls())
library(igraph)
library(network)
library(sna)
library(ndtv)
file_00 <- "~/work-claudius/general/non-paper-projects/17_08_Sommerakademie/material/EE-Complexity17/networks/example_data/expl_graph_00.txt"
file_01 <- "~/work-claudius/general/non-paper-projects/17_08_Sommerakademie/material/EE-Complexity17/networks/example_data/expl_graph_01.txt"
file_02 <- "~/work-claudius/general/non-paper-projects/17_08_Sommerakademie/material/EE-Complexity17/networks/example_data/expl_graph_02.txt"
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
base_name <- "/Users/graebnerc/work-claudius/general/non-paper-projects/17_08_Sommerakademie/material/EE-Complexity17/networks/output/dir-undir"
dev.off()
pdf(file=paste(base_name, "_dir.pdf", sep = ""), 10, 10)
pl <- g_02
l <- 1.5*layout.kamada.kawai(pl)
plot_02_undirected <- make_plot(pl, l, paste(base_name, "_dir.pdf", sep = ""))
dev.off()

dev.off()
pdf(file=paste(base_name, "_undir.pdf", sep = ""), 10, 10)
plot_02_undirected <- make_plot(as.undirected(pl), l, paste(base_name, "_undir.pdf", sep = ""))
dev.off()

dev.off()
pdf(file=paste(base_name, "_p00.pdf", sep = ""), 10, 10)
l <- layout.fruchterman.reingold(g_00)
plot_00 <- make_plot(g_00, l, paste(base_name, "_p00.pdf", sep = ""))
dev.off()

dev.off()
pdf(file=paste(base_name, "_p01.pdf", sep = ""), 10, 10)
plot_01 <- make_plot(as.undirected(g_00), l, paste(base_name, "_p00.pdf", sep = ""))
dev.off()

# Figure 3: Adjacency matrix and adjacency list ----
library(xtable)
base_name <- "/Users/graebnerc/work-claudius/general/non-paper-projects/17_08_Sommerakademie/material/EE-Complexity17/networks/output/adj"
file_adj <- "~/work-claudius/general/non-paper-projects/17_08_Sommerakademie/material/EE-Complexity17/networks/example_data/expl_graph_adj.txt"
g_adj <- read_graph(file_adj, format = "edgelist")
l <- layout.fruchterman.reingold(g_adj)
pdf(file=paste(base_name, "_adj00.pdf", sep = ""))
plot_adj <- make_plot(as.undirected(g_adj), l, paste(base_name, "_adj00.pdf", sep = ""))
dev.off()

adj_m <- as_adjacency_matrix(g_adj)
inc_m <- as_incidence_matrix(g_adj)
adj_l <- as_adj_list(g_adj)
as.matrix(adj_l)
as.matrix(inc_m)
print(xtable(as.matrix(adj_m), type = "latex", digits=0), file = "adj_matrix.tex")
print(xtable(as.matrix(adj_m), type = "latex", digits=0), file = "inc_matrix.tex")

library(intergraph)
library(network)
as.matrix(asNetwork(g_adj),matrix.type="incidence")
as.matrix(asNetwork(g_adj),matrix.type="edgelist")

fileConn<-file("adj_list.tex")
sink("adj_list.tex",split=FALSE,append = FALSE)
for (i in 1:8){
  print(paste(c(i, "&", as.vector(adj_l[[i]])), collapse=" "), quote = FALSE)
  # writeLines(paste(c(i, "&", as.vector(adj_l[[i]]), "\\"), collapse=" "), fileConn)
}
close(fileConn)
paste(c("The first three notes are: ", notes), collapse=" ")


#-----
expl_graph <- read.graph("networks/output/expl_graph.gml",format=c("gml"))



l <- layout.kamada.kawai(expl_graph)
l <- layout.fruchterman.reingold(expl_graph)

l <- layout.lgl(expl_graph)
l <- layout.graphopt(expl_graph)
l <- layout.kamada.kawai(expl_graph)
dev.off()

l <- layout.lgl(expl_graph)
l <- layout.norm(l, ymin=-0.9, ymax=0.9, xmin=-0.9, xmax=0.9)
pdf(file="networks/output/example_graph.pdf")

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


l <- layout.kamada.kawai(expl_graph) 
plot(expl_graph, layout=l)