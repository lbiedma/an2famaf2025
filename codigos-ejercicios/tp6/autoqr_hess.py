import numpy as np

import sys
sys.path.append('codigos-ejercicios')
sys.path.append('tp4')

from tp4.Ejercicio_3givens import qrgivens
from tp4.Ejercicio_3givens import rotgivens
from ejer_hess import fhess


def autqr(A, err= 1e-10, M = 500):
    n = A.shape[0]
    Q, H = fhess(A)
    G_rot = np.zeros((n, 2))
    
    for k in range(M):
        for j in range(n-1):
            c, s = rotgivens(H[j, j], H[j+1, j])
            G_rot[j, :] = np.array([c, s])
            G_cs = np.array([[c, -s], [s, c]])
            H[[j, j+1], j:] = G_cs @ H[[j, j+1], j:]
            
        for i in range(n-1):
            c, s = G_rot[i, :]
            G_cs = np.array([[c, -s], [s, c]])
            H[: , [i, i+1]] = H[: , [i, i+1]] @ G_cs.T
            Q[: , [i, i+1]] = Q[: , [i, i+1]] @ G_cs.T 
            
        if np.linalg.norm(H - np.diag(np.diag(H)), 'fro') < err:
            print ("llegamos a la tolerancia")
            break    
            
    return Q, H        


# A = np.random.random((3, 3))
# Q, H = autqr(A)
# print(np.linalg.eigvals(A))
# print(np.diag(H))

# print(np.linalg.norm(Q @ H @ Q.T - A))