# %%
import torch
import time
# %%

# Check if CUDA is available
device_cpu = torch.device("cpu")
device_gpu = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using GPU: {torch.cuda.is_available()}")

print(f"{torch.cuda.is_available()}")
# %%

# Create a large tensor
size = (10_000, 10_000)
x_cpu = torch.randn(size, device=device_cpu)
x_gpu = torch.randn(size, device=device_gpu)

# %%

# CPU computation
start_cpu = time.time()
y_cpu = x_cpu @ x_cpu  # Matrix multiplication
end_cpu = time.time()
print(f"CPU time: {end_cpu - start_cpu:.4f} seconds")

# %%

# GPU computation
torch.cuda.synchronize()  # Ensure GPU is ready
start_gpu = time.time()
y_gpu = x_gpu @ x_gpu
torch.cuda.synchronize()  # Wait for GPU to finish
end_gpu = time.time()
print(f"GPU time: {end_gpu - start_gpu:.4f} seconds")
# %%
