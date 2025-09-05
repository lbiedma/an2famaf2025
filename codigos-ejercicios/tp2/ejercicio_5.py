import numpy as np 

def egauss(A,b):
    U = A.copy()
    y = b.copy()
    n = U.shape[0]

    for i in range(n):
        if A[i,i] ==0:
            print('se necesita pivoteo!')
        break

    for k in range(n-1):

        v = U[k+1:, k]/U[k,k]
        U[k+1:,k:] = U[k+1:,k:]- np.outer(v,U[k,k:]) 
        y[k+1:] = y[k+1:]-v*y[k]

    return U, y 

#Ejercicio 10

def egaussp(A,b):

    U = A.copy()
    y = b.copy()
    n = U.shape[0]
    # P = np.eye(n)

    for k in range(n-1):
        l =k+np.argmax(np.abs(U[k, k:]))
        U[[k,l],:] = U[[l,k],:]
        y[[k,l]] = y[[l, k]] 
        # P[[k,l],:] = P[[l,k],:] no hace falta para gauss si para lu
        v = U[k+1:, k]/U[k,k]  
        U[k+1:,k+1:] = U[k+1:,k+1:]-np.outer(v, U[k, k+1:])  

        y[k+1:] = y[k+1:]- v*y[k]

    return U, y  









