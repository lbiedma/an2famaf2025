import numpy as np 

def dlup(A):
    n = A.shape[0]
    U = A.copy()
    P = np.eye(n)
    for k in range(n): 
        l = k + np.argmax(np.abs(U[k:, k]))
        if l != k:
            
            U[[k, l], :] = U[[l, k], :]
            P[[k, l], :] = P[[l, k], :]
        
        U[k+1: , k] = U[k+1:, k]/U[k, k] 
        U[k+1: , k +1:] = U[k+1: , k+1:]-np.outer(U[k+1: , k], U[k, k+1:])
        
    L = np.tril(U,-1)+np.eye(n)
    U = np.triu(U)
           
    return U, L, P 


# A1 = np.array([[2., 10, 8, 8, 6], [1, 4, -2, 4, -1], [0, 2, 3, 2, 1], [3, 8, 3, 10, 9], [1, 4, 1, 2, 1]])

# U, L, P = dlup(A1)

# x = 1 + np.argmax(np.abs(A1[1:, 1]))
# #print(x)
# #print(A1)
# #print(P.T@L@U)
