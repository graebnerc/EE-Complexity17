"""
This program simulates a technology choice model of the type researched by Brian Arthur, but with local neighborhoods 
arranged as a double ring network: each agent is connected to her 2 immediate predeseccors and her 2 immediate 
successors. Network effects are only generated by the direct neighborhood, i.e. the agent places her decision on the 
basis of the choices of only her direct neighbors. As with other Arthur-type technology choice models, she prefers 
technologies that are used more widely (in her neighborhood).
"""

# Molule imports
import matplotlib.pyplot as plt
import random

# Class definitions
# Agent class
class Agent():
    """Agent class; defines an agent which can choose a technology and remember her choice."""
    def __init__(self):
        """Constructor method, sets up placeholder variables for chosen technology (None) and neighborhood (empty list)"""
        self.neighborhood = []       
        self.tec = None
    def tec_choice(self):
        """Technology choice method; selects and assigns a technology with probabilities proportional to the current
           usage shares in the agent's neighborhood."""
        # survey technology choices of the neighborhood
        s0 = 0
        subs = 0
        for a in self.neighborhood:
            if a.tec in [0, 1]:
                subs += 1
                if a.tec == 0:
                    s0 += 1
        # draw random number
        r = random.uniform(0, 1)
        # make technology choice proportional to current usage shares in the neighborhood
        if subs > 0:        
            if r < float(s0) / subs:
                self.tec = 0
            else:
                self.tec = 1
        else:
            if r < 0.5:
                self.tec = 0
            else:
                self.tec = 1

# Simulation class
class Simulation():
    """The Simulation class defines an object for an entire simulation run, the simulation environment including agents 
       and neighborhood structure is created in the constructor; the run() method conducts the simulation run and outputs 
       the results."""
    def __init__(self, neighborhood_str):
        """Constructor method; accepts an argument neighborhood_str which defines the neighborhood structure to be 
           applied. It then 1. sets up sumulation variables (control variable, counters, list of agent objects, 
           development recording list), 2. creates and records the agents, 3. creates the neighborhood structure by 
           calling one of the create_neighborhood_structure() functions handing over the simulation's agentlist."""
        self.agentlist = []
        no_of_agents = 1000
        for i in range(no_of_agents):
            self.agentlist.append(Agent())
        if neighborhood_str == 0:
            create_neighborhood_structure_ring(self.agentlist)      # ring neighborhood structure
        elif neighborhood_str == 1:
            create_neighborhood_structure_complete(self.agentlist)  # complete network neighborhood structure          
        else:
            create_neighborhood_structure_pa(self.agentlist)        # preferential attachment neighborhood structure
    def run(self):
        """Run method; it 1. conducts the time iteration of the simulation (all agents choose their technology); 
           2. records usage shares and 3. calls the global plotting() function to provide graphical output."""
        s0_total = 0
        s_total = 0
        time_list = []
        share0_list = []
        random.shuffle(self.agentlist)
        for a in self.agentlist:
            s_total += 1
            a.tec_choice()
            if a.tec == 0:
                s0_total += 1
            time_list.append(s_total)
            share0_list.append(float(s0_total) / s_total)
        plotting(time_list, share0_list)
        

# Global function definitions
# Plotting function
def plotting(xvalues, yvalues):
    """Plotting function. 
    Creates a line plot figure with axes from the two lists it is given as arguments."""    
    ax = plt.gca()
    ax.plot(xvalues, yvalues, 'b')
    ax.set_xlabel("")		# Labels for the axes (currently empty) could be inserted here.
    ax.set_ylabel("")
    plt.show()

# Neighborhood structure creating functions
def create_neighborhood_structure_ring(alist):
    """Function for the creation of a double ring neighborhood structure. 
       It accepts one argument: a list of Agent-type objects.
       It goes through the agent list and modifies the .neighborhood list of all agents such that their two predecessor 
       agents (or the last agents as predecessors for the first agents) are included. In order to keep the structure 
       strictly symmetric, it also adds the agent to the neighborhood lists of its new neighbors. Thus, a complete 
       double ring network is created.
       See https://en.wikipedia.org/wiki/Ring_network (the article describes a single ring, not a double ring as used 
       here)."""
    for i in range(len(alist)):
        if i == 0:
            alist[i].neighborhood.append(alist[-1])
            alist[i].neighborhood.append(alist[-2])
            alist[-1].neighborhood.append(alist[i])
            alist[-2].neighborhood.append(alist[i])
        elif i == 1:
            alist[i].neighborhood.append(alist[i-1])
            alist[i].neighborhood.append(alist[-1])
            alist[i-1].neighborhood.append(alist[i])
            alist[-1].neighborhood.append(alist[i])
        else:
            alist[i].neighborhood.append(alist[i-1])
            alist[i].neighborhood.append(alist[i-2])
            alist[i-1].neighborhood.append(alist[i])
            alist[i-2].neighborhood.append(alist[i])

def create_neighborhood_structure_complete(alist):
    """Function for the creation of a complete network neighborhood structure: every agent is appended to the
       neighborhood of every other agent.
       See https://en.wikipedia.org/wiki/Complete_graph
       It accepts one argument: a list of Agent-type objects."""
    for a in alist:
        for a2 in alist:
            if a != a2:
                a.neighborhood.append(a2)

def create_neighborhood_structure_pa(alist):
    """Funcrion for the creation of a preferential attachment neighborhood structure: Unconnected agents (held in the list agentlist1) 
       are added successively into the connected network (held in agentlist2) by connecting every newly introduced agent randomly to one 
       agent in the network. This agent is chosen with a probability proportional to her number of connections (i.e., her degree). Thus,
       agents with high numbers of neighbors tend to accumulate more neighbors resulting in an asymmetric degree distribution (some very
       central agents, many agents with very few connections).
       See https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model
       It accepts one argument: a list of Agent-type objects."""
    agentlist_1 = list(alist[1:])
    agentlist_2 = [alist[0]]
    weightlist = [1]
    while len(agentlist_1) > 0:
        r = random.randint(0, sum(weightlist))
        i = 0
        while r > 0:
            r -= weightlist[i]
            i += 1            
        agentlist_2.append(agentlist_1[0])
        agentlist_2[-1].neighborhood.append(agentlist_2[i])
        agentlist_2[i].neighborhood.append(agentlist_2[-1])
        agentlist_1 = agentlist_1[1:]
        weightlist.append(1)
        weightlist[i] += 1        
    
# Main entry point
"""Create 3 simulation environments with different neighborhood structures."""
sim0 = Simulation(0)
sim1 = Simulation(1)
sim2 = Simulation(2)
"""Run all 3 simulation environments."""
sim0.run()
sim1.run()
sim2.run()
    

