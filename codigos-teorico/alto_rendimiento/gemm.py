import matplotlib.pyplot as plt
import numpy as np
from time import time

def gemm_ijk(n=100):
    alpha = np.random.random((n, n))
    beta = np.random.random((n, n))
    gamma = np.zeros((n, n))

    start = time()
    for idx in range(n):
        for jdx in range(n):
            for kdx in range(n):
                gamma[idx, jdx] += alpha[idx, kdx] * beta[kdx, jdx]
    total_time = time() - start

    return total_time

def gemm_ikj(n=100):
    alpha = np.random.random((n, n))
    beta = np.random.random((n, n))
    gamma = np.zeros((n, n))

    start = time()
    for idx in range(n):
        for kdx in range(n):
            for jdx in range(n):
                gamma[idx, jdx] += alpha[idx, kdx] * beta[kdx, jdx]
    total_time = time() - start

    return total_time

def gemm_jik(n=100):
    alpha = np.random.random((n, n))
    beta = np.random.random((n, n))
    gamma = np.zeros((n, n))

    start = time()
    for jdx in range(n):
        for idx in range(n):
            for kdx in range(n):
                gamma[idx, jdx] += alpha[idx, kdx] * beta[kdx, jdx]
    total_time = time() - start

    return total_time

def gemm_jki(n=100):
    alpha = np.random.random((n, n))
    beta = np.random.random((n, n))
    gamma = np.zeros((n, n))

    start = time()
    for jdx in range(n):
        for kdx in range(n):
            for idx in range(n):
                gamma[idx, jdx] += alpha[idx, kdx] * beta[kdx, jdx]
    total_time = time() - start

    return total_time

def gemm_kij(n=100):
    alpha = np.random.random((n, n))
    beta = np.random.random((n, n))
    gamma = np.random.random((n, n))

    start = time()
    for kdx in range(n):
        for idx in range(n):
            for jdx in range(n):
                gamma[idx, jdx] += alpha[idx, kdx] * beta[kdx, jdx]
    total_time = time() - start

    return total_time

def gemm_kji(n=100):
    alpha = np.random.random((n, n))
    beta = np.random.random((n, n))
    gamma = np.zeros((n, n))

    start = time()
    for kdx in range(n):
        for jdx in range(n):
            for idx in range(n):
                gamma[idx, jdx] += alpha[idx, kdx] * beta[kdx, jdx]
    total_time = time() - start

    return total_time

fig, ax = plt.subplots(1, 2)
ax[0].set_title("Tiempos")
ax[1].set_title("GFLOPS")
dims = np.arange(250, 751, 50)

for func in [gemm_ijk, gemm_ikj, gemm_jik, gemm_jki, gemm_kij, gemm_kji]:
    total_times = []
    gflops = []
    for n in dims:
        tot_time = func(n)
        total_times.append(tot_time)
        gflops.append(2 * n**3 * 1e-9 / tot_time)

    ax[0].plot(dims, total_times, label=func.__name__)
    ax[1].plot(dims, gflops, label=func.__name__)

ax[0].legend()
ax[1].legend()
fig.savefig("rendimiento_gemm.png")
plt.show()
