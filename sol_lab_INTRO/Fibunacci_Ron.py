# -*- coding: utf-8 -*-
"""
This is the solution to the Fibunacci task by Ron.

It does not contain any tests of the inputs, but it is a very short and 
concise solution.
"""

def fibo (n):
    l = [1,1]
    while len(l) <= n:
        l.append(l[-1]+l[-2])
l = fibo(10)
print(l)

