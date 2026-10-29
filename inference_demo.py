
import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# NVIDIA GPU AI Inference Demonstration
model_name = "Qwen/Qwen2.5-0.5B-Instruct"

assert torch.cuda.is_available(), "CUDA GPU not found"

print("GPU:", torch.cuda.get_device_name(0))
print("Loading model:", model_name)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float16
).to("cuda")

model.eval()

# Prepare inference request
messages = [
    {
        "role": "user",
        "content": (
            "In two concise sentences, explain how NVIDIA "
            "CUDA cores and Tensor Cores help accelerate "
            "AI inference."
        )
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to("cuda")

# Run GPU inference and measure execution time
torch.cuda.synchronize()
start = time.perf_counter()

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=False
    )

torch.cuda.synchronize()
elapsed = time.perf_counter() - start

# Decode generated response
new_tokens = outputs[0][inputs["input_ids"].shape[1]:]

response = tokenizer.decode(
    new_tokens,
    skip_special_tokens=True
)

# Display AI response
print("\nAI Response:")
print(response)

# Display inference performance metrics
print()
print("Inference Metrics:")
print(f"Generation time: {elapsed:.3f} seconds")
print(f"Generated tokens: {len(new_tokens)}")
print(f"Generation rate: {len(new_tokens)/elapsed:.2f} tokens/sec")

print(
    f"GPU memory allocated: "
    f"{torch.cuda.memory_allocated()/1024**2:.2f} MiB"
)

print()
print("Inference demonstration completed.")
