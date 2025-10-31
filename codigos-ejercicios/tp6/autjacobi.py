import numpy as np 

def jacobi_cs(A):
    c = 1
    s = 0

    if A[0, 1] == 0:
        return c, s
    
    tau = (A[1, 1] - A[0,0])/(2*A[0,1])

    if tau < 0:
        t = 1/(-tau + np.sqrt(1+tau**2))
    else:
        t = -1/(tau + np.sqrt(1+tau**2))
    
    c = 1/np.sqrt(1+t**2)
    s = t*c

    return c, s

def off(A): # Era conveniente tener una funcion de off 
    A_aux = A - np.diag(np.diag(A))
    off_A = np.linalg.norm(A_aux, "fro")
    return off_A

def autjacobi(A, eps = 1e-10, m= 500):

    if np.linalg.norm(A-A.T, 'fro') != 0:
          return print('A no es simetrica')
    
    B = A.copy()
    n = B.shape[0]
    Q = np.eye(n)
    off_B = off(B) # Antes de entrar al ciclo calculamos off de B

    for k in range(m):
        if off_B <= eps:
            break 

        else: 
             B_diag = np.diag(np.diag(B))
             B_k = B - B_diag
             i, j = np.unravel_index(np.argmax(np.abs(B_k)), B.shape)
             B_aux = np.array([[B[i,i], B[i,j]], 
                              [B[j, i], B[j,j]]])
             
             c, s =  jacobi_cs(B_aux)

             J = np.array([[c, -s], [s, c]])

             B[[i,j], :] = J.T@B[[i,j], :]
             B[:, [i,j]] = B[:, [i,j]]@J

             Q[:, [i,j]] = Q[:, [i,j]]@J

             off_B = off(B) # Este paso no lo tenia entonces habia que actualizar para el nuevo B

    return Q, B

A = np.random.rand(3,3)
A  = A.T@A

Q, B = autjacobi(A)

B_np, _ = np.linalg.eig(A)

print(np.diag(B))

print(B_np)