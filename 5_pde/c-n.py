#!/usr/bin/python
import numpy as np
from math import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

# Grid size
m=64
a=np.zeros((m))
b=np.zeros((m))
c=np.zeros((m))
iters=10000
#iters=1000
snaps=100

sola = np.zeros((m,snaps))
solb = np.zeros((m,snaps))
vis_iter = 0

# PDE-related constants. The timestep is chosen to be just larger than the
# point of stability, causing the 2-gridpoint oscillation to slowly grow.
alpha=0.1
dx=1.0/(m-1)
dt=0.51*dx*dx/alpha
#dt=0.1*dx*dx/alpha
nu=alpha*dt/(dx*dx)

# Matrix for Crank-Nicolson
u=np.zeros((m,m))
u[0,0]=1;u[m-1,m-1]=1
for i in range(1,m-1):
    u[i,i]=(1+nu)
    u[i,i-1]=-0.5*nu
    u[i,i+1]=-0.5*nu

# Initial condition
for i in range(1,m-1):
    a[i]=sin(i*dx*pi)
    b[i]=sin(i*dx*pi)

# Integrate the PDE
print 0.,0.,0.
for j in range(0,iters+1):

    # Forward Euler
    for i in range(1,m-1):
        c[i]=(1-2*nu)*a[i]+nu*(a[i-1]+a[i+1])
    a=np.copy(c)

    # Crank-Nicolson
    for i in range(1,m-1):
        c[i]=(1-nu)*b[i]+0.5*nu*(b[i-1]+b[i+1])
    c[0]=0;c[m-1]=0;
    b=np.linalg.solve(u,c)

    # L2 norm
    if (j+1)%100==0:
        t=(j+1)*dt
        l2a=0;l2b=0
        for i in range(1,m-1):
            sol=sin(i*dx*pi)*exp(-alpha*pi*pi*t)
            l2a+=(sol-a[i])**2
            l2b+=(sol-b[i])**2

            sola[i,vis_iter] = a[i] 
            solb[i,vis_iter] = b[i] 
        vis_iter += 1
        #print t,sqrt(l2a/m),sqrt(l2b/m)

# Plot using Matplotlib
xa=np.linspace(0,1,m)
xt=np.linspace(0,dt*iters,snaps)
mgt,mgx=np.meshgrid(xa,xt);
fig=plt.figure()
ax=fig.gca(projection='3d')
print mgt.shape
print mgx.shape
print sola.shape
surf=ax.plot_surface(mgt,mgx,sola.T,cmap=cm.coolwarm,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')

fig=plt.figure()
ax=fig.gca(projection='3d')
print mgt.shape
print mgx.shape
print solb.shape
surf=ax.plot_surface(mgt,mgx,solb.T,cmap=cm.coolwarm,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')
plt.show()
