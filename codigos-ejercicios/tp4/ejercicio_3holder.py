import numpy as np 

def refhholder(x):
    x_ = x.copy()
    n = len(x_)

    if n==1:
        sigma = 0
    else:
        sigma = np.sum(x_[1:]**2)
    
    if sigma == 0 and x_[0]>=0:
        rho = 0
        u = x_
        u[0]=1.
    else:
        mu = np.sqrt(x_[0]**2 + sigma)    
        if x_[0]<=0:
            gamma = x_[0]-mu
        else:
            gamma = -sigma/(x_[0]+mu)
        rho = 2*(gamma**2)/(gamma**2+sigma)
        u = x_/gamma
        u[0] = 1.
        
    return u, rho 

def qrhholder(A):
    R = A.copy()
    m,n = R.shape
    Q = np.eye(m)
    p = np.min([m,n])
    for j in range(p):
        u, rho = refhholder(R[j:, j])
        u = u.reshape(-1,1)
        w = rho*u
        R[j:,j:] = R[j:,j:]-np.outer(w, u.T@R[j:,j:])
        Q[:, j:] = Q[:, j:] - ((Q[:, j:]@w)@ u.T) # Se puede usar np.outer tambien

    return Q, R 

A = np.array([[2., 3], [5, 7]])
#A = np.random.rand(3,4)

Q, R = qrhholder(A)

print(A)
print('-----------------------')
print(R)
print('-----------------------')
print(Q@R-A)
print('-----------------------')
print(Q.T@Q)
