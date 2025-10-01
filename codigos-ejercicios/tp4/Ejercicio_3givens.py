import numpy as np

def rotgivens(x1, x2):
    x_1 = x1.copy()
    x_2 = x2.copy()

    if np.abs(x_1)+np.abs(x_2)==0:
        c =1
        s= 0
    elif np.abs(x_2)>np.abs(x_1):
         tau = -x_1/x_2
         s= -np.sign(x_2)/np.sqrt(1+tau**2)
         c = s*tau

    else:
        tau = -x_2/x_1
        c= np.sign(x_1)/np.sqrt(1+tau**2)
        s = c*tau
    
    return c, s

def qrgivens(A):
    R = A.copy()
    m,n = A.shape[0],A.shape[1]
    Q = np.eye(m)
    p = np.min([m-1, n]) 

    if p > 0:
        for j in range(p):
            for i in range(j+1,m):
                if R[i,j]!=0:
                    c,s = rotgivens(R[j,j],R[i,j])
                    G = np.array([[c, -s], [s, c]])
                    R[[j,i], j:] = G@R[[j,i], j:]
                    Q[:, [j,i]] = Q[:, [j,i]]@G.T
        
        if m<= n and R[m-1, m-1]<0:
            R[m-1, m-1:] = -R[m-1, m-1:]  
            Q[:, m-1] = -Q[:, m-1]

    return Q, R 

A = np.array([[2., 3], [5, 7]])

Q, R = qrgivens(A)

A = np.random.rand(3,4)
print(A)
Q, R = qrgivens(A)
print('-----------------------')
print(R)
print('-----------------------')
print(Q@R-A)
print('-----------------------')
print(Q.T@Q)










            








      
















     
       






