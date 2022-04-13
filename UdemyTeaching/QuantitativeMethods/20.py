'''
  
(MEDIUM)        (AUDIENCE REACHED PER AD)       (COST PER AD)    (MAXIMUM ADS PER WEEK)

TV spot (1 minute)  5,000                           800                  12
Daily newspaper     8,500                           925                   5
(full-page ad)
Radio spot          2,400                           290                  25
(30 seconds, prime time)
Radio spot          2,800                           380                  20
(1 minute, afternoon)

X1 = number of 1-minute TV spots taken each week
X2 = number of full-page daily newspaper ads taken each week
X3 = number of 30-second prime-time radio spots taken each week
X4 = number of 1-minute afternoon radio spots taken each week

 Maximize audience coverage = 5,000X1 + 8,500X2 + 2,400X3 + 2,800X4
 
Maximize audience coverage = 5,000X1 + 8,500X2 + 2,400X3 + 2,800X4
subject to
 X1 <= 12  (maximum TV spots/week)
 X2 <=  5  (maximum newspaper ads/week)
 X3 <= 25  (maximum 30-second radio spots/week)
X4 <= 20  (maximum 1-minute radio spots/week)
800X1 + 925X2 + 290X3 + 380X4 <= $8,000 (weekly advertising budget)
X3 + X4 >= 5 (minimum radio spots contracted)
290X3 + 380X4 <= $1,800 (maximum dollars spent on radio)
X 1, X 2, X 3, X 4 >= 0

X1 = 1.97  TV spots
X2 = 5  newspaper ads
X3 = 6.2 30-second radio spots
X4 = 0  one-minute radio spots

'''

from scipy.optimize import linprog
'''
Media selection page number 328
'''
obj = [-5000, -8500,-2400,-2800]
lhs_ineq = [[ 1,0,0,0],
 [0,1,0,0],
 [0,0,1,0],
 [0,0,0,1],
 [800,925,290,380],
 [0,0,-1,-1],
 [0,0,290,380]]
rhs_ineq = [12,
 5,
 25,
 20,
 8000,
 -5,
 1800]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
 method="revised simplex")
print(opt)
