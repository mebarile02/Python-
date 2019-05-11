"""

heat_equation.py

This file uses the finite difference method to solve the one-dimensional
heat equation.  A rod of length 10 is discretized uniformly with steps of
0.1.  The left endpoint is at -5, the right endpoint at 5.  Alpha is set
at 0.5.  The initial condition has temperature 20 at the left endpoint and
zero everywhere else.  The boundary conditions fix the left endpoint at 20 and
the right endpoint at 0.  The results are plotted after 0.10 seconds.
The problem is from a Numerical Methods class I took where we were
coding in Mathematica.  I wanted to recode it using Python.
"""


import sys
import numpy as np
import matplotlib.pyplot as plt

### Calculating lamd based off of given values of alpha, deltax, deltat.


alpha = 0.5
deltax = 0.1
deltat = 0.01
lamd = alpha*deltat/(deltax*deltax)


### list of x values from -5 to 5 in steps of deltax

x0 = -5.
xvec = [x0]

while max(xvec) < 5.0:
    x = x0 + deltax
    xvec.append(round(x,2))
    x0 = x


"""
temperature along rod at time t = 0, 20 at left endpoint,
0 everywhere else
"""

uvec = []

for i in range(len(xvec)):
    if i == 0:
        uvec.append(20.0)
    else:
        uvec.append(0.0)

### constructing matrix A

A = []

for i in range(len(xvec)):
    inew = []
    if i == 0:         # first row [1, 0, 0........., 0]
        for h in range(len(xvec)):
            if h == 0:
                inew.append(1.0)
            else:
                inew.append(0.0)
    elif i == len(xvec) - 1:      # last row is [0, 0, 0...... , 1]
        for h in range(len(xvec)):
            if h == len(xvec) - 1:
                inew.append(1.0)
            else:
                inew.append(0.0)
    else:               # constructing rows 2 through second-to-last row
        for j in range(len(xvec)):
            if j == i:
                inew.append(1 - 2*lamd)
            elif j == i-1 or j == i + 1:
                inew.append(lamd)
            else:
                inew.append(0.0)
    A.append(inew)
                
A = np.array(A)
uvec = np.array(uvec)
xvec = np.array(xvec)

for i in range(0,10):
    unew = A.dot(uvec)
    uvec = unew

plt.scatter(xvec, uvec, color = 'red', s = 7)
plt.title('Temperature along rod at t = .10 s')
plt.xlabel('position')
plt.ylabel('temperature')
plt.show()

sys.exit(0)

