#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg
from scipy.integrate import odeint
from math import *

# ODE definition
def odefun(u,t):
  dudt = t-t*tan(u)
  return dudt

# Initial conditions 
t0=0.0
u0=15.0
t1 = 10.0

# Set grid resolution
n=1000
h=(t1-t0)/(n-1)
t=np.linspace(t0,t1,n)

usol = odeint(odefun,u0,t)

plt.plot(t, np.tan(usol), 'b', label='u(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.show()

# Several different initial conditions 
u0=20.0
usol20 = odeint(odefun,u0,t)
u0=15.0
usol15 = odeint(odefun,u0,t)
u0=5.0
usol5 = odeint(odefun,u0,t)
u0=0.0
usol0 = odeint(odefun,u0,t)
u0=-5.0
usolm5 = odeint(odefun,u0,t)

plt.plot(t,np.tan(usol20),t,np.tan(usol), \
  t,np.tan(usol15),t,np.tan(usol5), \
  t,np.tan(usol0),t,np.tan(usolm5))
plt.legend(['u_0=20','u_0=15', \
  'u_0=10','u_0=5', \
  'u_0=0','u_0=-5' \
],loc='best')
plt.xlabel('t')
plt.show()

# ODE definition
def odefun(u,t):
  dudt = -u+1.0/(1+t*t)
  return dudt

# Initial conditions 
t0=2.0
u0=3.0
t1 = 1000.0

# Set grid resolution
n=1000
h=(t1-t0)/(n-1)
t=np.linspace(t0,t1,n)

usol = odeint(odefun,u0,t)
uinit = 3.0*np.exp(2.0-t)
uasymp = 1.0/(t*t)

# Plot the results
#plt.loglog(t,usol,'-',t,uasymp,'o',t,uinit,'+')
plt.loglog(t,usol,'-',t,uinit,'+')
plt.loglog(uasymp,'o',mfc='none')
plt.legend(['exact','initial','asymptotic'],loc='best')
plt.xlabel('t')
plt.ylim(10**-8,10**2)
plt.show()
