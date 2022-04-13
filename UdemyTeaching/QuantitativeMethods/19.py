'''
Holiday meal turkey ranch page 290

The Holiday Meal Turkey Ranch is considering buying two different brands of turkey feed and
blending them to provide a good, low-cost diet for its turkeys. Each feed contains, in varying
proportions, some or all of the three nutritional ingredients essential for fattening turkeys. Each
pound of brand 1 purchased, for example, contains 5 ounces of ingredient A, 4 ounces of ingredient B, and 0.5 ounce
of ingredient C. Each pound of brand 2 contains 10 ounces of ingredient
A, 3 ounces of ingredient B, but no ingredient C. The brand 1 feed costs the ranch 2 cents a
pound, while the brand 2 feed costs 3 cents a pound. The owner of the ranch would like to use
LP to determine the lowest-cost diet that meets the minimum monthly intake requirement for
each nutritional ingredient

X1 = number of pounds of brand 1 feed purchased
X2 = number of pounds of brand 2 feed purchased

Minimize cost1 in cents2 = 2X1 + 3X2

Subjected to following constraints:

 5X1 + 10X2 >= 90 ounces (ingredient A constraint)
 4X1 + 3X2 >= 48 ounces (ingredient B constraint)
 0.5 X1 >= 1.5 ounces (ingredient C constraint)
 X1 >= 0 (nonnegativity constraint)
 X2 >= 0 (nonnegativity constraint)

 Expected Results: X1 = 8.4 and X2 = 4.8
'''

'''
More examples at:
https://realpython.com/linear-programming-python/
'''
from scipy.optimize import linprog
obj = [2,3]
lhs_ineq = [[-5,-10 ],
[-4,-3],
[-0.5,0]]
rhs_ineq = [-90,
-48,
-1.5]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
 method="revised simplex")
print(opt)
