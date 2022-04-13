#!/usr/bin/env python
"""Basic example
Prepared with help of Sympy documentation
Demonstrates how to create symbols and print some algebra
operations. Demonstrates the pprint aka PrettyPrint
"""
from sympy import Symbol, pprint
def main():
    print(__doc__) #Print the documentation
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    e = ( a*b*b + 2*b*a*b )**c
    print('')
    pprint(e) #Solves the expression and does pretty printing
    print('')
if __name__ == "__main__":
 main()
