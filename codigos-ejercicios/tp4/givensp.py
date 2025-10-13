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

def qrgivensp(A):
    m, n = A.shape
    Q = np.eye(m)
    P = np.eye(n)
    R = A.copy()
    c_tilde = np.linalg.norm(A, axis=0) ** 2
    p = min(m - 1, n)

    for j in range(p):
        # Pivoteo por derecha, cambiando columnas en vez de filas
        l = j + np.argmax(c_tilde[j:])
        if l != j:
            R[:, [l, j]] = R[:, [j, l]]
            P[:, [l, j]] = P[:, [j, l]]
            c_tilde[[l, j]] = c_tilde[[j, l]]
        # Givens común y corriente
        for i in range(j+1, m):
            if R[i, j] != 0:
                c, s = rotgivens(R[j, j], R[i, j])
                G = np.array([[c, -s], [s, c]])

                R[[j, i], j:] = G @ R[[j, i], j:]
                Q[:, [j, i]] = Q[:, [j, i]] @ G.T
        # Actualización de c SOLO UNA VEZ DESPUES DE ACTUALIZAR FILAS
        c_tilde[j:] = c_tilde[j:] - R[j, j:] * R[j, j:]

    if m <= n and R[m - 1, m - 1] < 0:
        # J = m:
        R[m - 1, m - 1:] = -R[m - 1, m - 1:]
        Q[:, m - 1] = -Q[:, m - 1]

    return Q, R, P