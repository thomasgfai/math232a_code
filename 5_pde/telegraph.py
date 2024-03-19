#!/usr/bin/python
import numpy as np
from scipy.integrate import odeint
from math import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

# Grid size
m=64
vinit=np.zeros((m))
v2init=np.zeros((m))
snaps=40
iters=10
dt=0.001
dt=0.0001

# Function to return one lower index, wrapping around at zero
def li(i):
	if i==0: return m-1
	else: return i-1

# Function to return one higher index, wrapping around at m
def ri(i):
	if i==m-1: return 0
	else: return i+1

# Semi-discretization
def deriv(x,t):
        temp = np.array([x[i+m] for i in range(m)])
	temp1 = np.array([c*c*idx*idx*(x[ri(i)]-2*x[i]+x[li(i)]) for i in range(m)])
        temp2 = np.array([-a*x[i+m]-b*x[i] for i in range(m)])
        return np.hstack((temp,temp1+temp2))

# PDE-related constants
a=10.0
#a=0.01
c=1.0
#c=0.1
b=0.1
b=0
dx=1.0/m
idx=1.0/dx

# Initial condition
tinit=10.0/80
tinit=1.0/80
xc=0.5
for i in range(m):
    x=dx*i
    vinit[i]=np.sqrt(1.0/(4*np.pi*c*c/a*tinit)) \
             *np.exp(-(x-xc)**2/(4*c*c/a*tinit))
    #v2init[i]=0
    v2init[i]=4*c*c/a*(x-xc)**2/(4*c*c/a*tinit)**2 \
             *np.exp(-(x-xc)**2/(4*c*c/a*tinit)) \
             *np.sqrt(1.0/(4*np.pi*c*c/a*tinit)) \
             -0.5*4*np.pi*c*c/a*(4*np.pi*c*c/a*tinit)**-1.5 \
             *np.exp(-(x-xc)**2/(4*c*c/a*tinit))
vinit=np.hstack((vinit,v2init))

# Solve ODE using the "odeint" library in SciPy
steps=snaps*iters
time=np.linspace(0,dt*steps,steps+1)

# Integrate the semi-discretized PDE
v=odeint(deriv,vinit,time);
u=v[:,0:m]

uu=np.zeros((snaps+1,m))
ex_uu=np.zeros((snaps+1,m))
err_uu=np.zeros((snaps+1,m))
for j in range(snaps+1):
  for i in range(m):
      uu[j,i]=u[j*iters,i]
      ex_uu[j,i]=1/np.sqrt(4*np.pi*c*c/a*(dt*iters*j+tinit)) \
                  *np.exp(-(dx*i-xc)**2/(4*c*c/a*(dt*iters*j+tinit)))
err_uu=ex_uu-uu

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
surf=ax.plot_surface(mgt,mgx,uu,cmap=cm.coolwarm,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')

fig=plt.figure()
ax=fig.gca(projection='3d')
surf=ax.plot_surface(mgt,mgx,ex_uu,cmap=cm.coolwarm,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')

fig=plt.figure()
ax=fig.gca(projection='3d')
surf=ax.plot_surface(mgt,mgx,err_uu,cmap=cm.coolwarm,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')
plt.show()
