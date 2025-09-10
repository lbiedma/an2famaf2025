import numpy as np

A = np.array([
    [1000., 999],
    [999, 998],
])
b = np.array([1., 1])

# Solución del sistema lineal
x = np.linalg.solve(A, b)
print(x)

# obtenemos autovectores
autvals, autvecs = np.linalg.eig(A)
print(f"Autovalores: {autvals}")
print(f"Autovectores: {autvecs}")

# Avanzamos un paso pequeño por el autovector asociado al autovalor más grande y resolvemos
epsilon = 0.0001
x_1 = np.linalg.solve(A, b + epsilon * autvecs[:, 0])
print(x_1)

# Avanzamos un paso pequeño por el autovector asociado al autovalor más pequeño y resolvemos
x_2 = np.linalg.solve(A, b + epsilon * autvecs[:, 1])
print(x_2)

# Cuál es la diferencia relativa? CALCULAR
