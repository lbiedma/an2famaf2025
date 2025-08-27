import numpy as np

import matplotlib.pyplot as plt

# B+B.T matriz simetrica
# B@B.T matriz simetrica definida positiva

def level(niveles): # Definimos una función 'level' que tiene por entrada una lista de números positivos.
                    # La función debe generar un paraboloide en el plano xy. Para ello, usamos una matriz
                    # aleatoria simétrica y definida positiva.
                    # level tiene por salida las curvas de nivel del paraboloide correspondiente a los números
                    # de la lista de entrada.
    B = np.random.rand(2,2) # Generamos una matriz random 2x2 usando np.random (no es la única forma).

    A = B@B.T # Transformamos la matriz B en una matriz simétrica definida positiva.
    n_puntos = 500 # Definimos el número de puntos que usaremos para generar la gráfica de niveles
                   # (pueden probar con otros valores).

    x = np.linspace(-2, 2, n_puntos) # La lista de puntos sobre el Eje x.
    y = np.linspace(-2, 2, n_puntos) # La lista de puntos sobre el Eje y.

    xgrid, ygrid = np.meshgrid(x, y) # Generamos una malla de puntos sobre el plano xy usando np.meshgrid.
                                     # meshgrid tiene por salida dos matrices de las distintas combinaciones
                                     # del par (x,y) que corresponde a un punto de la cuadrícula (malla).

    z = np.zeros((n_puntos, n_puntos)) # Generamos una matriz de tamaño n_puntos x n_puntos donde iremos guardando los
                                       # valores de z.

    for idx in range(n_puntos): # Generamos un loop de indice idx
        for jdx in range(n_puntos): # Generamos un loop de indice jdx

            v = np.array([xgrid[idx, jdx], ygrid[idx, jdx]]) # Generamos el vector v = [x y].T
            z[idx, jdx] = v.T @ A @ v    # Obtenemos z = v.T @ A @ v > 0 pues A es definida positiva.

    plt.contour(xgrid, ygrid, z, niveles) # Usamos np.contour para generas las curvas de nivel.
                                          # 'niveles' determina la cantidad y las posiciones de las regiones
                                          # del contorno (curvas de nivel).
                                          # A TENER EN CUENTA: plt.contour le gusta que los valores de los niveles
                                          # sean crecientes.
    plt.show()

# Test
grafica = level([0.03, 0.05, 0.09, 0.2, 0.5]) # Pueden elegir la cantidad de valores de niveles que quieran
                                              # siempre y cuando sea creciente.

# Imprimimos las curvas
print(grafica)