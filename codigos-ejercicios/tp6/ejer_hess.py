
import numpy as np 

import sys
sys.path.append('codigos-ejercicios')
sys.path.append('tp4')

from tp4.ejercicio_3holder import refhholder

def fhess(A):
    m, n = A.shape
    if m != n:
        print("La matriz no es cuadrada")
        return None
    Q = np.eye(m)
    H = A.copy()
    
     
    for j in range(n-2):
            #I = j+1: , J =j:
            u, rho = refhholder(H[j+1:, j])
            w = rho * u 
            H[j+1:, j:] = H[j+1:, j:] - np.outer(w, u.T @ H[j+1:, j:])
            H[:, j+1:] = H[:, j+1:] - H[:, j+1:]@ np.outer(w, u.T)
            Q[:, j+1:] = Q[:, j+1:] - Q[:, j+1:]@np.outer(w, u.T)
      
    return Q, H 
  
#Test
# A = np.random.random((5,5))
# Q_h, H_h = fhess(A)
# print(np.linalg.norm(Q_h@H_h@Q_h.T -A))




