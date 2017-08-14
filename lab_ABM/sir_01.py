import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

"""
g0 = nx.complete_graph(3000)
g1 = nx.watts_strogatz_graph(3000, 16, 0)
g2 = nx.barabasi_albert_graph(3000, 5)
"""

class Simulation():
    def __init__(self):
        self.p_infect = 0.1
        self.p_death = 0.01
        self.infected_period = 10
        self.immune_period = 5
        self.max_t = 200
        self.no_of_agents = 3000
        self.g = nx.barabasi_albert_graph(self.no_of_agents, 5)
        self.agents = []
        self.vulnerable_list = []
        self.immune_list = []
        self.infected_list = []
        self.dead_list = []
        self.timelist = []
        for i in range(self.g.order()):
            agent = Agent(self, self.g, i)
            self.agents.append(agent)
            self.g.node[i]["agent"] = agent
    
    def run(self):
        # seed epidemic
        patient_zero_id = np.random.choice(self.g.nodes())
        patient_zero = self.g.node[patient_zero_id]["agent"]
        patient_zero.become_infected()
        
        # time iteration
        for t in range(self.max_t):
            #for node in self.g:
            #    agent = self.g[node]["agent"]
            for agent in self.agents:
                    agent.iterate()
            self.timelist.append(t)
            immune = [a for a in self.agents if a.immune]
            infected = [a for a in self.agents if a.infected]
            dead = [a for a in self.agents if a.dead]
            self.vulnerable_list.append(self.no_of_agents - len(immune) - len(infected) - len(dead))
            self.immune_list.append(len(immune))
            self.infected_list.append(len(infected))
            self.dead_list.append(len(dead))
            print(self.timelist[-1], self.vulnerable_list[-1], self.infected_list[-1], self.immune_list[-1], self.dead_list[-1],)
    
    def plot(self):
        """function for plotting simulation results"""
        # initialize matplotlib figure
        plt.figure()
        # set axis labels
        #plt.title("Population Size")
        plt.xlabel("Time")
        plt.ylabel("Population Sizes")
        # define plots
        plt.plot(self.timelist, self.vulnerable_list, 'g')
        plt.plot(self.timelist, self.dead_list, 'r')
        plt.plot(self.timelist, self.infected_list, 'm')
        plt.plot(self.timelist, self.immune_list, 'b')
        # save as pdf
        plt.savefig("sir.pdf")
        # show figure
        plt.show()


class Agent():
    def __init__(self, S, graph, node_id):
        self.simulation = S
        self.g = graph
        self.node_id = node_id
        self.infected = False
        self.immune = False
        self.dead = False
        self.becoming_infected = False
        self.time_until_healed = None
        self.time_until_vulnerable = None
    
    def get_neighbors(self):
        return nx.neighbors(self.g, self.node_id)
    
    def iterate(self):
        if not self.dead:
            neighbors = self.get_neighbors()
            if self.immune:
                self.time_until_vulnerable -= 1
                if self.time_until_vulnerable == 0:
                    self.immune = False
            if self.infected:
                for n_id in neighbors:
                    if np.random.random() < self.simulation.p_infect:
                        self.g.node[n_id]["agent"].become_infected()
                self.time_until_healed -= 1
                if np.random.random() < self.simulation.p_death:
                    self.dead = True
                    self.infected = False
                    self.g.remove_node(self.node_id)
                elif self.time_until_healed == 0:
                    self.infected = False
                    self.immune = True
                    self.time_until_vulnerable = self.simulation.immune_period
            if self.becoming_infected:
                self.infected = True
                self.time_until_healed = self.simulation.infected_period
                self.becoming_infected = False
    
    def become_infected(self):
        if (not self.immune) and (not self.infected) and (not self.dead):
            self.becoming_infected = True
            
S = Simulation()
S.run()
S.plot()
