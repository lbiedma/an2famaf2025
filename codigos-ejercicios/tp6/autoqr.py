import numpy as np

import sys
sys.path.append("codigos-ejercicios")
sys.path.append("tp4")

from tp4.Ejercicio_3givens import qrgivens
from tp4.givensp import qrgivensp

def autqr(A, m = 500):

    T0 = A.copy()
    n = T0.shape[0]
    Q = np.eye(n)
    for k in range(m):
        U, R =  qrgivens(T0) # Paso 1 
        T = R@U # paso 2

        Q = Q@U # paso adicional ir actualizando Q
        
        T0 = T # Actualizar T0
    
    return Q,T

A = np.random.rand(3,3)

Q, T = autqr(A) 
auto_A = np.linalg.eig(A)[0] 

print(auto_A)
print('--------------')
print(T)

    


    


