# NVIDIA GPU Infrastructure Demo

## Project Objective

Demonstrate hands-on NVIDIA GPU infrastructure
deployment, CUDA acceleration, AI model inference,
and performance measurement using a cloud-hosted
NVIDIA GeForce RTX 4090.

## Technologies

### Used and Verified
- Windows 11
- Visual Studio Code
- Git and GitHub
- RunPod GPU Cloud
- NVIDIA GeForce RTX 4090
- Ubuntu Linux
- NVIDIA CUDA
- Python
- PyTorch
- Hugging Face Transformers
- Qwen2.5-0.5B-Instruct

### Planned Technologies
- Docker
- vLLM
- NVIDIA GPU monitoring tools
- Prometheus and Grafana

## Demonstration Progress

### Completed
- [x] NVIDIA RTX 4090 deployment on RunPod
- [x] NVIDIA driver validation
- [x] PyTorch CUDA availability verification
- [x] GPU matrix multiplication benchmark
- [x] GPU benchmark results recorded
- [x] AI language model loaded onto the GPU
- [x] Successful AI model inference
- [x] Single-request inference timing measurement
- [x] GPU memory allocation measurement

### Upcoming
- [ ] Deploy vLLM inference API server
- [ ] Test inference API endpoints
- [ ] Benchmark concurrent inference requests
- [ ] Monitor GPU utilization under load
- [ ] Measure inference latency and throughput
- [ ] Design NVIDIA NVL72 reference architecture
- [ ] Compare NVIDIA CUDA and AMD ROCm

## Verified GPU Environment

- **GPU:** NVIDIA GeForce RTX 4090
- **Cloud Provider:** RunPod
- **NVIDIA Driver:** 595.91.07
- **Driver-supported CUDA:** 13.2
- **PyTorch Version:** 2.8.0+cu128
- **CUDA Available:** True

## Verified GPU Computation Benchmark

- **Matrix Size:** 4096 x 4096
- **Operations:** 20
- **Total Execution Time:** 0.0481 seconds
- **Average Operation Time:** 0.002406 seconds
- **GPU Memory Allocated:** 200.12 MiB
- **Peak Allocated GPU Memory:** 264.12 MiB

The benchmark used PyTorch to execute 20
GPU-accelerated matrix multiplications on an
NVIDIA RTX 4090.

These measurements represent one benchmark run,
not peak theoretical GPU performance.

See `results/gpu_benchmark.txt`.

## Verified AI Inference Demonstration

### Model Configuration

- **Model:** Qwen2.5-0.5B-Instruct
- **GPU:** NVIDIA GeForce RTX 4090
- **Framework:** PyTorch / CUDA
- **Model Precision:** FP16
- **Inference Type:** Single-request text generation

### Measured Results

- **Generation Time:** 1.448 seconds
- **Generated Tokens:** 55
- **Generation Speed:** 37.98 tokens/second
- **PyTorch GPU Memory Allocated:** 958.29 MiB
- **Execution Status:** Successful

### Technical Implementation

1. Verified NVIDIA CUDA availability.
2. Loaded the pretrained Qwen language model.
3. Transferred model weights to GPU memory.
4. Tokenized the input prompt.
5. Executed GPU-accelerated text generation.
6. Synchronized CUDA execution for timing.
7. Measured generation speed and GPU memory.
8. Saved inference output for documentation.

These results represent one inference request.
They do not establish concurrent serving
performance or production-scale throughput.

See `results/inference_output.txt`.

## Project Files

- `README.md` - Project documentation
- `gpu_benchmark.py` - GPU computation benchmark
- `inference_demo.py` - AI inference demonstration
- `results/gpu_benchmark.txt` - GPU benchmark results
- `results/inference_output.txt` - AI inference results

## Next Phase: AI Inference API

The next milestone is to deploy an API-based
inference service using vLLM.

Planned activities:

1. Configure and start a vLLM inference server.
2. Load an AI language model onto the RTX 4090.
3. Send requests through an API endpoint.
4. Benchmark sequential and concurrent requests.
5. Collect GPU utilization and memory metrics.
6. Document architecture and deployment decisions.
7. Publish reproducible configuration and results.

## Future Infrastructure Architecture Project

Develop a conceptual NVIDIA NVL72 AI infrastructure
reference architecture covering:

- GPU compute architecture
- NVLink interconnect topology
- High-speed networking
- Storage architecture
- Workload orchestration
- Power and liquid cooling requirements
- Infrastructure monitoring
- Fault tolerance and scalability

This will be a design study, not a claim of
physical NVL72 deployment experience.

## Project Purpose

This portfolio documents independently completed
AI infrastructure engineering exercises.

It demonstrates practical learning and verified
technical execution, while distinguishing lab
experience from production infrastructure ownership.