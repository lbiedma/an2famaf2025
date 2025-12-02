
import numpy as np

# metodo ce cauchy

def sol_cauchy(A, b, x0, eps, m):
    
    A_ = A.copy()
    x0_ = x0.copy()
    r0 = b-A_@x0_
    sigma = np.linalg.norm(r0, 2)

    for k in range(m):
        if sigma <= eps:
            break
        else:
            v = A_@r0
            t = sigma**2 / (r0.T @ v)
            x_mas = x0_ + t*r0
            r = r0 - t*v
        x0_ = x_mas
        r0 = r
        sigma = np.linalg.norm(r0, 2)
            
    return x_mas

# A = np.random.rand(4,4)
# A = 0.5*(A+A.T)
# A = np.eye(4)+A
# b = np.random.rand(4)
# x0 = np.zeros(4)
# m = 100
# eps = 1e-10

# x_sol = sol_cauchy(A, b, x0, eps, m)

# print(A@x_sol-b)

def sol_gastinel(A, b, x0, eps, m):
    
    A_ = A.copy()
    x0_ = x0.copy()
    r0 = b-A_@x0_
    sigma = np.linalg.norm(r0, np.inf)
    d = np.sign(r0)

    for k in range(m):
        if sigma <= eps:
            break
        else:
            v = A_@d
            t = np.dot(r0, d) / np.dot(d,v)
            x_mas = x0_ + t*d
            r = r0 - t*v
        x0_ = x_mas
        r0 = r
        d = np.sign(r0)
        sigma = np.linalg.norm(r0, np.inf)
            
    return x_mas

A = np.random.rand(4,4)
A = 0.5*(A+A.T)
A = np.eye(4)+A
b = np.random.rand(4)
x0 = np.zeros(4)
m = 100
eps = 1e-20

x_sol = sol_gastinel(A, b, x0, eps, m)

print(A@x_sol-b)