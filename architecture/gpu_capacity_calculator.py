
import math

# Reference model: Llama 3.1 405B Instruct
parameters = 405_000_000_000
layers = 126
kv_heads = 8
head_dim = 128

bytes_per_weight = 2
bytes_per_kv_element = 2

# Hypothetical workload
context_tokens = 32_000
concurrent_requests = 100

# Approximate nominal memory per GB200 GPU
gpu_memory_gb = 186

# Memory calculations (decimal GB)
weights_bytes = parameters * bytes_per_weight

kv_per_token = (
    2 * layers * kv_heads *
    head_dim * bytes_per_kv_element
)

kv_total_bytes = (
    kv_per_token *
    context_tokens *
    concurrent_requests
)

total_bytes = weights_bytes + kv_total_bytes
total_gb = total_bytes / 1e9

print("GB200 NVL72 — Preliminary Capacity Analysis")
print("-----------------------------------------")
print(f"Model weights: {weights_bytes / 1e9:.2f} GB")
print(f"KV cache: {kv_total_bytes / 1e9:.2f} GB")
print(f"Combined: {total_gb:.2f} GB")
print()

# Theoretical aggregate capacity only
minimum = math.ceil(total_gb / gpu_memory_gb)
print(f"Theoretical minimum GPUs: {minimum}")
print("This excludes runtime overhead.")
print()

for gpu_count in [8, 16, 24, 72]:
    capacity = gpu_count * gpu_memory_gb
    headroom = capacity - total_gb

    print(f"{gpu_count} GPUs:")
    print(f"  Nominal capacity: {capacity:.0f} GB")
    print(f"  Headroom: {headroom:.2f} GB")
    print()
