import torch
import time

device = torch.device("cuda:0")

print("GPU:", torch.cuda.get_device_name(0))
print("CUDA available:", torch.cuda.is_available())

# Create two large matrices directly on GPU
size = 4096
a = torch.randn(size, size, device=device)
b = torch.randn(size, size, device=device)

# Warm up CUDA before measuring
for _ in range(5):
    c = torch.matmul(a, b)

torch.cuda.synchronize()

# Run and measure 20 GPU computations
start = time.perf_counter()

for _ in range(20):
    c = torch.matmul(a, b)

torch.cuda.synchronize()
elapsed = time.perf_counter() - start

print(f"Matrix size: {size} x {size}")
print(f"Total execution time: {elapsed:.4f} seconds")
print(f"Average per multiplication: {elapsed/20:.6f} seconds")
print(f"GPU memory allocated: {torch.cuda.memory_allocated()/1024**2:.2f} MiB")
print(f"Peak allocated memory: {torch.cuda.max_memory_allocated()/1024**2:.2f} MiB")
print("Result checksum:", c.sum().item())
