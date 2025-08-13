import numpy as np 

A = np.random.randint(0, 10,(9,6))

n,m = A.shape

for i in range(m):
    A_block = A[0:i+1, 0:i+1]
    print(f'A{i,i} ={A_block} ')
