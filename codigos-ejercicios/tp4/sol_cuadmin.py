import numpy as np 
from tp1.ejercicio_5 import sol_trsupcol

from givensp import qrgivensp


def sol_cuadmin(A, b):
    m,n = A.shape
    y = np.zeros(n)

    p = min(m, n)
    Q, R, P = qrgivensp(A)
    q = Q.T@b

    r_i = np.diag(R)
    ceros = np.where(r_i == 0)[0]
    
    if len(ceros)!=0:
        p = ceros[0]
    y[:p] = sol_trsupcol(R[:p,:p], q[:p])
    
    return P@y, np.linalg.norm(q[p:])