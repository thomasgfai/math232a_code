#!/usr/bin/python
import numpy as np
from math import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Grid size
m=64
a=np.zeros((m))
b=np.zeros((m))
snaps=40
iters=10
z=np.zeros((m,snaps+1))

# PDE-related constants; try switching c to -0.1 to see the unstable scheme
c=0.1
dx=1.0/m
dt=0.01
nu=c*dt/dx
print 'nu is', nu

# Initial condition
for i in range(m):
    x=dx*i
    a[i]=exp(-20*(x-0.5)**2)
z[:,0]=a

# Integrate the PDE
for i in range(1,snaps+1):
    for k in range(iters):
        for j in range(m):
            jl=j-1
            if jl<0: jl+=m
            b[j]=(1-nu)*a[j]+nu*a[jl]
        a=np.copy(b)
    z[:,i]=a

## Output results
#for j in range(m):
#    e=[str(j*dx)]
#    for i in range(snaps+1):
#        e.append(str(z[j,i]))
#    print " ".join(e)

# Plot using Matplotlib
xa=np.linspace(0,1,m)
xt=np.linspace(0,dt*snaps*iters,snaps+1)
mgt,mgx=np.meshgrid(xa,xt);
fig=plt.figure()
ax=fig.gca(projection='3d')
print mgt.shape
print mgx.shape
print z.shape
surf=ax.plot_surface(mgt,mgx,z.T,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')
plt.show()
