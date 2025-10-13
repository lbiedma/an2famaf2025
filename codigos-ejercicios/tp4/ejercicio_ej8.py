
import numpy as np 

import sys
sys.path.append('codigos-ejercicios')
sys.path.append('tp1')

from tp1.ejercicio_5 import sol_trinffil
from tp1.ejercicio_5 import sol_trsupcol
from tp1.ejercicio_13 import cholesky_int
from sol_cuadmin import sol_cuadmin

#----------------------------------------------------------------

import matplotlib.pyplot as plt

def matriz_a(eps, res):
    A = np.array([[1., 1], 
                  [eps, 0], 
                  [0, eps]])
    
    b = np.array([1., 1, 1])
    
    A_tilde = A.T@A

    b_tilde = A.T@b 

    # resolviendo con Cholesky
    if res == 0:
        G = cholesky_int(A_tilde)
        y = sol_trinffil(G.T, b_tilde)
        x = sol_trsupcol(G, y)
    if res == 1:
        x, r = sol_cuadmin(A_tilde, b_tilde) 

    return x

eps = np.linspace(1e-10, 2, 100)

n = len(eps)

x_sol_G = np.zeros((n, 2))

for i in range(n):
     x_sol_G[i, :] = matriz_a(eps[i], 0)


x_sol_cuad = np.zeros((n, 2))

for i in range(n):
     x_sol_cuad[i, :] = matriz_a(eps[i], 1)

print(x_sol_cuad)

plt.plot(eps, x_sol_G[:, 0], 'r')
plt.plot(eps, x_sol_G[:, 1], 'r')
plt.show()

plt.plot(eps, x_sol_cuad[:, 0], 'b')
plt.plot(eps, x_sol_cuad[:, 1], 'b')
plt.show()




     




