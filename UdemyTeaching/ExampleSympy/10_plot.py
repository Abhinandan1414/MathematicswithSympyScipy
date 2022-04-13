from sympy import *
from sympy.plotting import *
x,y = symbols('x y')
p = plot3d_parametric_surface(sin(x)*sin(y), sin(x)*cos(y),
cos(x), (x, 0, pi), (y, 0, 2*pi))
p = plot3d(sin(x)*y, (x, 0, 6*pi), (y, -5, 5))
