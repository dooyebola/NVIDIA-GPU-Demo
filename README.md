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
- vLLM 0.32.0
- NVIDIA GPU monitoring with nvidia-smi

### Planned / Not Yet Tested

- AMD ROCm
- Docker deployment workflows
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
- [x] Single-request inference timing
- [x] GPU memory allocation measurement
- [x] vLLM 0.32.0 installation
- [x] OpenAI-compatible inference API deployment
- [x] API health and model endpoint verification
- [x] Successful HTTP inference request
- [x] Concurrent inference benchmarking
- [x] GPU telemetry collection
- [x] Benchmark results published to GitHub
- [x] Conceptual GB200 NVL72 architecture design
- [x] GPU memory and capacity calculations
- [x] Hypothetical GPU infrastructure cost analysis
- [x] Architecture Decisions 002–007 documented

### Future Work

- [ ] AMD ROCm hands-on deployment
- [ ] Long-duration production-style load testing
- [ ] NVL72 hardware performance validation
- [ ] Production infrastructure deployment

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

### NVIDIA GPU Demonstrations

- `README.md` - Project documentation
- `gpu_benchmark.py` - CUDA GPU computation benchmark
- `inference_demo.py` - PyTorch AI inference demonstration

### GB200 NVL72 Architecture

- [Architecture Decisions](architecture/GB200_NVL72_Architecture_Decisions.md)
- [Reference Architecture Diagram](architecture/GB200_NVL72_Reference_Architecture.drawio)
- [GPU Capacity Calculator](architecture/gpu_capacity_calculator.py)
- [GPU Cost Model](architecture/gpu_cost_model.py)

### Benchmark Results

- `results/gpu_benchmark.txt` - GPU computation results
- `results/inference_output.txt` - AI inference results
- `results/gpu_capacity_analysis.txt` - GPU memory sizing
- `results/gpu_cost_analysis.txt` - Hypothetical cost analysis
- `results/vllm_benchmark_summary.txt` - Concurrency benchmarks
- `results/vllm_c1.json` - Concurrency 1 results
- `results/vllm_c5.json` - Concurrency 5 results
- `results/vllm_c10.json` - Concurrency 10 results
- `results/vllm_gpu_telemetry.csv` - GPU monitoring data


## Completed: AI Inference API Deployment

Deployed vLLM 0.32.0 on a cloud-hosted NVIDIA
RTX 4090 using RunPod.

Successfully served Qwen2.5-0.5B-Instruct
through an OpenAI-compatible inference API.

Validated the API health endpoint, model
listing, and chat completion requests.

Conducted concurrency benchmarks with
1, 5, and 10 simultaneous requests.

All 60 measured requests completed successfully.

The highest measured output throughput was
606.09 tokens/second during the 10-concurrent
request test.

Higher concurrency improved aggregate throughput
but increased first-token latency.

See the vLLM Inference API and Concurrency
Benchmark section below for detailed results.

## GB200 NVL72 Conceptual Reference Architecture

Completed a conceptual AI infrastructure
architecture study based on the NVIDIA
GB200 NVL72 rack-scale system.

### Architecture Components

- 72 NVIDIA Blackwell GPUs
- 36 NVIDIA Grace CPUs
- 18 GB200 compute trays
- 9 NVLink switch trays
- Internal NVLink GPU interconnect
- Proposed external InfiniBand networking
- Proposed vLLM inference serving
- Proposed Kubernetes orchestration
- GPU monitoring and management
- Storage and facility considerations

### Engineering Analysis

- 405B parameter reference model
- BF16 model-weight calculations
- KV-cache memory estimation
- GPU capacity comparison
- Hypothetical infrastructure cost modeling
- Performance validation planning

### Project Documentation

- [Architecture Decisions](architecture/GB200_NVL72_Architecture_Decisions.md)
- [Editable Architecture Diagram](architecture/GB200_NVL72_Reference_Architecture.drawio)
- [GPU Capacity Calculator](architecture/gpu_capacity_calculator.py)
- [GPU Cost Model](architecture/gpu_cost_model.py)

### Important Limitations

This architecture is an independent design study.

No physical GB200 NVL72 system was deployed.

Hardware capacity, performance, reliability,
and costs have not been production-validated.

Hypothetical cost assumptions are not vendor quotes.

## Project Purpose

This portfolio documents independently completed
AI infrastructure engineering exercises.

It demonstrates practical learning and verified
technical execution, while distinguishing lab
experience from production infrastructure ownership.

## vLLM Inference API and Concurrency Benchmark

### Deployment

- GPU: NVIDIA GeForce RTX 4090
- Cloud provider: RunPod
- Inference server: vLLM 0.32.0
- Model: Qwen2.5-0.5B-Instruct
- API: OpenAI-compatible chat completions
- Health endpoint: HTTP 200 OK
- Model endpoint: Verified
- API inference request: Successful

### Measured Performance

| Concurrency | Output Tokens/sec | p95 TTFT |
|---|---:|---:|
| 1 | 425.80 | 19.12 ms |
| 5 | 511.78 | 1801.90 ms |
| 10 | 606.09 | 1760.43 ms |

All 60 measured requests succeeded.

These results demonstrate an increase in
aggregate output throughput with higher concurrency,
accompanied by significantly higher first-token latency.

### Benchmark Limitations

- Small synthetic workload
- 20 measured requests per concurrency level
- Single RTX 4090 GPU
- No sustained production load test
- No GB200 NVL72 performance validation
- No AMD ROCm hardware testing

### Evidence

- `results/vllm_c1.json`
- `results/vllm_c5.json`
- `results/vllm_c10.json`
- `results/vllm_benchmark_summary.txt`
- `results/vllm_gpu_telemetry.csv`
