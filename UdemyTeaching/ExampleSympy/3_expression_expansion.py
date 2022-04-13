#!/usr/bin/env python
""" Algebraic Expression Expansion Example
Demonstrates how to expand expressions.
Prepared with the help of Sympy documentation
"""
from sympy import pprint, Symbol
def main():
    print(__doc__)
    a = Symbol('a')
    b = Symbol('b')
    c = (a + b)**2
    d = (a +b)**5
    e = (a + b)**10
    print("\nExpression:")
    pprint(c)
    print('\nExpansion of the above expression:')
    pprint(c.expand())
    print("\nExpression:")
    pprint(d)
    print('\nExpansion of the above expression:')
    pprint(d.expand())
    print("\nExpression:")
    pprint(e)
    print('\nExpansion of the above expression:')
    pprint(e.expand())
    print()
if __name__ == "__main__":
    main()