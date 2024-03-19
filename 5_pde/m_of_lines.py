#!/usr/bin/python
import numpy as np
from scipy.integrate import odeint
from math import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Grid size
m=64
a=np.zeros((m))
snaps=40
iters=10

# Function to return one lower index, wrapping around at zero
def li(i):
	if i==0: return m-1
	else: return i-1

# Semi-discretization
def deriv(x,t):
	return np.array([-cidx*(x[i]-x[li(i)]) for i in range(m)])

# PDE-related constants
c=0.1
dx=1.0/m
cidx=c/dx
dt=0.01

# Initial condition
for i in range(m):
    x=dx*i
    a[i]=exp(-20*(x-0.5)**2)

# Solve ODE using the "odeint" library in SciPy
steps=snaps*iters
time=np.linspace(0,dt*steps,steps+1)

# Integrate the semi-discretized PDE
u=odeint(deriv,a,time);

uu=np.zeros((snaps+1,m))
for j in range(snaps+1):
  for i in range(m):
      uu[j,i]=u[j*iters,i]

## Output results
#for j in range(m):
#    e=[str(j*dx)]
#    for i in range(snaps+1):
#        e.append(str(u[i*iters,j]))
#    print " ".join(e)

# Plot using Matplotlib
xa=np.linspace(0,1,m)
xt=np.linspace(0,dt*steps,snaps+1)
mgt,mgx=np.meshgrid(xa,xt);
fig=plt.figure()
ax=fig.gca(projection='3d')
print mgt.shape
print mgx.shape
print uu.shape
surf=ax.plot_surface(mgt,mgx,uu,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')
plt.show()
