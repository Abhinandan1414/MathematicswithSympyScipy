'''

Jenny Wilson Real Estate Data


SELLING 
SQUARE
PRICE ($)   FOOTAGE     AGE     CONDITION
95,000      1,926       30      Good
119,000     2,069       40      Excellent
124,800     1,720       30      Excellent
135,000     1,396       15      Good
142,800     1,706       32      Mint
145,000     1,847       38      Mint
159,000     1,950       27      Mint
165,000     2,323       30      Excellent
182,000     2,285       26      Mint
183,000     3,752       35      Good
200,000     2,300       18      Good
211,000     2,525       17      Good
215,000     3,800       40      Excellent
219,000     1,740       12      Mint

const and x1 and x2 coefficients and const are important
Simply Ypredicted = 146,700 + 43.6738X1 - 2898.84X2
Problem definition from Qualitative Analysis for Management 11th Edition
'''



import numpy as np
import statsmodels.api as sm
x = [[1900, 30], [2000, 40], [1700, 30], [1400, 15], [1700, 32],
[1850, 38], [2000,27], [2300, 30],
[2200,26],[3752,35],[2300,18],[2500,17],[3800,40],[1740,12]]
y = [95000, 119000, 124800, 135000, 142800, 145000, 159000,
165000,182000,183000,200000,
211000,215000,219000]
x, y = np.array(x), np.array(y)
x = sm.add_constant(x)
print('x :',x)
print('y :',y)
model = sm.OLS(y, x)
results = model.fit()
print('regression coefficients:', results.params)
print(results.summary())