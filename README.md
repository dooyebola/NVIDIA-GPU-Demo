# NVIDIA GPU Infrastructure Demo

## Project Objective

Demonstrate hands-on NVIDIA GPU infrastructure deployment,
AI inference, and performance monitoring using a cloud-hosted
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

### Planned Technologies
- Docker
- vLLM
- GPU monitoring tools

## Demonstration Progress

### Completed
- [x] NVIDIA RTX 4090 deployment on RunPod
- [x] NVIDIA driver validation
- [x] PyTorch CUDA availability verification
- [x] GPU matrix multiplication benchmark
- [x] Benchmark results saved
- [x] Benchmark script published to GitHub

### Upcoming
- [ ] AI model inference deployment
- [ ] Inference API testing
- [ ] GPU utilization monitoring under load
- [ ] Inference performance benchmarking
- [ ] NVIDIA GPU reference architecture

## Verified GPU Environment

- **GPU:** NVIDIA GeForce RTX 4090
- **Driver Version:** 595.91.07
- **Driver-supported CUDA:** 13.2
- **PyTorch Version:** 2.8.0+cu128
- **CUDA Available:** True
- **Cloud Provider:** RunPod

## Verified GPU Benchmark

- **Matrix Size:** 4096 x 4096
- **Operations:** 20
- **Total Execution Time:** 0.0481 seconds
- **Average Operation Time:** 0.002406 seconds
- **GPU Memory Allocated:** 200.12 MiB
- **Peak Allocated GPU Memory:** 264.12 MiB

The benchmark used PyTorch to execute GPU-accelerated
matrix multiplication on an NVIDIA RTX 4090.

These measurements represent a single benchmark run,
not peak GPU performance or production AI inference.

See `results/gpu_benchmark.txt` for the recorded results.

## Project Files

- `gpu_benchmark.py` - GPU computation benchmark
- `results/gpu_benchmark.txt` - Recorded benchmark output
- `README.md` - Project documentation

## Next Phase

Deploy a small language model on the NVIDIA RTX 4090,
serve inference requests through an API, and measure
inference latency, throughput, and GPU utilization.