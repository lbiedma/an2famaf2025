import numpy as np
import matplotlib.pyplot as plt

def aut_rayleigh(matrix, q_0, eps, mit):
    q = q_0 / np.linalg.norm(q_0, 2)
    q_hat = q.copy()
    rho = np.inner(q_0, (matrix @ q_0))
    m, _ = matrix.shape
    aproxs = [rho]

    for _ in range(mit):
        # definir z tal que (A - rho * I)z = q_hat (recomendado LU con pivoteo)
        z = np.linalg.solve(matrix - rho * np.eye(m), q_hat) # RESOLVER SIN LINALG.SOLVE
        sigma = np.sqrt(np.inner(z, z))
        q = z / sigma
        theta = np.inner(q, q_hat) / sigma

        if abs(theta) <= eps:
            break

        q_hat = q
        rho = rho + theta
        aproxs.append(rho)

    return q, rho, aproxs


# TEST
A = np.random.random((10, 10))
q_0 = np.random.random(10)
eps = 1e-8
mit = 1000

q, rho, aproxs = aut_rayleigh(A, q_0, eps, mit)
lambdas, vs = np.linalg.eig(A)
print(f"Autovalores: {lambdas}")
print(f"Autovectores: {vs}")

print(f"q = {q}, rho = {rho}")
plt.plot(aproxs)
plt.show()
