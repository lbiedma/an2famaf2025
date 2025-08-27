import numpy as np 
import matplotlib.pyplot as plt

#Llamamos a sol_defpos
from ejercicio_14 import sol_defpos

n = 500
# np.diag nos devuelve una matriz de ceros salvo una diagonal.
A = -np.diag(np.ones(n-1), 1)-np.diag(np.ones(n-1), -1)+2*np.eye(n)


b_2 = np.zeros(n)
c = n/2 # Falta probar los otros c
for j in range(n):
    b_2[j] = np.exp(-((j+1)-c)**2/100)

x_sol = sol_defpos(A, b_2)

# Graficamos
plt.plot(b_2, label = 'b_2')
plt.plot(x_sol, label = 'x_sol')
plt.legend()
plt.show()

# Graficamos en una escala logaritmica
plt.semilogy(b_2, label = 'b_2')
plt.semilogy(x_sol, label = 'x_sol')
plt.ylim([1e-4, 1e4])
plt.legend()
plt.show()

# IMPORTANTE
# La idea de graficar la solucion y el vector b_2 es observar que la solucion es 'rara' y el vector b
# es practicamente nulo.
# Esto se de a que la matriz del sistema es mal condicionada.