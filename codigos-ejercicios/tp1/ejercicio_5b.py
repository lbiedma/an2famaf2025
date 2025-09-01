import numpy as np

def soltrsup_fil(A, b):
    x = b.copy()
    n = A.shape[0]
    for i in range(n-1, -1, -1):
        # J = [i+1:]
        x[i] = (x[i] - np.inner(A[i, i+1:], x[i+1:])) / A[i, i]

    return x


# TEST
A = np.random.random((5, 5))
A = np.triu(A)
b = np.random.random(5)

y = np.linalg.solve(A, b)
x = soltrsup_fil(A, b)
print(np.allclose(y, x))
