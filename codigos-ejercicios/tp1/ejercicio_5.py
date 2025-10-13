'''
Implementación sol_trinffil y sol_trsupcol

'''

import numpy as np 

'''Triangular inferior por filas'''
# Resuelve Ax=b con A triangular inferior utilizando 
# el método de sustitución hacia adelante por filas

def sol_trinffil(A,b):
    n = len(b)
    x = np.copy(b)
    for idx, b_i in enumerate(b):
        if b_i!=0:
            j = idx
            break

    for i in range(j,n):
        x[i] = (b[i]- A[i, :i]@x[:i])/A[i,i]

    return x

# # TEST
# A = np.array([[1., 0, 0, 0], [-1., 1, 0, 0], [0., -1, 1, 0], [0., 0, -2, 2]])
# b = np.array([0., 0, 1, 1]) 
# x_sol = sol_trinffil(A, b)

# print('Aplicando la funcion sol_trinffil')
# print(f'x_sol = {x_sol}')
# print(f'b-A@x_sol = {b - A@x_sol}')
# print('----------------------------------------')


'''Triangular superior por columnas'''
# resuelve Ax=b con A triangular superior utilizando 
# el método de sustitución hacia atrás por columnas

def sol_trsupcol(A, b):
    n = len(b)
    x = b.copy()

    for idx in reversed(range(n)):
        if b[idx] != 0:
            j = idx
            break

    for i in reversed(range(j + 1)):
        x[i] = x[i] / A[i, i]
        x[:i] = x[:i] - A[:i, i] * x[i]

    return x

# # TEST
# B = np.array([[1., 2, -1, 1], [0, 1, 0, -1], [0, 0, -1, 4], [0, 0, 0, 1]])
# b = np.array([2, -1, 0, 0])
# x_sol = sol_trsupcol(B, b)

# print('Aplicando la funcion sol_trsupcol')
# print(f'x_sol = {x_sol}')
# print(f'b-B@x_sol = {b - B@x_sol}')
# print('----------------------------------------')

# Probemos los métodos para matrices random

# '''Triangular inferior'''
# B_inf = np.random.rand(4,4)
# C_inf = np.tril(B_inf) # Me devuelve la matriz random como una triangular inferior 
# d = np.random.rand(4)
# x_sol_inf = sol_trinffil(C_inf, d)
# print('Aplicando la funcion sol_trinffil para una matriz random tril')
# print(f'x_sol_inf = {x_sol_inf}')
# print(f'd - C_inf@x_sol_inf = {d - C_inf@x_sol_inf}')
# print('----------------------------------------')

# '''Triangular superior'''
# B_sup = np.random.rand(4,4)
# C_sup = np.triu(B_sup) # Me devuelve la matriz random como una triangular superior 
# d1 = np.random.rand(4)
# x_sol_sup = sol_trsupcol(C_sup, d1)
# print(C_sup@x_sol_sup-d1)

# print('Aplicando la funcion sol_trisupcol para una matriz random sup')
# print(f'x_sol_sup = {x_sol_sup}')
# print(f'd1 - C_sup@x_sol_sup = {d1 - C_sup@x_sol_sup}')
# print('----------------------------------------')