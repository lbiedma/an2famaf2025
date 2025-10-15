import numpy as np 

def dlu(A):
     A = A.copy()
     n = A.shape[0]
     for k in range(n-1):
         A[k+1:, k] = A[k+1:, k]/A[k,k]
         A[k+1:, k+1:] = A[k+1: , k+1:] - np.outer(A[k+1: , k],A[k, k+1:])
    
     U = np.triu(A)
     L = np.tril(A,-1)+np.eye(n)
   
     return L, U 

# A = np.random.random((4,4))
# b = np.random.random(4)

# U, L = dlu(A)

# print(A)

# print(L@U) 
