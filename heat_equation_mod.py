"""

heat_equation_mod.py

Modified version of heat_equation.py with instructor edits for efficiency.  
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

### Calculate lamd based off of given values of alpha, deltax, deltat.

alpha = 0.5
deltax = 0.1
deltat = 0.01
lamd = alpha * deltat / (deltax * deltax)

### list of x values from -5 to 5 in steps of deltax
x0 = -5.0

#Divide the rod into 100 intervals.  Each interval is of length 1/10
n = 101
xvec = [round(i / 10 + x0, 2) for i in range(n)] #list comprehension

"""
temperature along rod at time t = 0, 20 at left endpoint,
0 everywhere else
"""

uvec = [0.0] * n
uvec[0] = 20.0

### construct matrix A
#Initially A is a two-dimensional list (101 by 101) of zeroes.

A = [[0.0 for col in range(n)] for row in range(n)] #list comprehension
A[0][0] = A[n-1][n-1] = 1.0

# construct rows 2 through second-to-last row
#Diagonal stripe from upper left corner to lower right.

for i in range(1, n - 1):
    A[i][i] = 1 - 2 * lamd
    A[i][i - 1] = A[i][i + 1] = lamd
                
A = np.array(A)
uvec = np.array(uvec)
xvec = np.array(xvec)

nt = 10   #number of time intervals
for i in range(nt):
    uvec = A.dot(uvec)

plt.scatter(xvec, uvec, color = 'red', s = 7)
plt.title(f'Temperature along rod at t = {nt * deltat} s')
plt.xlabel('position')
plt.ylabel('temperature')
plt.show()

sys.exit(0)
