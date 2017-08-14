# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 11:47:27 2017

@author: Andreas Lichtenberger
"""

# solution new:
def fib_number (n):
    """
    Fibunacci function
    """
    if n >=3:
        x_n2 = 1
        x_n1 = 1
        i = 3
        while i <= n:
            x_n = x_n2 + x_n1
            i += 1
            x_n2 = x_n1
            x_n1 = x_n
        print("Fibunacci number: ", x_n)
    elif n == 1:
        print("Fibunacci is 1")
    elif n == 2:
        print("Fibunacci is 1")
    else:
        print("Enter a valid number!")
fib_number(1)
fib_number(2)
fib_number(3)
fib_number(4)
fib_number(5)
fib_number(6)
fib_number(7)
fib_number(10)
fib_number(-1)
