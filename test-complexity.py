#!/usr/bin/env python
import sys

something_wrong = False
issues = []

# 1. Test whether a Python 3 version is used:

try:
    assert sys.version_info >= (3, 4)
except AssertionError:
    something_wrong = True
    issues.append("Too old python version installed: ", sys.version_info)
    pass

# 2. Test whether all required packages are installed:

#numpy, scipy and matplotlib, and

try:
    import numpy as np
except ImportError:
    something_wrong = True
    print("WARNING: {} is not installed.\
          Please try to install as described in the installation guideline.\
          If you are unable to install {} please inform us about your difficulties!".format("numpy", "numpy"))
    issues.append("Numpy not correctly installed.\n")
    pass

try:
    import scipy as sc
except ImportError:
    something_wrong = True
    print("WARNING: {} is not installed.\
          Please try to install as described in the installation guideline.\
          If you are unable to install {} please inform us about your difficulties!".format("scipy", "scipy"))
    issues.append("Scipy not correctly installed.\n")
    pass 

try:
    import matplotlib.pyplot as plt
except ImportError:
    something_wrong = True
    print("WARNING: {} is not installed!\n\
          Please try to install as described in the installation guideline.\n\
          If you are unable to install {} please inform us about your difficulties!".format("matplotlib", "matplotlib"))
    issues.append("Matplotlib not correctly installed.\n")
    pass 

try:
    import networkx as nx
except ImportError:
    something_wrong = True
    print("WARNING: {} is not installed!\n\
          Please try to install as described in the installation guideline.\n\
          If you are unable to install {} please inform us about your difficulties!".format("networkx", "networkx"))
    issues.append("Networkx not correctly installed.\n")
    pass

# 3. Print results

if something_wrong:
    print("WARNING: something went wrong! Your system is not ready for the course because you have the following issues:\n", issues,
          "\nTry to install the software again according to the installation guideline.",
          "\nIn case you are unable to fix the problem, please copy the terminal output and send it to Claudius. Please also copy the following lines:\n",
          sys.version)
else:
    print("GREAT! Your system is ready for the course. We are looking forward meeting you in Neudietendorf!")
