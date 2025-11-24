# %%
import numpy as np
import cupy as cp
import time

print(f"Cuda is avaiable: {cp.is_available()}")
# %%
tstart = time.time()
A_cpu = np.linspace(0, 1, 10000000).reshape(10000, 1000)
b_cpu = np.linspace(1, 2, 1000)
for iter in range(500):
    dot_prod = np.dot(A_cpu, b_cpu)

tend = time.time()
print(f"telapsed (CPU) = {tend - tstart}")

# %%
tstart = time.time()
A_gpu = cp.linspace(0, 1, 10000000).reshape(10000, 1000)
b_gpu = cp.linspace(1, 2, 1000)
for iter in range(500):
    dot_prod = cp.dot(A_gpu, b_gpu)
tend = time.time()
print(f"telapsed (GPU) = {tend - tstart}")