#!/usr/bin/env python
"""Pretty print example
Demonstrates pretty printing.
Refer Sympy documentation for more details
"""
from sympy import Symbol, pprint, sin, cos, exp, sqrt,MatrixSymbol, KroneckerProduct, Matrix
def main():
    print(__doc__)


    x = Symbol("x")
    y = Symbol("y")
    a = MatrixSymbol("a", 1, 1)
    b = MatrixSymbol("b", 1, 1)
    c = MatrixSymbol("c", 1, 1)
    pprint( x**x )
    print('\n') # separate with two blank likes
    pprint(x**2 + y + x)
    print('\n')
    pprint(sin(x)**x)
    print('\n')
    pprint( sin(x)**cos(x) )
    print('\n')
    pprint( sin(x)/(cos(x)**2 * x**x + (2*y)) )
    print('\n')
    pprint( sin(x**2 + exp(x)) )
    print('\n')
    pprint( sqrt(exp(x)) )
    print('\n')
    pprint( sqrt(sqrt(exp(x))) )
    print('\n')
    pprint( (1/cos(x)).series(x, 0, 10) )
    print('\n')
    A= Matrix([[1, -1, 1], [3, 4, 5], [0, 2, 6]])
    pprint(A)
    print('\n')
    pprint(a*(KroneckerProduct(b, c)))
    print('\n')
if __name__ == "__main__":
    main()
