from scipy.optimize import linprog

'''
Page 313...

Maximize profit = $16.24 X 1 + $8.22 X 2 + $8.77 X 3 + $8.66 X 4
subject to
 0.125X1 + 0.066X4 <= 1,200 (yards of silk)
0.08X 2 + 0.05X 3 <= 3,000 (yards of polyester)
0.05X3 + 0.044X4 <= 1,600 (yards of cotton)
X1 >=5,000 (contract minimum for all silk)
X1 <= 7,000 (contract maximum)
X2 >= 10,000 (contract minimum for all polyester)
X2 <= 14,000 (contract maximum)
X3 >= 13,000 (contract minimum for blend 1)
X3 <= 16,000 (contract maximum)
X4 >= 5,000  (contract minimum for blend 2)
X4 <= 8,500  (contract maximum)
X 1, X 2, X 3, X 4 >= 0

'''
obj = [-16.24, -8.22, -8.77, -8.66]
lhs_ineq = [[0.125, 0, 0, 0.066],
[0, 0.08, 0.05, 0],
[0, 0, 0.05, 0.044]]
rhs_ineq = [ 1200,
3000,
1600]
bnd = [(5000, 7000),
(10000,14000),
(13000,16000),
(5000, 8500)]
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,bounds=bnd, method="revised simplex")
print(opt)
