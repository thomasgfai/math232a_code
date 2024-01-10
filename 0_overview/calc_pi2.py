#program to calculate digits of pi

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

#Here we get Python's pi calculation to 30 digits
try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp
mp.dps = 60  # set number of digits
print(mp.pi)   # print ground truth pi

#Compare to Gregory formula
n_iter = 100
pi_gregory = []
sum = mp.mpf(0.0)
for i in range(0,n_iter):
  sum = sum+(-1)**i/(mp.mpf(2*i)+1.0)
  pi_gregory.append(sum*4.0)

pi_arctan = []
sum1 = mp.mpf(0.0)
sum2 = mp.mpf(0.0)
for i in range(0,n_iter):
  sum1 = sum1+(-1)**i/(mp.mpf(2.0)**(2*i+1)*(2*i+1.0))
  sum2 = sum2+(-1)**i/(mp.mpf(3.0)**(2*i+1)*(2*i+1.0))
  pi_arctan.append((sum1+sum2)*4.0)

pi_machin = []
sum1 = mp.mpf(0.0)
sum2 = mp.mpf(0.0)
for i in range(0,n_iter):
  sum1 = sum1+(-1)**i/(mp.mpf(5.0)**(2*i+1)*(2*i+1.0))
  sum2 = sum2+(-1)**i/(mp.mpf(239.0)**(2*i+1)*(2*i+1.0))
  pi_machin.append((4.0*sum1-sum2)*4.0)

pi_ramanujan = []
sum = mp.mpf(0.0)
for i in range(0,n_iter):
  sum = sum+mp.factorial(4*i)/(mp.mpf(4)**i*mp.factorial(i))**4*(1103+26390*mp.mpf(i))/mp.mpf(99)**(4*i)
  pi_ramanujan.append(1.0/(2.0*mp.sqrt(2)/9801*sum))

plt.figure()
plt.plot(pi_gregory,label='Gregory')
plt.plot(pi_arctan,label='simple arctan')
plt.plot(pi_machin,label='Machin')
plt.plot(pi_ramanujan,label='Ramanujan')
plt.legend()
plt.xlabel('Iteration',Fontsize=16)
plt.title("Convergence to $\pi$",Fontsize=16)

plt.figure()
error_gregory = [x-mp.pi for x in pi_gregory]
plt.semilogy(error_gregory,'g.',label='Gregory')
error_arctan = [x-mp.pi for x in pi_arctan]
plt.semilogy(error_arctan,'r.',label='simple arctan')
error_machin = [x-mp.pi for x in pi_machin]
plt.semilogy(error_machin,'b.',label='Machin')
error_ramanujan = [x-mp.pi for x in pi_ramanujan]
plt.semilogy(error_ramanujan,'k.',label='Ramanujan')
plt.legend()
plt.xlabel('Iteration',Fontsize=16)
plt.ylabel('Error',Fontsize=16)
plt.show()
  
