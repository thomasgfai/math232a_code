#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

# Matrices
a=np.array([[998,1998],[-999,-1999]])
i=np.identity(2)

# Initial conditions
ye=np.array([[1],[0]])
yi=np.array([[1],[0]])

# Starting time and timestep (currently chosen within the stability region of
# the explicit method)
t=0
dt=0.001
#dt=0.002

Nsteps = np.ceil(2/dt)
tvec = []
ex1vec = []
ex2vec = []
ye1vec = []
ye2vec = []
yi1vec = []
yi2vec = []

while t<2:

    # Print solutions and exact solution
    ex1=2*exp(-t)-exp(-1000*t)
    ex2=-exp(-t)+exp(-1000*t)

    tvec.append(t) 
    ex1vec.append(ex1)
    ex2vec.append(ex2)
    ye1vec.append(ye[0,0])
    ye2vec.append(ye[1,0])
    yi1vec.append(yi[0,0])
    yi2vec.append(yi[1,0])

    # Explicit step
    ye=ye+dt*np.dot(a,ye)

    # Implicit step
    yi=np.linalg.solve(i-dt*a,yi)

    t+=dt

# Plot the results
plt.plot(tvec,ex1vec,'.',tvec,ye1vec,'-',tvec,yi1vec,'+',)
plt.legend(['exact','explicit','implicit'],loc='best')
plt.show()

plt.figure()
plt.plot(tvec,ex2vec,'.',tvec,ye2vec,'-',tvec,yi2vec,'+',)
plt.legend(['exact','explicit','implicit'],loc='best')
plt.show()
