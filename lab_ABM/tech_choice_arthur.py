# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random



class Agent():
    def __init__(self):
        self.neighborhood = []       
        self.tec = None
        
    def tec_choice(self):
        # survey technology choices of the neighborhood
        tec_0_chosen = 0
        tec_total_chosen = 0
        for a in self.neighborhood:
            if a.tec in [0, 1]:
                tec_total_chosen += 1
                if a.tec == 0:
                    tec_0_chosen += 1
        r = random.uniform(0, 1)  # draw random number
        
        if tec_total_chosen > 0:  # make technology choice proportional to current usage shares in the neighborhood
            if r < float(tec_0_chosen) / tec_total_chosen:
                self.tec = 0
            else:
                self.tec = 1
        else:
            if r < 0.5:
                self.tec = 0
            else:
                self.tec = 1



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
        tec_0_chosen_total = 0
        tec_chosen_total = 0
        time_list = []
        share0_list = []
        random.shuffle(self.agentlist)
        for a in self.agentlist:
            s_total += 1
            a.tec_choice()
            if a.tec == 0:
                tec_0_chosen_total += 1
            time_list.append(s_total)
            share0_list.append(float(tec_0_chosen_total) / tec_chosen_total)
        plotting(time_list, share0_list)