# %%
import numpy as np
import cupy as cp
import time

print(f"Cuda is avaiable: {cp.is_available()}")
# %%
tstart = time.time()
x_cpu = np.random.random((1000, 1000))
for i in range(500):
    A = x_cpu.T @ x_cpu
tend = time.time()
print(f"telapsed (CPU) = {tend - tstart}")

# %%
cp.cuda.runtime.deviceSynchronize()
tstart = time.time()
x_gpu = cp.random.random((1000, 1000))

for iter in range(500):
    A_gpu = x_gpu.T @ x_gpu

cp.cuda.runtime.deviceSynchronize()
tend = time.time()
print(f"telapsed (GPU) = {tend - tstart}")
# %%
