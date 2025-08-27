import numpy as np 

# llamamos algunas funciones para poder resolver Ax=b
from ejercicio_13 import cholesky_int
from ejercicio_5 import sol_trinffil
from ejercicio_5 import sol_trsupcol

'''
Resolver el sistema lineal Ax=b usando Cholesky, sol_trinffil y sol_trsupcol
'''
def sol_defpos(A,b):
    G = cholesky_int(A) 
    y = sol_trinffil(G.T, b)
    x = sol_trsupcol(G, y)
    return x
