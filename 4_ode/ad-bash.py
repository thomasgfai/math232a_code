#!/usr/bin/python
# Import math functions
from math import *
import matplotlib.pyplot as plt

lam=0.5
def f(x):
    return lam*x

# Initialize two values to exactly match solution
t=0
dt=0.05
yy = exp(lam*dt)
y=[1,yy]

yvec = [y[0]]
yexvec = [y[0]]
tvec = [0]

t+=dt

# Apply second-order Adams-Bashforth scheme
while t<=2:

    # Analytical solution
    yexact=exp(lam*t)

    tvec.append(t)
    yvec.append(yy)
    yexvec.append(yexact)

    # Print the solutions and error
    print t,y[1],yexact,y[1]-yexact

    # Multi step
    yy=y[1]+dt*(1.5*f(y[1])-0.5*f(y[0]))
    y[0]=y[1]
    y[1]=yy

    # Update time
    t+=dt

plt.plot(tvec,yvec,'-o',tvec,yexvec,'--')
plt.legend(['computed','exact'],loc='best')
plt.show()
