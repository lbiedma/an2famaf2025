import numpy as np

# Algoritmo de cholesky con producto interior
def cholesky_int(A):
    n = A.shape[0]
    G = np.zeros((n,n))
    if A[0,0] <= 0:
        raise Exception('La matriz no es definida positiva') # Si se cumple la condicion
                                                             # salimos del algoritmo  
    G[0,:] = A[0,:]
    G[0,:] = G[0,:]/np.sqrt(G[0,0])

    for i in range(1, n):
        G[i,i:] = A[i, i:]- G[0:i,i].T@G[0:i,i:]
        if G[i,i] < 0:
            raise Exception('La matriz no es definida positiva') # Si se cumple la condicion
                                                                 # hay una excepcion
        G[i,i:] = G[i,i:]/np.sqrt(G[i,i])
    return G

# TEST
B = np.array([[4., -1, 0,], [-1, 4, -1], [0, -1, 4]])
I = np.eye(3)
ceros = np.zeros((3,3))
B_ = np.block([[B, -I, ceros], [-I, B, -I], [ceros, -I, B]])

#G_sol = cholesky_int(B_)
#print(f'B_={B_}')
#print(f'G = {G_sol}')
#print(f'G.T@G ={G_sol.T@G_sol}')