#program to calculate digits of pi

import numpy as np
import matplotlib.pyplot as plt

#Compare to Gregory formula
n_iter = 20
pi_gregory = []
sum = 0.0
for i in range(0,n_iter):
  sum = sum+(-1)**i/(2*i+1.0)
  pi_gregory.append(sum*4.0)

pi_arctan = []
sum1 = 0.0
sum2 = 0.0
for i in range(0,n_iter):
  sum1 = sum1+(-1)**i/(2.0**(2*i+1)*(2*i+1.0))
  sum2 = sum2+(-1)**i/(3.0**(2*i+1)*(2*i+1.0))
  pi_arctan.append((sum1+sum2)*4.0)

pi_manchin = []
sum1 = 0.0
sum2 = 0.0
for i in range(0,n_iter):
  sum1 = sum1+(-1)**i/(5.0**(2*i+1)*(2*i+1.0))
  sum2 = sum2+(-1)**i/(239.0**(2*i+1)*(2*i+1.0))
  pi_manchin.append((4.0*sum1-sum2)*4.0)

pi_ramanujan = []
sum = 0.0
for i in range(0,n_iter):
  sum = sum+np.math.factorial(4*i)/(4.0**i*np.math.factorial(i))**4*(1103.0+26390.0*i)/99.0**(4.0*i)
  pi_ramanujan.append(1.0/(2.0*np.sqrt(2)/9801*sum))

print(pi_ramanujan)
error_arctan = [x-np.pi for x in pi_arctan]
plt.semilogy(error_arctan,'r.',label='simple arctan')
error_gregory = [x-np.pi for x in pi_gregory]
plt.semilogy(error_gregory,'g.',label='Gregory')
error_machin = [x-np.pi for x in pi_manchin]
plt.semilogy(error_machin,'b.',label='Machin')
error_ramanujan = [x-np.pi for x in pi_ramanujan]
plt.semilogy(error_ramanujan,'k.',label='Ramanujan')
plt.legend()
plt.xlabel('Iteration',Fontsize=16)
plt.ylabel('Error',Fontsize=16)
plt.show()
  
