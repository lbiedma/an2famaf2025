import numpy as np 

# 0, 1, 2 indices de las filas 
# 0, 1, 2 indices de columnas 

A = np.array([[1, 3, 2],[2, 1, 1],[-1, 0 ,1]])
#print(A)
B = np.array([[1, 0, 1],[2, 1, 1],[-1, 2 ,0]])

A_00 = A[0:2, 0:1]
A_01 = A[0:2, 1:3]
A_10 = A[2:3, 0:1]
A_11 = A[2:3, 1:3]

B_00 = B[0:1, 0:1]
B_01 = B[0:1, 1:3]
B_10 = B[1:3, 0:1]
B_11 = B[1:3, 1:3]

# Muestre que AB = C
# A_i0 @ B_0j + A_i1 @ B_1j = C_ij 

# i = 0, j = 0
C_00 = A_00@B_00 + A_01@B_10 
# i = 1, j = 0
C_10 = A_10@B_00 + A_11@B_10 
# i = 0, j = 1
C_01 = A_00@B_01 + A_01@B_11 
# i = 1, j = 1
C_11 = A_10@B_01 + A_11@B_11 

C = np.block([[C_00, C_01], [C_10, C_11]])

print(f'C2= {C}')

# Otra forma...

A_00 = np.array([[1], [2]])
A_01 = np.array([[3, 2], [1, 1]])
A_10 = np.array([[-1]])
A_11 = np.array([[0, 1]])

A = np.block([[A_00, A_01], [A_10, A_11] ])

B_00 = np.array([[1]])
B_01 = np.array([[0, 1]])
B_10 = np.array([[2], [-1]])
B_11 = np.array([[1, 1],[2, 0]])

B = np.block([[B_00, B_01], [B_10, B_11] ])

print(f'C1= {A@B}')

# A[i, :] Recorre la fila i y toda la columna j
# A[i:j, :] Recorre la fila i hasta el indice j-1 y toda la columna j
# A[:i, :] Recorre desde la fila 0 hasta la fila i-1 y toda la columna j

# A[:, j] Recorre toda la fila i y solo toma la columna j
# A[:, j:i] Recorre toda la fila i y la columna j hasta el indice i-1 
# A[:, :j] Recorre toda la fila i  y recorre desde la columna 0 hasta el indice j-1
