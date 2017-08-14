import networkx as nx
import numpy as np
import matplotlib
import matplotlib.pylab as py
from matplotlib import rc

slmbda = [1, 4, 6, 10, 15] # lambda is c, the mean degree
k = np.arange(0, 21, 1)

c = 1
exp_prob1 = []
for i in range(len(k)):
    exp_prob1.append(e**(-1*c)*c**k[i] / factorial(k[i]))

c = 4
exp_prob4 = []
for i in range(len(k)):
    exp_prob4.append(e**(-1*c)*c**k[i] / factorial(k[i]))

c = 6
exp_prob6 = []
for i in range(len(k)):
    exp_prob6.append(e**(-1*c)*c**k[i] / factorial(k[i]))
    
c = 10
exp_prob10 = []
for i in range(len(k)):
    exp_prob10.append(e**(-1*c)*c**k[i] / factorial(k[i]))

c = 15
exp_prob15 = []
for i in range(len(k)):
    exp_prob15.append(e**(-1*c)*c**k[i] / factorial(k[i]))



results = [exp_prob1,exp_prob4,exp_prob6,exp_prob10,exp_prob15]

py.clf()
for i in range(len(results)):
    py.plot(k, results[i],marker='.',label='c=%s' % (str(lmbda[i])) )

py.rc('text', usetex=True)
py.rc('font', family='serif')
py.title('Grad-Verteilung im ER Modell')
py.xlabel(r'k')
py.ylabel(r'$P(\delta(u)=k)$')
py.ylim(0,0.40)
py.legend(loc='upper right')
#py.show()
py.savefig('ER-Distribution.pdf')