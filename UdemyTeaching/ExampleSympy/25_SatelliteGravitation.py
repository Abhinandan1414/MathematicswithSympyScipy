from sympy import *

Ms,Rs,Alt = symbols('Ms Rs Alt')
Me = 5.9742 * 10**(24)
G = 6.77 * 10**(-11)
re = 6378100

gravitation = Function('Ms Rs')
gravitation1 = Function('Ms Alt')

def gravitation(Ms,Rs):
    return (G * Me * Ms)/(Rs**2)

def gravitation1(Ms,Alt):
    return gravitation(Ms,Alt+re)


print(gravitation1(1000,3621900))


