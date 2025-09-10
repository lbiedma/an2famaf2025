import numpy as np
import matplotlib.pyplot as plt

def transformacion_esfera(matrix):
    """
    Función que genera la esfera unidad en 2-D y la grafica junto con su transformación a través de matrix
    """
    if A.shape != (2, 2):
        assert ValueError("A no es una matriz 2x2")
    
    # generacion esfera unidad {(cos(x), sen(x)), 0 < x < 2pi}
    angles = np.linspace(0, 2 * np.pi, 100)
    sphere = np.vstack([
        np.cos(angles),
        np.sin(angles),
    ])

    # transformar esfera multiplicando todos los vectores por matrix
    transf_sphere = matrix @ sphere

    # grafico los x vs y
    plt.plot(sphere[0, :], sphere[1, :])
    plt.plot(transf_sphere[0, :], transf_sphere[1, :])
    plt.axis("equal")

    plt.show()


# Definimos la matriz A del ejemplo teórico
A = np.array([
    [1000., 999],
    [999, 998],
])
transformacion_esfera(A)
