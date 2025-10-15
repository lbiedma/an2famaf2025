
import numpy as np 

import sys
sys.path.append('codigos-ejercicios')
sys.path.append('tp1')
sys.path.append('tp2')


from tp1.ejercicio_5 import sol_trinffil
from tp1.ejercicio_5 import sol_trsupcol
from tp1.ejercicio_13 import cholesky_int
from sol_cuadmin import sol_cuadmin
from tp2.ejrcicio_6_lu import dlu

#----------------------------------------------------------------

import matplotlib.pyplot as plt

def matriz_a(n, met_res):

    eps = np.zeros(n)
    x_sol = np.zeros((n,2))
    kappa = np.zeros(n)

    b = np.array([1., 1, 1])
    
    for i in range(n):
        eps[i] = 2**(-(i))
    
    for i in range(n):
        A = np.array([[1., 1], 
                     [eps[i], 0], 
                     [0, eps[i]]])
        
        # resolviendo con Cholesky para ecuacion normal
        if met_res == 0:
           A_tilde = A.T@A
           b_tilde = A.T@b 

           G = cholesky_int(A_tilde)
           y = sol_trinffil(G.T, b_tilde)
           x_sol[i] = sol_trsupcol(G, y)
           kappa[i] = np.linalg.cond(A_tilde)

        # resolviendo con lu para ecuacion normal 
        if met_res == 1:
            A_tilde = A.T@A
            b_tilde = A.T@b
            
            L, U = dlu(A_tilde)
            y = sol_trinffil(L, b_tilde)
            x_sol[i] = sol_trsupcol(U, y)
            kappa[i] = np.linalg.cond(A_tilde)

        # resolviendo con cuadmin
        if met_res == 2:
           x_sol[i], r = sol_cuadmin(A, b) 
           kappa[i] = np.linalg.cond(A)

    return x_sol, kappa

n = 100

x_sol_G, cond_G = matriz_a(n, 0)
print(f'sol con Cholesky {x_sol_G[0, :]}', f'cond con Cholesky {cond_G[0]}')

x_sol_LU, cond_LU = matriz_a(n, 1)
print(f'sol con LU {x_sol_LU[-1, :]}', f'cond con LU {cond_LU[-1]}')

x_sol_cm, cond_cm = matriz_a(n, 2)
print(f'sol con cuadmin {x_sol_cm[-1, :]}', f'cond con cuadmin {cond_cm[-1]}')




# # for i in range(n):
# #      x_sol_G[i, :] = matriz_a(eps[i], 0)


# x_sol_cuad = np.zeros((n, 2))

# for i in range(n):
#      x_sol_cuad[i, :] = matriz_a(eps[i], 1)

# # plt.plot(eps, x_sol_G[:, 0], 'r')
# # plt.plot(eps, x_sol_G[:, 1], 'r')
# # plt.show()
# print(x_sol_cuad)

# plt.plot(eps, x_sol_cuad[:, 0], 'b')
# plt.plot(eps, x_sol_cuad[:, 1], 'b')
# plt.show()




     




